from django import forms
from .models import *
class detailsform(forms.ModelForm):
    class Meta:
        model=alumni
        fields=('fname','lname','year_pass','student','inst_name','phno','email','a_street','a_city','a_state','a_country','a_pin')
    def __init__(self, *args, **kwargs):
        super(detailsform, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
class ec_form(forms.ModelForm):
    class Meta:
        model=ec
        fields=('fname',)
    def __init__(self, *args, **kwargs):
        super(ec_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })