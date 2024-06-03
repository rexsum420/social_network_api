An API for a simple social network app with 1 chatroom that allows direct messages and logging.

I wanted to make a simple app with full protections, logging, and authentications to show how each are accomplished in django.

No migrations have been made and no users have been made so if you want to use this project you will need to run the following commands:

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
   
./manage.py runserver