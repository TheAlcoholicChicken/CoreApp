from django.db import models
import json, time

"""
for debugging purposes in terminal, use below to interact with DB 
from login.models import UsersCollection as UC
"""


def generate_default():
    return (time.time() * 1e3).__str__()[3:13]


# Create your models here.
class UsersCollection(models.Model):
    user_id = models.CharField(max_length=100, blank=False, unique=True,
                               default=generate_default)
    user_profile_link = models.URLField(
        null=True)  # first_name + last_name(camelcase)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture_url = models.URLField(
        null=True)  # ImageField? or standard char/text field
    description = models.TextField(null=True)

    def __str__(self):
        return self.user_id

    def GET_FIELD(self):
        fields = UsersCollection._meta.get_fields()
        short_fields = []
        for i in fields:
            short_fields.append(i.__str__().split('.')[-1])
        return short_fields

    # Returns JSON of user data from Users Collection
    # Returns empty json with error text 'User does not exist' for no user
    def get_user_json(user_id):
        user = UsersCollection.objects.filter(user_id=user_id)
        if user.exists() == False:
            return {
                'error': 'User does not exist'
            }
        user = user[0]
        return {
            'user_id': user.user_id,
            'user_profile_link': user.user_profile_link,
            'data': {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_picture_url': user.profile_picture_url,
                'description': user.description
            }
        }

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    # Grabs users by filtering rows in DB for those that match user_id, first_name, last_name
    # Second parameter sets if string list of names to be returned, else QuerySet
    def search_user(terms, id_only=True):
        if (id_only == True):
            query = UsersCollection.objects.filter(user_id__icontains=terms) | \
                    UsersCollection.objects.filter(first_name__icontains=terms) | \
                    UsersCollection.objects.filter(last_name__icontains=terms) | \
                    UsersCollection.objects.filter(description__icontains=terms)
            query_list = {'users': []}
            for row in query:
                query_list['users'].append(row.user_id)
            return query_list
        else: # returns a list of user jsons
            query = UsersCollection.objects.filter(user_id__icontains=terms) | \
                    UsersCollection.objects.filter(first_name__icontains=terms) | \
                    UsersCollection.objects.filter(last_name__icontains=terms) | \
                    UsersCollection.objects.filter(description__icontains=terms)
            query_list = {'users': []}
            for row in query:
                query_list['users'].append(UsersCollection.get_user_json(row.user_id))
            return query_list

    # Add new user to DB for sign-up. Auto-populate links/urls
    # Returns ID (index) of user added to DB
    def set_user(info):
        try:
            row = ''
            if info['user_id'] != '':
                row, created = UsersCollection.objects.get_or_create(user_id = info['user_id'])
            else:
                row = UsersCollection(user_id = generate_default().__str__())
            data = info['data']
            row.first_name = data['first_name']
            row.last_name = data['last_name']
            row.user_profile_link = info['user_profile_link']
            row.profile_picture_url = data['profile_picture_url']
            row.description = data['description']
            row.save()
            return row.id, not created
        except Exception:
            return 'DB ERROR' + Exception
