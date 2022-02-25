from vpython import *
#GlowScript 3.0 VPython

# 상수 초기화
g = 9.8 #중력상수
R = 0.035 #공의 반지름
C = 0.35  #공의 저항계수
L = 250 #field의 길이
thick = 1 #field의 두께
density = 1.3 #공기 밀도 ##kg/m**3

# ball, ballnoair, field 만들기
ball =   sphere(pos = vec(10,0,0), radius = 20*R, color = color.white)
ballnoair =   sphere(pos = vec(10,0,0), radius = 20*R, color = color.red) 
field =   box(pos = vec(L/2.,-thick/2.,0), size = vec(L,thick,L/4.), color = color.green)

# 물리 성질 초기화
ball.m = ballnoair.m = 0.155 #ball, ballnoair의 질량
v0 = 100*1600/3600. 
theta0 = 45*2*pi/360.
ball.p = ballnoair.p = ball.m*vec(v0*cos(theta0),v0*sin(theta0),0) #운동량

# 화면 설정
scene.width = 800
scene.height = 600
scene.x = scene.y = 0
scene.center = vec(0.45*L,0,0)
scene.forward = -vec(-L/4.,L/4.,L)

# 자취 그리기 (curve 함수 이용)
ball.trail = curve(color = ball.color, radius = ball.radius) 
ballnoair.trail = curve(color = ballnoair.color, radius = ballnoair.radius) 

# 벡터 Fgrav 지정 (중력)
Fgrav = vec(0,-ball.m*g,0)
# 시간 설정
dt = 0.01

for b in [ball, ballnoair]:
    t = 0
    # 시뮬레이션 루프 (바닥과 충돌 시 루프 탈출)
    while b.pos.y >= 0: 
        rate(300)
        # 경우1. ball 
        if b == ball:
            # 중력 + 공기저항력 
            F = Fgrav-0.5*C*density*pi*R**2*mag(b.p/b.m)*(b.p/b.m) 
        # 경우2. ballnoair
        else: 
            # 중력
            F = Fgrav   
        # 운동량, 위치 업데이트
        b.p = b.p + F*dt 
        b.pos = b.pos + (b.p/b.m)*dt 

        b.trail.append(pos=b.pos) #자취 업데이트

    # 시간 업데이트
    t = t+dt 

    scene.waitfor('click') #클릭 대기
