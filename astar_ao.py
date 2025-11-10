import heapq
def a_star(g, s, e):
    r, c = len(g), len(g[0])
    def h(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
    ol = [(0, 0, s)]; cf = {}
    gs = { (i, j): float('inf') for i in range(r) for j in range(c) }
    gs[s] = 0
    fs = { (i, j): float('inf') for i in range(r) for j in range(c) }
    fs[s] = h(s, e)
    oh = {s}
    while ol:
        _, cg, cp = heapq.heappop(ol)
        oh.remove(cp)
        if cp == e:
            p = []
            while cp in cf: p.append(cp); cp = cf[cp]
            p.append(s); return p[::-1]
        cr, cc = cp
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = (cr + dr, cc + dc)
            if not (0 <= np[0] < r and 0 <= np[1] < c) or g[np[0]][np[1]] == 1: continue
            tgs = cg + 1
            if tgs < gs[np]:
                cf[np] = cp; gs[np] = tgs; fs[np] = tgs + h(np, e)
                if np not in oh: heapq.heappush(ol, (fs[np], tgs, np)); oh.add(np)
    return None

def ao_star(g, h, s):
    sol = {}
    def get_n(n): return g.get(n, [])
    def get_h(n): return h.get(n, 0)
    def set_h(n, v): h[n] = v
    def min_cost_c(n):
        mc = 0; c_dict = {0: []}; f = True
        for p in get_n(n):
            cst = 0; cn = []
            for c in p: cst += get_h(c) + 1; cn.append(c)
            if f: mc = cst; c_dict[mc] = cn; f = False
            elif cst < mc: mc = cst; c_dict.clear(); c_dict[mc] = cn
        return mc, c_dict.get(mc)
    def solve(n, bt):
        if get_h(n) >= 0:
            mc, cn = min_cost_c(n)
            set_h(n, mc); sol[n] = cn
            if bt:
                for p_n in g:
                    if n in [c for p in g[p_n] for c in p]: solve(p_n, True)
            if cn:
                for c in cn:
                    if not get_h(c) == -1: solve(c, False)
    solve(s, False)
    return sol