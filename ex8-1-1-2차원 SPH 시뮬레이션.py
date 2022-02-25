from vpython import *
#GlowScript 3.0 VPython

# 화면 설정
scene.autoscale = True
scene.center = vec(50,50,0)
 
# 상수 초기화
radiusSphere = 2 #파티클 반지름
column = 5 #가로 파티클 개수
row = 20 #세로 파티클 개수
numOfSphere = column * row #전체 파티클 개수
kernel = radiusSphere * 2 #커널 크기
side_space = 0.9*kernel #파티클 좌우 간격
high_space = 0.9*kernel #파티클 위 아래 간격

#수조, 파티클 만들기
watertank = box(pos = vec(55,50,0), size = vec(110,150,10), color = color.cyan, opacity = 0.2)
a = []
for i in range(0, row):
    for j in range(0,column):
        a.append(sphere(pos = vec(2+j*side_space, high_space*i-22, 0),
                            radius = radiusSphere, color = color.white))

# 물리 성질 초기화
for i in a :
    i.mass = 12 #파티클 질량
    i.vel = vec(0,0,0) #파티클 초기 속도
    i.density = 0 #파티클 밀도
    i.pressure = 0 #파티클 초기 압력
    i.viscosity = vec(0,0,0) #파티클 초기 점성힘
    i.pressureforce = vec(0,0,0) #파티클 초기 압력힘
    i.force = vec(0,0,0) #파티클 초기 외력

m_kernel_h = radiusSphere * 2 #+ 0.5 #12 #정지 상태일때 커널 크기
m_limit_velocity = 80 #파티클 최대 속도

mu = 100 #마찰계수
gravity = -9.8 #중력가속도
repulsive = 0.3 #경계면처리 상수
m_restDensity = a[0].mass * poly6Kernel(0, m_kernel_h) #고유밀도
k = 5000 #압력과 밀도 관련 상수

# 경계설정
boundary_xmin = watertank.pos.x - watertank.size.x/2+radiusSphere
boundary_xmax = watertank.pos.x + watertank.size.x/2-radiusSphere
boundary_ymin = watertank.pos.y - watertank.size.y/2+radiusSphere
boundary_ymax = watertank.pos.y + watertank.size.y/2-radiusSphere

# poly6커널(2D)
def poly6Kernel(r, h):
    if r < 0 or h < r:
        return 0
    return (4*(h*h-r*r)**3 / (pi*(h**8)))

# spiky커널(2D)
def grid_Spiky(r,h,dis):
    if r == 0 or r > h:
        return 0
    return (30 / (pi*h**6)*(h-r)**2*h*dis/r)

# viscosity커널(2D)
def viscosityKernel(r, h):
    if r < 0 or r > h:
        return 0    
    return (40/(pi*h**5)* (h-r))
   
# 경계면 처리 함수
def boundary(obj, y_min, y_max, x_min, x_max, repul):
  if obj.pos.y < y_min:
      obj.pos.y = y_min
      obj.vel.y *= -repul
  if obj.pos.y > y_max:
     obj.pos.y = y_max
     obj.vel.y *= -repul
  if obj.pos.x < x_min:
      obj.pos.x = x_min
      obj.vel.x *= -repul
  if obj.pos.x > x_max:
      obj.pos.x = x_max
      obj.vel.x *= -repul
      
# 시간 설정
t = 0
dt = 0.03

# 시뮬레이션 루프
while t < 100000:
    rate(100)     
    
    # 밀도 업데이트
    for i in range(numOfSphere):  
        rSum = 0
        for j in range(numOfSphere):
            rdistance = mag(a[i].pos- a[j].pos)
            if rdistance < 0 or rdistance > m_kernel_h:
                continue
            rSum += a[j].mass * poly6Kernel(rdistance, m_kernel_h)   
        a[i].density = rSum      
    
    # 압력
    for i in range(numOfSphere): 
        a[i].pressure = k * (a[i].density - m_restDensity)
    
    # 압력힘
    for i in range(numOfSphere):
        psum=[0.0,0.0,0.0]
        for j in range(numOfSphere):
            pdistance = mag(a[i].pos-a[j].pos)
            if pdistance < 0 or pdistance > m_kernel_h:
                continue
            psum[0] += a[j].mass * (a[i].pressure + a[j].pressure) / (2 * a[j].density) * grid_Spiky(pdistance, m_kernel_h,a[i].pos.x - a[j].pos.x)
            psum[1] += a[j].mass * (a[i].pressure + a[j].pressure) / (2 * a[j].density) * grid_Spiky(pdistance, m_kernel_h,a[i].pos.y - a[j].pos.y)
            psum[2] += a[j].mass * (a[i].pressure + a[j].pressure) / (2 * a[j].density) * grid_Spiky(pdistance, m_kernel_h,a[i].pos.z - a[j].pos.z)
            
        a[i].pressureforce.x  = psum[0]
        a[i].pressureforce.y  = psum[1]
        a[i].pressureforce.z  = 0.0           

    # 점성힘
    for i in range(numOfSphere):
        vsum=[0,0,0]
        for j in range(numOfSphere):
            vdistance = mag(a[i].pos-a[j].pos)
            if vdistance <0 or pdistance > m_kernel_h:
                continue
            re_vi = viscosityKernel(vdistance,m_kernel_h)
        
        vsum[0] += a[j].mass * (a[j].vel.x - a[i].vel.x) / a[j].density * re_vi
        vsum[1] += a[j].mass * (a[j].vel.y - a[i].vel.y) / a[j].density * re_vi
        vsum[2] += a[j].mass * (a[j].vel.z - a[i].vel.z) / a[j].density * re_vi
        
        a[i].viscosity.x = mu * vsum[0]
        a[i].viscosity.y = mu * vsum[1]
        a[i].viscosity.z = 0.0 #mu * vsum[2]        
        
    # 외력
    for i in range(numOfSphere):
        a[i].force.x = a[i].pressureforce.x + a[i].viscosity.x
        a[i].force.y = a[i].pressureforce.y + a[i].viscosity.y + a[i].mass * gravity
        a[i].force.z = 0.0 
              
    # 속도 업데이트
    for i in range(numOfSphere):
        a[i].vel.x = a[i].vel.x + a[i].force.x/a[i].mass * dt
        a[i].vel.y = a[i].vel.y + a[i].force.y/a[i].mass * dt
        a[i].vel.z = 0.0
        if a[i].vel.x > m_limit_velocity:
            a[i].vel.x = m_limit_velocity
        if a[i].vel.y > m_limit_velocity:
            a[i].vel.y = m_limit_velocity
            
        if a[i].vel.x < -m_limit_velocity:
            a[i].vel.x = -m_limit_velocity
        if a[i].vel.y < -m_limit_velocity:
            a[i].vel.y = -m_limit_velocity 
        
        # 경계면 처리
        boundary(a[i], boundary_ymin, boundary_ymax, boundary_xmin,                                               boundary_xmax, repulsive)
        
        # 위치 업데이트
        a[i].pos = a[i].pos + a[i].vel * dt            
    
    # 시간 업데이트
    t += dt
