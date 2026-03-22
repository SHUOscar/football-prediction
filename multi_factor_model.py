# -*- coding: utf-8 -*-
# 多因素综合模型研究

# 完整数据集 (37场)
# 格式: {id, r(结果0/1/2), ih/ia/fh/fa(赔率), ch(变化次数), hc/ac(历史交锋主胜/客胜次数)}

# 由于缺少历史交锋数据，我们用现有特征构建模型

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

# 特征工程
def extract_features(m):
    ih, ia, fh, fa = m["ih"], m["ia"], m["fh"], m["fa"]
    
    # 市场概率
    total = 1/fh + 1/3.2 + 1/fa
    market_home = (1/fh/total)*100
    market_draw = (1/3.2/total)*100
    market_away = (1/fa/total)*100
    
    # 赔率变化
    home_change = fh - ih
    away_change = fa - ia
    home_change_pct = (fh-ih)/ih*100 if ih else 0
    away_change_pct = (fa-ia)/ia*100 if ia else 0
    
    # 特征向量
    return {
        "r": m["r"],
        # 原始特征
        "initial_home": ih,
        "initial_away": ia,
        "final_home": fh,
        "final_away": fa,
        "changes": m["ch"],
        # 变化特征
        "home_change": home_change,
        "away_change": away_change,
        "home_change_pct": home_change_pct,
        "away_change_pct": away_change_pct,
        # 市场特征
        "market_home": market_home,
        "market_away": market_away,
        "market_favorite": 0 if market_home > market_away else 2,
        "market_prob_diff": market_home - market_away,
        # 衍生特征
        "strong_home": 1 if ih < 1.5 else 0,  # 强队
        "strong_away": 1 if ia < 1.5 else 0,
        "home_upset_risk": 1 if ih < 1.5 and home_change > 0 else 0,  # 强队赔率上升
    }

data = [extract_features(m) for m in matches]
n = len(data)
results = [d["r"] for d in data]

print(f"样本: {n}")
print(f"主胜: {results.count(0)}, 平局: {results.count(1)}, 客胜: {results.count(2)}")

# 多因素加权评分模型
def weighted_model(d, weights):
    score = 0
    
    # 1. 市场概率 (权重可调)
    score += weights[0] * d["market_prob_diff"] / 50
    
    # 2. 赔率变化幅度
    score += weights[1] * (-d["away_change_pct"]) / 10  # 客胜下降加分
    score += weights[2] * (-d["home_change_pct"]) / 10  # 主胜下降加分
    
    # 3. 变化次数
    if d["changes"] > 5:
        score += weights[3] * (-d["away_change"]) * 2
        score += weights[4] * (-d["home_change"]) * 2
    
    # 4. 强队风险
    if d["home_upset_risk"] == 1:
        score -= weights[5]
    
    # 5. 强队支撑
    if d["strong_home"] == 1 and d["home_change"] < 0:
        score += weights[6]
    
    if score > 0.5:
        return 0
    elif score < -0.5:
        return 2
    else:
        return d["market_favorite"]

# 网格搜索最优权重
best_acc = 0
best_weights = None

print("\n网格搜索最优权重...")
for w0 in [0.3, 0.5, 0.7]:
    for w1 in [0.1, 0.3, 0.5]:
        for w2 in [0.1, 0.3, 0.5]:
            for w3 in [0.1, 0.3]:
                for w4 in [0.1, 0.3]:
                    for w5 in [0.2, 0.5]:
                        for w6 in [0.2, 0.5]:
                            weights = [w0, w1, w2, w3, w4, w5, w6]
                            correct = sum(1 for d in data if weighted_model(d, weights) == d["r"])
                            acc = correct / n * 100
                            if acc > best_acc:
                                best_acc = acc
                                best_weights = weights

print(f"\n最优权重: {best_weights}")
print(f"训练准确率: {best_acc:.1f}%")

# 留一法验证
print("\n留一法交叉验证:")
loo_correct = 0
for i in range(n):
    test = data[i]
    train = data[:i] + data[i+1:]
    
    # 用训练数据找最优权重
    best_train_acc = 0
    best_train_weights = None
    for w0 in [0.3, 0.5, 0.7]:
        for w1 in [0.1, 0.3, 0.5]:
            for w2 in [0.1, 0.3, 0.5]:
                for w3 in [0.1, 0.3]:
                    for w4 in [0.1, 0.3]:
                        for w5 in [0.2, 0.5]:
                            for w6 in [0.2, 0.5]:
                                weights = [w0, w1, w2, w3, w4, w5, w6]
                                correct = sum(1 for d in train if weighted_model(d, weights) == d["r"])
                                acc = correct / len(train) * 100
                                if acc > best_train_acc:
                                    best_train_acc = acc
                                    best_train_weights = weights
    
    pred = weighted_model(test, best_train_weights)
    if pred == test["r"]:
        loo_correct += 1

loo_acc = loo_correct / n * 100
print(f"LOO准确率: {loo_acc:.1f}%")

# 对比简单模型
simple_correct = sum(1 for d in data if d["market_favorite"] == d["r"])
simple_acc = simple_correct / n * 100
print(f"市场概率准确率: {simple_acc:.1f}%")

print(f"\n结论: 加权模型 vs 市场概率 = {loo_acc:.1f}% vs {simple_acc:.1f}%")
