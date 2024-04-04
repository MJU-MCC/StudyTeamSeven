from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as num
def index(request):
    
    return render(request, "index.html")

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        # POST 요청에서 데이터 추출
        data = json.loads(request.body)
        
        # 입력값 추출
        number1 = data.get('number1')
        number2 = data.get('number2')
        
        # 계산 수행
        result = int(number1) + int(number2)  # 여기에 원하는 계산을 수행하세요
        
        # 결과 반환
        return JsonResponse({'result': result})
    return render(request, "caculate.html")
