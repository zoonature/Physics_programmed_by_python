from vpython import *
#GlowScript 3.0 VPython


r = 0.9144/(2*pi) #스톤 반지름 ##m

# 경기장 사이즈
GROUND_SIZEX = 45.720 ##m
GROUND_SIZEY = 5 ##m
GROUND_SIZEZ = 1 ##m

# 컬링 경기장 만들기
sheet = box(size = vec(GROUND_SIZEX, GROUND_SIZEY, GROUND_SIZEZ), color = color.white) #컬링시트
wall1 = box(pos = vec(0, GROUND_SIZEY/2+0.1, 0.25), size = vec(GROUND_SIZEX, 0.2, 1.5)) #위쪽 벽
wall1 = box(pos = vec(0, -GROUND_SIZEY/2-0.1, 0.25), size = vec(GROUND_SIZEX, 0.2, 1.5)) #아래쪽 벽
startPoint = box(pos = vec(-GROUND_SIZEX/2+1.22,0,0), size = vec(0.1, 1, GROUND_SIZEZ+0.01), color = color.black) #시작포인트
endPoint = box(pos = vec(GROUND_SIZEX/2-1.22,0,0), size = vec(0.1, 1, GROUND_SIZEZ+0.01), color = color.black) #종료 포인트

# 시작지점 하우스 만들기
start_circle_1st = cylinder(pos = vec(startPoint.pos.x + 3.66, 0, -0.496), axis = vec(0,0,1), radius = 0.15, color = color.white)
start_circle_2nd = cylinder(pos = vec(startPoint.pos.x + 3.66, 0, -0.497), axis = vec(0,0,1), radius = 0.61, color = color.red)
start_circle_3rd = cylinder(pos = vec(startPoint.pos.x + 3.66, 0, -0.498), axis = vec(0,0,1), radius = 1.22, color = color.white)
start_circle_4th = cylinder(pos = vec(startPoint.pos.x + 3.66, 0, -0.499), axis = vec(0,0,1), radius = 1.83, color = color.blue)

# 타켓지점 하우스 만들기
end_circle_1st = cylinder(pos = vec(endPoint.pos.x - 3.66, 0, -0.496), axis = vec(0,0,1), radius = 0.15, color = color.white)
end_circle_2nd = cylinder(pos = vec(endPoint.pos.x - 3.66, 0, -0.497), axis = vec(0,0,1), radius = 0.61, color = color.red)
end_circle_3rd = cylinder(pos = vec(endPoint.pos.x - 3.66, 0, -0.498), axis = vec(0,0,1), radius = 1.22, color = color.white)
end_circle_4th = cylinder(pos = vec(endPoint.pos.x - 3.66, 0, -0.499), axis = vec(0,0,1), radius = 1.83, color = color.blue)

sf = 3 #크기 조정을 위한 변수

# 스톤 만들기
stone = cylinder(pos = vec(-20, 0,1) , axis = vec(0,0,0.1143), radius = r, color = color.black)
stone.radius = stone.radius * sf

# 물리 성질 초기화
g = 9.8 #중력상수
mu = 0.05 #마찰 계수
stone.v = vec(5,0,0) #스톤의 초기속도 ##m/s
stone.m = 19.96 #스톤 질량##kg
# Draw버튼
btnDraw = button(text = 'Draw', bind = drawBtn)
# Draw버튼 조작함수
def drawBtn(b):
    b.disabled = True
    return b.disabled

# 속도 슬라이더
velocitySlider = slider(min = 3, max = 7, value = 5, bind = myVelocity)
# 속도 슬라이더 조작함수
def myVelocity():
    global stone
    stone.v = velocitySlider.value * vec(1,0,0)

# 시간 설정
t = 0
dt = 0.01

# 시뮬레이션 루프
while True:
    rate(100)
    # 버튼이 눌렸을 때
    if btnDraw.disabled == True:
        # 마찰력
        Ffr = -mu*stone.m*g*norm(stone.v)
        # 속도, 위치 업데이트
        stone.v = stone.v + Ffr/stone.m * dt
        stone.pos = stone.pos + stone.v * dt
        # 스톤이 멈췄을 때 운동 초기화
        if mag(stone.v) < 0.05:
            stone.v = vec(0,0,0)
            scene.waitfor('click')
            btnDraw.disabled = False
            stone.pos = vec(-20, 0, 1)
            t = 0

        # 시간 업데이트
        t = t + dt
