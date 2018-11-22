from django import forms

# Global Constants
__Form = forms.Form

# API Request must contain a string
class SearchForm(__Form):
    search = forms.CharField()

# API Request must contain userid
class UserForm(__Form):
    userid = forms.CharField()

# API Request must contain the minimum, firstname and lastname
# userid, profile link are auto populated
# random userid created is
class AddUserForm(__Form):
    userid = forms.CharField(required=False)
    user_profile_link = forms.URLField(required=False)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    profile_picture_url = forms.URLField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

class LoginUserForm(__Form):
    user_email = forms.CharField(required=True)
    password = forms.CharField(required=True)