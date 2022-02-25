from vpython import *
#GlowScript 3.0 VPython

# 지구, 달 탐사선, 달 만들기
Earth = sphere(pos = vec(0,0,0), radius = 6.4e6, color = color.blue)
craft = sphere(pos = vec(-10*Earth.radius,0,0), radius = 1e6, color = color.yellow, make_trail = True)
Moon  = sphere(pos = vec(4e8,0,0), radius = 1.75e6)

# 물리 성질 & 상수 초기화
G = 6.7e-11 #중력 상수
Earth.m = 6e24 #지구 질량
craft.m = 15e3 #달 탐사선 질량
Moon.m = 7e22 #달 질량

# 달 탐사선 초기속도 초기화
craft.v = vec(0,2e3,0) #1.달이 없을 경우
#craft.v = vec(0,4e3,0)  #2.쌍곡선1
#craft.v = vec(0,3.5e3,0) #3.쌍곡선2
#craft.v = vec(0,3.27e3,0) #4.임계속도

# 시간 설정
t = 0
dt = 60

# 시뮬레이션 루프
while t < 10*365*24*60*60:
    rate(500)    
    # 지구 – 달 만유인력
    r = craft.pos - Earth.pos
    rmag = mag(r)
    rhat = r/rmag
    Earth.f = -G*Earth.m*craft.m/rmag**2*rhat 
    # 달 – 달 탐사선 만유인력
    rmoon = craft.pos - Moon.pos
    rmoon_mag = mag(rmoon)
    rmoon_hat = rmoon/rmoon_mag
    Moon.f = -G*Moon.m*craft.m/rmoon_mag**2*rmoon_hat 

    # 알짜힘 (달과 지구가 달 탐사선에 가하는 힘)
    craft.f = Earth.f + Moon.f
    #print("Fnet = ", craft.f) #출력

    # 속도, 위치 업데이트
    craft.v = craft.v + craft.f/craft.m*dt
    craft.pos = craft.pos + craft.v*dt

    # 시간 업데이트
    t = t + dt
