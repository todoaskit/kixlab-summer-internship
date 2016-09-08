from django.contrib import admin
from fourthexp.models import Politician, SubmitLog
# Register your models here.

class PoliticianAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "pid")
    list_filter = ("name",)

class SubmitLogAdmin(admin.ModelAdmin):
    list_display = ("token", "q_kind", "users_fav", "shown_list", "select_list")
    list_filter = ("token", "q_kind", "users_fav")

admin.site.register(Politician, PoliticianAdmin)
admin.site.register(SubmitLog, SubmitLogAdmin)
