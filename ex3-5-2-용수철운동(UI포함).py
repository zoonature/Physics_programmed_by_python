from vpython import *
#GlowScript 3.0 VPython

drag = False #드래그 여부 확인 변수
chosenObj = None #드래그 객체 확인 변수

# 마우스 조작1 (마우스 클릭 시)
scene.bind("mousedown", down)
def down():
    global drag, chosenObj
    chosenObj = scene.mouse.pick()
    drag = True

# 마우스 조작2 (드래그 시)
scene.bind("mousemove", move)
def move():
    global drag, chosenObj
    if drag == True: # mouse button is down
        if chosenObj == ball:
            ball.pos = scene.mouse.pos
            spring.axis = ball.pos - ceiling.pos

# 마우스 조작3 (마우스 클릭 해제 시)
scene.bind("mouseup", up)
def up():
    global drag, chosenObj
    chosenObj = None
    drag = False

# 캡션
scene.append_to_caption('Modifying Physical Properties\n\n')

# 질량 슬라이더
massSlider = slider(min = 0.1, max = 10, value = 1, bind = setMass)
scene.append_to_caption('\nMass of Ball',massSlider.min, 'to' ,massSlider.max, '\n\n')
# 질량 슬라이더 조작함수
def setMass():
    global ball
    ball.m = massSlider.value
    ball.radius = 0.025*ball.m**(1/3)

# 강성계수 슬라이더
stiffnessSlider = slider(min = 50, max = 200, value = 100, bind = setKs)
scene.append_to_caption('\nStiffness of Spring',stiffnessSlider.min, 'to' , stiffnessSlider.max, '\n\n')

# 강성계수 슬라이더 조작함수
def setKs():
    global ks, spring
    ks = stiffnessSlider.value
    spring.thickness = 0.003e-2*ks 

# 감쇠계수 슬라이더
dampingSlider = slider(min = 0.01, max = 10, value = 1, bind = setDamping)
scene.append_to_caption('\nDamping of Spring',dampingSlider.min, 'to' , dampingSlider.max, '\n\n')

# 감쇠계수 슬라이더 조작함수
def setDamping():
    global kd
    kd = dampingSlider.value

# 천장, 공, 스프링 만들기
ceiling = box(size = vec(0.3, 0.01, 0.3))        
ball = sphere(pos = vec(0,-0.3,0), radius = 0.03, texture = textures.metal, make_trail = True, trail_color = color.blue, retain = 50)
spring = helix(pos = ceiling.pos, axis = ball.pos - ceiling.pos, color = color.black, thickness = 0.003, coils = 30, radius = 0.01)
# 물리 성질 & 상수 초기화
g = 9.8 #중력 가속도
ball.m = 1.0 #공의 질량
l0 = 0.3 #스프링 초기 길이
ks = 100 #강성계수
kd = 1#감쇠계수
ball.v = vec(0,0,0) #공의 초기 속도      

# 초기 중력
Fgrav = ball.m*g*vec(0,-1,0) 

# 시간 설정
t = 0           
dt = 0.001 

# 화면 설정
scene.background = color.white #배경을 흰색으로 설정
scene.autoscale = False  #자동 화면 맞춤 해제
scene.center = vec(0,-l0,0) #화면 중심설정
scene.waitfor('click') #클릭대기         

# 그래프
motion_graph = graph(title = 'Motion graph', xtitle = 'time', ytitle = 'spring length')
traj = gcurve(color=color.blue)

# 시뮬레이션 루프
while True:
    rate(1/dt) 

    # 스프링 힘
    l = mag(ball.pos - ceiling.pos)
    s = l - l0 
    lhat = norm(ball.pos)
    Fspr = -ks*s*lhat    
    # 댐퍼 힘
    Fdamp = -kd*dot(ball.v,lhat)*lhat

    # 알짜힘
    Fnet = Fgrav + Fspr + Fdamp #Fdamp _Step 2
    
    # 드래그 시 알짜힘, 공의속도 초기화
    if drag == True:
        Fnet = vec(0,0,0)
        ball.v = vec(0,0,0)        

    # 속도, 위치 업데이트
    ball.v = ball.v + Fnet/ball.m*dt
    ball.pos = ball.pos + ball.v*dt

    # 스프링 업데이트
    spring.axis = ball.pos - ceiling.pos

    # 시간 업데이트
    t = t + dt

    # 그래프 업데이트
    traj.plot(pos=(t,l))
