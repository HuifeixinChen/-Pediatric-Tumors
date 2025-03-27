import json
import matplotlib.pyplot as plt

# 读取JSON文件
with open('fold0_metrics_output.json', 'r') as f:
    data = json.load(f)

# 提取每个类别的 Dice 和 IoU
categories = ['1', '2', '3', '4']
dice_scores = [data['mean'][c]['Dice'] for c in categories]
iou_scores = [data['mean'][c]['IoU'] for c in categories]

# 可视化
x = range(len(categories))
plt.figure(figsize=(10, 6))
bar1 = plt.bar(x, dice_scores, width=0.4, label='Dice', align='center')
bar2 = plt.bar([i + 0.4 for i in x], iou_scores, width=0.4, label='IoU', align='center')

plt.xticks([i + 0.2 for i in x], ['Label ' + c for c in categories])
plt.ylabel('Score')
plt.title('Average Dice and IoU per Label')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
