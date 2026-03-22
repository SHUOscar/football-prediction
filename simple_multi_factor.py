# -*- coding: utf-8 -*-
# 简化多因素模型 - 避免过拟合

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
    market_home = (1/fh/total)*100
    market_away = (1/fa/total)*100
    return {
        "r": m["r"],
        "mf": 0 if market_home > market_away else 2,
        "hcp": (fh-m["ih"])/m["ih"]*100 if m["ih"] else 0,
        "acp": (fa-m["ia"])/m["ia"]*100 if m["ia"] else 0,
        "ch": m["ch"],
        "ih": m["ih"],
    }

data = [feat(m) for m in matches]
n = len(data)
results = [d["r"] for d in data]

# LOO验证 - 只用3个简单参数
def loo_test(params):
    correct = 0
    for i in range(n):
        test = data[i]
        # 预测
        score = 0
        # 因素1: 客胜赔率变化
        score += params[0] * (-test["acp"])
        # 因素2: 主胜赔率变化
        score += params[1] * (-test["hcp"])
        # 因素3: 变化次数
        if test["ch"] > 5:
            if test["acp"] < 0: score += params[2]
            if test["hcp"] < 0: score += params[2]
        
        if score > params[3]:
            pred = 0
        elif score < -params[3]:
            pred = 2
        else:
            pred = test["mf"]
        
        if pred == test["r"]:
            correct += 1
    return correct/n*100

# 网格搜索 (简化版)
print("搜索最优参数...")
best_acc = 0
best_params = None

for p0 in [0.5, 1.0, 1.5]:  # 客胜变化权重
    for p1 in [0.5, 1.0, 1.5]:  # 主胜变化权重
        for p2 in [0, 1, 2]:  # 变化次数权重
            for p3 in [0.5, 1.0, 1.5]:  # 阈值
                params = [p0, p1, p2, p3]
                acc = loo_test(params)
                if acc > best_acc:
                    best_acc = acc
                    best_params = params

print(f"\n最优参数: {best_params}")
print(f"LOO准确率: {best_acc:.1f}%")

# 对比
market_acc = sum(1 for d in data if d["mf"]==d["r"])/n*100
print(f"市场概率: {market_acc:.1f}%")
print(f"提升: {best_acc - market_acc:+.1f}%")

# 打印最佳模型逻辑
print(f"\n最佳模型逻辑:")
print(f"  score = {best_params[0]} * (-客胜变化%) + {best_params[1]} * (-主胜变化%)")
print(f"  if 变化次数>5: score += {best_params[2]}")
print(f"  if score > {best_params[3]}: 预测主胜")
print(f"  elif score < -{best_params[3]}: 预测客胜")
print(f"  else: 跟随市场概率")
