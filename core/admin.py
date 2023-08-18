from django.contrib import admin
from core.models import leaderboard
# Register your models here.


@admin.register(leaderboard)
class reg(admin.ModelAdmin):
    list_display=['id','Username','Email','Points_Scored']
