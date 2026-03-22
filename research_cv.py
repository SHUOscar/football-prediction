# -*- coding: utf-8 -*-
import random

# 数据
matches = [
    {"id": "周日007", "r": 1, "ih": 2.37, "ia": 2.63, "fh": 2.30, "fa": 2.66, "ch": 5},
    {"id": "周日008", "r": 0, "ih": 2.25, "ia": 2.52, "fh": 1.94, "fa": 3.02, "ch": 6},
    {"id": "周日009", "r": 0, "ih": 1.43, "ia": 5.40, "fh": 1.43, "fa": 5.30, "ch": 4},
    {"id": "周日010", "r": 0, "ih": 1.86, "ia": 3.32, "fh": 1.90, "fa": 3.25, "ch": 2},
    {"id": "周日011", "r": 0, "ih": 3.63, "ia": 1.80, "fh": 3.35, "fa": 1.91, "ch": 4},
    {"id": "周日012", "r": 0, "ih": 2.22, "ia": 2.85, "fh": 2.25, "fa": 2.85, "ch": 2},
    {"id": "周日013", "r": 0, "ih": 1.32, "ia": 6.10, "fh": 1.30, "fa": 6.15, "ch": 6},
    {"id": "周日014", "r": 0, "ih": 2.10, "ia": 3.15, "fh": 2.13, "fa": 3.12, "ch": 2},
    {"id": "周日015", "r": 0, "ih": 1.88, "ia": 3.30, "fh": 2.05, "fa": 2.92, "ch": 5},
    {"id": "周日016", "r": 0, "ih": 1.45, "ia": 5.30, "fh": 1.45, "fa": 5.30, "ch": 0},
    {"id": "周日017", "r": 0, "ih": 1.95, "ia": 3.15, "fh": 1.92, "fa": 3.30, "ch": 1},
    {"id": "周日018", "r": 0, "ih": 2.89, "ia": 2.34, "fh": 2.66, "fa": 2.59, "ch": 5},
    {"id": "周日019", "r": 1, "ih": 1.72, "ia": 3.95, "fh": 1.57, "fa": 4.60, "ch": 3},
    {"id": "周日020", "r": 2, "ih": 3.62, "ia": 1.71, "fh": 3.62, "fa": 1.71, "ch": 0},
    {"id": "周日021", "r": 1, "ih": 2.40, "ia": 2.74, "fh": 2.43, "fa": 2.79, "ch": 3},
    {"id": "周日022", "r": 0, "ih": 1.92, "ia": 3.25, "fh": 1.81, "fa": 3.48, "ch": 9},
    {"id": "周日023", "r": 2, "ih": 2.21, "ia": 2.80, "fh": 2.21, "fa": 2.93, "ch": 2},
    {"id": "周日024", "r": 2, "ih": 2.68, "ia": 2.06, "fh": 3.15, "fa": 1.81, "ch": 6},
    {"id": "周一001", "r": 1, "ih": 1.69, "ia": 4.20, "fh": 1.82, "fa": 3.60, "ch": 3},
    {"id": "周一003", "r": 2, "ih": 3.65, "ia": 1.86, "fh": 3.90, "fa": 1.80, "ch": 5},
    {"id": "周一005", "r": 0, "ih": 3.08, "ia": 2.07, "fh": 3.20, "fa": 2.02, "ch": 2},
    {"id": "周一006", "r": 2, "ih": 4.35, "ia": 1.64, "fh": 4.50, "fa": 1.60, "ch": 4},
    {"id": "周一007", "r": 2, "ih": 2.33, "ia": 2.57, "fh": 2.78, "fa": 2.14, "ch": 7},
    {"id": "周一008", "r": 2, "ih": 1.18, "ia": 11.0, "fh": 1.22, "fa": 9.50, "ch": 3},
    {"id": "周一009", "r": 2, "ih": 5.20, "ia": 1.52, "fh": 6.10, "fa": 1.38, "ch": 7},
    {"id": "周二001", "r": 1, "ih": 2.25, "ia": 2.90, "fh": 2.14, "fa": 3.10, "ch": 8},
    {"id": "周二003", "r": 1, "ih": 3.60, "ia": 1.89, "fh": 4.31, "fa": 1.79, "ch": 6},
    {"id": "周二004", "r": 0, "ih": 3.80, "ia": 1.61, "fh": 3.90, "fa": 1.57, "ch": 6},
    {"id": "周二005", "r": 1, "ih": 2.25, "ia": 2.58, "fh": 2.35, "fa": 2.46, "ch": 3},
    {"id": "周二006", "r": 0, "ih": 1.46, "ia": 5.60, "fh": 1.41, "fa": 6.10, "ch": 3},
    {"id": "周二009", "r": 1, "ih": 2.70, "ia": 2.24, "fh": 2.84, "fa": 2.20, "ch": 5},
    {"id": "周二010", "r": 0, "ih": 1.39, "ia": 4.90, "fh": 1.37, "fa": 5.08, "ch": 2},
    {"id": "周二011", "r": 0, "ih": 1.39, "ia": 6.15, "fh": 1.41, "fa": 5.88, "ch": 2},
    {"id": "周二012", "r": 0, "ih": 6.00, "ia": 1.35, "fh": 6.25, "fa": 1.33, "ch": 2},
    {"id": "周三001", "r": 2, "ih": 1.50, "ia": 4.63, "fh": 1.49, "fa": 4.40, "ch": 11},
    {"id": "周三002", "r": 2, "ih": 3.05, "ia": 2.15, "fh": 3.37, "fa": 2.05, "ch": 8},
    {"id": "周三003", "r": 1, "ih": 1.18, "ia": 10.0, "fh": 1.14, "fa": 12.5, "ch": 3},
]

