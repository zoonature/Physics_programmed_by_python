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
r0 = 0.25 #스프링 초기길이
ks = 100  #탄성계수
kv = 0  #감쇠계수

# 화면 설정
scene.autoscale = True          
scene.center = vec(0,-r0,0)   

# 그래프
traj = gcurve(color = color.red)

# 함수
def fx(t, x, v):
    global ks
    global kv
    global ball
    global g
    global r0
    
    # 중력
    Fgrav = ball.m*g
    # 스프링 힘
    r = mag(x)
    s = r - r0
    rhat = norm(x)
    Fspr = -ks*s*rhat
    # 댐퍼 힘
    Fdamp = -kv*dot(v,rhat)*rhat    
    # 알짜힘
    Fnet = Fgrav + Fspr + Fdamp
    # 가속도
    a = Fnet/ball.m 
    # 속도, 가속도 반환
    return v, a 

# 시간 설정
t = 0           
dt = 0.01

# 시뮬레이션 루프
while t < 300:
    rate(100)
    
    # 속도, 위치 업데이트 (4차 룽게-쿠타 방법)
    k1_v, k1_a = fx(t, ball.pos, ball.v)
    k2_v, k2_a = fx(t + dt/2,  ball.pos + dt * k1_v/2, ball.v + dt * k1_a/2)
    k3_v, k3_a = fx(t + dt/2,ball.pos + dt * k2_v/2, ball.v + dt * k2_a/2)
    k4_v, k4_a = fx(t + dt, ball.pos + dt * k3_v,  ball.v + dt * k3_a)    
    ball.pos = ball.pos + dt * ((1/6) *k1_v + (1/3)*k2_v + (1/3)*k3_v+(1/6)*k4_v)
    ball.v = ball.v + dt * ((1/6) * k1_a + (1/3)*k2_a + (1/3)*k3_a + (1/6)*k4_a)
    
    # 시간 업데이트
    t = t + dt
    
    # 스프링 업데이트
    spring.axis = ball.pos
    
    # 그래프 업데이트
    traj.plot(pos = (t,ball.pos.y))
