from django.http import HttpResponse

def main(request):
    return HttpResponse("안녕하세요, 정보통신공학과 이종윤입니다\n 1주차 django환경 구축 완료했습니다.")
def burger_list(request):
    return HttpResponse("pyburger의 햄버거 목록입니다.")