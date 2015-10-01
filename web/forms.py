from django.forms import ModelForm
from models import tasks

class TasksForms(ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'

    error_css_class = 'class-error'
    required_css_class = 'class-required'
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'some-class other-class'
    def as_div(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)

    def as_div2(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s><p>%(label)s</p> <p> %(field)s </p> %(help_text)s %(errors)s</div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)