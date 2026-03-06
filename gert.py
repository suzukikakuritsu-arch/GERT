# GERT制御器 v1.0 - 調整ゼロ最強制御
import numpy as np

class GERT:
    def __init__(self):
        self.G, self.E, self.R = 0.0, 0.0, 0.1
    
    def control(self, error):
        G_new = 0.95 * (self.G + self.R * self.E + error)
        E_new = 0.5 * (self.E + np.tanh(G_new))
        R_new = 0.1 * np.clip(G_new / max(E_new, 1e-8), -1, 1)
        self.G, self.E, self.R = G_new, E_new, R_new
        return self.G * 0.236  # 最適δ*

# 使い方: gert = GERT(); u = gert.control(error)
