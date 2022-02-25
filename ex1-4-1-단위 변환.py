from vpython import *
#GlowScript 3.0 VPython

# 우사인 볼트의 속력 설정 
bolt_speed_mph = 27.8 ##mi/hour

# 단위 변환
bolt_speed_kph = 27.8 * 1.60934 ##km/h mi → km:
print("bolt's top speed =", bolt_speed_kph,"km/h")
bolt_speed_mps = bolt_speed_kph * 1000/60/60 ##m/s (km→m, h→s)
print("bolt's top speed =", bolt_speed_mps,"m/s")
