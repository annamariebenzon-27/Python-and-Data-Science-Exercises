import numpy as np
rng=np.random.default_rng(1303)
from matplotlib.pyplot import plt
fig, ax=plt(figsize=(8,8))
x4=rng.standard_normal(100)
y4=rng.standard_normal(100)
ax.plot(x4,y4)
ax.show()
