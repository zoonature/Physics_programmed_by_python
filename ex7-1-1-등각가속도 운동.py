from vpython import *
#GlowScript 3.0 VPython

# 지구 만들기
earth = sphere(radius = 6.4e6, texture = textures.earth)

# 물리 성질 초기화
earth.rot_axis = vec(0,1,0) #지구의 회전 축
earth.w = 2*pi/(24*60*60)*earth.rot_axis #지구의 초기 각속도 ##rad/s 
earth.alpha = -2*pi/(24*60*60)*earth.rot_axis/5000 #지구의 각가속도
#earth.alpha = vec(0,0,0) #지구의 각가속도를 0으로 설정

# 화면 설정
scene.range = 10e6
scene.waitfor('click')

# 시간 설정 
t = 0 ##s
dt = 60 ##s

# 시뮬레이션 루프
while t < 24*60*60:
    rate(1/dt*6000)
    # 각속도, 각변위 업데이트 (Euler – Cromer Method)
    earth.w = earth.w + earth.alpha*dt
    dtheta = mag(earth.w)*dt
    earth.rotate(angle=dtheta,axis=norm(earth.w), origin=earth.pos) #회전
    t = t + dt # 시간 업데이트

