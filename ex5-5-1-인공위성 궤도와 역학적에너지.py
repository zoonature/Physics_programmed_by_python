from vpython import *
#GlowScript 3.0 VPython

sf = 6 #크기 조정을 위한 변수

# 시간 설정
t = 0 
dt = 60*60 

# 상수 초기화
G = 6.673e-11 #중력 상수
r = 384400000 
# 지구, 달 만들기
Earth = sphere(pos = vector(0,0,0), radius = sf*6400000, texture = textures.earth)
Moon = sphere(pos = vector(r,0,0), radius = sf*1737000, color = color.white, make_trail = True)

# 물리 성질 초기화
Earth.mass = 5.972e24 #지구 질량
Moon.mass = 7.36e22 #달 질량 

# 달의 초기속도 설정
vi = sqrt(G*Earth.mass/r**1) 
#Moon.v = vec(0,0,0)
Moon.v = vec(0,vi*0.7,0) #타원
#Moon.v = sqrt(2)*vec(0,vi,0) 
#Moon.v = sqrt(3)*vec(0,vi,0) #쌍곡선
#Earth.v = vec(0,0,0)
Earth.v = -Moon.v*Moon.mass/Earth.mass 
# 그래프
k_graph = gcurve(color = color.cyan) 
u_graph = gcurve(color = color.green)
ku_graph = gcurve(color = color.black)

# 화면 설정
scene.waitfor('click')

# 시뮬레이션 루프
while t < 10*365*24*60*60:
    rate(100)
    # 만유인력
    r = Moon.pos-Earth.pos 
    Moon.f = -G*Earth.mass*Moon.mass/mag(r)**2*norm(r) 
    # 뉴턴 제 3법칙 적용 (작용반작용)
    Earth.f= -Moon.f 
    # 속도, 위치 업데이트
    Moon.v = Moon.v + Moon.f/Moon.mass*dt 
    #Earth.v = Earth.v + Earth.f/Earth.mass*dt
    Moon.pos = Moon.pos + Moon.v*dt
    #Earth.pos = Earth.pos + Earth.v*dt
    # 에너지 업데이트
    k = 0.5*Moon.mass*mag(Moon.v)**2 #운동에너지
    u = -G*Earth.mass*Moon.mass/mag(Moon.pos) #퍼텐셜 에너지
    # 그래프 업데이트
    k_graph.plot(t/60/60/24, k)
    u_graph.plot(t/60/60/24, u)
    ku_graph.plot(t/60/60/24, k + u)
    # 달과 지구의 충돌시 시뮬레이션 루프 탈출
    if mag(r) < Earth.radius+Moon.radius: 
        print(t/60/60/24)
        break 
        
    # 시간 업데이트
    t = t + dt