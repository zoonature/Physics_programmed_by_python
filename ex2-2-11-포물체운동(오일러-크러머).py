from vpython import *
#GlowScript 3.0 VPython

# 벡터 pos_i, v_i, acc 지정
pos_i = vec(-5,0,0) 
v_i = vec(1.0,0.5,0) 
acc = vec(0.0,-0.2,0) 


# cart, acart 만들기
cart = box(pos = pos_i, size = vec(0.3,0.3,0.3), color = color.yellow, make_trail = True, trail_type = "points", trail_radius = 0.02, interval = 2)
acart = box(pos = pos_i + vec(0,1,0), size = vec(0.3,0.3,0.3), color = color.white, make_trail = True, trail_type = "points", trail_radius = 0.02, interval = 2)

# 물리 성질 초기화
cart.v = v_i #cart의 초기 속도 ##m/s
acart.v = v_i #acart의 초기 속도 ##m/s

scale = 2.0  #크기 조정을 위한 변수

# cart의 속도 벡터 표현
cart_vel = arrow(pos = cart.pos, axis = scale*cart.v, shaftwidth = 0.1) 

# 화면 설정
scene.autoscale = False #수동으로 화면 조정
#scene.range = 5

# 시간 설정
t = 0 ##s
dt = 0.1 ##s

# 시뮬레이션 루프
while t < 10:
    rate(30)
    # 수치적인 방법으로 속도, 위치 업데이트 
    cart.v = cart.v + acc*dt
    cart.pos = cart.pos + cart.v*dt  
    # 벡터 cart_vel 업데이트
    cart_vel.pos = cart.pos #시작 좌표
    cart_vel.axis = scale*cart.v #축
    # 시간 업데이트
    t = t + dt
    # 해석적인 방법으로 위치 업데이트
    acart.pos = pos_i + vec(0,1,0) + v_i * t + 0.5*acc*t**2 

    # 출력
    print(cart.pos, acart.pos, mag(acart.pos-cart.pos)-1) 
