from django.contrib import admin
from .models import Member

# Register your models here.

#six or seven
#7<6 change my mind

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)
