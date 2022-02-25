from vpython import *
#GlowScript 3.0 VPython


# 벡터 v, r 지정
v = vec(3,4,0)
r = vec(1,0.2,0)

# 단위 벡터 계산
rhat = norm(r) 

# 벡터 v 분해
v_para = dot(v, rhat)*rhat 
v_perp = v - v_para 

# 벡터 v ,v_para_vec, v_perp_vec 표현
v_vec = arrow(axis = v, shaftwidth = 0.2)
v_para_vec = arrow(axis = v_para, shaftwidth = 0.1, color = color.blue)
v_perp_vec = arrow(axis = v_perp, shaftwidth = 0.1, color = color.red)

# 출력
print("v = ", v)
print("rhat = ", rhat)
print("v_para = ", v_para)
print("v_perp = ", v_perp)
