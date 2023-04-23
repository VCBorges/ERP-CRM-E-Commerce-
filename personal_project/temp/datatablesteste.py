from django.http import QueryDict
from django.db.models.query import QuerySet
from django.db.models.base import Model
from django.db.models import Q


class DatatableServerSidePOST:

    def __init__(
        self,
        request: QueryDict,
        queryset: QuerySet[Model],
        columns: list[str],
        searchable_fields: list[str] = None,
        extra_filters: dict[str, str] = None,
        index_column: bool = False,
        *args,
        **kwargs
    ):
        self.request = request
        self.draw = request.POST['draw']
        self._start = request.POST['start']
        self._length = request.POST['length']
        self.order_column = request.POST['order[0][column]']
        self.order_dir = request.POST['order[0][dir]']
        self.search = request.POST['search[value]']
        self.queryset = queryset
        self.columns = columns
        self.searchable_fields = searchable_fields
        self.extra_filters = extra_filters
        self.index_column = index_column
        self.total = None
    
    
    
    def __search_filter(self) -> QuerySet[Model]:
        if self.search:
            lookup_expression = Q()
            for column in self.searchable_fields:
                lookup_expression |= Q(**{f"{column}__icontains": self.search})

            self.queryset = self.queryset.filter(lookup_expression)
            return self.queryset
        else:
            return self.queryset
        


    def __additional_filtering(self) -> QuerySet[Model]:
        if self.extra_filters:
            if self.request.POST[list(self.extra_filters.keys())[0]]:
                self.queryset = self.queryset.filter(**self.extra_filters)
                return self.queryset
        
        
        
    def __ordering(self) -> QuerySet[Model]:
        if self.order_column != '0':
            if self.order_dir == 'asc':
                self.queryset = self.queryset.order_by(f'{self.columns[int(self.order_column)]}')
            else:
                self.queryset = self.queryset.order_by(f'-{self.columns[int(self.order_column)]}')
        else:
            return self.queryset
        
        
        
    def __paginate(self) -> QuerySet[Model]|Exception:
        if self._start and self._length:
            self.total = self.queryset.count()
            start = int(self._start)
            length = int(self._length)
            self.queryset = self.queryset[start:start + length]
            return self.queryset
        else:
            raise Exception('Start e Length não foram informados.')
        
        
        
    def __add_index_column(self) -> QuerySet[Model]:
        if self.index_column:
            self.queryset = [
                {'index': index + int(self._start)+1, **record}
                for index, record in enumerate(self.queryset)
            ]
            return self.queryset
    
    
    
    def __response_dict(self, dados_adicionais: dict = None) -> dict:
        response = {
            'data': self.queryset,
            'draw':self.draw,
            'recordsTotal': self.total,
            'recordsFiltered': self.total,
        }
        
        if dados_adicionais:
            response.update(dados_adicionais)
        
        return response
    
    
    
    def get_response(self, dados_adicionais: dict = None):
        self.__search_filter()
        self.__additional_filtering()
        self.__ordering()
        self.__paginate()
        self.__add_index_column()
        return self.__response_dict(dados_adicionais)
    
            
            
    def __str__(self):
        return f'{self.draw} - {self._start} - {self._length} - {self.order_column} - {self.order_dir} - {self.search}'

    
    
    