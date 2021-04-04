from django.db import models
from datetime import datetime

# Create your models here.
class Board(models.Model):
    idx=models.AutoField(primary_key=True) #프라이머리키
    writer=models.CharField(null=False, max_length=50) #글자는 50자까지 적겠다는 말
    title=models.CharField(null=False, max_length=200)
    content=models.TextField(null=False) #글자가 좀 크니까 TextField를 사용한다.
    hit=models.IntegerField(default=0) #
    post_date=models.DateTimeField(default=datetime.now, blank=True)
    filename=models.CharField(null=True, blank=True, default='', max_length=500)
    filesize=models.IntegerField(default=0)
    down=models.IntegerField(default=0) #다운로드 몇번했는가
    
   #개시물 조회수 몇번증가 했는가
   #자동 증가하도록 함수 만들어준다.
   #함수호출하면 자동증가하도록 만들어준다.
    def hit_up(self): 
        self.hit+=1 
        
    def down_up(self):
        self.down+=1
        
class Comment(models.Model): #댓글테이블
    idx=models.AutoField(primary_key=True)
    board_idx=models.IntegerField(null=False) #게시물에는 board_idx가 있어야 누구댓글인지 알수가 있다.
        #반드시 게시물번호가 있어야 한다.

    writer=models.CharField(null=False, max_length=50)
    content=models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now, blank=True)

# Create your models here.
