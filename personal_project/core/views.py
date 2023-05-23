from django.views.generic import View, TemplateView

from core.viewmixins import RegularModelFormSubmissionViewMixin
from core.viewmixins import RegularTemplateViewMixin
from core.viewmixins import (
    BaseFormViewMixin,
    RequestFormViewMixin,
    BaseUpdateModelFormViewMixin,
    ModelFormMethodsMixin,
    ResquestUpdateModelFormViewMixin,
    CsrfExemptMixin,
)


class ModelFormSubmissionView(RegularModelFormSubmissionViewMixin, View):
    pass




class CreateRequestModelFormView(
    CsrfExemptMixin,
    ModelFormMethodsMixin,
    RequestFormViewMixin,
    BaseFormViewMixin,
    View
):
    pass




class UpdateRequestModelFormView(
    CsrfExemptMixin,
    ModelFormMethodsMixin,
    ResquestUpdateModelFormViewMixin,
    BaseUpdateModelFormViewMixin,
    BaseFormViewMixin,
    View
):
    pass



class BaseTemplateView(RegularTemplateViewMixin, TemplateView):
    pass