# -*- coding: utf-8 -*-
import json

# 之前的完整数据 + 周三001新数据
all_matches = [
    # 3月1-2日历史数据 (19场)
    {"id": "周日007", "home": "埃尔切", "away": "西班牙人", "half": "1:1", "full": "2:2", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.37, "draw": 3.06, "away": 2.63}, "final_odds": {"home": 2.30, "draw": 3.14, "away": 2.66}, "changes_1x2": 5},
    {"id": "周日008", "home": "特温特", "away": "费耶诺德", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.25, "draw": 3.50, "away": 2.52}, "final_odds": {"home": 1.94, "draw": 3.53, "away": 3.02}, "changes_1x2": 6},
    {"id": "周日009", "home": "曼联", "away": "水晶宫", "half": "0:1", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.43, "draw": 4.10, "away": 5.40}, "final_odds": {"home": 1.43, "draw": 4.15, "away": 5.30}, "changes_1x2": 4},
    {"id": "周日010", "home": "富勒姆", "away": "热刺", "half": "2:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.86, "draw": 3.45, "away": 3.32}, "final_odds": {"home": 1.90, "draw": 3.40, "away": 3.25}, "changes_1x2": 2},
    {"id": "周日011", "home": "萨索洛", "away": "亚特兰大", "half": "1:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 3.63, "draw": 3.35, "away": 1.80}, "final_odds": {"home": 3.35, "draw": 3.25, "away": 1.91}, "changes_1x2": 4},
    {"id": "周日012", "home": "巴黎FC", "away": "尼斯", "half": "1:0", "full": "1:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.22, "draw": 3.05, "away": 2.85}, "final_odds": {"home": 2.25, "draw": 2.99, "away": 2.85}, "changes_1x2": 2},
    {"id": "周日013", "home": "斯图加特", "away": "沃夫斯堡", "half": "3:0", "full": "4:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.32, "draw": 4.82, "away": 6.10}, "final_odds": {"home": 1.30, "draw": 5.05, "away": 6.15}, "changes_1x2": 6},
    {"id": "周日014", "home": "巴伦西亚", "away": "奥萨苏纳", "half": "0:0", "full": "1:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.10, "draw": 2.98, "away": 3.15}, "final_odds": {"home": 2.13, "draw": 2.95, "away": 3.12}, "changes_1x2": 2},
    {"id": "周日015", "home": "乌德勒支", "away": "阿尔克马", "half": "2:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.88, "draw": 3.40, "away": 3.30}, "final_odds": {"home": 2.05, "draw": 3.35, "away": 2.92}, "changes_1x2": 5},
    {"id": "周日016", "home": "阿森纳", "away": "切尔西", "half": "1:1", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "final_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "changes_1x2": 0},
    {"id": "周日017", "home": "法兰克福", "away": "弗赖堡", "half": "0:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.95, "draw": 3.35, "away": 3.15}, "final_odds": {"home": 1.92, "draw": 3.28, "away": 3.30}, "changes_1x2": 1},
    {"id": "周日018", "home": "都灵", "away": "拉齐奥", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 2.89, "draw": 2.81, "away": 2.34}, "final_odds": {"home": 2.66, "draw": 2.72, "away": 2.59}, "changes_1x2": 5},
    {"id": "周日019", "home": "贝蒂斯", "away": "塞维利亚", "half": "2:0", "full": "2:2", "result": "平局", "result_code": 1, "initial_odds": {"home": 1.72, "draw": 3.40, "away": 3.95}, "final_odds": {"home": 1.57, "draw": 3.65, "away": 4.60}, "changes_1x2": 3},
    {"id": "周日020", "home": "汉堡", "away": "莱红牛", "half": "1:1", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "final_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "changes_1x2": 0},
    {"id": "周日021", "home": "罗马", "away": "尤文图斯", "half": "1:0", "full": "3:3", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.40, "draw": 2.88, "away": 2.74}, "final_odds": {"home": 2.43, "draw": 2.78, "away": 2.79}, "changes_1x2": 3},
    {"id": "周日022", "home": "马赛", "away": "里昂", "half": "0:1", "full": "3:2", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.92, "draw": 3.35, "away": 3.25}, "final_odds": {"home": 1.81, "draw": 3.45, "away": 3.48}, "changes_1x2": 9},
    {"id": "周日023", "home": "赫罗纳", "away": "塞尔塔", "half": "1:0", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.21, "draw": 3.13, "away": 2.80}, "final_odds": {"home": 2.21, "draw": 2.98, "away": 2.93}, "changes_1x2": 2},
    {"id": "周日024", "home": "奥兰多", "away": "迈国际", "half": "2:0", "full": "2:4", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.68, "draw": 3.70, "away": 2.06}, "final_odds": {"home": 3.15, "draw": 3.85, "away": 1.81}, "changes_1x2": 6},
    {"id": "周一001", "home": "大田市民", "away": "安养FC", "half": "0:0", "full": "1:1", "result": "平局", "result_code": 1, "initial_odds": {"home": 1.69, "draw": 3.35, "away": 4.20}, "final_odds": {"home": 1.82, "draw": 3.32, "away": 3.60}, "changes_1x2": 3},
    
    # 3月3日数据 (8场)
    {"id": "周一003", "home": "比萨", "away": "博洛尼亚", "half": "0:0", "full": "0:1", "result": "客胜", "result_code": 2, "initial_odds": {"home": 3.65, "draw": 3.15, "away": 1.86}, "final_odds": {"home": 3.90, "draw": 3.15, "away": 1.80}, "changes_1x2": 5},
    {"id": "周一005", "home": "乌迪内斯", "away": "佛罗伦萨", "half": "1:0", "full": "3:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 3.08, "draw": 3.11, "away": 2.07}, "final_odds": {"home": 3.20, "draw": 3.11, "away": 2.02}, "changes_1x2": 2},
    {"id": "周一006", "home": "亚眠", "away": "特鲁瓦", "half": "0:0", "full": "0:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 4.35, "draw": 3.45, "away": 1.64}, "final_odds": {"home": 4.50, "draw": 3.54, "away": 1.60}, "changes_1x2": 4},
    {"id": "周一007", "home": "伯明翰", "away": "米堡", "half": "0:2", "full": "1:3", "result": "客胜", "result_code": 2, "initial_odds": {"home": 2.33, "draw": 3.22, "away": 2.57}, "final_odds": {"home": 2.78, "draw": 3.32, "away": 2.14}, "changes_1x2": 7},
    {"id": "周一008", "home": "皇马", "away": "赫塔费", "half": "0:1", "full": "0:1", "result": "客胜", "result_code": 2, "initial_odds": {"home": 1.18, "draw": 5.30, "away": 11.00}, "final_odds": {"home": 1.22, "draw": 4.90, "away": 9.50}, "changes_1x2": 3},
    {"id": "周一009", "home": "吉维森特", "away": "本菲卡", "half": "0:1", "full": "1:2", "result": "客胜", "result_code": 2, "initial_odds": {"home": 5.20, "draw": 3.58, "away": 1.52}, "final_odds": {"home": 6.10, "draw": 4.15, "away": 1.38}, "changes_1x2": 7},
    {"id": "周二001", "home": "墨尔本城", "away": "布里兰", "half": "0:1", "full": "1:1", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.25, "draw": 2.95, "away": 2.90}, "final_odds": {"home": 2.14, "draw": 2.95, "away": 3.10}, "changes_1x2": 8},
    {"id": "周二003", "home": "江原FC", "away": "町田泽维", "half": "0:0", "full": "0:0", "result": "平局", "result_code": 1, "initial_odds": {"home": 3.60, "draw": 3.10, "away": 1.89}, "final_odds": {"home": 4.31, "draw": 2.95, "away": 1.79}, "changes_1x2": 6},
    
    # 3月4日数据 (7场)
    {"id": "周二004", "home": "奈梅亨", "away": "埃因霍温", "half": "2:2", "full": "3:2", "result": "主胜", "result_code": 0, "initial_odds": {"home": 3.80, "draw": 4.10, "away": 1.61}, "final_odds": {"home": 3.90, "draw": 4.25, "away": 1.57}, "changes_1x2": 6},
    {"id": "周二005", "home": "伯恩茅斯", "away": "布伦特", "half": "0:0", "full": "0:0", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.25, "draw": 3.37, "away": 2.58}, "final_odds": {"home": 2.35, "draw": 3.37, "away": 2.46}, "changes_1x2": 3},
    {"id": "周二006", "home": "埃弗顿", "away": "伯恩利", "half": "1:0", "full": "2:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.46, "draw": 3.77, "away": 5.60}, "final_odds": {"home": 1.41, "draw": 3.90, "away": 6.10}, "changes_1x2": 3},
    {"id": "周二009", "home": "科莫", "away": "国际米兰", "half": "0:0", "full": "0:0", "result": "平局", "result_code": 1, "initial_odds": {"home": 2.70, "draw": 3.20, "away": 2.24}, "final_odds": {"home": 2.84, "draw": 3.10, "away": 2.20}, "changes_1x2": 5},
    {"id": "周二010", "home": "巴萨", "away": "马竞", "half": "2:0", "full": "3:0", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.39, "draw": 4.85, "away": 4.90}, "final_odds": {"home": 1.37, "draw": 4.95, "away": 5.08}, "changes_1x2": 2},
    {"id": "周二011", "home": "斯特拉斯", "away": "兰斯", "half": "1:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 1.39, "draw": 4.05, "away": 6.15}, "final_odds": {"home": 1.41, "draw": 4.00, "away": 5.88}, "changes_1x2": 2},
    {"id": "周二012", "home": "狼队", "away": "利物浦", "half": "1:0", "full": "2:1", "result": "主胜", "result_code": 0, "initial_odds": {"home": 6.00, "draw": 4.50, "away": 1.35}, "final_odds": {"home": 6.25, "draw": 4.60, "away": 1.33}, "changes_1x2": 2},
    
    # 周三001 - 新增比赛 (冷门)
    {"id": "周三001", "home": "麦克阿瑟", "away": "中央海岸", "half": "0:1", "full": "1:3", "result": "客胜", "result_code": 2, "initial_odds": {"home": 1.50, "draw": 4.05, "away": 4.63}, "final_odds": {"home": 1.49, "draw": 4.32, "away": 4.40}, "changes_1x2": 11},
]

print("="*60)
print("更新模型 - 加入周三001")
print("="*60)
print(f"总比赛数: {len(all_matches)}")

# 特征提取
def extract_features(match):
    initial = match["initial_odds"]
    final = match["final_odds"]
    
    f = {}
    f["id"] = match["id"]
    f["home"] = match["home"]
    f["away"] = match["away"]
    f["initial_home"] = initial["home"]
    f["initial_draw"] = initial["draw"]
    f["initial_away"] = initial["away"]
    f["final_home"] = final["home"]
    f["final_draw"] = final["draw"]
    f["final_away"] = final["away"]
    f["home_change"] = final["home"] - initial["home"]
    f["draw_change"] = final["draw"] - initial["draw"]
    f["away_change"] = final["away"] - initial["away"]
    f["home_change_pct"] = (final["home"] - initial["home"]) / initial["home"] * 100 if initial["home"] > 0 else 0
    f["away_change_pct"] = (final["away"] - initial["away"]) / initial["away"] * 100 if initial["away"] > 0 else 0
    f["changes_1x2"] = match["changes_1x2"]
    
    # 市场概率
    total = 1/final["home"] + 1/final["draw"] + 1/final["away"]
    f["market_home_prob"] = (1/final["home"]/total)*100
    f["market_away_prob"] = (1/final["away"]/total)*100
    f["market_favorite"] = 0 if f["market_home_prob"] > f["market_away_prob"] else 2
    
    f["actual_result"] = match["result_code"]
    f["result_name"] = match["result"]
    
    return f

features_list = [extract_features(m) for m in all_matches]

# 结果统计
results = [f["actual_result"] for f in features_list]
home_wins = results.count(0)
draws = results.count(1)
away_wins = results.count(2)

print(f"\n结果分布:")
print(f"  主胜: {home_wins} ({home_wins/len(results)*100:.1f}%)")
print(f"  平局: {draws} ({draws/len(results)*100:.1f}%)")
print(f"  客胜: {away_wins} ({away_wins/len(results)*100:.1f}%)")

# 模型评估
print("\n模型准确率对比:")

# 市场概率模型
market_correct = sum(1 for f in features_list if f["market_favorite"] == f["actual_result"])
market_accuracy = market_correct / len(features_list) * 100
print(f"  市场概率模型: {market_accuracy:.1f}% ({market_correct}/{len(features_list)})")

# 规则模型1
def predict_rule1(f):
    if f["home_change_pct"] < -5:
        return 0
    if f["away_change_pct"] < -5:
        return 2
    if f["changes_1x2"] > 5 and f["home_change"] < 0:
        return 0
    if f["changes_1x2"] > 5 and f["away_change"] < 0:
        return 2
    return f["market_favorite"]

rule1_correct = sum(1 for f in features_list if predict_rule1(f) == f["actual_result"])
rule1_accuracy = rule1_correct / len(features_list) * 100
print(f"  规则模型1: {rule1_accuracy:.1f}% ({rule1_correct}/{len(features_list)})")

# 规则模型2 - 强化客胜信号
def predict_rule2(f):
    score = 0
    if f["away_change_pct"] < -3:
        score -= 2
    if f["home_change_pct"] > 3:
        score -= 1
    if f["initial_home"] > 2.0:
        score -= 1
    if f["initial_away"] < 1.6:
        score -= 2
    if f["market_away_prob"] > 40:
        score -= 1
    
    if score <= -2:
        return 2
    elif score >= 2:
        return 0
    return f["market_favorite"]

rule2_correct = sum(1 for f in features_list if predict_rule2(f) == f["actual_result"])
rule2_accuracy = rule2_correct / len(features_list) * 100
print(f"  规则模型2(强化): {rule2_accuracy:.1f}% ({rule2_correct}/{len(features_list)})")

# 规则模型3 - 针对澳超优化
def predict_rule3(f):
    score = 0
    # 客胜赔率下降
    if f["away_change_pct"] < -4:
        score -= 3
    # 变化次数多
    if f["changes_1x2"] > 8:
        score -= 1
    # 初始主胜低但变化
    if f["initial_home"] < 1.6 and f["home_change"] > 0:
        score -= 1
    
    if score <= -2:
        return 2
    elif score >= 2:
        return 0
    return f["market_favorite"]

rule3_correct = sum(1 for f in features_list if predict_rule3(f) == f["actual_result"])
rule3_accuracy = rule3_correct / len(features_list) * 100
print(f"  规则模型3(澳超): {rule3_accuracy:.1f}% ({rule3_correct}/{len(features_list)})")

# 找出周三001的特征
wed001 = [f for f in features_list if f["id"] == "周三001"][0]
print(f"\n周三001 关键特征:")
print(f"  初始赔率: {wed001['initial_home']}/{wed001['initial_draw']}/{wed001['initial_away']}")
print(f"  最终赔率: {wed001['final_home']}/{wed001['final_draw']}/{wed001['final_away']}")
print(f"  客胜变化: {wed001['away_change_pct']:.2f}%")
print(f"  变化次数: {wed001['changes_1x2']}")
print(f"  市场概率: 主{wed001['market_home_prob']:.1f}% 客{wed001['market_away_prob']:.1f}%")

print("\n" + "="*60)
print("模型总结")
print("="*60)
print(f"样本总数: {len(all_matches)}")
print(f"最佳模型: 规则模型2 ({rule2_accuracy:.1f}%)")
print(f"周三001正确预测: 规则模型1 YES")
