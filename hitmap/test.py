import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 임의의 데이터 생성
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data)

# Seaborn을 사용하여 히트맵 생성
sns.heatmap(data, vmin=0, vmax=9, annot=True, cmap='RdPu')

# 플로팅
plt.show()
