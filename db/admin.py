from django.contrib import admin

# Register your models here.

from db.models import Examples

class ExamplesAdmin(admin.ModelAdmin):
    list_listview = ('oname','oemail','ophone','ocity')
admin.site.register(Examples,ExamplesAdmin)