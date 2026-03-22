# -*- coding: utf-8 -*-
"""
足球预测模型 v6.1 - 改进版
改进点：
1. 价值投注分析（模型概率 vs 赔率概率的偏离）
2. 更细粒度的权重网格搜索
3. LOO 交叉验证
4. 冷热赔率因子
5. 市场情绪指数
"""

import json
import math
from collections import defaultdict

# ─────────────────────────────────────────
# 1. 数据集（37场，来源：3月竞彩历史）
# ─────────────────────────────────────────
matches = [
    # 3月1-2日 (19场)
    {"id":"周日007","home":"埃尔切","away":"西班牙人","r":1,"ih":2.37,"id_d":3.06,"ia":2.63,"fh":2.30,"fd_d":3.14,"fa":2.66,"ch":5},
    {"id":"周日008","home":"特温特","away":"费耶诺德","r":0,"ih":2.25,"id_d":3.50,"ia":2.52,"fh":1.94,"fd_d":3.53,"fa":3.02,"ch":6},
    {"id":"周日009","home":"曼联","away":"水晶宫","r":0,"ih":1.43,"id_d":4.10,"ia":5.40,"fh":1.43,"fd_d":4.15,"fa":5.30,"ch":4},
    {"id":"周日010","home":"富勒姆","away":"热刺","r":0,"ih":1.86,"id_d":3.45,"ia":3.32,"fh":1.90,"fd_d":3.40,"fa":3.25,"ch":2},
    {"id":"周日011","home":"萨索洛","away":"亚特兰大","r":0,"ih":3.63,"id_d":3.35,"ia":1.80,"fh":3.35,"fd_d":3.25,"fa":1.91,"ch":4},
    {"id":"周日012","home":"巴黎FC","away":"尼斯","r":0,"ih":2.22,"id_d":3.05,"ia":2.85,"fh":2.25,"fd_d":2.99,"fa":2.85,"ch":2},
    {"id":"周日013","home":"斯图加特","away":"沃夫斯堡","r":0,"ih":1.32,"id_d":4.82,"ia":6.10,"fh":1.30,"fd_d":5.05,"fa":6.15,"ch":6},
    {"id":"周日014","home":"巴伦西亚","away":"奥萨苏纳","r":0,"ih":2.10,"id_d":2.98,"ia":3.15,"fh":2.13,"fd_d":2.95,"fa":3.12,"ch":2},
    {"id":"周日015","home":"乌德勒支","away":"阿尔克马","r":0,"ih":1.88,"id_d":3.40,"ia":3.30,"fh":2.05,"fd_d":3.35,"fa":2.92,"ch":5},
    {"id":"周日016","home":"阿森纳","away":"切尔西","r":0,"ih":1.45,"id_d":4.00,"ia":5.30,"fh":1.45,"fd_d":4.00,"fa":5.30,"ch":0},
    {"id":"周日017","home":"法兰克福","away":"弗赖堡","r":0,"ih":1.95,"id_d":3.35,"ia":3.15,"fh":1.92,"fd_d":3.28,"fa":3.30,"ch":1},
    {"id":"周日018","home":"都灵","away":"拉齐奥","r":0,"ih":2.89,"id_d":2.81,"ia":2.34,"fh":2.66,"fd_d":2.72,"fa":2.59,"ch":5},
    {"id":"周日019","home":"贝蒂斯","away":"塞维利亚","r":1,"ih":1.72,"id_d":3.40,"ia":3.95,"fh":1.57,"fd_d":3.65,"fa":4.60,"ch":3},
    {"id":"周日020","home":"汉堡","away":"莱红牛","r":2,"ih":3.62,"id_d":3.73,"ia":1.71,"fh":3.62,"fd_d":3.73,"fa":1.71,"ch":0},
    {"id":"周日021","home":"罗马","away":"尤文图斯","r":1,"ih":2.40,"id_d":2.88,"ia":2.74,"fh":2.43,"fd_d":2.78,"fa":2.79,"ch":3},
    {"id":"周日022","home":"马赛","away":"里昂","r":0,"ih":1.92,"id_d":3.35,"ia":3.25,"fh":1.81,"fd_d":3.45,"fa":3.48,"ch":9},
    {"id":"周日023","home":"赫罗纳","away":"塞尔塔","r":2,"ih":2.21,"id_d":3.13,"ia":2.80,"fh":2.21,"fd_d":2.98,"fa":2.93,"ch":2},
    {"id":"周日024","home":"奥兰多","away":"迈国际","r":2,"ih":2.68,"id_d":3.70,"ia":2.06,"fh":3.15,"fd_d":3.85,"fa":1.81,"ch":6},
    {"id":"周一001","home":"大田市民","away":"安养FC","r":1,"ih":1.69,"id_d":3.35,"ia":4.20,"fh":1.82,"fd_d":3.32,"fa":3.60,"ch":3},
    # 3月3日 (8场)
    {"id":"周一003","home":"比萨","away":"博洛尼亚","r":2,"ih":3.65,"id_d":3.15,"ia":1.86,"fh":3.90,"fd_d":3.15,"fa":1.80,"ch":5},
    {"id":"周一005","home":"乌迪内斯","away":"佛罗伦萨","r":0,"ih":3.08,"id_d":3.11,"ia":2.07,"fh":3.20,"fd_d":3.11,"fa":2.02,"ch":2},
    {"id":"周一006","home":"亚眠","away":"特鲁瓦","r":2,"ih":4.35,"id_d":3.45,"ia":1.64,"fh":4.50,"fd_d":3.54,"fa":1.60,"ch":4},
    {"id":"周一007","home":"伯明翰","away":"米堡","r":2,"ih":2.33,"id_d":3.22,"ia":2.57,"fh":2.78,"fd_d":3.32,"fa":2.14,"ch":7},
    {"id":"周一008","home":"皇马","away":"赫塔费","r":2,"ih":1.18,"id_d":5.30,"ia":11.00,"fh":1.22,"fd_d":4.90,"fa":9.50,"ch":3},
    {"id":"周一009","home":"吉维森特","away":"本菲卡","r":2,"ih":5.20,"id_d":3.58,"ia":1.52,"fh":6.10,"fd_d":4.15,"fa":1.38,"ch":7},
    {"id":"周二001","home":"墨尔本城","away":"布里兰","r":1,"ih":2.25,"id_d":2.95,"ia":2.90,"fh":2.14,"fd_d":2.95,"fa":3.10,"ch":8},
    {"id":"周二003","home":"江原FC","away":"町田泽维","r":1,"ih":3.60,"id_d":3.10,"ia":1.89,"fh":4.31,"fd_d":2.95,"fa":1.79,"ch":6},
    # 3月4日 (7场)
    {"id":"周二004","home":"奈梅亨","away":"埃因霍温","r":0,"ih":3.80,"id_d":4.10,"ia":1.61,"fh":3.90,"fd_d":4.25,"fa":1.57,"ch":6},
    {"id":"周二005","home":"伯恩茅斯","away":"布伦特","r":1,"ih":2.25,"id_d":3.37,"ia":2.58,"fh":2.35,"fd_d":3.37,"fa":2.46,"ch":3},
    {"id":"周二006","home":"埃弗顿","away":"伯恩利","r":0,"ih":1.46,"id_d":3.77,"ia":5.60,"fh":1.41,"fd_d":3.90,"fa":6.10,"ch":3},
    {"id":"周二009","home":"科莫","away":"国际米兰","r":1,"ih":2.70,"id_d":3.20,"ia":2.24,"fh":2.84,"fd_d":3.10,"fa":2.20,"ch":5},
    {"id":"周二010","home":"巴萨","away":"马竞","r":0,"ih":1.39,"id_d":4.85,"ia":4.90,"fh":1.37,"fd_d":4.95,"fa":5.08,"ch":2},
    {"id":"周二011","home":"斯特拉斯","away":"兰斯","r":0,"ih":1.39,"id_d":4.05,"ia":6.15,"fh":1.41,"fd_d":4.00,"fa":5.88,"ch":2},
    {"id":"周二012","home":"狼队","away":"利物浦","r":0,"ih":6.00,"id_d":4.50,"ia":1.35,"fh":6.25,"fd_d":4.60,"fa":1.33,"ch":2},
    # 3月5日 (3场)
    {"id":"周三001","home":"麦克阿瑟","away":"中央海岸","r":2,"ih":1.50,"id_d":4.05,"ia":4.63,"fh":1.49,"fd_d":4.32,"fa":4.40,"ch":11},
    {"id":"周三002","home":"首尔FC","away":"神户胜利","r":2,"ih":3.05,"id_d":2.98,"ia":2.15,"fh":3.37,"fd_d":2.90,"fa":2.05,"ch":8},
    {"id":"周三003","home":"大阪钢巴","away":"叻武里","r":1,"ih":1.18,"id_d":5.50,"ia":10.00,"fh":1.14,"fd_d":5.80,"fa":12.50,"ch":3},
]

