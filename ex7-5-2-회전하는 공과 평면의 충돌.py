from vpython import *
#GlowScript 3.0 VPython


# 충돌 처리 함수
def collision(ball, plane):
    col = False
    # 충돌 확인
    if ball.pos.y - ball.radius < plane.pos.y + plane.height/2:
        ball.pos.y = ball.radius + plane.pos.y + plane.height/2
        col = True
        
    # 충돌 처리 (각운동량 변화를 고려)
    if col == True:
        n_hat = vec(0,1,0)
        cr = -ball.radius*n_hat
        ball.vel = ball.vel + cross(ball.omega, cr)
                
        j = -(1+e)*ball.vel.y
        I1 = cross(cr,n_hat)/ball.I
        I2 = cross(I1,cr)
        I3 = dot(n_hat,I2)
        j /= 1/ball.mass + I3
        
        ball.vel += j/ball.mass*n_hat
        ball.omega += cross(cr,j*n_hat)/ball.I
        ball.w = ball.omega.z    
             
        # 마찰에 의한 충격량 고려
        f_t = -dot(ball.vel,-n_hat)*n_hat
        f_t = ball.vel - f_t

        if mag(f_t) > tol:
            f_hat = norm(f_t)
        else:
            f_hat = vec(0,0,0)
        jt = -dot(f_t,f_hat)
        muj = mu*j
        if -muj < jt < muj:
            I1 = cross(cr,f_hat)/ball.I
            I2 = cross(I1,cr)
            I3 = dot(f_hat,I2)
            jt /= 1/ball.mass + I3

        elif -muj >= jt:
            jt= -muj
        elif muj <= jt:
            jt = muj
        else:
            jt = 0

        ball.vel += jt/ball.mass*f_hat
        ball.omega += cross(cr,jt*f_hat)/ball.I
        
        # 구름 마찰
        ball.omega += -k_g*ball.omega*dt
        ball.w = ball.omega.z  
              
    return col



# 상수 초기화
M = 2 #공의 질량
R = 1 #공의 반지름
I = 2/5*M*R**2 #공의 회전관성
tol = 1e-8 # 비교를 위한 작은 변수
e = 0.9 #탄성계수
mu = 0.5 #마찰계수
#air resist.for rotation
k = 0.0
#ground resist. for rotation
k_g = 0

# 공, 평면 만들기
ball = sphere(pos = vec(0,4,0), radius = R, texture = textures.earth) 
plane = box(pos = vec(0,-10,0), length = 30, height = 0.1, width = 30, color = color.green)

# 물리 성질 초기화
ball.vel = vec(0,0,0) #공의 초기속도
ball.mass = M #공의질량
ball.I = I #공의 회전관성
ball.angle_z = 0 #-pi/3#pi/3#0#-pi/2#0#pi/3 #공의 초기 각변위
ball.w = 10  #공의초기 각속력
ball.omega = vec(0,0,ball.w) #공의 초기 각속도
dtheta = 0
ball.rotate(angle = ball.angle_z, axis = vec(0,0,1)) #공의 초기 회전
g = vec(0,-9.8,0) #중력가속도


# 시간 설정
t = 0
dt = 0.01

# 시뮬레이션 루프
while t < 100:
    rate(100)
    # 중력
    F = ball.mass*g
    # 충돌 처리
    col = collision(ball,plane)
    # 충돌하지 않은 경우
    if !col:
        # 속도, 위치 업데이트 (병진운동)
        ball.vel = ball.vel + F/ball.mass*dt
        ball.pos = ball.pos + ball.vel*dt
    
        # 돌림힘, 각속도 업데이트 (회전운동)
        ball.T = -k*ball.omega
        ball.omega = ball.omega + ball.T*dt
        ball.w = ball.omega.z
    
    # 각변위 업데이트
    dtheta = ball.w*dt
    ball.angle_z = ball.angle_z + dtheta
    ball.rotate(angle=dtheta, axis=vec(0,0,1))
    
    # 시간 업데이트
    t = t + dt
