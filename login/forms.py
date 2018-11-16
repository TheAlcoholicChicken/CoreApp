from django import forms

class UserForm(forms.Form):
    search = forms.CharField()


class AddUserForm(forms.Form):
    userid = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()