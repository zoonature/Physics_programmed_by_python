from vpython import *
#GlowScript 3.0 VPython

# ball1, ball2 만들기
ball1 = sphere(radius = 0.5*65.5e-3) 
ball2 = sphere(radius = 0.5*65.5e-3, pos = vec(1,0,0), color =color.red)

# 물리 성질 & 상수 초기화
ball1.v = vec(1,0,0) #ball1의 초기속도
ball2.v = vec(0,0,0) #ball2의 초기속도
ball1.m = 0.21 #ball1의 질량
ball2.m = 0.21 #ball2의 질량
ball1.f = vec(0,0,0) #ball1의 초기 알짜힘
ball2.f = vec(0,0,0) #ball2의 초기 알짜힘
e  = 1.0 #반발계수 
tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2 

# 시간 설정
t = 0
dt = 0.03

# 그래프
traj = gcurve()
en_traj = gcurve(color = color.cyan)

# 화면 설정
scene.autoscale = True
scene.range = 2

# 충돌 처리 함수 
def collision(b1, b2, e):
    dist = mag(b1.pos - b2.pos)
    tot_m = b1.m + b2.m 
    # 충돌 시 두 물체의 속도 변경
    if dist < b1.radius + b2.radius: 
        v1 = ((b1.m-e*b2.m)*b1.v + (1+e)*b2.m*b2.v) / tot_m
        v2 = ((b2.m-e*b1.m)*b2.v + (1+e)*b1.m*b1.v) / tot_m
        b1.v = v1
        b2.v = v2
        return True
    else:
        return False

# 시뮬레이션 루프
while t < 10:
    rate(30)
    # 충돌 처리 (collision 함수 이용)
    colcheck = collision(ball1,ball2, e) 
    if colcheck == True:
        print("Collision!")
    # 속도, 위치 업데이트 (Euler – Cramer Method)
    ball1.v = ball1.v + ball1.f/ball1.m*dt 
    ball2.v = ball2.v + ball2.f/ball2.m*dt
    ball1.pos = ball1.pos + ball1.v*dt
    ball2.pos = ball2.pos + ball2.v*dt
    # 두 공의 총 에너지     
    tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2
    # 그래프 업데이트
    traj.plot(pos = (t,ball1.v.x))
    en_traj.plot(pos = (t,tot_energy))
    # 시간 업데이트
    t = t + dt
