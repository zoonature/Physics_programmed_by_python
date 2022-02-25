from vpython import *
#GlowScript 3.0 VPython

# 화면 설정
scene.center = vec(0, -5, 0)

# 천장, 추, 실 만들기
ceiling = box(size = vec(20,0.1,10))
ball = list()
ballr = list()
ceilr = list()
for i in range(10):
    ballr.append(vec(2*i-9, -(i+15), 15))
    ceilr.append(vec(2*i-9,0,0))
for i in ballr:
    ball.append(sphere(pos = i, texture = textures.metal, make_trail = True))
rod = list()
for i in range(10):
    rod.append(cylinder(axis = vec(0, ball[i].pos.y,ball[i].pos.z),  pos = vec(ball[i].pos.x,0,0), color = color.blue, radius = 0.1))

# 물리 성질 & 상수 초기화
for i in range(10):
    ball[i].v = vec(0,0,0) #공의 초기 속도
    ball[i].w = 0*vec(0,0,1) #공의 초기 각속도
    ball[i].m = 1 #공 질량
    ball[i].l =  2/5*ball[i].m*mag(ball[i].pos-ceilr[i])**2 #공의 회전관성
 
for i in range(10):
    rod[i].m = 1 #실 질량
    rod[i].center = 0.5*(ball[i].pos - ceilr[i]) #실 무게중심
    rod[i].l = 1/3*rod[i].m*mag(ball[i].pos-ceilr[i])**2 #실의 회전관성
g = vec(0,-9.8,0) #중력 가속도

# 시간 설정
t = 0
dt = 0.01

# 초기 중력, 돌림힘
for i in range(10):   
    ball[i].f = ball[i].m*g
    ball[i].torque = cross(ball[i].pos-ceilr[i], ball[i].f)
for i in range(10): 
    rod[i].f = rod[i].m * g
    rod[i].torque = cross(rod[i].center-ceilr[i], rod[i].f)

scene.waitfor('click') #클릭 대기

# 시뮬레이션 루프
while True:
    rate(100)
    for i in range(10):
        # 중력, 돌림힘
        rod[i].center =  0.5*(ball[i].pos- ceilr[i])
        ball[i].torque = cross(ball[i].pos - ceilr[i], ball[i].f) 
        rod[i].torque = cross(rod[i].center - ceilr[i]+vec(ball[i].pos.x,0,0),rod[i].f) 
        torque = ball[i].torque + rod[i].torque
        
        # 각속도, 각변위 업데이트
        ball[i].w += torque/(ball[i].l+rod[i].l)*dt
        ball[i].dangle = mag(ball[i].w)*dt
        ball[i].rotate(angle = ball[i].dangle,axis = norm(ball[i].w), origin=ceilr[i])
        rod[i].axis = vec( ball[i].pos.x-ceilr[i].x, ball[i].pos.y,ball[i].pos.z)
        
        # 시간 업데이트
        t += dt
