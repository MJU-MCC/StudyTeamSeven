from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger
"""
def main(request):
    return HttpResponse("안녕하세요 정보통신공학과 21학번 이윤태입니다")

def yeah(request):
    return HttpResponse("화이팅!")
    
"""
def main(request):
    return render(request, "main.html")
def yeah(request):
    return render(request, "yeaha.html")
def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록: ",burgers)
    context = {
        "burger" : burgers,
    }
    return render(request, "burger_list.html", context)
def search(request):
    key = request.GET.get("key")

    if(key):
        burgers = Burger.objects.filter(name__contains = key)
    else:
        burgers = Burger.objects.none()
    
    context = {
        "burger_search" : key,
        "burgers" : burgers,
    }
    return render(request, "burger_search.html", context)