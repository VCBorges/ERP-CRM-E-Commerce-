from django.views.generic import View, TemplateView

from core.viewmixins import (
    BaseContextTemplateViewMixin,
    BaseFormViewMixin,
    RequestFormKwargsMixin,
    # RequestFilesFormKwargsMixin,
    BaseUpdateFormViewMixin,
    ModelFormMethodsMixin,
    UpdateResquestFormKwargsMixin,
    CsrfExemptMixin,
)



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



class UpdateRequestModelFormView(
    CsrfExemptMixin,
    ModelFormMethodsMixin,
    UpdateResquestFormKwargsMixin,
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