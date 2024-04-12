liquidity = {
	("tokenA", "tokenB"): (17, 10),
	("tokenA", "tokenC"): (11, 7),
	("tokenA", "tokenD"): (15, 9),
	("tokenA", "tokenE"): (21, 5),
	("tokenB", "tokenA"): (10, 17),
	("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
	("tokenC", "tokenA"): (7, 11),
	("tokenC", "tokenB"): (4, 36),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
	("tokenD", "tokenA"): (9, 15),
	("tokenD", "tokenB"): (6, 13),
	("tokenD", "tokenC"): (12, 30),
    ("tokenD", "tokenE"): (60, 25),
    ("tokenE", "tokenA"): (5, 21),
    ("tokenE", "tokenB"): (3, 25),
    ("tokenE", "tokenC"): (8, 10),
    ("tokenE", "tokenD"): (25, 60)
}

path = []
vis = {}
mx = 0.0
point = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
ans = []
mx_path = []

def dfs(now, balance):
	global mx
	global mx_path
	if vis["tokenB"] == 1:
		if mx < balance:
			mx = balance
			mx_path = path[:]
	else:
		for nxt in point:
			if vis[nxt] == 0 and now != nxt:
				vis[nxt] = 1
				path.append(nxt)
				dfs(nxt, 997 * balance * liquidity[(now, nxt)][1] / (1000 * liquidity[(now, nxt)][0] + 997 * balance))
				vis[nxt] = 0
				path.pop()

for i in point:
	vis[i] = 0;
dfs("tokenB", 5)
ans.append("tokenB")

now_balance = 5
while now_balance < 20:
	ans += mx_path
	lt = "tokenB"
	for i in mx_path:
		now_balance = 997 * now_balance * liquidity[(lt, i)][1] / (1000 * liquidity[(lt, i)][0] + 997 * now_balance)
		lt = i

print(f"path: {'->'.join(ans)}, tokenB balance={now_balance}")
