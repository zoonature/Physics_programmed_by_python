from vpython import *
#GlowScript 3.0 VPython

# ball1, ball2 만들기
ball1 = sphere(radius = 0.5*65.5e-3, make_trail = True)
ball2 = sphere(radius = 0.5*65.5e-3, make_trail = True, pos = vec(1,0.5*65.5e-3,0), color = color.red)

# 물리 성질 & 상수 초기화
ball1.v = vec(1,0,0) #ball1의 초기 속도
ball2.v = vec(0,0,0) #ball2의 초기 속도
ball1.m = 0.21 #ball1의 질량
ball2.m = 0.21 #ball2의 질량
ball1.f = vec(0,0,0) #ball1의 초기 알짜힘
ball2.f = vec(0,0,0) #ball2의 초기 알짜힘
e  = 1.0 #반발계수
tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2 

# 시간 설정
t = 0
dt = 0.01

# 그래프
traj = gcurve()
en_traj = gcurve(color = color.cyan)

# 화면 설정
scene.autoscale = True
scene.range = 1

# 충돌 처리 함수
def collision(b1, b2, e):
    c = b2.pos - b1.pos
    c_hat = norm(c)
    dist = mag(c)
    # 멀어지고 있는 경우 False 반환
    if dot(b1.v - b2.v, c_hat) < 0:
        return False
    v1_c = dot(b1.v,c_hat)*c_hat #b1의 속도 수평방향
    v1_p = b1.v - v1_c #b1의 속도 수직방향
    v2_c = dot(b2.v,c_hat)*c_hat #b2의 속도 수평방향
    v2_p = b2.v - v2_c #b2의 속도 수직방향
    tot_m = b1.m + b2.m

    # 충돌 시 두 물체의 속도 변경
    if dist < b1.radius + b2.radius:
        v1 = ((b1.m-e*b2.m)*v1_c + (1+e)*b2.m*v2_c) / tot_m
        v2 = ((b2.m-e*b1.m)*v2_c + (1+e)*b1.m*v1_c) / tot_m
        b1.v = v1 + v1_p
        b2.v = v2 + v2_p
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
    # 속도, 위치 업데이트
    ball1.v = ball1.v + ball1.f/ball1.m*dt
    ball2.v = ball2.v + ball2.f/ball2.m*dt
    ball1.pos = ball1.pos + ball1.v*dt
    ball2.pos = ball2.pos + ball2.v*dt
    # 두 공의 총 에너지  
    tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2
    # 그래프 업데이트
    traj.plot(pos = (t,mag(ball1.v)))
    en_traj.plot(pos = (t,tot_energy))
    # 시간 업데이트
    t = t + dt
