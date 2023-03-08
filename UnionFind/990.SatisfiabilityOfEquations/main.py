class Solution:
    def equationsPossible(self, equations: list) -> bool:

        def find(a):
            if a != uf[a]:
                uf[a] = find(uf[a])
            return uf[a]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return True
            uf[pa] = pb
            return False

        uf = dict()
        ineqs = []
        for eq in equations:
            if eq[0] not in uf:
                uf[eq[0]] = eq[0]
            if eq[3] not in uf:
                uf[eq[3]] = eq[3]

            if eq[1] == "=":
                union(eq[0], eq[3])
            else:
                ineqs.append((eq[0], eq[3]))

        for l, r in ineqs:
            if find(l) == find(r):
                return False

        return True