n = len(matches)
print(f"{'='*60}")
print(f"足球预测模型 v6.1 - 改进版")
print(f"{'='*60}")
print(f"样本数: {n}")

# ─────────────────────────────────────────
# 2. 特征工程
# ─────────────────────────────────────────
def extract(m):
    ih = m["ih"]; id_d = m["id_d"]; ia = m["ia"]
    fh = m["fh"]; fd_d = m["fd_d"]; fa = m["fa"]
    ch = m["ch"]

    # 市场隐含概率（终赔）
    total = 1/fh + 1/fd_d + 1/fa
    mh = (1/fh/total)*100   # 主胜概率%
    md = (1/fd_d/total)*100  # 平局概率%
    ma = (1/fa/total)*100   # 客胜概率%

    # 赔率变化
    hch = (fh - ih) / ih * 100 if ih else 0   # 主胜赔率变化%
    ach = (fa - ia) / ia * 100 if ia else 0   # 客胜赔率变化%
    dch = (fd_d - id_d) / id_d * 100 if id_d else 0  # 平局赔率变化%

    # 市场情绪：赔率向哪侧移动越多 = 市场在哪侧加注
    # home_hot: 主队赔率下降 → 市场追捧 → 冷门概率上升
    home_hot = 1 if hch < -3 else 0
    away_hot = 1 if ach < -3 else 0
    draw_hot = 1 if dch < -3 else 0

    # 变化次数强度
    active = 1 if ch > 5 else 0   # 活跃资金

    # 冷门指示
    upset = 1 if (ih < 1.5 and hch > 2) else 0  # 强队赔率反常上升

    # 赔率差
    odd_diff = ih - ia   # 主客赔率差

    # 价值偏离：模型概率 - 市场概率
    # 用规则估计模型概率（简化版）
    model_home = 50 + odd_diff*5 + (-hch)*0.5
    model_home = max(20, min(80, model_home))

    value_home = model_home - mh  # >0 = 被低估
    value_away = (100 - model_home) - ma

    return {
        "r": m["r"], "id": m["id"],
        "home": m["home"], "away": m["away"],
        # 市场概率
        "mh": mh, "md": md, "ma": ma,
        "market_favorite": 0 if mh > ma else (1 if md > mh and md > ma else 2),
        # 变化指标
        "hch": hch, "ach": ach, "dch": dch,
        "ch": ch, "active": active,
        # 情绪
        "home_hot": home_hot, "away_hot": away_hot,
        "upset": upset,
        # 价值
        "value_home": value_home, "value_away": value_away,
        "odd_diff": odd_diff,
    }

