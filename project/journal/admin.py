from django.contrib import admin
from .models import user_profile,diary
# Register your models here.
admin.site.register(user_profile)
admin.site.register(diary)
