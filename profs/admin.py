from django.contrib import admin

# Register your models here.

from .models import prof, favourite

class profileAdmin(admin.ModelAdmin):
    class meta:
        model = prof
        
admin.site.register(prof, profileAdmin)
admin.site.register(favourite)