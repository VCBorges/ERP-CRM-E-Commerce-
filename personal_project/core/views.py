from django.views.generic import View

from core.viewmixins import RegularModelFormSubmissionViewMixin
from core.viewmixins import RegularTemplateViewMixin



class ModelFormSubmissionView(RegularModelFormSubmissionViewMixin, View):
    pass