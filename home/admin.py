from django.contrib import admin


# Register your models here.

# The Database we register to backend control


from .models import Tool , CurAlarm

@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    pass

@admin.register(CurAlarm)
class CurAlarmAdmin(admin.ModelAdmin):
    pass