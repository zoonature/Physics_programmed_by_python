from vpython import *
#GlowScript 3.0 VPython

# 물, 나무 만들기
# 투명도 50% 적용
water = box(size = vec(10,10,10), color = color.blue, opacity = 0.5) 
wood = box(size = vec(1,1,1), color = color.yellow)

# 물리 성질 & 상수 초기화
wood.v = vec(0,0,0) #나무 초기 속도
wood.rho = 950 #나무 밀도
water.rho = 1000 #물 밀도
wood.volume = wood.size.x*wood.size.y*wood.size.z #나무 부피
wood.volume_im = wood.volume #물에 잠긴 나무 부피
wood.m = wood.rho*wood.volume #나무 밀도
g = vec(0,-9.8,0) #중력가속도
kv = 1000 #항력 관련 계수
kv_im = kv

# 시간 설정
t = 0
dt = 0.03

thold = 0.001 #크기 비교를 위한 작은 변수


# 충돌 처리 함수
def collision(pBox,pbox, thold):
    r1 = pbox.pos.y - 0.5*pbox.size.y
    r2 = pBox.pos.y - 0.5*pBox.size.y
    colcheck = r1 - r2
    # 충돌 시 True 반환
    if  colcheck < thold:
        return True
    else:
        return False

# 물에 잠긴 부피 계산 함수
def calc_im(pBox, pbox, kv):
    r1 = pbox.pos.y + 0.5*pbox.size.y
    r2 = pBox.pos.y + 0.5*pBox.size.y
    floatcheck = r1 - r2  
    # 물에 잠긴 부피 계산
    if floatcheck > 0:
        pbox.volume_im = pbox.volume - floatcheck*pbox.size.x*pbox.size.z
    else:
        pbox.volume_im = pbox.volume 
    if pbox.volume_im < 0:
        pbox.volume_im = 0
    # 물에 잠긴 부피에 따라 kv_im값 변환
    kv_im  = pbox.volume_im/pbox.volume*kv
    # 물에 잠긴 부피, kv_im 반환
    return pbox.volume_im, kv_im

# 시뮬레이션 루프
while t < 100:
    rate(100)
    # 수조 바닥과 나무의 충돌 시 시뮬레이션 루프 탈출(collision 함수 이용)
    if collision(water, wood, thold):
        print("colliding")
        break
    # 나무의 물에 잠긴 부분과 kv_im 계산
    wood.volume_im, kv_im = calc_im(water, wood, kv)
    print(wood.volume_im)  
    # 알짜힘
    wood.f = wood.m*g #중력
    wood.f = wood.f - kv_im*mag(wood.v)**2*norm(wood.v) #항력
    wood.f = wood.f - water.rho*wood.volume_im*g #부력

    # 속도, 위치 업데이트
    wood.v = wood.v + wood.f/wood.m*dt
    wood.pos = wood.pos + wood.v*dt

    # 시간 업데이트
    t = t + dt
