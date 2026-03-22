# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from datetime import datetime

# ==================== DATA ====================
march_1 = [
    {"id": "周日007", "home": "埃尔切", "away": "西班牙人", "half": "1:1", "full": "2:2", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.37, "draw": 3.06, "away": 2.63}, "final_odds": {"home": 2.30, "draw": 3.14, "away": 2.66}, "changes_1x2": 5, "changes_handicap": 4},
    {"id": "周日008", "home": "特温特", "away": "费耶诺德", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.25, "draw": 3.50, "away": 2.52}, "final_odds": {"home": 1.94, "draw": 3.53, "away": 3.02}, "changes_1x2": 6, "changes_handicap": 5},
    {"id": "周日009", "home": "曼联", "away": "水晶宫", "half": "0:1", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.43, "draw": 4.10, "away": 5.40}, "final_odds": {"home": 1.43, "draw": 4.15, "away": 5.30}, "changes_1x2": 4, "changes_handicap": 2},
    {"id": "周日010", "home": "富勒姆", "away": "热刺", "half": "2:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.86, "draw": 3.45, "away": 3.32}, "final_odds": {"home": 1.90, "draw": 3.40, "away": 3.25}, "changes_1x2": 2, "changes_handicap": 2},
    {"id": "周日011", "home": "萨索洛", "away": "亚特兰大", "half": "1:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 3.63, "draw": 3.35, "away": 1.80}, "final_odds": {"home": 3.35, "draw": 3.25, "away": 1.91}, "changes_1x2": 4, "changes_handicap": 6},
    {"id": "周日012", "home": "巴黎FC", "away": "尼斯", "half": "1:0", "full": "1:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.22, "draw": 3.05, "away": 2.85}, "final_odds": {"home": 2.25, "draw": 2.99, "away": 2.85}, "changes_1x2": 2, "changes_handicap": 2},
    {"id": "周日013", "home": "斯图加特", "away": "沃夫斯堡", "half": "3:0", "full": "4:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.32, "draw": 4.82, "away": 6.10}, "final_odds": {"home": 1.30, "draw": 5.05, "away": 6.15}, "changes_1x2": 6, "changes_handicap": 7},
    {"id": "周日014", "home": "巴伦西亚", "away": "奥萨苏纳", "half": "0:0", "full": "1:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.10, "draw": 2.98, "away": 3.15}, "final_odds": {"home": 2.13, "draw": 2.95, "away": 3.12}, "changes_1x2": 2, "changes_handicap": 3},
    {"id": "周日015", "home": "乌德勒支", "away": "阿尔克马", "half": "2:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.88, "draw": 3.40, "away": 3.30}, "final_odds": {"home": 2.05, "draw": 3.35, "away": 2.92}, "changes_1x2": 5, "changes_handicap": 5},
]

march_2 = [
    {"id": "周日016", "home": "阿森纳", "away": "切尔西", "half": "1:1", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "final_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "changes_1x2": 0, "changes_handicap": 1},
    {"id": "周日017", "home": "法兰克福", "away": "弗赖堡", "half": "0:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.95, "draw": 3.35, "away": 3.15}, "final_odds": {"home": 1.92, "draw": 3.28, "away": 3.30}, "changes_1x2": 1, "changes_handicap": 1},
    {"id": "周日018", "home": "都灵", "away": "拉齐奥", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.89, "draw": 2.81, "away": 2.34}, "final_odds": {"home": 2.66, "draw": 2.72, "away": 2.59}, "changes_1x2": 5, "changes_handicap": 5},
    {"id": "周日019", "home": "贝蒂斯", "away": "塞维利亚", "half": "2:0", "full": "2:2", "result": "平局", "result_code": 1, "initial_odds": {"home": 1.72, "draw": 3.40, "away": 3.95}, "final_odds": {"home": 1.57, "draw": 3.65, "away": 4.60}, "changes_1x2": 3, "changes_handicap": 2},
    {"id": "周日020", "home": "汉堡", "away": "莱红牛", "half": "1:1", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "final_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "changes_1x2": 0, "changes_handicap": 0},
    {"id": "周日021", "home": "罗马", "away": "尤文图斯", "half": "1:0", "full": "3:3", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.40, "draw": 2.88, "away": 2.74}, "final_odds": {"home": 2.43, "draw": 2.78, "away": 2.79}, "changes_1x2": 3, "changes_handicap": 2},
    {"id": "周日022", "home": "马赛", "away": "里昂", "half": "0:1", "full": "3:2", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.92, "draw": 3.35, "away": 3.25}, "final_odds": {"home": 1.81, "draw": 3.45, "away": 3.48}, "changes_1x2": 9, "changes_handicap": 8},
    {"id": "周日023", "home": "赫罗纳", "away": "塞尔塔", "half": "1:0", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.21, "draw": 3.13, "away": 2.80}, "final_odds": {"home": 2.21, "draw": 2.98, "away": 2.93}, "changes_1x2": 2, "changes_handicap": 1},
    {"id": "周日024", "home": "奥兰多", "away": "迈国际", "half": "2:0", "full": "2:4", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.68, "draw": 3.70, "away": 2.06}, "final_odds": {"home": 3.15, "draw": 3.85, "away": 1.81}, "changes_1x2": 6, "changes_handicap": 6},
    {"id": "周一001", "home": "大田市民", "away": "安养FC", "half": "0:0", "full": "1:1", "result": "平局", "result_code": 1, "initial_odds": {"home": 1.69, "draw": 3.35, "away": 4.20}, "final_odds": {"home": 1.82, "draw": 3.32, "away": 3.60}, "changes_1x2": 3, "changes_handicap": 2},
    {"id": "周一002", "home": "韩国女", "away": "伊朗女", "half": "1:0", "full": "3:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": None, "draw": None, "away": None}, "final_odds": {"home": None, "draw": None, "away": None}, "changes_1x2": 0, "changes_handicap": 1},
]

all_matches = march_1 + march_2

# ==================== FEATURE EXTRACTION ====================
def extract_features(match):
    initial = match["initial_odds"]
    final = match["final_odds"]
    
    if initial["home"] is None:
        return None
    
    f = {}
    f["initial_home"] = initial["home"]
    f["initial_draw"] = initial["draw"]
    f["initial_away"] = initial["away"]
    f["final_home"] = final["home"]
    f["final_draw"] = final["draw"]
    f["final_away"] = final["away"]
    f["home_change"] = final["home"] - initial["home"]
    f["draw_change"] = final["draw"] - initial["draw"]
    f["away_change"] = final["away"] - initial["away"]
    f["home_change_pct"] = (final["home"] - initial["home"]) / initial["home"] * 100
    f["draw_change_pct"] = (final["draw"] - initial["draw"]) / initial["draw"] * 100 if initial["draw"] > 0 else 0
    f["away_change_pct"] = (final["away"] - initial["away"]) / initial["away"] * 100
    f["changes_1x2"] = match["changes_1x2"]
    f["changes_handicap"] = match["changes_handicap"]
    
    total = 1/final["home"] + 1/final["draw"] + 1/final["away"]
    f["market_home_prob"] = (1/final["home"]/total)*100
    f["market_draw_prob"] = (1/final["draw"]/total)*100
    f["market_away_prob"] = (1/final["away"]/total)*100
    
    probs = [f["market_home_prob"], f["market_draw_prob"], f["market_away_prob"]]
    f["market_favorite"] = probs.index(max(probs))
    f["home_odds_down"] = 1 if f["home_change"] < 0 else 0
    f["away_odds_down"] = 1 if f["away_change"] < 0 else 0
    f["actual_result"] = match["result_code"]
    
    return f

features_list = [extract_features(m) for m in all_matches]
features_list = [f for f in features_list if f is not None]

print("="*50)
print("DATA ANALYSIS")
print("="*50)
print(f"Valid samples: {len(features_list)}")

results = [f["actual_result"] for f in features_list]
home_wins = results.count(0)
draws = results.count(1)
away_wins = results.count(2)

print(f"\nActual results:")
print(f"  Home wins: {home_wins} ({home_wins/len(results)*100:.1f}%)")
print(f"  Draws: {draws} ({draws/len(results)*100:.1f}%)")
print(f"  Away wins: {away_wins} ({away_wins/len(results)*100:.1f}%)")

# Market accuracy
market_correct = sum(1 for f in features_list if f["market_favorite"] == f["actual_result"])
market_accuracy = market_correct / len(features_list) * 100
print(f"\nMarket accuracy: {market_accuracy:.1f}% ({market_correct}/{len(features_list)})")

# Rule-based model
print("\n" + "="*50)
print("RULE-BASED MODEL")
print("="*50)

def predict_rule(f):
    if f["home_change_pct"] < -5:
        return 0
    if f["away_change_pct"] < -5:
        return 2
    if f["changes_1x2"] > 5 and f["home_change"] < 0:
        return 0
    if f["changes_1x2"] > 5 and f["away_change"] < 0:
        return 2
    return f["market_favorite"]

rule_correct = sum(1 for f in features_list if predict_rule(f) == f["actual_result"])
rule_accuracy = rule_correct / len(features_list) * 100
print(f"Rule model accuracy: {rule_accuracy:.1f}% ({rule_correct}/{len(features_list)})")

# Improved model
print("\n" + "="*50)
print("IMPROVED MODEL")
print("="*50)

def predict_improved(f):
    score = 0
    if f["home_change"] < -0.05:
        score += 2
    elif f["home_change"] > 0.05:
        score -= 1
    if f["away_change"] < -0.05:
        score -= 2
    elif f["away_change"] > 0.05:
        score += 1
    if f["changes_1x2"] >= 5:
        if f["home_change"] < 0:
            score += 1
        if f["away_change"] < 0:
            score -= 1
    if f["initial_home"] < 1.6:
        score += 1
    elif f["initial_home"] > 2.5:
        score -= 1
    
    if score >= 2:
        return 0
    elif score <= -2:
        return 2
    return f["market_favorite"]

improved_correct = sum(1 for f in features_list if predict_improved(f) == f["actual_result"])
improved_accuracy = improved_correct / len(features_list) * 100
print(f"Improved model accuracy: {improved_accuracy:.1f}% ({improved_correct}/{len(features_list)})")

# Final report
print("\n" + "="*50)
print("TRAINING REPORT")
print("="*50)
print(f"""
Sample size: {len(features_list)} matches

Model Accuracy Comparison:
- Market probability: {market_accuracy:.1f}%
- Rule model: {rule_accuracy:.1f}%
- Improved model: {improved_accuracy:.1f}%

Improvement: {improved_accuracy - market_accuracy:+.1f}%

Key Prediction Patterns Found:
1. Home odds drop > 5% = higher home win probability
2. Away odds drop > 5% = higher away win probability  
3. Many changes (>5) + odds drop = more reliable signal
4. Initial odds < 1.6 = strong home team, higher win probability
5. Few changes = market probability more accurate
""")

# Save data
output = {
    "total": len(features_list),
    "home_wins": home_wins, "draws": draws, "away_wins": away_wins,
    "market_accuracy": market_accuracy,
    "rule_accuracy": rule_accuracy,
    "improved_accuracy": improved_accuracy,
    "improvement": improved_accuracy - market_accuracy,
    "matches": features_list
}
with open("training_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print("Data saved to training_data.json")
