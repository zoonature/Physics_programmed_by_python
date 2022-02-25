from vpython import *
#GlowScript 3.0 VPython

# 리스트 생성
rList = list()
objList = list()

# 바닥 만들기 
ground = box(pos = vec(0,-5,0), size = vec(15, 0.01,15))

# 위치 벡터 리스트 초기화
for i in range(0,100):
    rList.append(vec(0,-4,0)) 

# 불꽃 입자 리스트 초기화
for r in rList:
    objList.append(sphere(pos = r, radius = 0.1, color = vec(random(),      random(), random()), make_trail = True, retain = 30))  

# 벡터 vi, a 지정
vi = vec(0,5.0,0) 
a = vec(0,-3,0)

explosion = False #폭발 여부

# 불꽃 입자의 초기 속도 설정
for obj in objList:
    obj.v = vi
    
# 시간 설정
t = 0
dt = 0.01

# 시뮬레이션 루프
while t < 12:
    rate(1/dt)
    # 폭발 (불꽃놀이 시작 1초 후 & 아직 폭발하기 전)
    if t > 1 and explosion == False:
        print("explosion!")
        explosion = True  #폭발 여부 업데이트
        # 모든 입자에 대해 폭발 시 속도 변경
        for obj in objList:
            vp = vec(random()-0.5, random()-0.5, random()-0.5)
            obj.v = obj.v + vp
    # 모든 입자에 대해 속도, 위치 업데이트 적용      
    for obj in objList:
        obj.v = obj.v + a*dt
        obj.pos = obj.pos + obj.v*dt
        # 바닥과 충돌 시 불꽃 입자의 위치, 속도, 색 변경
        if obj.pos.y < ground.pos.y:
            obj.pos.y = ground.pos.y 
            obj.v.y = -0.8*obj.v.y 
            obj.color =  vec(random(), random(), random()) 
  
    # 시간 업데이트
    t = t + dt 
