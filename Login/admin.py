from django.contrib import admin
from .models import NewUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',)
# Register your models here.
admin.site.register(NewUser, CustomUserAdmin)

