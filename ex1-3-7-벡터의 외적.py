from vpython import *
#GlowScript 3.0 VPython

# 벡터 a, b 지정
a = vec(2,3,4)
b = vec(1,-1,1)

# 벡터 c, d 지정  
c = cross(a,b) #벡터 a, b의 외적
#c = a.cross(b) 
d = cross(b,a) #벡터 b, a의 외적

# 벡터 a, b, c, d 표현
a_vec = arrow(axis = a, shaftwidth = 0.2)
b_vec = arrow(axis = b, shaftwidth = 0.2)
c_vec = arrow(axis = c, shaftwidth = 0.2, color = color.cyan)
d_vec = arrow(axis = d, shaftwidth = 0.2, color = color.magenta)

# 출력
print(a, "x", b, "=", c)
print(b, "x", a, "=", d)
