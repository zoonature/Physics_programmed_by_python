from vpython import *
#GlowScript 3.0 VPython

scale_factor = 5.0 #크기조정을 위한 변수

# 상수 초기화
r = 384400000 #지구와 달 사이의 거리 ##m
G = 6.67e-11 #만유인력상수 ##N*m**2/kg**2

# 지구, 달 만들기
earth = sphere(pos = vec(0,0,0), radius = scale_factor*6371000,       
         texture = textures.earth) #지구 텍스처 적용
moon = sphere(pos = vec(r,0,0), radius = scale_factor*1737000,
         color = color.white)

# 물리성질 초기화
earth.mass = 5.974e24 #지구 질량 ##kg
moon.mass = 7.347e22 #달 질량 ##kg

# 지구와 달 사이의 인력
F = G*earth.mass*moon.mass/r**2  ##N

# 뉴턴 제 3법칙 적용 (작용 반작용)
earth.force = F
moon.force = -F

# 지구와 달 사이의 인력 출력
print("earth.force =", earth.force, "N")
print("moon.force =", moon.force, "N")

# 가속력 계산
earth.acc = F/earth.mass 
moon.acc = F/moon.mass
# 지구와 달의 가속력(가속도의 크기) 출력
print("earth.acc =", earth.acc, "m/s^2")
print("moon.acc =", moon.acc, "m/s^2")
