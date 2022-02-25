from vpython import *
#GlowScript 3.0 VPython

# 상수 초기화
A = 1 #진폭
w = 1 #주파수

# 그래프
gh1 = graph( xtitle = 't')
f_rt = gcurve(graph = gh1, color = color.black, label = "r(t)")
f_vt = gcurve(graph = gh1, color = color.blue, label = "v(t)")
f_at = gcurve(graph = gh1, color = color.red, label = "a(t)")

# 그래프 업데이트
for t in arange(-10, 10, 0.01): 
    f_rt.plot(pos = (t, A*sin(w*t))) #위치
    f_vt.plot(pos = (t, w*A*cos(w*t))) #속도
    f_at.plot(pos = (t,-w**2*A*sin(w*t)) ) #가속도
