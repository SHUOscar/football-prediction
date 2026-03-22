# -*- coding: utf-8 -*-
# 使用留一法交叉验证 (Leave-One-Out)

matches = [
    {"r": 1, "ih": 2.37, "ia": 2.63, "fh": 2.30, "fa": 2.66, "ch": 5},
    {"r": 0, "ih": 2.25, "ia": 2.52, "fh": 1.94, "fa": 3.02, "ch": 6},
    {"r": 0, "ih": 1.43, "ia": 5.40, "fh": 1.43, "fa": 5.30, "ch": 4},
    {"r": 0, "ih": 1.86, "ia": 3.32, "fh": 1.90, "fa": 3.25, "ch": 2},
    {"r": 0, "ih": 3.63, "ia": 1.80, "fh": 3.35, "fa": 1.91, "ch": 4},
    {"r": 0, "ih": 2.22, "ia": 2.85, "fh": 2.25, "fa": 2.85, "ch": 2},
    {"r": 0, "ih": 1.32, "ia": 6.10, "fh": 1.30, "fa": 6.15, "ch": 6},
    {"r": 0, "ih": 2.10, "ia": 3.15, "fh": 2.13, "fa": 3.12, "ch": 2},
    {"r": 0, "ih": 1.88, "ia": 3.30, "fh": 2.05, "fa": 2.92, "ch": 5},
    {"r": 0, "ih": 1.45, "ia": 5.30, "fh": 1.45, "fa": 5.30, "ch": 0},
    {"r": 0, "ih": 1.95, "ia": 3.15, "fh": 1.92, "fa": 3.30, "ch": 1},
    {"r": 0, "ih": 2.89, "ia": 2.34, "fh": 2.66, "fa": 2.59, "ch": 5},
    {"r": 1, "ih": 1.72, "ia": 3.95, "fh": 1.57, "fa": 4.60, "ch": 3},
    {"r": 2, "ih": 3.62, "ia": 1.71, "fh": 3.62, "fa": 1.71, "ch": 0},
    {"r": 1, "ih": 2.40, "ia": 2.74, "fh": 2.43, "fa": 2.79, "ch": 3},
    {"r": 0, "ih": 1.92, "ia": 3.25, "fh": 1.81, "fa": 3.48, "ch": 9},
    {"r": 2, "ih": 2.21, "ia": 2.80, "fh": 2.21, "fa": 2.93, "ch": 2},
    {"r": 2, "ih": 2.68, "ia": 2.06, "fh": 3.15, "fa": 1.81, "ch": 6},
    {"r": 1, "ih": 1.69, "ia": 4.20, "fh": 1.82, "fa": 3.60, "ch": 3},
    {"r": 2, "ih": 3.65, "ia": 1.86, "fh": 3.90, "fa": 1.80, "ch": 5},
    {"r": 0, "ih": 3.08, "ia": 2.07, "fh": 3.20, "fa": 2.02, "ch": 2},
    {"r": 2, "ih": 4.35, "ia": 1.64, "fh": 4.50, "fa": 1.60, "ch": 4},
    {"r": 2, "ih": 2.33, "ia": 2.57, "fh": 2.78, "fa": 2.14, "ch": 7},
    {"r": 2, "ih": 1.18, "ia": 11.0, "fh": 1.22, "fa": 9.50, "ch": 3},
    {"r": 2, "ih": 5.20, "ia": 1.52, "fh": 6.10, "fa": 1.38, "ch": 7},
    {"r": 1, "ih": 2.25, "ia": 2.90, "fh": 2.14, "fa": 3.10, "ch": 8},
    {"r": 1, "ih": 3.60, "ia": 1.89, "fh": 4.31, "fa": 1.79, "ch": 6},
    {"r": 0, "ih": 3.80, "ia": 1.61, "fh": 3.90, "fa": 1.57, "ch": 6},
    {"r": 1, "ih": 2.25, "ia": 2.58, "fh": 2.35, "fa": 2.46, "ch": 3},
    {"r": 0, "ih": 1.46, "ia": 5.60, "fh": 1.41, "fa": 6.10, "ch": 3},
    {"r": 1, "ih": 2.70, "ia": 2.24, "fh": 2.84, "fa": 2.20, "ch": 5},
    {"r": 0, "ih": 1.39, "ia": 4.90, "fh": 1.37, "fa": 5.08, "ch": 2},
    {"r": 0, "ih": 1.39, "ia": 6.15, "fh": 1.41, "fa": 5.88, "ch": 2},
    {"r": 0, "ih": 6.00, "ia": 1.35, "fh": 6.25, "fa": 1.33, "ch": 2},
    {"r": 2, "ih": 1.50, "ia": 4.63, "fh": 1.49, "fa": 4.40, "ch": 11},
    {"r": 2, "ih": 3.05, "ia": 2.15, "fh": 3.37, "fa": 2.05, "ch": 8},
    {"r": 1, "ih": 1.18, "ia": 10.0, "fh": 1.14, "fa": 12.5, "ch": 3},
]

