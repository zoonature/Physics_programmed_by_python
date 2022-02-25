from vpython import *
#GlowScript 3.0 VPython

# 공 만들기
myBall = sphere()
# 박스 만들기
myBox = box()

myBox = box(pos = vec(5,0,0)) #박스의 위치 변경
myBox.size = vec(0.5, 4, 1) #박스의 크기 변경
myBall.color = color.green #공의 색상 변경
myBox.pos.x = 10 #박스의 x좌표 위치 변경

