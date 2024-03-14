from django.http import HttpResponse

def main(request):
    return HttpResponse("안녕하세요 정보통신공학과 21학번 이윤태입니다")

def yeah(request):
    return HttpResponse("화이팅!")