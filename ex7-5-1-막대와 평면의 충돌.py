from vpython import *
#GlowScript 3.0 VPython

# 상수 초기화
M = 2 #막대 질량
l = 8 #막대 길이
h = 0.1 #막대 밑면 가로 길이
w = 0.1 #막대 밑면 세로 길이
I = (1/12)*M*(l**2 + h**2) #막대의 회전관성
e = 0.5 #반발 계수
mu =0.5 #마찰 계수

# 막대, 평면 만들기
rod = box(pos = vec(0,4,0), size = vec(l,h,w)) 
plane = box(pos = vec(0,-10,0), length = 30, height = 0.1, width = 30, color = color.green)

# 물리 성질 초기화
rod.vel = vec(0,0,0) #막대 초기 속도
rod.mass = M #막대 질량
rod.I = I #막대 회전관성
rod.angle_z = -pi/3#pi/3#0#-pi/2#0#pi/3
rod.w = 1 #막대 초기 각속력
rod.omega=vec(0,0,rod.w) #막대 초기 각속도
dtheta = 0
g = vec(0,-9.8,0) #중력 가속도

# 회전
rod.rotate(angle = rod.angle_z, axis = vec(0,0,1)) 

# 막대와 평면의 충돌 처리 함수
def collision(rod, plane):
    lcol = False #왼쪽 충돌 여부
    rcol = False #오른쪽 충돌 여부
    rod.ly = rod.pos.y - 1/2*rod.size.x*sin(rod.angle_z) 
    rod.ry = rod.pos.y + 1/2*rod.size.x*sin(rod.angle_z) 
    ly = plane.pos.y + 0.5*plane.height - rod.ly #막대 왼쪽 끝 위치
    ry = plane.pos.y + 0.5*plane.height - rod.ry #막애 오른쪽 끝 위치

    # 충돌 여부 확인
    if ly > 0 and ry < 0:
        rod.pos.y += ly
        lcol = True
    if ry > 0 and ly < 0:
        rod.pos.y += ry
        rcol = True
    if ly > 0 and ry > 0:
        if ly > ry:
            rod.pos.y += ly
        else:
            rod.pos.y += ry
        lcol = True
        rcol = True
    rod.lp = vec(0,0,0)
    rod.lp.x = rod.pos.x - 1/2*rod.size.x*cos(rod.angle_z)
    rod.lp.y = rod.pos.y - 1/2*rod.size.x*sin(rod.angle_z)
    rod.lp.z = rod.pos.z
    
    rod.rp = vec(0,0,0)
    rod.rp.x = rod.pos.x + 1/2*rod.size.x*cos(rod.angle_z)
    rod.rp.y = rod.pos.y + 1/2*rod.size.x*sin(rod.angle_z)
    rod.rp.z = rod.pos.z
    
    # 충돌 처리 (각운동량 변화를 고려)
    if lcol == True or rcol == True:
        cr = vec(0,0,0)
        if lcol == True and rcol != True:
            cr = rod.lp - rod.pos
        if rcol == True and lcol != True:
            cr = rod.rp - rod.pos
        if rcol == True and lcol == True:
            cr = rod.pos
        rod.cvel = rod.vel + cross(rod.omega, cr)
        n_hat = vec(0,1,0)
            
        j = -(1+e)*rod.cvel.y
        I1 = cross(cr,n_hat)/rod.I
        I2 = cross(I1,cr)
        I3 = dot(n_hat,I2)
        j /= 1/rod.mass + I3      
        rod.vel += j/rod.mass*n_hat
        rod.omega += cross(cr,j*n_hat)/rod.I
        rod.w = rod.omega.z
        
        # 마찰에 의한 충격량 고려
        v_t = dot(rod.cvel,n_hat)*n_hat
        v_t = rod.cvel - v_t
        t_hat = norm(v_t)
  
        jt = mag(v_t)
        I1 = cross(cr,t_hat)/rod.I
        I2 = cross(I1,cr)
        I3 = dot(t_hat,I2)
        jt /= -(1/rod.mass + I3)      
        muj = mu*j
        jt = max(jt, -muj)
        jt = min(jt, muj)

        rod.vel += jt/rod.mass*t_hat
        rod.omega += cross(cr,jt*t_hat)/rod.I
        rod.w = rod.omega.z            
    return lcol or rcol

# 시간 설정
t = 0
dt = 0.01

# 시뮬레이션 루프
while t < 100:
    rate(100)
    # 중력
    F = rod.mass*g
    # 속도, 위치 업데이트 (병진 운동)
    rod.vel = rod.vel + F/rod.mass*dt
    rod.pos = rod.pos + rod.vel*dt
    # 각변위 업데이트 (회전 운동)
    dtheta = rod.w*dt
    rod.angle_z = rod.angle_z + dtheta
    rod.rotate(angle = dtheta, axis = vec(0,0,1)) 
    
    # 충돌 처리 
    collision(rod, plane)
    
    # 시간 업데이트
    t = t + dt

