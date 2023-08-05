from django.contrib import admin

# certificate_app/admin.py
from django.contrib import admin
from .models import Certificate

admin.site.register(Certificate)

