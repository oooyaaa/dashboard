from django.contrib import admin
from board.models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin): #ModelAdmin으로 부터 상속받았다는 것
    list_display=('writer','title','content') #list를 어떻게 표시할것인가.
        #데이터 등록하면 이 3개가 표시된다.
    
admin.site.register(Board,BoardAdmin)
