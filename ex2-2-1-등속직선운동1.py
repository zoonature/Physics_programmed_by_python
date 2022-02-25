from vpython import *
#GlowScript 3.0 VPython


# 공 만들기
ball = sphere(radius = 0.2) ##m

# 물리 성질 초기화
ball.pos = vec(-2,0,0) #공의 초기 위치 ##m
ball.v = vec(0.8,0,0) #공의 속도 ##m/s

# 시간 설정
t = 0 ##s
dt = 1 ##s

# 화살표 부착
attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) 
# 위치 업데이트1
scene.waitfor('click')
ball.pos = ball.pos + ball.v*dt #r1 → r2
t = t + dt

# 위치 업데이트2
scene.waitfor('click')
ball.pos = ball.pos + ball.v*dt #r2 → r3
t = t + dt

# 위치 업데이트3
scene.waitfor('click')
ball.pos = ball.pos + ball.v*dt #r3 → r4
t = t + dt

# 위치 업데이트4
scene.waitfor('click')
ball.pos = ball.pos + ball.v*dt #r4 → r5
t = t + dt
