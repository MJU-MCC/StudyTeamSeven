from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import io
import urllib, base64

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

def process_values(request):
    if request.method == 'POST':
        omega_1_input = request.POST.get('omega_1')
        omega_2_input = request.POST.get('omega_2')
        test_sample_input = request.POST.get('test_sample')

        # 입력된 값으로 omega_1과 omega_2 배열 생성 (입력 형식에 따라 적절한 변환 필요)
        omega_1_list = [list(map(float, sample.split(','))) for sample in omega_1_input.split(' ')]
        omega_2_list = [list(map(float, sample.split(','))) for sample in omega_2_input.split(' ')]
        test_sample = list(map(float, test_sample_input.split(',')))
        omega_1 = np.array(omega_1_list).T
        omega_2 = np.array(omega_2_list).T

        # 분류 작업 수행
        X = np.hstack([omega_1, omega_2])
        y = np.array([0] * len(omega_1_list) + [1] * len(omega_2_list))
        # 테스트 샘플
        x = np.transpose(np.array(test_sample))

        # 클래스별 평균 벡터 계산
        mean_omega_1 = np.mean(omega_1, axis=1)
        mean_omega_2 = np.mean(omega_2, axis=1)

        # 클래스별 공분산 행렬 계산
        cov_omega_1 = np.cov(omega_1, ddof=0)
        cov_omega_2 = np.cov(omega_2, ddof=0)

        # 다변수 정규분포를 사용하여 조건부 확률밀도함수 추정
        pdf_omega_1 = multivariate_normal(mean=mean_omega_1, cov=cov_omega_1, allow_singular=True)
        pdf_omega_2 = multivariate_normal(mean=mean_omega_2, cov=cov_omega_2, allow_singular=True)
        
        # 분류 작업 수행
        X = np.hstack([omega_1, omega_2])
        y = np.array([0] * len(omega_1_list) + [1] * len(omega_2_list))
        # 테스트 샘플
        x = np.transpose(np.array(test_sample))

        classification_results = ""
        p_x_given_omega_1 = pdf_omega_1.pdf(x)
        p_x_given_omega_2 = pdf_omega_2.pdf(x)
        if p_x_given_omega_1 > p_x_given_omega_2:
            classification_results="omega_1에 속합니다."
        else:
            classification_results="omega_2에 속합니다."
        # 시각화를 위한 그래프 생성
        fig, ax = plt.subplots()
        
        # 테스트 샘플 시각화
        ax.scatter(x[0], x[1], color='green', marker='x', label='Test Sample')

        # 결정 경계 그리기
        x_min, x_max = X[0].min() - 1, X[0].max() + 1
        y_min, y_max = X[1].min() - 1, X[1].max() + 1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
        grid = np.c_[xx.ravel(), yy.ravel()]
        Z_omega_1 = pdf_omega_1.pdf(grid).reshape(xx.shape)
        Z_omega_2 = pdf_omega_2.pdf(grid).reshape(xx.shape)
        Z_decision = Z_omega_1 - Z_omega_2
        ax.contour(xx, yy, Z_decision, levels=[0], colors='black')
        
        # 클래스별 샘플 시각화
        ax.scatter(omega_1[0], omega_1[1], label='omega_1')
        ax.scatter(omega_2[0], omega_2[1], label='omega_2')
        ax.legend()
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_title('Decision Boundary')
        ax.grid(True)
        plt.tight_layout()

        # 결과 이미지를 메모리에 저장
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        # 분류 결과와 함께 입력된 샘플의 클래스 출력
        result = classification_results
        # 이미지를 Base64로 인코딩하여 HTML에 넣을 수 있도록 함
        graphic = base64.b64encode(image_png).decode('utf-8')

        # 결과 이미지를 HTML에 렌더링
        return render(request, 'result.html', {
            'graphic': f'data:image/png;base64,{graphic}',
            'result':result,
            'mean_omega_1': mean_omega_1,
            'mean_omega_2': mean_omega_2,
            'cov_omega_1': cov_omega_1,
            'cov_omega_2': cov_omega_2
        })
    
    return render(request, "decision_boundary.html")