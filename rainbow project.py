import math

def gulzul_compute(n1, theta1_degree, n2):
    theta1_radian = math.radians(theta1_degree)
    sin_theta2 = n1 * math.sin(theta1_radian) / n2

    theta2_radian = math.asin(sin_theta2)
    theta2_degree = math.degrees(theta2_radian)
    return theta2_degree    

gulzul = {
    "RED": 1.331,
    "ORANGE": 1.333,
    "YELLOW": 1.335,
    "GREEN": 1.337,
    "BLUE": 1.340,
    "INDIGO": 1.342,
    "VIOLET": 1.344
}

air_gulzul = 1.0003
light_angle = 60

input_num = input("원하는 빛의 파장(색)을 영어로 입력 (예: red, blue 등): ").upper()

if input_num in gulzul:
    result = gulzul_compute(air_gulzul, light_angle, gulzul[input_num])
    print(f"{input_num} 색의 굴절각은 약 {result:.2f}도입니다.")
else:
    print("올바른 색상이 아닙니다. 다음 중 하나를 입력하세요:")
    print(", ".join(gulzul.keys()))