# 特征计算
def feat(m):
    ih, ia, fh, fa = m["ih"], m["ia"], m["fh"], m["fa"]
    total = 1/fh + 1/3.2 + 1/fa
    mhp = (1/fh/total)*100
    map_ = (1/fa/total)*100
    return {
        "r": m["r"],
        "mf": 0 if mhp > map_ else 2,
        "hcp": (fh-ih)/ih*100 if ih else 0,
        "acp": (fa-ia)/ia*100 if ia else 0,
        "ch": m["ch"],
    }

data = [feat(m) for m in matches]
n = len(data)

# 留一法交叉验证
def loo(predict_fn):
    correct = 0
    for i in range(n):
        train = data[:i] + data[i+1:]
        test = data[i]
        pred = predict_fn(test, train)
        if pred == test["r"]:
            correct += 1
    return correct/n*100

# 策略
def market(f, t): return f["mf"]

def rule1(f, t):
    if f["hcp"] < -5: return 0
    if f["acp"] < -5: return 2
    if f["ch"] > 5 and f["hcp"] < 0: return 0
    if f["ch"] > 5 and f["acp"] < 0: return 2
    return f["mf"]

def rule2(f, t):  # 变化次数
    if f["ch"] > 6 and f["acp"] < 0: return 2
    if f["ch"] > 6 and f["hcp"] < 0: return 0
    if f["acp"] < -5: return 2
    if f["hcp"] < -5: return 0
    return f["mf"]

def rule3(f, t):  # 客胜加强
    score = 0
    if f["acp"] < -3: score -= 2
    if f["hcp"] > 3: score -= 1
    if f["mf"] == 2: score -= 1
    if score <= -2: return 2
    return f["mf"]

def rule4(f, t):  # 强队
    if f["mf"] == 0 and f["hcp"] > 0: return 2  # 强队赔率上升=危险
    if f["mf"] == 0 and f["hcp"] < -3: return 0
    if f["acp"] < -5: return 2
    return f["mf"]

def rule5(f, t):  # 综合
    score = 0
    if f["acp"] < -4: score -= 3
    if f["hcp"] > 5: score -= 1
    if f["ch"] > 5: score += 1 if f["hcp"] < 0 else -1
    if score < -1: return 2
    if score > 1: return 0
    return f["mf"]

print(f"样本: {n}, 主胜:{sum(1 for d in data if d['r']==0)}, 平局:{sum(1 for d in data if d['r']==1)}, 客胜:{sum(1 for d in data if d['r']==2)}")

# 测试所有策略
results = []
for name, fn in [("市场概率", market), ("规则模型", rule1), ("变化次数", rule2), 
                   ("客胜加强", rule3), ("强队危险", rule4), ("综合评分", rule5)]:
    acc = loo(fn)
    results.append((name, acc))

results.sort(key=lambda x: x[1], reverse=True)
print("\n留一法交叉验证结果:")
for name, acc in results:
    print(f"  {name}: {acc:.1f}%")

# 统计显著性检验
print("\n两两对比:")
best_name, best_acc = results[0]
best_fn = None
for name, fn in [("市场概率", market), ("规则模型", rule1), ("变化次数", rule2), 
                   ("客胜加强", rule3), ("强队危险", rule4), ("综合评分", rule5)]:
    if name == best_name:
        best_fn = fn
        continue
    # 简单对比
    better = sum(1 for i in range(n) if fn(data[i], []) != data[i]["r"] and best_fn(data[i], []) == data[i]["r"])
    worse = sum(1 for i in range(n) if fn(data[i], []) == data[i]["r"] and best_fn(data[i], []) != data[i]["r"])
    print(f"  {best_name} vs {name}: 最佳多对{better}, 对方多对{worse}")
