from django import forms
from django.forms import ModelMultipleChoiceField
from ajax_select.fields import AutoCompleteSelectMultipleField

from fields.models import Field , Job , Worker
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'square', 'square_ha', 'coordinate', 'cadastral_number')
        labels = {
            'name': 'Название:',
            'square': 'Площадь м²:',
            'square_ha': 'Площадь га:',
            'coordinate': 'Координаты:',
            'cadastral_number': 'Кадастровый номер:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coordinate'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Column('name', css_class='form-group col-md-12 mb-2'),
            Column('square', css_class='form-group col-md-12 mb-2'),
            Column('square_ha', css_class='form-group col-md-12 mb-2'),
            Column('coordinate' , css_class='form-group col-md-12 mb-2') ,
            Column('cadastral_number', css_class='form-group col-md-12 mb-2'),
            Submit('submit', 'Добавить', css_class='form-row text-center')
        )


class SchedulerProfileChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.firstname, obj.lastname)


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('category', 'season', 'start_job', 'end_job', 'fields', 'workers', 'comment')

        start_job = forms.DateTimeField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )

        end_job = forms.DateTimeField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('category', css_class='form-group col-sm-6 mb-0'),
                Column('season', css_class='form-group col-sm-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('start_job', css_class='form-group col-sm-6 mb-0'),
                Column('end_job', css_class='form-group col-sm-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('fields', css_class='form-group col-sm-6 mb-0'),
                Column('workers', css_class='form-group col-sm-6 mb-0'),
                css_class='form-row'
            ),
            'comment',
            Submit('submit' , 'Добавить' , css_class='form-row text-center mt-2')
        )