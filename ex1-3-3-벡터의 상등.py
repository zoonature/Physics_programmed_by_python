from vpython import *
#GlowScript 3.0 VPython

# 벡터 a, b 지정
a = vec(1, 2, 3)
b = vec(1.01, 2, 3)

#벡터 a, b 출력
print(a, b) 

#tol = 0.1 #크기 비교를 위한 변수

# 벡터 a, b의 x, y, z 성분 비교 (벡터의 상등 여부)#시뮬레이션에서는 두 값의 차이가 설정해 놓은 임의의 작은 숫자보다 더 작다면 같은 것으로 간주하는 경우도 있음
#if abs(a.x - b.x) < tol and abs(a.y - b.y)< tol and abs(a.z - b.z)< tol:  
if a.x == b.x and a.y == b.y and a.z == b.z: 
    print("equal!")
else:
    print("Not equal!")
