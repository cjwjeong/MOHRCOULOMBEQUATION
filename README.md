# MOHRCOULOMBEQUATION
Visualize Mohr Circle and Failure Envelope for Python 3.5.2
# 만든 이유 및 참고 코드
최대 주응력과 최소 주응력을 대입하여 모어원을 그리고 바로 파괴포락선을 그리는 코드가 없어 제작하였다. 
https://github.com/massgame/Mohr_Envelope/blob/master/README_kr.md 를 많이 참고하였다.
# 구동 순서
1. 각 시험 결과의 최소 주응력과 최대 주응력을 통해 모어원을 그린다.
2. a의 범위 0~90도로 정하고 모어원과 파괴 포락선의 접선을 (x1-rcos(a),rsin(a))로 정한다.
3. 각 점들을 최소자승법을 통해 직선으로 만든다.
4. 이 직선과 원의 중점 사이의 거리 그리고 원의 반지름들 간의 차이의 평균을 구한다.
5. 만들어진 직선 중 4번의 결과가 가장 작은 직선을 파괴 포락선으로 정한다.
# 사용 모듈
numpy, scipy, matplotlib
# 사용법
main 파일 실행 후, 모어원의 최대 주응력과 최소주응력을 입력한 후 plot한 결과를 보면 된다.
# 입력
각 실험 결과의 최소 주응력과 최대 주응력
# 출력
모어원 + 파괴 포락선

