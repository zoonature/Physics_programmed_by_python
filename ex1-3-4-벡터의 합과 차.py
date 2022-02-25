from vpython import *
#GlowScript 3.0 VPython


# 벡터 a, b 지정
a = vec(1, 2, 3)
b = vec(-4, 5, 6)

# 벡터 c, d 지정 (벡터 a, b의 합과 차)
c = a + b 
d = a - b
print(c, d) # 벡터 c, d 출력

# 벡터 a, b, c 표현 (벡터의 합)
a_vec = arrow(pos = vec(0,0,0), axis = a, shaftwidth = 0.1)
b_vec = arrow(pos = a, axis = b, shaftwidth = 0.1) #시작점a, 축b로 설정
c_vec = arrow(pos = vec(0,0,0), axis = c, shaftwidth = 0.1, color = color.red)

# 벡터 a, b, d(시작점b, 축d) 표현 (벡터의 차) 
a_vec_2 = arrow(pos = vec(0,0,0), axis = a, shaftwidth = 0.1, color = color.yellow)
b_vec_2 = arrow(pos = vec(0,0,0), axis = b, shaftwidth = 0.1, color = color.yellow) 
d_vec = arrow(pos = b, axis = d, shaftwidth = 0.1, color = color.blue) 
