# from django.views.generic import TemplateView
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# from core.viewmixins import RegularTemplateViewMixin
# from core.views import ModelFormSubmissionView
# from customers.forms import CreateCustomerForm, UpdateCustomerForm

# from core.views import (
#     CreateRequestModelFormView,
#     UpdateRequestModelFormView
# )



# class CustomerTemplateView(RegularTemplateViewMixin, TemplateView):
    
#     template_name = 'customers/customers.html'





# class CustomerCreateView3(ModelFormSubmissionView):

#     form_class = CreateCustomerForm
#     valid_form_message = 'Customer created successfully.'
#     invalid_form_message = 'There was an error creating the customer. Please try again later.'
    
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         # print(request.session['teste'])
#         return super().dispatch(request, *args, **kwargs)
    
    
#     def form_methods(self, form) -> list[str]:
#         self.teste = 'teste'
#         return super().form_methods(form)
    
    
#     def valid_form_response(self, form,*args, **kwargs) -> dict:
#         response = super().valid_form_response(form, *args, **kwargs)
#         response['teste'] = self.teste
#         return response
    
    
    
    
    
# class CustomerCreateView(CreateRequestModelFormView):
#     form_class = CreateCustomerForm
#     valid_form_message = 'Customer created successfully.'
#     invalid_form_message = 'There was an error creating the customer. Please try again later.'
    
    


# class CustomerUpdateView(UpdateRequestModelFormView):
#     form_class = UpdateCustomerForm
#     valid_form_message = 'Customer updated successfully.'
#     invalid_form_message = 'There was an error updating the customer. Please try again later.'