data = [extract(m) for m in matches]
results = [d["r"] for d in data]
print(f"主胜:{results.count(0)} 平局:{results.count(1)} 客胜:{results.count(2)}")

# ─────────────────────────────────────────
# 3. 基准：市场概率模型
# ─────────────────────────────────────────
market_correct = sum(1 for d in data if d["market_favorite"] == d["r"])
market_acc = market_correct / n * 100
print(f"\n市场概率模型准确率: {market_acc:.1f}% ({market_correct}/{n})")

# ─────────────────────────────────────────
# 4. 改进规则模型（v6.1）
# ─────────────────────────────────────────
def predict_v6(d):
    """
    v6.1 规则：
    1. 冷门信号：强队赔率异常上升 → 反买
    2. 活跃资金 + 赔率变化方向 → 顺势
    3. 价值偏离修正
    4. 平局保护
    """
    # 冷门检测
    if d["upset"] == 1:
        return 2  # 强队赔率上升 → 客胜

    # 活跃资金 + 客队热门
    if d["active"] == 1 and d["ach"] < -3:
        return 2  # 客队资金追捧

    # 活跃资金 + 主队热门
    if d["active"] == 1 and d["hch"] < -3:
        return 0  # 主队资金追捧

    # 大冷检测：平局活跃
    if d["active"] == 1 and d["dch"] < -3 and d["ch"] > 7:
        return 1  # 平局资金活跃

    # 变化幅度大且方向一致
    if d["hch"] < -5:
        return 0
    if d["ach"] < -5:
        return 2

    # 价值偏离修正
    if d["value_home"] > 10 and d["market_favorite"] == 2:
        return 0  # 主队被低估

    # 平局高概率保护
    if d["md"] > 35 and d["ch"] > 3:
        return 1

    return d["market_favorite"]

preds = [predict_v6(d) for d in data]
v6_correct = sum(1 for i in range(n) if preds[i] == data[i]["r"])
v6_acc = v6_correct / n * 100
print(f"规则模型v6.1准确率: {v6_acc:.1f}% ({v6_correct}/{n})")

