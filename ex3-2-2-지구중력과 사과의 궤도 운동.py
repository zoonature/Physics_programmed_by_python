from vpython import *
#GlowScript 3.0 VPython

# 화면 설정
scene.range = 20000

# 크기 조정을 위한 변수
sf = 10000
sf_e = 1

# 지구, 사과 만들기
earth = sphere(pos = vec(0,-6400000,0), radius = sf_e*6400000, color = color.blue)  
apple = sphere(pos = vec(0,1000,0), radius = sf*0.1, color = color.red, make_trail = True) 

# 물리 성질 & 상수 초기화
apple.m = 0.1 #사과 질량 ##kg
apple.v = vec(7900,0,0) #사과 초기 속도 ##m/s
earth.m = 5.98e24 #지구 질량 
earth.v = vec(0,0,0) #지구 초기 속도
G = 6.67e-11 #중력상수 ##N*m**2/kg**2

# 시간 설정
t = 0 ##s
dt = 1 ##s

# 시뮬레이션 루프
while t < 10000:
    rate(10000)
    
    # 만유인력
    F = -G*earth.m*apple.m/mag(earth.pos-apple.pos)**2*norm(earth.pos-apple.pos)
    
    # 뉴턴 제 3법칙 적용 (작용 반작용)
    earth.force = F
    apple.force = -F

    # 속도, 위치 업데이트
    apple.v = apple.v + apple.force/apple.m*dt
    earth.v = earth.v + earth.force/earth.m*dt
    apple.pos = apple.pos + apple.v*dt
    earth.pos = earth.pos + earth.v*dt
    
    print(t/3600,":",mag(apple.pos-earth.pos)) #출력

    scene.center = apple.pos #화면 업데이트

    # 시간 업데이트
    t += dt
