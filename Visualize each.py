import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 加载 JSON 文件（确保路径正确）
with open("fold0_metrics_output.json", "r") as f:
    data = json.load(f)

# 遍历每个病例，提取 Dice 分数
rows = []
for case in data['metric_per_case']:
    case_id = case['prediction_file'].split('\\')[-1].split('.')[0]
    for label, metrics in case['metrics'].items():
        dice = metrics['Dice']
        if dice == dice:  # 排除 NaN
            rows.append({'case': case_id, 'label': label, 'Dice': dice})

# 转为 DataFrame
df = pd.DataFrame(rows)

# 生成 heatmap
pivot = df.pivot(index='case', columns='label', values='Dice')
plt.figure(figsize=(14, 10))
sns.heatmap(pivot, annot=True, cmap='YlGnBu', cbar_kws={'label': 'Dice Score'})
plt.title("Dice Score per Case and Label")
plt.ylabel("Case ID")
plt.xlabel("Label")
plt.tight_layout()
plt.show()
