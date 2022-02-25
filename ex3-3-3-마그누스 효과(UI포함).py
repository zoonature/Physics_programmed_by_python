from vpython import *
#GlowScript 3.0 VPython

# ground, ball 만들기
ground = box(pos = vec(0,0,0), size = vec(100,0.10,70), color = color.green)
init_pos = vec(-30,0.11,0) #ball의 초기 위치
ball = sphere(pos = init_pos, radius = 0.11, color = color.orange, make_trail = False) ##m

# 크기 조정
sf = 5 #크기 조정을 위한 변수
ball.r = 0.11
ball.radius = sf*0.11
ball.pos.y = ball.radius

# 물리 성질 초기화
ball.m = 0.45 ##kg
ball.speed = 25 #공의 속력 ##m/s
ball.angle = radians(35) ##degree to radian
ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0) #공의 속도

# 화살표 부착
attach_arrow(ball, "v", shaftwidth = 0.1, scale = 0.3, color=color.yellow)

# 화면 설정
scene.range = 30

# 상수 초기화
g = -9.8 ##m/s**2
rho = 1.204 #공기밀도 ##kg/m**3
Cd = 0.3#0.3#0.3#1 #공기저항 계수 #laminar
Cm = 1 #마그누스 계수 #0.5 
w = 10*2*pi #각속력(10rev/sec)

# 캡션
scene.append_to_caption('\nInitial Values\n\n')
# 속도 슬라이더
velocitySlider = slider(min = 0, max = 45, value = 25, bind = setVelocity)
scene.append_to_caption('\nVelocity:',velocitySlider.min, 'to' ,velocitySlider.max, '\n\n')

# 속도 슬라이더 조작함수
def setVelocity():
    global ball
    ball.speed = velocitySlider.value
    ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0)
 
# 각도 슬라이더
angleSlider = slider(min = 0, max = 90, value = 35, bind = setAngle)
scene.append_to_caption('\nAngle:',angleSlider.min, 'to' ,angleSlider.max, '\n\n')

# 각도 슬라이더 조작함수
def setAngle():
    global ball
    ball.angle = radians(angleSlider.value)
    ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0)

# 각속도 슬라이더
angularvSlider = slider(min = -10, max = 10, value = 10, bind = setAngualr)
scene.append_to_caption('\nAngular velocity:',angularvSlider.min, 'to' ,angularvSlider.max, '\n\n')

# 각속도 슬라이더 조작함수
def setAngualr():
    global w
    w = angularvSlider.value*2*pi


# 스타트 버튼
btnStart = button(text = 'Shoot', bind = startbtn)

# 스타트 버튼 조작함수
def startbtn(b):
    b.disabled = True
    return b.disabled

# 시간 설정
t = 0
dt = 0.01

# 시뮬레이션 루프
while t<20:
    rate(1/dt)

    # 버튼이 눌렸을 때
    if btnStart.disabled == True:   
        ball.make_trail = True  
        # 중력
        grav = ball.m * vec(0,g,0)

        # 공기저항력
        drag = -0.5*rho*Cd*(pi*ball.r**2)*mag(ball.v)**2*norm(ball.v)   
        # 마그누스힘
        magnus = 0.5*rho*Cm*(pi*ball.r**2)*ball.r*w*mag(ball.v)*cross(vec(0,1,0),norm(ball.v))                                 
        # 알짜힘
        ball.f = grav + drag + magnus

        # 시간, 속도 업데이트
        ball.v = ball.v + ball.f/ball.m*dt
        ball.pos = ball.pos + ball.v*dt 

        # 땅과 공의 충돌 시 운동 초기화
        if ball.pos.y - ball.radius < 0:
            scene.waitfor('click') #클릭 대기
            btnStart.disabled = False
            ball.pos = init_pos 
            ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0)
            ball.pos.y = ball.radius
            ball.make_trail = False
            t = 0

        # 시간 업데이트
        t = t + dt
