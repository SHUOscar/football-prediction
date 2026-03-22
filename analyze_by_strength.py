# -*- coding: utf-8 -*-
# 按强弱队分组分析

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

# 按强弱队分组
strong_home = []  # 主队强 (ih < 1.6)
weak_home = []     # 主队弱 (ih > 2.0)
neutral = []       # 中立

for m in matches:
    fh, fa = m["fh"], m["fa"]
    total = 1/fh + 1/3.2 + 1/fa
    market_home = (1/fh/total)*100
    market_away = (1/fa/total)*100
    
    f = {
        "r": m["r"],
        "mf": 0 if market_home > market_away else 2,
        "hcp": (fh-m["ih"])/m["ih"]*100,
        "acp": (fa-m["ia"])/m["ia"]*100,
        "ch": m["ch"],
        "ih": m["ih"],
    }
    
    if m["ih"] < 1.6:
        strong_home.append(f)
    elif m["ih"] > 2.0:
        weak_home.append(f)
    else:
        neutral.append(f)

print("="*60)
print("按强弱队分组分析")
print("="*60)

for name, group in [("强队主场", strong_home), ("弱队主场", weak_home), ("均势", neutral)]:
    if not group:
        continue
    n = len(group)
    r = [g["r"] for g in group]
    home = r.count(0)
    draw = r.count(1)
    away = r.count(2)
    
    # 市场概率准确率
    market_correct = sum(1 for g in group if g["mf"] == g["r"])
    market_acc = market_correct/n*100
    
    print(f"\n【{name}】共{n}场")
    print(f"  结果分布: 主{home}({home/n*100:.0f}%) 平{draw}({draw/n*100:.0f}%) 客{away}({away/n*100:.0f}%)")
    print(f"  市场概率准确率: {market_acc:.1f}%")

# 分析强队主场的规律
print("\n" + "="*60)
print("强队主场详细分析")
print("="*60)

print("\n【强队主场 - 客胜赔率变化与结果】")
for g in strong_home:
    r_name = ["主胜", "平", "客胜"][g["r"]]
    print(f"  客胜变化: {g['acp']:+.1f}%  变化次数:{g['ch']:2d}  结果:{r_name}")

# 强队主场的规律
print("\n【强队主场规律】")
# 客胜变化 < -5%
cond1 = [g for g in strong_home if g["acp"] < -5]
if cond1:
    correct = sum(1 for g in cond1 if g["r"] == 2)
    print(f"  客胜变化<-5%: {len(cond1)}场, 客胜{correct}场 ({correct/len(cond1)*100:.0f}%)")

# 变化次数多
cond2 = [g for g in strong_home if g["ch"] > 5]
if cond2:
    correct = sum(1 for g in cond2 if g["r"] == 2)
    print(f"  变化次数>5: {len(cond2)}场, 客胜{correct}场 ({correct/len(cond2)*100:.0f}%)")

# 强队主场赔率上升
cond3 = [g for g in strong_home if g["hcp"] > 0]
if cond3:
    correct = sum(1 for g in cond3 if g["r"] == 2)
    print(f"  主胜赔率上升: {len(cond3)}场, 客胜{correct}场 ({correct/len(cond3)*100:.0f}%)")
