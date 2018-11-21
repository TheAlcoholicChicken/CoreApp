from django import forms


# API Request must contain a string
class SearchForm(forms.Form):
    search = forms.CharField()

# API Request must contain userid
class UserForm(forms.Form):
    userid = forms.CharField()

# API Request must contain the minimum, firstname and lastname
# userid, profile link are auto populated
# random userid created is
class AddUserForm(forms.Form):
    userid = forms.CharField(required=False)
    user_profile_link = forms.URLField(required=False)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    profile_picture_url = forms.URLField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
