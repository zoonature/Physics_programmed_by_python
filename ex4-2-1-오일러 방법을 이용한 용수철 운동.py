from vpython import *
#GlowScript 3.0 VPython

# 천장, 공, 스프링 만들기
ceiling = box(pos = vec(0,0,0), size = vec(0.2, 0.01, 0.2))        
ball = sphere(pos = vec(0.0, -0.25,0.0), radius = 0.025, color = color.orange, make_trail = True)
spring = helix(pos = ceiling.pos, axis = ball.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)

# 물리 성질 & 상수 초기화
ball.v = vec(0,0,0) #공의 초기속도
g = vec(0,-9.8,0) #중력가속도
ball.m = 1 #공의 질량
r0 = 0.25 #스프링 초기 길이
ks = 100  #탄성계수
kv = 0.0  #감쇠계수

# 시간 설정
t = 0           
dt = 0.01  

# 화면 설정
scene.autoscale = True          
scene.center = vec(0,-r0,0)      

# 그래프
traj = gcurve(color = color.red)

# 시뮬레이션 루프
while t < 300:
    rate(100)
    # 중력
    Fgrav = ball.m*g
    # 스프링 힘
    r = mag(ball.pos)
    s = r - r0
    rhat = norm(ball.pos)
    Fspr = -ks*s*rhat
    # 댐퍼 힘
    Fdamp = -kv*dot(ball.v,rhat)*rhat    

    # 알짜힘
    Fnet = Fgrav + Fspr + Fdamp

    # 위치, 속도 업데이트 (오일러 방법)
    ball.pos = ball.pos + ball.v*dt
    ball.v = ball.v + Fnet/ball.m*dt

    # 시간 업데이트
    t = t + dt

    # 스프링 업데이트
    spring.axis = ball.pos

    # 그래프 업데이트
    traj.plot(pos = (t,ball.pos.y))