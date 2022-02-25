from vpython import *
#GlowScript 3.0 VPython


# 3차원 좌표축 표현
x_axis = arrow(pos = vec(0,0,0), axis = vec(10,0,0), color = color.red, shaftwidth =0.1)
y_axis = arrow(pos = vec(0,0,0), axis = vec(0,10,0), color = color.green, shaftwidth =0.1)
z_axis = arrow(pos = vec(0,0,0), axis = vec(0,0,10), color = color.blue, shaftwidth =0.1)

# 공 만들기
ball = sphere(pos = vec(3,4,5), radius = 0.2)

# 스칼라 곱 계산
#ball.pos = ball.pos*2.0
ball.pos = ball.pos/2.0
print("ball.pos = ", ball.pos)

# 벡터 크기 계산
ball.mag = mag(ball.pos) 
check_ball_mag = sqrt(ball.pos.x**2 + ball.pos.y**2 + ball.pos.z**2) 
print("ball.mag = ", ball.mag)
print("check! mag.: ", check_ball_mag)

# 단위 벡터 계산
ball.dir = ball.pos/ball.mag 
#ball.dir = norm(ball.pos) 
print("ball.dir = ", ball.dir)
print("check! mag of unit vector: ",mag(ball.dir)) 

# 원점에서 ball을 가리키는 벡터 표현
pos_vec = arrow(pos = vec(0,0,0), axis = ball.pos, color = color.yellow, shaftwidth = 0.2) 
