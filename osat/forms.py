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
        fields=('email','password1','password2','event')
        widgets={'password1':forms.PasswordInput(),'password2':forms.PasswordInput()}
    def __init__(self, *args, **kwargs):
        super(ec_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class alumnievent_form(forms.ModelForm):
    class Meta:
        model=alumnievent
        fields=('email',)
    def __init__(self,*args, **kwargs):
        super(alumnievent_form,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
class ec_login_form(forms.ModelForm):
    class Meta:
        model=ec_login
        fields=('email','password')
        widgets={'password':forms.PasswordInput()}
    def __init__(self, *args, **kwargs):
        super(ec_login_form, self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
class view_events_form(forms.ModelForm):
    class Meta:
        model=view_events
        fields=('email',)
    def __init__(self,*args,**kwargs):
        super(view_events_form,self).__init__(*args, **kwargs)
        for field in iter(self. fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })