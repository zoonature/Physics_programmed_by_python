from vpython import *
#GlowScript 3.0 VPython

rf = vec(3, 3.5, 0) #나중 위치
ri = vec(2, 4, 0) #처음 위치
dr = rf - ri #변위
#rf = ri + dr

tf = 15.1 #나중 시간
ti = 15.0 #처음 시간
dt = tf - ti #시간 간격

vavg = dr/dt #평균 속력 

# 출력
print(rf, "-", ri, "=", dr) ##m
print("v_avg = ", vavg, "speed = ", mag(vavg)) ##m/s
print("v_hat = ", norm(vavg)) 
print(mag(vavg)*norm(vavg)) #vavg벡터(크기와 방향의 곱)

# 2차원 좌표축 표현
x_axis = arrow(axis = vector(7,0,0),shaftwidth = 0.1)
y_axis = arrow(axis = vector(0,7,0),shaftwidth = 0.1)

# 위치 표현 (sphere 함수 이용)
sphere(radius = 0.1, pos = ri) #시작 위치 
sphere(radius = 0.1, pos = rf) #나중 위치

sf = 1.0/3.0 #크기 조정을 위한 변수

# 벡터 rf, ri, dr, vavg 표현
ri_vec = arrow(axis = ri, shaftwidth = 0.2, color = color.yellow)
rf_vec = arrow(axis = rf, shaftwidth = 0.2, color = color.yellow)
dr_vec = arrow(pos = ri, axis = dr, shaftwidth = 0.2, color = color.blue)
vavg_vec = arrow(pos = ri, axis = sf*vavg, shaftwidth = 0.1, color = color.green) 
