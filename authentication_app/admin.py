from django.contrib import admin
from .models import CustomUser  # Import your custom user model

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
    # You can add or remove fields to display in the admin list as necessary

# Or alternatively without the decorator:
# admin.site.register(CustomUser, CustomUserAdmin)
