from vpython import *
#GlowScript 3.0 VPython

# 화면 설정
scene.range = 20

# 배경(curve 메소드 사용), 착륙지점, 달 착륙선 만들기
obs = curve() #배경
obspos = list() #배경 꼭짓점 위치 리스트
land = list() #착륙지점
landpos = list() #착륙지점 위치 리스트
landcount = 0 #착륙지점 개수
height = -10.05
interval = 0 #간격
st = True #시작 지점인지 아닌지 판별하기 위한 변수

for i in range(40):
    flag = random()
    if st == True: #시작지점일 경우 무조건 바닥에서 시작
        obspos.append(vec(random()*2+interval, height, 0))
        st = False
    else:
        if flag < 0.2 :
            temppos = vec(random()+interval, random()*10+random(), 0)
            obspos.append(temppos) #배경 꼭짓점 위치
            flag2 = random()
            if flag2 < 0.5:
                landpos.append(temppos) #착륙지점 위치
                landcount += 1
        elif flag < 0.4:
            temppos = vec(random()+interval, random()*10*2, 0)
            obspos.append(temppos) #배경 꼭짓점 위치
            flag2 = random()
            if flag2 < 0.5:
                landpos.append(temppos) #착륙지점 위치
                landcount += 1
        elif flag < 0.6:
            temppos = vec(random()+interval, random()*10*4, 0)
            obspos.append(temppos) #배경 꼭짓점 위치
            flag2 = random()
            if flag2 < 0.5:
                landpos.append(temppos) #착륙지점 위치
                landcount += 1
        else:
            #배경 꼭짓점 위치
            obspos.append(vec(random()+interval, height, 0)) 
    interval += 10 #간격 10씩 증가
obs.append(obspos) #배경
for i in range(landcount): #착륙지점
    land.append(cylinder(pos = landpos[i], axis = vec(0, 1, 0), radius =2,                               color = color.blue))

#달착륙선 만들기
spaceship = box(pos = vec(0,8,0), size = vec(2,5,2), color = color.yellow)

# 물리 성질 & 상수 초기화
spaceship.m = 1 #달 착륙선 질량 
spaceship.v = vec(0 ,0 ,0) #달 착륙선 초기 속도 
g = 1/6 * vec(0,-10,0) #달 중력가속도(지구의 1/6배)

# 시간 설정
t = 0
dt = 0.05

scale = 5.0 #크기 조정을 위한 변수

# 게임을 위한 변수 설정
fuel = 200 #연료
point = 0 #점수
clickcount = 0 #클릭횟수

# 게임 라벨
gametxt = label( pos = scene.center - vec(scene.range, 0,0), text='left fuel : ' + fuel + '\n' + 'point : ' + point )

# 벡터 Fthrust 지정 (추력)
Fthrust  = vec(0,0,0) 

# 중력, 추력 벡터 표현
FgravArrow = arrow(pos = spaceship.pos, axis = scale*spaceship.m*g, color = color.red) 
FthrustArrow = arrow(pos = spaceship.pos, axis = Fthrust, color = color.cyan) 

# 키보드 조작 함수1 (키를 누를 경우)
def keydown(evt):
    # 키에 따라 추력 벡터 값 변환
    s = evt.key 
    if s == 'left': 
        global Fthrust
        Fthrust = vec(-2,0,0) 
    if s == 'right':
        global Fthrust
        Fthrust = vec(2,0,0)

# 키보드 조작 함수2 (키를 눌렀다 뗄 경우)
def keyup(evt):
    s = evt.key
    if s == 'left' or s == 'right' : 
        global Fthrust
        global fuel
        Fthrust = vec(0,0,0) #추력 제거
        fuel -=5 #연료 감소



# 마우스 조작 함수1 (마우스 버튼이 눌릴 경우 추력 벡터의 y값 변환)
def down(ev):
    global Fthrust
    global fuel
    global clickcount
    #처음 클릭 시 연료 사용 안함(첫 시뮬레이션 시작에서 사용)
    if clickcount != 0:
        fuel -= 5 #연료 감소
    clickcount +=1 #클릭 횟수 증가
    Fthrust = vec(0,4,0) #추력 증가

# 마우스 조작 함수2 (마우스 버튼을 눌렀다 뗄 경우 추력 제거)
def up(ev):
    global Fthrust
    Fthrust = vec(0,0,0) #추력 제거

# 키보드/마우스 조작함수 등록
scene.bind('mouseup', up)
scene.bind('mousedown', down)
scene.bind('keydown', keydown)
scene.bind('keyup', keyup)
scene.waitfor('click')

Flag = True #중력이 작용하는지 체크
cFlag = False #충돌이 된 상태인지 체크

# 시뮬레이션 루프
while t < 1000:
    rate(100)
    # 달 착륙선이 비행 중인 상태
    if Flag == True: 
        #중력
        Fgrav = spaceship.m * g 
        #알짜힘
        Fnet = Fgrav + Fthrust 
    #착륙지점에 착륙해 대기 중인 상태
    else: 
        scene.waitfor('click') #클릭 대기
        Fthrust = vec(0,4,0)
        Flag = True
        cFlag = True 
    
    # 착륙지점에서 다시 비행을 시작하는 상태
    if (spaceship.pos.y - spaceship.size.y/2) - (land[i].pos.y + land[i].size.y/2) > 1 and cFlag == True:
            cFlag = False
            Flag = True
            Fthrust = vec(0,0,0)
    
    # 속도, 위치 업데이트
    spaceship.v = spaceship.v + Fnet/spaceship.m*dt 
    spaceship.pos = spaceship.pos + spaceship.v*dt
    
    # 착륙지점에 막 착륙한 상태
    if cFlag == False :
        for i in range(landcount):
            if abs(spaceship.pos.x - land[i].pos.x) < 2 and 0 <= (spaceship.pos.y - spaceship.size.y/2) -                                            (land[i].pos.y + land[i].size.y/2) <= 0.5:
                Flag = False
                spaceship.pos = vec(land[i].pos.x, land[i].pos.y +                                                            spaceship.size.y/2, 0)
                spaceship.v = vec(0,0,0) #달 착륙선 정지
                point += 5 #점수 획득
                break
    
    # 게임 라벨 업데이트
    gametxt.pos = scene.center - vec(scene.range, 0,0)
    gametxt.text = 'left fuel : ' + fuel + '\n' + 'point : ' + point 
    
    #화면 업데이트
    scene.center = vec(spaceship.pos.x, 0,0)
    if spaceship.pos.y > 20:
        scene.range = spaceship.pos.y + 5
    
    # 중력, 추력벡터 업데이트 
    FgravArrow.pos = spaceship.pos
    FgravArrow.axis = scale*Fgrav
    FthrustArrow.pos = spaceship.pos
    FthrustArrow.axis = scale*Fthrust
    
    # 연료가 부족할 경우 시뮬레이션 루프 탈출
    if fuel <= 0:
        print("연료부족")
        spaceship.pos = vec(spaceship.pos.x, height, 0) #위치 업데이트
        FgravArrow.visible = False #중력 벡터 삭제
        FthrustArrow.visible = False #추력 벡터 삭제
        break
    
    # 바닥과 충돌시 시뮬레이션 루프 탈출
    if spaceship.pos.y < height:
        print("바닥과충돌")
        break
    
    # 시간 업데이트
    t = t + dt
