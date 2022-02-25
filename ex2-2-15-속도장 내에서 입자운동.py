from vpython import *
#GlowScript 3.0 VPython

# 2차원 선형 보간 함수
def biInterp(pos, dx, dy, grid):
    # 현재 위치 찾기
    cellx = int(pos.x/dx)
    celly = int(pos.y/dy)
    # 현재 위치에 cellbox 만들기 
    cellbox = box(pos = vec((cellx+0.5)*dx,(celly+0.5)*dy,-0.1), length =                    dx,  height = dy, width = 0.05)
    # 선형 보간
    rx = pos.x - cellx * dx
    ry = pos.y - celly * dy
    resultx0 = grid[cellx][celly]*(dx-rx)/dx + grid[cellx+1][celly]*rx/dx
    resultx1 = grid[cellx][celly+1]*(dx-rx)/dx +                                                                    grid[cellx+1][celly+1]*rx/dx
    result = resultx0*(dy-ry)/dy + resultx1*ry/dy
    return result

# 그리드 설정
n = 20
m = 20
dx = 1
dy = 1

# 화면 설정
scene.center = vec(n*dx/2,m*dy/2,0)

# 리스트 생성
rList = []
objList = []

# rList, objList 리스트 초기화
for i in range(0,n):
    rList.append([])
    objList.append([])
    for j in range(0,m):
        rList[i].append(vec(random(), random(), 0))
        objList[i].append(arrow(pos=vec(i*dx,j*dy,0), axis=rList[i][j]), shaftwidth = 0.2)
       

# 벡터 r_i 지정
r_i = vec(random(), random(), 0)

# 공 만들기
ball = sphere(pos = r_i, radius = 0.2, color = color.yellow, make_Trail = True)

# 물리 성질 초기화
ball.vel = vec(0,0,0) #공의 초기 속도

attach_arrow(ball, "vel") #화살표 부착
attach_trail(ball, color = color.red) #자취 그리기

# 시간 설정
t = 0
dt = 0.1

# 시뮬레이션 루프 (그리드를 벗어나면 종료)
while (ball.pos.x < (n-1)*dx and ball.pos.y < (m-1)*dy):
    rate(100)
    # 속도, 위치 업데이트 (bilinterp 함수 이용)
    ball.vel = biInterp(ball.pos,dx,dy,rList,objList)
    ball.pos += ball.vel*dt
    # 시간 업데이트
    t += dt 

# 출력
print("loop out")
