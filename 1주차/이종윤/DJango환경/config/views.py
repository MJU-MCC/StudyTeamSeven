# from django.http import HttpResponse
from django.shortcuts import render # render함수를 import
from burgers.models import Burger
def main(request):
    # return HttpResponse("안녕하세요, 정보통신공학과 이종윤입니다\n 1주차 django환경 구축 완료했습니다.")
    return render(request, "main.html") # HttpResponse 대신 render 함수 사용
def burger_list(request):
    burgers=Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers": burgers, # burgers 키에 burgers 변수 (QuerySet 객체)를 전달한다.
    }
    # render 함수의 마지막에 context 전달
    return render(request, "burger_list.html", context) # HttpResponse 대신 render 함수 사용
    # return HttpResponse("pyburger의 햄버거 목록입니다.")

def burger_search(request):
    keyword=request.GET.get("keyword")
    #print(keyword)

    #이름 (name 속성)에 전달받은 키워드 값이 포함된 Burger를 검색한다.
    # keyword 값이 주어진 경우
    if keyword is not None:
        # keyword 값으로 검색된 querySet을 할당
        burgers=Burger.objects.filter(name__contains=keyword)
    # 주소 표시줄을 통해 keyword가 주어지지 않아 , None이 할당된 경우
    else:
        # 검색 결과 없는 것과 가가은 빈 QuerySet을 할당
        burgers=Burger.objects.none()
    #print(burgers)
    context={
        "burgers": burgers,
    }
    return render(request, "burger_search.html", context)