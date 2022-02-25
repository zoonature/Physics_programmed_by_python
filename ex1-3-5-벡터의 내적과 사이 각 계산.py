from vpython import *
#GlowScript 3.0 VPython


# 벡터 a, b 지정
a = vec(1,2,0)
#a = vec(0,2,0)
#a = vec(-1,1,0)
b = vec(3,0,0)

# 벡터 a, b 표현
a_vec = arrow(axis = a, shaftwidth = 0.1, color = color.red)
b_vec = arrow(axis = b, shaftwidth = 0.1, color = color.green)

# c 지정 (벡터 a, b 의 내적)
c = dot(a,b)
#c = a.dot(b)

# 벡터 a, b의 사이 각 계산 (공식 이용)
cos_rad = c/mag(a)/mag(b) 
rad  = acos(cos_rad) #코사인의 역함수
deg = rad/pi*180 ##deg

# 벡터 a.b의 사이 각 출력 
print("dot product =", c, ", angle =", deg) 
