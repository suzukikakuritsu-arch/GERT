# GERT vs PID 比較デモ
from gert import GERT
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 500)
ref = np.ones_like(t)

# GERT
gert = GERT()
y_gert = []
for i in range(len(t)):
    error = ref[i] - (y_gert[-1] if y_gert else 0)
    y_gert.append(gert.control(error))

# PID（簡易）
y_pid = []
e_sum, e_prev = 0, 0
for i in range(len(t)):
    e = ref[i] - (y_pid[-1] if y_pid else 0)
    e_sum += e * 0.01
    u = 50*e + 1*e_sum + 5*(e-e_prev)/0.01
    y_pid.append(min(max(y_pid[-1]+u*0.01 if y_pid else u*0.01, -2), 2))
    e_prev = e

plt.plot(t, ref, 'k--', label='目標')
plt.plot(t, y_gert, 'r-', linewidth=3, label='GERT')
plt.plot(t, y_pid, 'b--', label='PID')
plt.legend(); plt.grid(); plt.title('GERT vs PID')
plt.savefig('demo.png')
plt.show()

print("GERT完動！demo.png保存")
