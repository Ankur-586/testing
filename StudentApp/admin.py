from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin  # type: ignore
from .models import CustomUser, Subject, Student

class UserAdmin(BaseUserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        #(_('user_info'), {'fields': ('native_name', 'phone_no')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff']
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )
admin.site.register(CustomUser, UserAdmin)

@admin.register(Subject)
class subjectadmin(admin.ModelAdmin):
    list_display = ['Subject_name']

@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display = ['stud','subject','marks']