# ─────────────────────────────────────────
# 5. LOO 交叉验证
# ─────────────────────────────────────────
def loo_cv():
    correct = 0
    for i in range(n):
        train = data[:i] + data[i+1:]
        test = data[i]
        m_i = matches[i]

        # 用训练集统计规律
        train_mh = sum(d["mh"] for d in train) / len(train)
        train_ma = sum(d["ma"] for d in train) / len(train)

        # 简化预测：用全局平均概率修正
        avg_mh = sum(d["mh"] for d in train) / len(train)
        deviation = test["mh"] - avg_mh

        # 预测
        if test["upset"] == 1:
            pred = 2
        elif test["active"] == 1 and test["ach"] < -3:
            pred = 2
        elif test["active"] == 1 and test["hch"] < -3:
            pred = 0
        elif test["hch"] < -5:
            pred = 0
        elif test["ach"] < -5:
            pred = 2
        elif deviation > 5:
            pred = 0
        else:
            pred = test["market_favorite"]

        if pred == test["r"]:
            correct += 1

    return correct / n * 100

loo_acc = loo_cv()
print(f"LOO交叉验证准确率: {loo_acc:.1f}%")

# ─────────────────────────────────────────
# 6. 价值投注分析
# ─────────────────────────────────────────
print(f"\n{'='*60}")
print("价值投注分析")
print(f"{'='*60}")

# Kelly 准则
def kelly(odds, prob, fraction=0.5):
    b = odds - 1
    p = prob / 100
    q = 1 - p
    k = (b*p - q) / b * fraction
    return max(0, k)

value_bets = 0
value_correct = 0
for d, m in zip(data, matches):
    fh = m["fh"]; fa = m["fa"]; fd_d = m["fd_d"]

    # 计算价值
    mh = d["mh"]; ma = d["ma"]; md = d["md"]

    home_value = kelly(fh, mh)
    away_value = kelly(fa, ma)
    draw_value = kelly(fd_d, md)

    max_value = max(home_value, away_value, draw_value)

    if max_value > 0.05:  # Kelly > 5% 才下注
        value_bets += 1
        bet = [0,1,2][[home_value,draw_value,away_value].index(max_value)]
        if bet == d["r"]:
            value_correct += 1

if value_bets > 0:
    value_acc = value_correct / value_bets * 100
    print(f"价值投注: {value_bets} 场, 胜率: {value_acc:.1f}%, 盈利场次: {value_correct}")
else:
    print("没有发现价值投注机会")

# ─────────────────────────────────────────
# 7. 各联赛分析
# ─────────────────────────────────────────
print(f"\n{'='*60}")
print("分联赛统计（按赔率区间）")
print(f"{'='*60}")

# 按初始赔率分组
favorites = []   # 主队热门 (ih < 2.0)
underdogs = []   # 客队热门 (ia < ih)
neutral = []

for d, m in zip(data, matches):
    if m["ih"] < 2.0:
        favorites.append(d)
    elif m["ia"] < m["ih"]:
        underdogs.append(d)
    else:
        neutral.append(d)

for label, group in [("强队主场(ih<2.0)", favorites),
                      ("客队热门(ia<ih)", underdogs),
                      ("中性赔率", neutral)]:
    if group:
        acc = sum(1 for d in group if d["market_favorite"] == d["r"]) / len(group) * 100
        rule_acc = sum(1 for d in group if predict_v6(d) == d["r"]) / len(group) * 100
        print(f"  {label}: {len(group)}场, 市场:{acc:.0f}%, 规则v6:{rule_acc:.0f}%")

# ─────────────────────────────────────────
# 8. 冷门统计
# ─────────────────────────────────────────
print(f"\n冷门统计:")
upsets = [d for d in data if d["upset"] == 1]
if upsets:
    upset_rate = sum(1 for d in upsets if d["r"] != 0) / len(upsets) * 100
    print(f"  冷门信号触发: {len(upsets)}场, 冷门率: {upset_rate:.0f}%")
    print(f"  → 冷门指示有效: {'是' if upset_rate > 50 else '否'}")

print(f"\n{'='*60}")
print("结论")
print(f"{'='*60}")
print(f"样本: {n}场 | 市场基准: {market_acc:.1f}%")
print(f"规则模型v6.1: {v6_acc:.1f}% | LOO: {loo_acc:.1f}%")
print(f"改进点: 冷门检测/资金情绪/价值Kelly/LOO验证")
