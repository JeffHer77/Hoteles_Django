from django.contrib import admin
from .models import Cliente, CustomUser

# Register your models here.

admin.site.register(Cliente)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser', 'user_type', 'is_active')  # Customize this list as needed
    search_fields = ('email',)  # Add searchable fields

    # If you want to make the fields editable in the list view
    list_filter = ('user_type', 'is_staff', 'is_superuser')

    # Optional: Specify fields to be shown in the detail view
    fields = ('email', 'user_type', 'is_staff', 'is_active', 'is_superuser')
