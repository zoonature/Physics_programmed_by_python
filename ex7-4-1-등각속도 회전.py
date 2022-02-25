from vpython import *
#GlowScript 3.0 VPython

# obj1 만들기
obj1 = box(texture = textures.wood)

# 벡터 omega 지정 (회전축)
omega = vec(-3.0,1.0,2.0)

# 벡터 omega 표현 
omega_axis = arrow(pos = -0.5*omega, axis = omega, shaftwidth = 0.02, color = color.red)

# 화면 설정
scene.range = 3

# 시간 설정
t = 0
dt = 0.01

# 시뮬레이션 루프
while 1:
    rate(100)
    # 각변위 업데이트
    dtheta = mag(omega)*dt
    obj1.rotate(angle = dtheta, axis = norm(omega)) #회전
    