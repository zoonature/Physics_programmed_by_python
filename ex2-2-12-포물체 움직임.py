from vpython import *
#GlowScript 3.0 VPython

# 벡터 pos_i, v_i, acc 지정
pos_i = vec(-5,0,0)
v_i = vec(1.0,1.5,0)
acc = vec(0.0,-0.2,0)
# cart 만들기
cart = box(pos = pos_i, size = vec(0.3,0.3,0.3), color = color.yellow, make_trail = True)

# 물리 성질 초기화
cart.v = v_i #cart의 초기 속도 ##m/s

# 그래프
gd = graph(xmin = 0, xmax = 20, ymin = -12, ymax =12)
gcart_vy = gcurve()
gcart_y = gcurve(color = color.cyan)

scale = 2.0  #크기 조정을 위한 변수

# 벡터 cart_vel 표현 (cart의 속도 벡터)
cart_vel = arrow(pos = cart.pos, axis = scale*cart.v, shaftwidth = 0.1)

# 화면 설정
scene.autoscale = False
scene.range = 10

# 시간 설정
t = 0 ##s
dt = 0.1 ##s

# 시뮬레이션 루프
while t < 20:
    rate(30)
    # 속도, 위치 업데이트
    cart.v = cart.v + acc*dt 
    cart.pos = cart.pos + cart.v*dt 
    # 벡터 cart_vel 업데이트
    cart_vel.pos = cart.pos #시작 좌표
    cart_vel.axis = scale*cart.v #축

    # 그래프 업데이트
    gcart_vy.plot(pos = (t,cart.v.y)) 
    gcart_y.plot(pos = (t,cart.pos.y))
    # 시간 업데이트
    t = t + dt 
