from django.contrib import admin
from .models import contact, registration, login
# Register your models here.
admin.site.register(contact)
admin.site.register(registration)
admin.site.register(login)