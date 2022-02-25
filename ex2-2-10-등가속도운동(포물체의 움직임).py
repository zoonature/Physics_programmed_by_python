from vpython import *
#GlowScript 3.0 VPython

# 공, 바닥 만들기
ball = sphere(radius = 0.2)
ground =box(pos = vec(0,-4,0), size = vec(15,-0.01,5)) 


# 물리 성질 초기화
ball.pos = vec(-2,0,0) #공의 초기 위치 ##m
ball.v = vec(1,1,0) #공의 초기 속도 ##m/s 
ball.a = vec(0,-0.35,0) #공의 가속도 ##m/s**2


# 시간 설정
t = 0 ##s
dt = 0.01##s


# 화살표 부착
attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) 
attach_arrow(ball, "a", shaftwidth = 0.05, color = color.red)


# 자취 그리기
attach_trail(ball, type = 'points', pps = 5) 


# 그래프
motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'y') 
g_bally = gcurve()
motion_graph2 = graph(title = 'velocity-time', xtitle = 't', ytitle = 'vy') 
g_ballvy = gcurve(color = color.green)


# 시뮬레이션 루프 (공이 바닥에 닿을 때까지)
while ball.pos.y > ground.pos.y:
    rate(1/dt)
    # 속도, 위치 업데이트
    ball.v = ball.v + ball.a*dt 
    ball.pos = ball.pos + ball.v*dt 
    # 그래프 업데이트
    g_bally.plot(pos = (t,ball.pos.y)) 
    g_ballvy.plot(pos = (t,ball.v.y)) 
    # 시간 업데이트
    t = t + dt 
