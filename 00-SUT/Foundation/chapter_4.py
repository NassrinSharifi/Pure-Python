import numpy as np


def interpolation(n: float, p1: float, p2: float, h1: float, h2: float) -> float:
    v = ((h1 * (n - p1)) + (h2 * (p2 - n))) / (p2 - p1)
    return v


def find_equation(B: float, m1: float, m2: float, Nq: float, Ngama: float, df: float, gama: float) -> tuple:
    a1 = (B ** 2) * (gama * df * Nq * (1 - m1) + 0.5 * gama * B * Ngama * (1 - m2))
    a2 = Qu
    if abs(a2 - a1) < 1000000:
        print(abs(a1 - a2))
        # print(a2)
        return ("done!", B, abs(a1 - a2))
    else:
        return ("wrong!", -1, abs(a1 - a2))


# __________________________________________________________________
df = 2.5
gama = 18
H_B_ratio = [0.1, 0.2, 0.4, 0.6]
H = 2
# __________________________________________________________________
m1_30 = [0.82, 0.65, 0.42, 0.21]
m2_30 = [0.83, 0.71, 0.49, 0.4]
Nq_30 = [None, 1100, 80, 35]
Ngama_30 = [None, 350, 30, 18]
m1_40 = [0.9, 0.82, 0.67, 0.48]
m2_40 = [0.9, 0.81, 0.66, 0.51]
Nq_40 = [None, 50000, 3000, 500]
Ngama_40 = [None, 20000, 1500, 300]
# __________________________________________________________________
phi = 30
Qu = 664687.5
# for B in range(1, 50000):
#     B /= 100
#     if phi == 30:
#         temp = H / B
#         for i in range(len(H_B_ratio) + 1):
#             try:
#                 if temp < H_B_ratio[i] and temp > H_B_ratio[i - 1]:
#                     m1 = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], m1_30[i - 1], m1_30[i])
#                     m2 = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], m2_30[i - 1], m2_30[i])
#                     Nq = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], Nq_30[i - 1], Nq_30[i])
#                     Ngama = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], Ngama_30[i - 1], Ngama_30[i])
#                     k, v, j = find_equation(B, m1, m2, Nq, Ngama, df, gama)
#                     # if k == "done!":
#                         # print("phi 30", k, v,temp)
#                 elif temp == H_B_ratio[i]:
#                     v_inter = H_B_ratio[i]
#             except:
#                 pass
# __________________________________________________________________
phi = 40
Qu = 1.35 * 10 ** 6
temp_j = []
temp_v = []
for B in range(1, 100000):
    B /= 100
    if phi == 40:
        temp = H / B
        for i in range(len(H_B_ratio) + 1):
            try:
                if temp < H_B_ratio[i] and temp > H_B_ratio[i - 1]:
                    m1 = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], m1_40[i - 1], m1_40[i])
                    m2 = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], m2_40[i - 1], m2_40[i])
                    Nq = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], Nq_40[i - 1], Nq_40[i])
                    Ngama = interpolation(temp, H_B_ratio[i - 1], H_B_ratio[i], Ngama_40[i - 1], Ngama_40[i])
                    k, v, j = find_equation(B, m1, m2, Nq, Ngama, df, gama)
                    temp_j.append(j)
                    temp_v.append(v)
                    if k == "done!":
                        print("phi 40", k, v)
                elif temp == H_B_ratio[i]:
                    v_inter = H_B_ratio[i]
            except:
                pass

print("\n\n")
mm = min(temp_j)
for i in range(len(temp_j)):
    if temp_j[i] == mm:
        print(temp_v[i])
        print(temp_j[i])
