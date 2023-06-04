from django.views.generic import View, TemplateView

from core.viewmixins import (
    BaseContextTemplateViewMixin,
    BaseFormViewMixin,
    RequestFormKwargsMixin,
    BaseUpdateFormViewMixin,
    ModelFormMethodsMixin,
    CsrfExemptMixin,
)




# class BaseRequestFormView(
class BaseRequestFormView(
    CsrfExemptMixin,
    ModelFormMethodsMixin,
    RequestFormKwargsMixin,
    BaseFormViewMixin,
    View,
):
    pass




class BaseFormView(
    CsrfExemptMixin,
    ModelFormMethodsMixin,
    BaseFormViewMixin,
    View,
):
    pass


# class BaseUpdateRequestFormView(
class UpdateRequestModelFormView(
    CsrfExemptMixin,
    ModelFormMethodsMixin,
    RequestFormKwargsMixin,
    BaseUpdateFormViewMixin,
    BaseFormViewMixin,
    View
):
    pass



class BaseTemplateView(
    BaseContextTemplateViewMixin,
    TemplateView
):
    pass