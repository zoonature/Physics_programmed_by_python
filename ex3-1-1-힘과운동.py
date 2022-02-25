from vpython import *
#GlowScript 3.0 VPython

# 화면 설정
scene.range = 20

# 객체 만들기
ball = []
N = 50 #공의 갯수

side = 10.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box(pos = vec( side, 0, side-4), size = vec(thk, s2, 6))
wallL = box(pos = vec(-side, 0, side-4), size = vec(thk, s2, 6))
wallB = box(pos = vec(0, -side, side-4), size = vec(s3, thk, 6))
wallT = box(pos = vec(0,  side, side-4), size = vec(s3, thk, 6))
wallBK = box(pos = vec(0, 0, side-4), size = vec(s2, s2, thk))

for i in range(N):
    ball[i] = sphere(radius = 0.5 + random(), color = vec(random(),random(),random()))
    ball[i].pos = 0.8*side*vec.random()
    ball[i].v = side*vec.random()
    ball[i].m = ball[i].radius**3 ##kg    
    # 2D
    ball[i].pos.z = side - 2
    ball[i].v.z = 0
    ball[i].mousedrag = False
    
# UI (마우스 조작 / 체크박스)
scene.bind("mousedown", down)
scene.bind("mousemove", move)
scene.bind("mouseup", up)
gravity_exist = checkbox(text = 'Zero-Gravity', bind = setGravity)

drag = False
chosenObj = None
chosenIdx = 0

# 조작 함수
def down():
    global drag, chosenObj
    chosenObj = scene.mouse.pick()
    drag = True
def move():
    global drag, chosenObj, chosenIdx, ball
    if drag == True:
        for i in range(N):
            if chosenObj == ball[i]:
                chosenIdx = i
                if -side < scene.mouse.pos.x  < side and -side < scene.mouse.pos.y  < side :
                    ball[i].pos.x = scene.mouse.pos.x
                    ball[i].pos.y = scene.mouse.pos.y
                    ball[i].pos.z = side - 2
                    ball[i].mousedrag = True
def up():
    global drag, chosenObj
    chosenObj = None
    drag = False
    ball[chosenIdx].mousedrag = False

def setGravity(b):
    return b.checked

# 물리 성질 초기화
g = 9.8 #중력가속도 ##m/s**2
ks = 100 #스프링 계수
kd =  1 #댐퍼 계수
e = 0.9 #탄성 계수

# 시간 설정
t = 0
dt = 0.01

scene.waitfor('click')

# 시뮬레이션 루프
while True:
    rate(1/dt)
    for i in range(N):
        # 중력
        if gravity_exist.checked == False:
            ball[i].f = ball[i].m*vec(0,-g,0)
        else:
            ball[i].f = vec(0,0,0)
        # 공 충돌 처리
        for j in range(N):
            if i == j:
                continue
            r_ij = ball[i].pos - ball[j].pos
            v_ij = ball[i].v - ball[j].v
            sum_radius = ball[i].radius + ball[j].radius
            # 스프링 & 댐퍼힘
            if sum_radius > mag(r_ij): 
                ball[i].f = ball[i].f - ks*(mag(r_ij) - sum_radius)*norm(r_ij)
                ball[i].f = ball[i].f - kd*(dot(v_ij,norm(r_ij))*norm(r_ij))    
                
    # 벽면 충돌 처리
    for i in range(N):
        side_b = side - thk*0.5 - ball[i].radius
        if not (side_b > ball[i].pos.x > -side_b):
            ball[i].pos.x = min(side_b, ball[i].pos.x)
            ball[i].pos.x = max(-side_b, ball[i].pos.x)
            ball[i].v.x = -e*ball[i].v.x          
        if not (side_b > ball[i].pos.y > -side_b):
            ball[i].pos.y = min(side_b, ball[i].pos.y)
            ball[i].pos.y = max(-side_b, ball[i].pos.y)
            ball[i].v.y = -e*ball[i].v.y
        if not (side_b > ball[i].pos.z > -side_b):
            ball[i].pos.z = min(side_b, ball[i].pos.z)
            ball[i].pos.z = max(-side_b, ball[i].pos.z)
            ball[i].v.z = -e*ball[i].v.z
        
    # 속도, 위치 업데이트
    for i in range(N):
        if ball[i].mousedrag == False:
            ball[i].v = ball[i].v + ball[i].f/ball[i].m*dt
            ball[i].pos = ball[i].pos + ball[i].v*dt
            
    # 시간 업데이트   
    t = t + dt
