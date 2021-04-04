from django.shortcuts import render,redirect
from board.models import Board
from board import bigdataPro


def main(request):
    return render(request, 'main.html')


# Create your views here.
def list(request):
    boardCount=Board.objects.count() # 게시물 개수 #전체 개수를 얻을 수 있음
    boardList=Board.objects.all().order_by('-idx') #게시물 인덱스별로 -idx 내림차순 정렬 // idx오름차순 (-없으면)
    return render(request, "board/list1.html",{'boardList':boardList, 'boardCount':boardCount})
        #board/list1.html로 전달할 값을 뒤에 적어준다.


# def cctv_map (request):
     # bigdataPro.cctv_map()
     # return render(request, 'map/map01.html')
 
def map (request):
    bigdataPro.cctv_map()
    return render(request, 'map.html')

def result (request):
    return render(request, 'result.html')
 



