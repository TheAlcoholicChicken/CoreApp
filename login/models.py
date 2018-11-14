from django.db import models


# Create your models here.
class UsersCollection(models.Model):
    user_id = models.CharField(max_length=100)
    user_profile_link = models.URLField()  # first_name + last_name(camelcase)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture_url = models.URLField()  # ImageField? or standard char/text field
    description = models.TextField()

    def __str__(self):
        return self.user_id
