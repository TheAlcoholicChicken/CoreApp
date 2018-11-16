release: python manage.py makemigrations && python manage.py migrate
web: gunicorn badgebook.wsgi --log-file -
