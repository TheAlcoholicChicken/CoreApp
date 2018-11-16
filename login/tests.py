from django.test import TestCase
import os
# Create your tests here
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
