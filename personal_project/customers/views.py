from django.shortcuts import render
from django.views.generic import View, UpdateView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import (
    HttpResponse,
    HttpRequest,
)

from core.viewmixins import RegularModelFormSubmissionViewMixin
from core.viewmixins import RegularTemplateViewMixin
from customers.forms import CreateCustomerForm


from typing import Any

class CustomerTemplateView(RegularTemplateViewMixin, TemplateView):
    
    template_name = 'customers/customers.html'
    
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


class CustomerCreateView(RegularModelFormSubmissionViewMixin, View):

    form_class = CreateCustomerForm
    form_valid_message = 'Customer created successfully.'
    form_invalid_message = 'There was an error creating the customer. Please try again later.'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)