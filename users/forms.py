from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ModelFormWithSubmit(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', "Valider", css_class="btn btn-lg btn-primary btn-block bg_main"))
    helper.form_method = 'POST'