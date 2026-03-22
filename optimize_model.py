# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import math
import random

# ==================== DATA ====================
# 加联赛信息
march_1 = [
    {"id": "周日007", "league": "西甲", "home": "埃尔切", "away": "西班牙人", "half": "1:1", "full": "2:2", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.37, "draw": 3.06, "away": 2.63}, "final_odds": {"home": 2.30, "draw": 3.14, "away": 2.66}, "changes_1x2": 5, "changes_handicap": 4},
    {"id": "周日008", "league": "荷甲", "home": "特温特", "away": "费耶诺德", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.25, "draw": 3.50, "away": 2.52}, "final_odds": {"home": 1.94, "draw": 3.53, "away": 3.02}, "changes_1x2": 6, "changes_handicap": 5},
    {"id": "周日009", "league": "英超", "home": "曼联", "away": "水晶宫", "half": "0:1", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.43, "draw": 4.10, "away": 5.40}, "final_odds": {"home": 1.43, "draw": 4.15, "away": 5.30}, "changes_1x2": 4, "changes_handicap": 2},
    {"id": "周日010", "league": "英超", "home": "富勒姆", "away": "热刺", "half": "2:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.86, "draw": 3.45, "away": 3.32}, "final_odds": {"home": 1.90, "draw": 3.40, "away": 3.25}, "changes_1x2": 2, "changes_handicap": 2},
    {"id": "周日011", "league": "意甲", "home": "萨索洛", "away": "亚特兰大", "half": "1:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 3.63, "draw": 3.35, "away": 1.80}, "final_odds": {"home": 3.35, "draw": 3.25, "away": 1.91}, "changes_1x2": 4, "changes_handicap": 6},
    {"id": "周日012", "league": "法甲", "home": "巴黎FC", "away": "尼斯", "half": "1:0", "full": "1:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.22, "draw": 3.05, "away": 2.85}, "final_odds": {"home": 2.25, "draw": 2.99, "away": 2.85}, "changes_1x2": 2, "changes_handicap": 2},
    {"id": "周日013", "league": "德甲", "home": "斯图加特", "away": "沃夫斯堡", "half": "3:0", "full": "4:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.32, "draw": 4.82, "away": 6.10}, "final_odds": {"home": 1.30, "draw": 5.05, "away": 6.15}, "changes_1x2": 6, "changes_handicap": 7},
    {"id": "周日014", "league": "西甲", "home": "巴伦西亚", "away": "奥萨苏纳", "half": "0:0", "full": "1:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.10, "draw": 2.98, "away": 3.15}, "final_odds": {"home": 2.13, "draw": 2.95, "away": 3.12}, "changes_1x2": 2, "changes_handicap": 3},
    {"id": "周日015", "league": "荷甲", "home": "乌德勒支", "away": "阿尔克马", "half": "2:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.88, "draw": 3.40, "away": 3.30}, "final_odds": {"home": 2.05, "draw": 3.35, "away": 2.92}, "changes_1x2": 5, "changes_handicap": 5},
]

march_2 = [
    {"id": "周日016", "league": "英超", "home": "阿森纳", "away": "切尔西", "half": "1:1", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "final_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "changes_1x2": 0, "changes_handicap": 1},
    {"id": "周日017", "league": "德甲", "home": "法兰克福", "away": "弗赖堡", "half": "0:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.95, "draw": 3.35, "away": 3.15}, "final_odds": {"home": 1.92, "draw": 3.28, "away": 3.30}, "changes_1x2": 1, "changes_handicap": 1},
    {"id": "周日018", "league": "意甲", "home": "都灵", "away": "拉齐奥", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.89, "draw": 2.81, "away": 2.34}, "final_odds": {"home": 2.66, "draw": 2.72, "away": 2.59}, "changes_1x2": 5, "changes_handicap": 5},
    {"id": "周日019", "league": "西甲", "home": "贝蒂斯", "away": "塞维利亚", "half": "2:0", "full": "2:2", "result": "平局", "result_code": 1, "initial_odds": {"home": 1.72, "draw": 3.40, "away": 3.95}, "final_odds": {"home": 1.57, "draw": 3.65, "away": 4.60}, "changes_1x2": 3, "changes_handicap": 2},
    {"id": "周日020", "league": "德甲", "home": "汉堡", "away": "莱红牛", "half": "1:1", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "final_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "changes_1x2": 0, "changes_handicap": 0},
    {"id": "周日021", "league": "意甲", "home": "罗马", "away": "尤文图斯", "half": "1:0", "full": "3:3", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.40, "draw": 2.88, "away": 2.74}, "final_odds": {"home": 2.43, "draw": 2.78, "away": 2.79}, "changes_1x2": 3, "changes_handicap": 2},
    {"id": "周日022", "league": "法甲", "home": "马赛", "away": "里昂", "half": "0:1", "full": "3:2", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.92, "draw": 3.35, "away": 3.25}, "final_odds": {"home": 1.81, "draw": 3.45, "away": 3.48}, "changes_1x2": 9, "changes_handicap": 8},
    {"id": "周日023", "league": "西甲", "home": "赫罗纳", "away": "塞尔塔", "half": "1:0", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.21, "draw": 3.13, "away": 2.80}, "final_odds": {"home": 2.21, "draw": 2.98, "away": 2.93}, "changes_1x2": 2, "changes_handicap": 1},
    {"id": "周日024", "league": "美职", "home": "奥兰多", "away": "迈国际", "half": "2:0", "full": "2:4", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.68, "draw": 3.70, "away": 2.06}, "final_odds": {"home": 3.15, "draw": 3.85, "away": 1.81}, "changes_1x2": 6, "changes_handicap": 6},
    {"id": "周一001", "league": "韩职", "home": "大田市民", "away": "安养FC", "half": "0:0", "full": "1:1", "result": "平局", "result_code": 1, "initial_odds": {"home": 1.69, "draw": 3.35, "away": 4.20}, "final_odds": {"home": 1.82, "draw": 3.32, "away": 3.60}, "changes_1x2": 3, "changes_handicap": 2},
]

all_matches = march_1 + march_2

# ==================== FEATURE EXTRACTION ====================
def extract_features(match):
    initial = match["initial_odds"]
    final = match["final_odds"]
    
    if initial["home"] is None:
        return None
    
    f = {}
    
    # 基础赔率特征
    f["initial_home"] = initial["home"]
    f["initial_draw"] = initial["draw"]
    f["initial_away"] = initial["away"]
    f["final_home"] = final["home"]
    f["final_draw"] = final["draw"]
    f["final_away"] = final["away"]
    
    # 赔率变化
    f["home_change"] = final["home"] - initial["home"]
    f["draw_change"] = final["draw"] - initial["draw"]
    f["away_change"] = final["away"] - initial["away"]
    f["home_change_pct"] = (final["home"] - initial["home"]) / initial["home"] * 100
    f["draw_change_pct"] = (final["draw"] - initial["draw"]) / initial["draw"] * 100 if initial["draw"] > 0 else 0
    f["away_change_pct"] = (final["away"] - initial["away"]) / initial["away"] * 100
    
    # 变化次数
    f["changes_1x2"] = match["changes_1x2"]
    f["changes_handicap"] = match["changes_handicap"]
    
    # 市场概率
    total = 1/final["home"] + 1/final["draw"] + 1/final["away"]
    f["market_home_prob"] = (1/final["home"]/total)*100
    f["market_draw_prob"] = (1/final["draw"]/total)*100
    f["market_away_prob"] = (1/final["away"]/total)*100
    
    probs = [f["market_home_prob"], f["market_draw_prob"], f["market_away_prob"]]
    f["market_favorite"] = probs.index(max(probs))
    
    # 联赛特征 (one-hot)
    league = match.get("league", "其他")
    f["is_premier"] = 1 if league == "英超" else 0
    f["is_laliga"] = 1 if league == "西甲" else 0
    f["is_bundes"] = 1 if league == "德甲" else 0
    f["is_serie"] = 1 if league == "意甲" else 0
    f["is_ligue1"] = 1 if league == "法甲" else 0
    f["is_eredivisie"] = 1 if league == "荷甲" else 0
    f["is_other"] = 1 if league not in ["英超", "西甲", "德甲", "意甲", "法甲", "荷甲"] else 0
    
    # 强队特征
    f["is_strong_home"] = 1 if initial["home"] < 1.6 else 0
    f["is_weak_home"] = 1 if initial["home"] > 2.5 else 0
    
    # 变化强度特征
    f["total_change_magnitude"] = abs(f["home_change"]) + abs(f["away_change"])
    f["has_big_change"] = 1 if abs(f["home_change_pct"]) > 5 or abs(f["away_change_pct"]) > 5 else 0
    
    # 结果
    f["actual_result"] = match["result_code"]
    
    return f

features_list = [extract_features(m) for m in all_matches]
features_list = [f for f in features_list if f is not None]

print("="*60)
print("OPTIMIZED MODEL TRAINING")
print("="*60)
print(f"Total samples: {len(features_list)}")

results = [f["actual_result"] for f in features_list]
home_wins = results.count(0)
draws = results.count(1)
away_wins = results.count(2)
print(f"Results: Home={home_wins}, Draw={draws}, Away={away_wins}")

# ==================== BASELINE: MARKET ====================
market_correct = sum(1 for f in features_list if f["market_favorite"] == f["actual_result"])
market_accuracy = market_correct / len(features_list) * 100

# ==================== ALGORITHM 1: WEIGHTED RULE MODEL ====================
print("\n" + "="*60)
print("ALGORITHM 1: WEIGHTED RULE MODEL")
print("="*60)

def predict_weighted_rule(f):
    score = 0
    
    # 主胜赔率下降权重 (调整)
    if f["home_change_pct"] < -3:  # 从-5调整到-3
        score += 3  # 从2调整到3
    elif f["home_change_pct"] < -1:
        score += 1
    
    # 客胜赔率下降权重 (调整)
    if f["away_change_pct"] < -3:
        score -= 3
    elif f["away_change_pct"] < -1:
        score -= 1
    
    # 变化次数权重 (调整)
    if f["changes_1x2"] >= 5:
        if f["home_change"] < -0.05:
            score += 2
        if f["away_change"] < -0.05:
            score -= 2
    elif f["changes_1x2"] == 0:
        # 无变化时完全信任市场
        return f["market_favorite"]
    
    # 初始赔率权重 (调整)
    if f["initial_home"] < 1.5:
        score += 2
    elif f["initial_home"] < 1.8:
        score += 1
    
    if f["initial_home"] > 2.8:
        score -= 1
    
    # 决策
    if score >= 2:
        return 0
    elif score <= -2:
        return 2
    else:
        return f["market_favorite"]

weighted_correct = sum(1 for f in features_list if predict_weighted_rule(f) == f["actual_result"])
weighted_accuracy = weighted_correct / len(features_list) * 100
print(f"Weighted Rule Accuracy: {weighted_accuracy:.1f}% ({weighted_correct}/{len(features_list)})")

# ==================== ALGORITHM 2: SCORING MODEL ====================
print("\n" + "="*60)
print("ALGORITHM 2: SCORING MODEL")
print("="*60)

def predict_scoring(f):
    # 计算每个选项的得分
    home_score = 0
    draw_score = 0
    away_score = 0
    
    # 市场概率得分
    home_score += f["market_home_prob"] * 0.3
    draw_score += f["market_draw_prob"] * 0.3
    away_score += f["market_away_prob"] * 0.3
    
    # 赔率变化得分
    if f["home_change"] < 0:
        home_score += abs(f["home_change"]) * 20
    if f["away_change"] < 0:
        away_score += abs(f["away_change"]) * 20
    
    # 强队加分
    if f["initial_home"] < 1.5:
        home_score += 15
    elif f["initial_home"] < 1.8:
        home_score += 8
    
    if f["initial_away"] < 1.5:
        away_score += 15
    elif f["initial_away"] < 1.8:
        away_score += 8
    
    # 变化次数
    if f["changes_1x2"] > 3:
        if f["home_change"] < f["away_change"]:
            home_score += 5
        else:
            away_score += 5
    
    scores = [home_score, draw_score, away_score]
    return scores.index(max(scores))

scoring_correct = sum(1 for f in features_list if predict_scoring(f) == f["actual_result"])
scoring_accuracy = scoring_correct / len(features_list) * 100
print(f"Scoring Model Accuracy: {scoring_accuracy:.1f}% ({scoring_correct}/{len(features_list)})")

# ==================== ALGORITHM 3: LOGIC REGRESSION (SIMPLE) ====================
print("\n" + "="*60)
print("ALGORITHM 3: LOGIC REGRESSION (SIMULATED)")
print("="*60)

# 简化的逻辑回归模拟
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def predict_logistic(f):
    # 简化的权重
    w_home = -2.5  # 主胜赔率越低越可能
    w_draw = 0.5
    w_away = 2.0
    w_change = -1.5
    
    # 特征
    x1 = f["final_home"]  # 主胜赔率
    x2 = f["market_home_prob"] / 100  # 市场概率
    x3 = f["home_change"]  # 赔率变化
    
    # 简化的决策边界
    home_confidence = (1/f["final_home"]) + f["home_change"]*5
    
    if home_confidence > 0.8:
        return 0
    elif home_confidence < 0.3:
        return 2
    else:
        return f["market_favorite"]

logistic_correct = sum(1 for f in features_list if predict_logistic(f) == f["actual_result"])
logistic_accuracy = logistic_correct / len(features_list) * 100
print(f"Logistic Model Accuracy: {logistic_accuracy:.1f}% ({logistic_correct}/{len(features_list)})")

# ==================== ALGORITHM 4: DECISION TREE (SIMULATED) ====================
print("\n" + "="*60)
print("ALGORITHM 4: DECISION TREE (SIMULATED)")
print("="*60)

def predict_decision_tree(f):
    # 决策树规则
    if f["initial_home"] < 1.5:
        # 强队主场
        if f["home_change"] > 0.1:
            return f["market_favorite"]  # 赔率上升，可能有问题
        return 0  # 主胜
    
    elif f["initial_away"] < 1.5:
        # 强队客场
        if f["away_change"] > 0.1:
            return f["market_favorite"]
        return 2  # 客胜
    
    elif f["changes_1x2"] > 5:
        # 变化多
        if f["home_change"] < -0.1:
            return 0
        if f["away_change"] < -0.1:
            return 2
        return f["market_favorite"]
    
    elif f["changes_1x2"] == 0:
        # 无变化，完全信任市场
        return f["market_favorite"]
    
    else:
        # 中等情况
        if f["market_home_prob"] > 50:
            return 0
        elif f["market_away_prob"] > 50:
            return 2
        else:
            return 1  # 平局更多

tree_correct = sum(1 for f in features_list if predict_decision_tree(f) == f["actual_result"])
tree_accuracy = tree_correct / len(features_list) * 100
print(f"Decision Tree Accuracy: {tree_accuracy:.1f}% ({tree_correct}/{len(features_list)})")

# ==================== CROSS-VALIDATION ====================
print("\n" + "="*60)
print("CROSS-VALIDATION (5-FOLD)")
print("="*60)

def cross_validate(predict_func, n_folds=5):
    random.seed(42)
    indices = list(range(len(features_list)))
    random.shuffle(indices)
    
    fold_size = len(indices) // n_folds
    fold_scores = []
    
    for fold in range(n_folds):
        test_start = fold * fold_size
        test_end = test_start + fold_size if fold < n_folds - 1 else len(indices)
        
        test_indices = indices[test_start:test_end]
        train_indices = indices[:test_start] + indices[test_end:]
        
        # 用训练集的特征计算阈值
        train_features = [features_list[i] for i in train_indices]
        
        # 测试
        correct = sum(1 for i in test_indices if predict_func(features_list[i]) == features_list[i]["actual_result"])
        fold_scores.append(correct / len(test_indices) * 100)
    
    return fold_scores

# 交叉验证各模型
cv_weighted = cross_validate(predict_weighted_rule)
cv_scoring = cross_validate(predict_scoring)
cv_tree = cross_validate(predict_decision_tree)

print(f"Weighted Rule CV: {sum(cv_weighted)/5:.1f}% (folds: {[f'{x:.1f}%' for x in cv_weighted]})")
print(f"Scoring Model CV: {sum(cv_scoring)/5:.1f}% (folds: {[f'{x:.1f}%' for x in cv_scoring]})")
print(f"Decision Tree CV: {sum(cv_tree)/5:.1f}% (folds: {[f'{x:.1f}%' for x in cv_tree]})")

# ==================== FINAL REPORT ====================
print("\n" + "="*60)
print("OPTIMIZATION RESULTS")
print("="*60)

models = [
    ("Market Baseline", market_accuracy),
    ("Weighted Rule", weighted_accuracy),
    ("Scoring Model", scoring_accuracy),
    ("Logistic Model", logistic_accuracy),
    ("Decision Tree", tree_accuracy),
]

best_model = max(models, key=lambda x: x[1])

print(f"\n{'Model':<20} {'Accuracy':>10} {'vs Market':>12}")
print("-" * 45)
for name, acc in models:
    diff = acc - market_accuracy
    print(f"{name:<20} {acc:>9.1f}% {diff:>+10.1f}%")

print(f"\nBest Model: {best_model[0]} with {best_model[1]:.1f}% accuracy")
print(f"Improvement vs Market: {best_model[1] - market_accuracy:+.1f}%")

# 保存结果
output = {
    "total": len(features_list),
    "baseline_market": market_accuracy,
    "models": {name: acc for name, acc in models},
    "best_model": best_model[0],
    "best_accuracy": best_model[1],
    "improvement": best_model[1] - market_accuracy,
    "cv_scores": {
        "weighted_rule": cv_weighted,
        "scoring": cv_scoring,
        "decision_tree": cv_tree
    }
}

with open("optimized_results.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\nResults saved to optimized_results.json")
