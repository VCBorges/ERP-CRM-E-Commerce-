from core.datatables import DataTableServerSideDRF
from core.datatables import DataTableServerSide


class EmployeeDataTable(DataTableServerSideDRF):
    
    columns = [
        # 'id',
        'name',
        # 'document',
        # 'email',
        # 'phone',
        # 'address',
    ]
    
    searchable_fields = [
        'name',
        # 'email',
        # 'document',
    ]