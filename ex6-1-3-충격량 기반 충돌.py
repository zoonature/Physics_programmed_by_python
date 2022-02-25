from vpython import *
#GlowScript 3.0 VPython

# ball1, ball2 만들기
ball1 = sphere(radius = 0.5*65.5e-3, make_trail = True) 
ball2 = sphere(radius = 0.5*65.5e-3, make_trail = True, pos = vec(0.3,-0.1*65.5e-3,0), color = color.red)

# 물리 성질 & 상수 초기화
ball1.v = vec(1,0,0) 
ball2.v = vec(0,0,0) 
ball1.m = 0.41
ball2.m = 0.21
ball1.f = vec(0,0,0) 
ball2.f = vec(0,0,0)
e  = 0.99
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
    c = b1.pos - b2.pos
    c_hat = norm(c)
    dist = mag(c)
    v_relm = dot(b1.v - b2.v, c_hat)
    # 멀어지고 있는 경우 False 반환
    if  v_relm > 0:
        return False

    # 충돌시 두 물체의 속도 변경 (충격량 기반)
    if dist < b1.radius + b2.radius:
        j = -(1+e)*v_relm
        j = j/(1/b1.m+1/b2.m)
        b1.v = b1.v + j*c_hat/b1.m
        b2.v = b2.v - j*c_hat/b2.m        
    else:
        return False

# 시뮬레이션 루프
while t < 10:
    rate(100)
    # 충돌 처리 (collision 함수 이용)
    colcheck = collision(ball1,ball2, e)
    if colcheck == True:
        print("Collision!")
        #scene.waitfor('click')

    # 속도, 위치 업데이트
    ball1.v = ball1.v + ball1.f/ball1.m*dt
    ball2.v = ball2.v + ball2.f/ball2.m*dt
    ball1.pos = ball1.pos + ball1.v*dt
    ball2.pos = ball2.pos + ball2.v*dt

    # 두 공의 총 에너지  
    tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2
    # 그래프 업데이트
    traj.plot(pos=(t,mag(ball1.v)))
    en_traj.plot(pos=(t,tot_energy))
    # 시간 업데이트
    t = t + dt

