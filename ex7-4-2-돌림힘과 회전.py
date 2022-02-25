from vpython import *
#GlowScript 3.0 VPython

# 물리 성질 & 상수 초기화
M = 2 #rod의 질량
Lrod = 1 #rod의 길이
R = 0.1 #rod의 밑면 반지름
Laxle = 4*R #axle의 길이
I = (1/12)*M*Lrod**2 + (1/4)*M*R**2 #회전관성
L = vector(0,0,0) #각운동량

# rod, axle 만들기
rod = cylinder(pos = vec(-1,0,0), radius = R, color = color.orange, axis = vec(Lrod,0,0)) 
axle = cylinder(pos = vec(-1+Lrod/2,0,-Laxle/2), radius = R/6, color = color.red, axis = vec(0,0,4*R))

# 시간 설정
t = 0 
dt = 0.0001 
# 각변위 설정
dtheta = 0

# 시뮬레이션 루프
while t < 20 : 
    rate(1000)
    # 돌림힘
    torque = vec(0,0,20) 
    # 각운동량 업데이트
    L = L + torque*dt
    # 각속도, 각변위 업데이트 
    omega = L/I
    omega_scalar = dot(omega, norm(axle.axis)) 
    dtheta = omega_scalar * dt
    rod.rotate(angle=dtheta, axis=norm(axle.axis), origin=axle.pos) #회전
    # 시간 업데이트
    t = t + dt

