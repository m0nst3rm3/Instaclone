from django import forms
from . models import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class PostForm(forms.ModelForm):
    def __init__(self, *arg, **kwargs):
        super(PostForm, self).__init__(*arg, **kwargs)
        self.helper = FormHelper
        self.helper.add_input(Submit( 'post','Post', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        fields = ('__all__')
