import numpy as np

theta = np.arange(90, 180.9, 0.9)
path_w = 'diagonal_phase.sh'
with open(path_w, mode='a') as f:
        f.write(str(theta))
