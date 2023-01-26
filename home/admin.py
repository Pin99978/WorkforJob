from django.contrib import admin


# Register your models here.

# The Database we register to backend control


from .models import Tool , CurAlarm

@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tool._meta.fields] #全顯示
    list_per_page = 10 #列表一頁顯示幾項
    search_fields = ('tools',) #搜尋設定 結尾要加逗號組成 list/tuple
    list_filter = ('fabs',) #過濾器
    ordering = ('pk',) #自定義排序
    # ordering = ('-pk',) #排序, 負號代表反向排列


@admin.register(CurAlarm)
class CurAlarmAdmin(admin.ModelAdmin):
    pass

""" def filter_tool(self, obj):
    return obj.location.city
filter_tool.admin_order_field = 'location' #允許排列
filter_tool.short_description = 'City (fk)' #清單名稱 """