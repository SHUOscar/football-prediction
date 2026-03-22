# -*- coding: utf-8 -*-
import json

# 完整数据集
all_matches = [
    {"id": "周日007", "home": "埃尔切", "away": "西班牙人", "result_code": 1, "initial_odds": {"home": 2.37, "draw": 3.06, "away": 2.63}, "final_odds": {"home": 2.30, "draw": 3.14, "away": 2.66}, "changes_1x2": 5},
    {"id": "周日008", "home": "特温特", "away": "费耶诺德", "result_code": 0, "initial_odds": {"home": 2.25, "draw": 3.50, "away": 2.52}, "final_odds": {"home": 1.94, "draw": 3.53, "away": 3.02}, "changes_1x2": 6},
    {"id": "周日009", "home": "曼联", "away": "水晶宫", "result_code": 0, "initial_odds": {"home": 1.43, "draw": 4.10, "away": 5.40}, "final_odds": {"home": 1.43, "draw": 4.15, "away": 5.30}, "changes_1x2": 4},
    {"id": "周日010", "home": "富勒姆", "away": "热刺", "result_code": 0, "initial_odds": {"home": 1.86, "draw": 3.45, "away": 3.32}, "final_odds": {"home": 1.90, "draw": 3.40, "away": 3.25}, "changes_1x2": 2},
    {"id": "周日011", "home": "萨索洛", "away": "亚特兰大", "result_code": 0, "initial_odds": {"home": 3.63, "draw": 3.35, "away": 1.80}, "final_odds": {"home": 3.35, "draw": 3.25, "away": 1.91}, "changes_1x2": 4},
    {"id": "周日012", "home": "巴黎FC", "away": "尼斯", "result_code": 0, "initial_odds": {"home": 2.22, "draw": 3.05, "away": 2.85}, "final_odds": {"home": 2.25, "draw": 2.99, "away": 2.85}, "changes_1x2": 2},
    {"id": "周日013", "home": "斯图加特", "away": "沃夫斯堡", "result_code": 0, "initial_odds": {"home": 1.32, "draw": 4.82, "away": 6.10}, "final_odds": {"home": 1.30, "draw": 5.05, "away": 6.15}, "changes_1x2": 6},
    {"id": "周日014", "home": "巴伦西亚", "away": "奥萨苏纳", "result_code": 0, "initial_odds": {"home": 2.10, "draw": 2.98, "away": 3.15}, "final_odds": {"home": 2.13, "draw": 2.95, "away": 3.12}, "changes_1x2": 2},
    {"id": "周日015", "home": "乌德勒支", "away": "阿尔克马", "result_code": 0, "initial_odds": {"home": 1.88, "draw": 3.40, "away": 3.30}, "final_odds": {"home": 2.05, "draw": 3.35, "away": 2.92}, "changes_1x2": 5},
    {"id": "周日016", "home": "阿森纳", "away": "切尔西", "result_code": 0, "initial_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "final_odds": {"home": 1.45, "draw": 4.00, "away": 5.30}, "changes_1x2": 0},
    {"id": "周日017", "home": "法兰克福", "away": "弗赖堡", "result_code": 0, "initial_odds": {"home": 1.95, "draw": 3.35, "away": 3.15}, "final_odds": {"home": 1.92, "draw": 3.28, "away": 3.30}, "changes_1x2": 1},
    {"id": "周日018", "home": "都灵", "away": "拉齐奥", "result_code": 0, "initial_odds": {"home": 2.89, "draw": 2.81, "away": 2.34}, "final_odds": {"home": 2.66, "draw": 2.72, "away": 2.59}, "changes_1x2": 5},
    {"id": "周日019", "home": "贝蒂斯", "away": "塞维利亚", "result_code": 1, "initial_odds": {"home": 1.72, "draw": 3.40, "away": 3.95}, "final_odds": {"home": 1.57, "draw": 3.65, "away": 4.60}, "changes_1x2": 3},
    {"id": "周日020", "home": "汉堡", "away": "莱红牛", "result_code": 2, "initial_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "final_odds": {"home": 3.62, "draw": 3.73, "away": 1.71}, "changes_1x2": 0},
    {"id": "周日021", "home": "罗马", "away": "尤文图斯", "result_code": 1, "initial_odds": {"home": 2.40, "draw": 2.88, "away": 2.74}, "final_odds": {"home": 2.43, "draw": 2.78, "away": 2.79}, "changes_1x2": 3},
    {"id": "周日022", "home": "马赛", "away": "里昂", "result_code": 0, "initial_odds": {"home": 1.92, "draw": 3.35, "away": 3.25}, "final_odds": {"home": 1.81, "draw": 3.45, "away": 3.48}, "changes_1x2": 9},
    {"id": "周日023", "home": "赫罗纳", "away": "塞尔塔", "result_code": 2, "initial_odds": {"home": 2.21, "draw": 3.13, "away": 2.80}, "final_odds": {"home": 2.21, "draw": 2.98, "away": 2.93}, "changes_1x2": 2},
    {"id": "周日024", "home": "奥兰多", "away": "迈国际", "result_code": 2, "initial_odds": {"home": 2.68, "draw": 3.70, "away": 2.06}, "final_odds": {"home": 3.15, "draw": 3.85, "away": 1.81}, "changes_1x2": 6},
    {"id": "周一001", "home": "大田市民", "away": "安养FC", "result_code": 1, "initial_odds": {"home": 1.69, "draw": 3.35, "away": 4.20}, "final_odds": {"home": 1.82, "draw": 3.32, "away": 3.60}, "changes_1x2": 3},
    {"id": "周一003", "home": "比萨", "away": "博洛尼亚", "result_code": 2, "initial_odds": {"home": 3.65, "draw": 3.15, "away": 1.86}, "final_odds": {"home": 3.90, "draw": 3.15, "away": 1.80}, "changes_1x2": 5},
    {"id": "周一005", "home": "乌迪内斯", "away": "佛罗伦萨", "result_code": 0, "initial_odds": {"home": 3.08, "draw": 3.11, "away": 2.07}, "final_odds": {"home": 3.20, "draw": 3.11, "away": 2.02}, "changes_1x2": 2},
    {"id": "周一006", "home": "亚眠", "away": "特鲁瓦", "result_code": 2, "initial_odds": {"home": 4.35, "draw": 3.45, "away": 1.64}, "final_odds": {"home": 4.50, "draw": 3.54, "away": 1.60}, "changes_1x2": 4},
    {"id": "周一007", "home": "伯明翰", "away": "米堡", "result_code": 2, "initial_odds": {"home": 2.33, "draw": 3.22, "away": 2.57}, "final_odds": {"home": 2.78, "draw": 3.32, "away": 2.14}, "changes_1x2": 7},
    {"id": "周一008", "home": "皇马", "away": "赫塔费", "result_code": 2, "initial_odds": {"home": 1.18, "draw": 5.30, "away": 11.00}, "final_odds": {"home": 1.22, "draw": 4.90, "away": 9.50}, "changes_1x2": 3},
    {"id": "周一009", "home": "吉维森特", "away": "本菲卡", "result_code": 2, "initial_odds": {"home": 5.20, "draw": 3.58, "away": 1.52}, "final_odds": {"home": 6.10, "draw": 4.15, "away": 1.38}, "changes_1x2": 7},
    {"id": "周二001", "home": "墨尔本城", "away": "布里兰", "result_code": 1, "initial_odds": {"home": 2.25, "draw": 2.95, "away": 2.90}, "final_odds": {"home": 2.14, "draw": 2.95, "away": 3.10}, "changes_1x2": 8},
    {"id": "周二003", "home": "江原FC", "away": "町田泽维", "result_code": 1, "initial_odds": {"home": 3.60, "draw": 3.10, "away": 1.89}, "final_odds": {"home": 4.31, "draw": 2.95, "away": 1.79}, "changes_1x2": 6},
    {"id": "周二004", "home": "奈梅亨", "away": "埃因霍温", "result_code": 0, "initial_odds": {"home": 3.80, "draw": 4.10, "away": 1.61}, "final_odds": {"home": 3.90, "draw": 4.25, "away": 1.57}, "changes_1x2": 6},
    {"id": "周二005", "home": "伯恩茅斯", "away": "布伦特", "result_code": 1, "initial_odds": {"home": 2.25, "draw": 3.37, "away": 2.58}, "final_odds": {"home": 2.35, "draw": 3.37, "away": 2.46}, "changes_1x2": 3},
    {"id": "周二006", "home": "埃弗顿", "away": "伯恩利", "result_code": 0, "initial_odds": {"home": 1.46, "draw": 3.77, "away": 5.60}, "final_odds": {"home": 1.41, "draw": 3.90, "away": 6.10}, "changes_1x2": 3},
    {"id": "周二009", "home": "科莫", "away": "国际米兰", "result_code": 1, "initial_odds": {"home": 2.70, "draw": 3.20, "away": 2.24}, "final_odds": {"home": 2.84, "draw": 3.10, "away": 2.20}, "changes_1x2": 5},
    {"id": "周二010", "home": "巴萨", "away": "马竞", "result_code": 0, "initial_odds": {"home": 1.39, "draw": 4.85, "away": 4.90}, "final_odds": {"home": 1.37, "draw": 4.95, "away": 5.08}, "changes_1x2": 2},
    {"id": "周二011", "home": "斯特拉斯", "away": "兰斯", "result_code": 0, "initial_odds": {"home": 1.39, "draw": 4.05, "away": 6.15}, "final_odds": {"home": 1.41, "draw": 4.00, "away": 5.88}, "changes_1x2": 2},
    {"id": "周二012", "home": "狼队", "away": "利物浦", "result_code": 0, "initial_odds": {"home": 6.00, "draw": 4.50, "away": 1.35}, "final_odds": {"home": 6.25, "draw": 4.60, "away": 1.33}, "changes_1x2": 2},
    {"id": "周三001", "home": "麦克阿瑟", "away": "中央海岸", "result_code": 2, "initial_odds": {"home": 1.50, "draw": 4.05, "away": 4.63}, "final_odds": {"home": 1.49, "draw": 4.32, "away": 4.40}, "changes_1x2": 11},
    {"id": "周三002", "home": "首尔FC", "away": "神户胜利", "result_code": 2, "initial_odds": {"home": 3.05, "draw": 2.98, "away": 2.15}, "final_odds": {"home": 3.37, "draw": 2.90, "away": 2.05}, "changes_1x2": 8},
    {"id": "周三003", "home": "大阪钢巴", "away": "叻武里", "result_code": 1, "initial_odds": {"home": 1.18, "draw": 5.50, "away": 10.00}, "final_odds": {"home": 1.14, "draw": 5.80, "away": 12.50}, "changes_1x2": 3},
]

# 特征提取
def get_features(m):
    i, f = m["initial_odds"], m["final_odds"]
    total = 1/f["home"] + 1/f["draw"] + 1/f["away"]
    market_home = (1/f["home"]/total)*100
    market_away = (1/f["away"]/total)*100
    
    return {
        "id": m["id"],
        "actual": m["result_code"],
        "initial_home": i["home"],
        "initial_away": i["away"],
        "final_home": f["home"],
        "final_away": f["away"],
        "home_change": f["home"] - i["home"],
        "away_change": f["away"] - i["away"],
        "home_change_pct": (f["home"] - i["home"]) / i["home"] * 100 if i["home"] > 0 else 0,
        "away_change_pct": (f["away"] - i["away"]) / i["away"] * 100 if i["away"] > 0 else 0,
        "changes": m["changes_1x2"],
        "market_home": market_home,
        "market_away": market_away,
        "market_fav": 0 if market_home > market_away else 2,
    }

data = [get_features(m) for m in all_matches]
n = len(data)

print(f"总样本: {n}")
results = [d["actual"] for d in data]
print(f"主胜: {results.count(0)}, 平局: {results.count(1)}, 客胜: {results.count(2)}")

# 尝试不同的策略
strategies = []

# 策略1: 市场概率
pred1 = [d["market_fav"] for d in data]
acc1 = sum(1 for p,a in zip(pred1, results) if p==a)/n*100
strategies.append(("市场概率", acc1))

# 策略2: 原始规则
def rule2(d):
    if d["home_change_pct"] < -5: return 0
    if d["away_change_pct"] < -5: return 2
    if d["changes"] > 5 and d["home_change"] < 0: return 0
    if d["changes"] > 5 and d["away_change"] < 0: return 2
    return d["market_fav"]
pred2 = [rule2(d) for d in data]
acc2 = sum(1 for p,a in zip(pred2, results) if p==a)/n*100
strategies.append(("规则模型", acc2))

# 策略3: 客胜加强
def rule3(d):
    score = 0
    if d["away_change_pct"] < -4: score -= 3
    if d["home_change_pct"] > 4: score -= 2
    if d["away_change"] < 0: score -= 1
    if d["initial_away"] < 1.5: score -= 2
    if score <= -2: return 2
    return d["market_fav"]
pred3 = [rule3(d) for d in data]
acc3 = sum(1 for p,a in zip(pred3, results) if p==a)/n*100
strategies.append(("客胜加强", acc3))

# 策略4: 强队主胜
def rule4(d):
    if d["initial_home"] < 1.4: return 0
    if d["home_change_pct"] < -5: return 0
    if d["away_change_pct"] < -5: return 2
    if d["initial_home"] > 3.0 and d["away_change_pct"] < -3: return 2
    return d["market_fav"]
pred4 = [rule4(d) for d in data]
acc4 = sum(1 for p,a in zip(pred4, results) if p==a)/n*100
strategies.append(("强队主胜", acc4))

# 策略5: 变化次数
def rule5(d):
    if d["changes"] > 6 and d["away_change"] < 0: return 2
    if d["changes"] > 6 and d["home_change"] < 0: return 0
    if d["away_change_pct"] < -5: return 2
    if d["home_change_pct"] < -5: return 0
    return d["market_fav"]
pred5 = [rule5(d) for d in data]
acc5 = sum(1 for p,a in zip(pred5, results) if p==a)/n*100
strategies.append(("变化次数", acc5))

# 策略6: 综合评分
def rule6(d):
    score = 0
    if d["away_change_pct"] < -3: score -= 2
    if d["home_change_pct"] > 5: score -= 1
    if d["initial_home"] > 2.5: score -= 1
    if d["initial_away"] < 1.5: score -= 2
    if d["changes"] > 5: score += 0.5 if d["home_change"] < 0 else -0.5
    if score <= -2: return 2
    if score >= 2: return 0
    return d["market_fav"]
pred6 = [rule6(d) for d in data]
acc6 = sum(1 for p,a in zip(pred6, results) if p==a)/n*100
strategies.append(("综合评分", acc6))

# 策略7: 冷门检测
def rule7(d):
    # 强队主胜赔率上升 = 危险信号
    if d["initial_home"] < 1.5 and d["home_change"] > 0: return 2
    if d["initial_home"] < 1.5 and d["home_change"] < 0: return 0
    if d["away_change_pct"] < -5: return 2
    if d["home_change_pct"] < -5: return 0
    return d["market_fav"]
pred7 = [rule7(d) for d in data]
acc7 = sum(1 for p,a in zip(pred7, results) if p==a)/n*100
strategies.append(("冷门检测", acc7))

# 策略8: 平局检测
def rule8(d):
    # 变化次数多+赔率接近
    if abs(d["final_home"] - d["final_away"]) < 0.3 and d["changes"] > 4: return 1
    if d["away_change_pct"] < -5: return 2
    if d["home_change_pct"] < -5: return 0
    return d["market_fav"]
pred8 = [rule8(d) for d in data]
acc8 = sum(1 for p,a in zip(pred8, results) if p==a)/n*100
strategies.append(("平局检测", acc8))

# 排序输出
strategies.sort(key=lambda x: x[1], reverse=True)
print("\n策略排名:")
for name, acc in strategies:
    print(f"  {name}: {acc:.1f}%")

print(f"\n最佳: {strategies[0][0]} ({strategies[0][1]:.1f}%)")
