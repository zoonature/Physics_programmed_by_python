from vpython import *
#GlowScript 3.0 VPython


# 벡터 pos_i, v_i 지정
pos_i = vec(-5, 0, 0) 
v_i = vec(1.0, 0, 0) 

# cart, acart 만들기 (자취 그리기 포함)
cart = box(pos = pos_i,size = vec(0.3,0.3,0.3), color = color.yellow, 
make_trail = True, trail_type = "points", trail_radius = 0.02, interval = 2)
acart = box(pos = pos_i + vec(0,1,0), size = vec(0.3,0.3,0.3), color = color.white, make_trail = True, trail_type = "points", trail_radius = 0.02, interval = 2)

# 화면 설정
scene.autoscale = True

# 시간 설정
t = 0 ##s
dt = 0.1 ##s
# 시뮬레이션 루프
while t < 10:
    rate(100)
    # 수치적인 방법으로 위치 업데이트
    cart.pos = cart.pos + v_i*dt 
    t = t + dt
    # 해석적인 방법으로 위치 업데이트 
    acart.pos = pos_i+vec(0,1,0) + v_i * t 