def feat(m):
    fh, fa = m["fh"], m["fa"]
    total = 1/fh + 1/3.2 + 1/fa
    mhp = (1/fh/total)*100
    map_ = (1/fa/total)*100
    return {
        "r": m["r"],
        "mf": 0 if mhp > map_ else 2,
        "hcp": (fh-m["ih"])/m["ih"]*100 if m["ih"] else 0,
        "acp": (fa-m["ia"])/m["ia"]*100 if m["ia"] else 0,
        "ch": m["ch"],
    }

data = [feat(m) for m in matches]
n = len(data)

# LOO交叉验证
def loo(predict_fn):
    correct = 0
    for i in range(n):
        test = data[i]
        train = data[:i] + data[i+1:]
        pred = predict_fn(test, train)
        if pred == test["r"]:
            correct += 1
    return correct/n*100

# 预测函数
def market(f, t): return f["mf"]

def rule_original(f, t):
    if f["hcp"] < -5: return 0
    if f["acp"] < -5: return 2
    if f["ch"] > 5 and f["hcp"] < 0: return 0
    if f["ch"] > 5 and f["acp"] < 0: return 2
    return f["mf"]

def rule_changes(f, t):
    if f["ch"] > 6 and f["acp"] < 0: return 2
    if f["ch"] > 6 and f["hcp"] < 0: return 0
    if f["acp"] < -5: return 2
    if f["hcp"] < -5: return 0
    return f["mf"]

def rule_away(f, t):
    score = 0
    if f["acp"] < -3: score -= 2
    if f["hcp"] > 3: score -= 1
    if f["mf"] == 2: score -= 1
    if score <= -2: return 2
    return f["mf"]

def rule_favorite(f, t):
    if f["mf"] == 0 and f["hcp"] > 0: return 2
    if f["mf"] == 0 and f["hcp"] < -3: return 0
    if f["acp"] < -5: return 2
    return f["mf"]

def rule_combo(f, t):
    score = 0
    if f["acp"] < -4: score -= 3
    if f["hcp"] > 5: score -= 1
    if f["ch"] > 5: score += 1 if f["hcp"] < 0 else -1
    if score < -1: return 2
    if score > 1: return 0
    return f["mf"]

strategies = [
    ("市场概率", market),
    ("规则模型", rule_original),
    ("变化次数", rule_changes),
    ("客胜加强", rule_away),
    ("强队危险", rule_favorite),
    ("综合评分", rule_combo),
]

print(f"样本: {n}, 主胜:{sum(1 for d in data if d['r']==0)}, 平局:{sum(1 for d in data if d['r']==1)}, 客胜:{sum(1 for d in data if d['r']==2)}")
print("\n留一法交叉验证 (避免过拟合):")

results = []
for name, fn in strategies:
    acc = loo(fn)
    results.append((name, acc))

results.sort(key=lambda x: x[1], reverse=True)
for name, acc in results:
    print(f"  {name}: {acc:.1f}%")

print(f"\n最佳: {results[0][0]} ({results[0][1]:.1f}%)")
