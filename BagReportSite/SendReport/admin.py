from django.contrib import admin
from .models import BagReport


@admin.register(BagReport)
class BagReportAdmin(admin.ModelAdmin):
    list_display = ("name_user", "date_added", 'active', 'id')
    #абобefewfewfауцауцауцацуацуа
    # коммент в ветке