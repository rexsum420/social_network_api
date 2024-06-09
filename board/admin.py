from django.contrib import admin
from .models import BoardMessage, Board

admin.site.register([BoardMessage, Board])
