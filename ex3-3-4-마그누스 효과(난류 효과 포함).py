from vpython import *
#GlowScript 3.0 VPython

# ground, ball 만들기
ground  = box(pos = vec(0,-0.05,0), size = vec(100,0.10,70), color = color.green)
ball = sphere(pos = vec(0,0.11,0), radius = 0.11, color = color.yellow, make_trail = True)

# 물리 성질 초기화
ball.m = 0.45 #공의 질량
ball.speed = 32 
ball.angle = 20*pi/180 ##rad
ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0) #공의 초기 속도
wind_speed = 0 
wind_v = wind_speed*vec(1,0,0) #바람의 속도

# 상수 초기화
g = -9.8 #중력 가속도
rho = 1.204 #공기 밀도
Cdl = 0.275#0.3#0.3#1 #공기 저항계수(층류)
Cdt = 0.05 #공기 저항계수(난류)
w = 10*2*pi #각속도
Cml = 1 #마그누스 계수(층류)
Cmt = 0.05 #마스누스 계수(난류)

# 그래프
#gd = graph(xmin = 0, xmax = 20, ymin = -12, ymax = 12)
gball_vy = gcurve()
gball_y = gcurve(color = color.cyan)

scale = 0.2 #크기 조정을 위한 변수

# 공의 속도 벡터 표현
ball_vel = arrow(pos = ball.pos, axis = scale*ball.v, shaftwidth = 0.1)

# 화면 설정
#scene.autoscale = False
scene.range = 10
#scene.waitfor('click')

# 시간 설정
t = 0 ##s
dt = 0.01 ##s

# 시뮬레이션 루프
while t < 20:
    rate(100)
    # 중력
    grav = ball.m * vec(0,g,0) 
    # 공기저항력 & 마그누스 힘 
    ball.v_w = ball.v - wind_v
    vhat_per = cross(vec(0,1,0),norm(ball.v)) 
    # 경우1. 난류
    if mag(ball.v) > 30:
        Cd = Cdt
        Cm = Cmt
    # 경우2. 층류
    else:
        Cd = Cdl 
        Cm = Cml
    drag = -0.5*rho*Cd*(pi*ball.radius**2)*mag(ball.v_w)**2*norm(ball.v_w)
    magnus = 0.5*rho*Cm*ball.radius*w*mag(ball.v_w)*(pi*ball.radius**2)*vhat_per
    print(mag(grav), mag(drag), mag(magnus))
    # 알짜힘
    ball.f = grav + drag + magnus

    # 속도, 위치 업데이트
    ball.v = ball.v + ball.f/ball.m*dt
    ball.pos = ball.pos + ball.v*dt 
   
    # 공의 속도 벡터 업데이트 
    ball_vel.pos = ball.pos 
    ball_vel.axis = scale*ball.v 

    # 그래프 업데이트
    gball_vy.plot(pos = (t,mag(ball.v)))
    gball_y.plot(pos = (t,ball.pos.y))

    # 공과 바닥의 충돌 시 시뮬레이션 루프 탈출
    if ball.pos.y - ball.radius < 0:
        print(ball.pos.x)
        break

    # 시간 업데이트
    t = t + dt
