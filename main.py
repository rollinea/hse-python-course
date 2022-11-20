import sys

print(sys.executable)
import numpy as np


def main(n, wire_colors, wire_to_connector):
    def read_data(n, wire_colors, wire_to_connector):
        connector_color = [-1 for _ in range(2 * n)]

        connector_to_wire = [[] for _ in range(n)]

        for i in range(2 * n):
            connector_color[i] = wire_colors[wire_to_connector[i] - 1]
            connector_to_wire[wire_to_connector[i] - 1].append(i)

        return n, wire_colors, wire_to_connector, connector_to_wire, connector_color

    def sat_construct(n, connector_to_wire, wire_to_connector, connector_color):
        wire_to_connector.append(wire_to_connector[0])
        connector_color.append(connector_color[0])
        g = [[] for _ in range(4 * n)]
        grev = [[] for _ in range(4 * n)]

        for v in range(2 * n):
            if v == 2 * n - 1:
                if wire_to_connector[v] == wire_to_connector[0]:
                    continue
                elif (wire_to_connector[v] != wire_to_connector[0]) and (connector_color[v] != connector_color[0]):
                    continue
                else:
                    g[v].append(0 + 2 * n)
                    g[0].append(v + 2 * n)

                    grev[0 + 2 * n].append(v)
                    grev[v + 2 * n].append(0)
            else:
                if wire_to_connector[v] == wire_to_connector[v + 1]:
                    continue
                elif (wire_to_connector[v] != wire_to_connector[v + 1]) and (
                        connector_color[v] != connector_color[v + 1]):
                    continue
                else:
                    g[v].append(v + 1 + 2 * n)
                    g[v + 1].append(v + 2 * n)

                    grev[v + 1 + 2 * n].append(v)
                    grev[v + 2 * n].append(v + 1)

        for connectors in connector_to_wire:
            c1, c2 = connectors

            g[c1].append(c2 + 2 * n)
            g[c2].append(c1 + 2 * n)
            g[c1 + 2 * n].append(c2)
            g[c2 + 2 * n].append(c1)

            grev[connectors[1] + 2 * n].append(connectors[0])
            grev[connectors[0] + 2 * n].append(connectors[1])
            grev[connectors[1]].append(connectors[0] + 2 * n)
            grev[connectors[0]].append(connectors[1] + 2 * n)

        return g, grev

    def topsort(v):
        used[v] = True
        for neigh in g[v]:
            if not used[neigh]:
                topsort(neigh)

        order.append(v)
        return

    def dfs2(v, no):
        cid[v] = no
        for neigh in grev[v]:
            if cid[neigh] == -1:
                dfs2(neigh, no)
        return

    n, wire_colors, wire_to_connector, connector_to_wire, connector_color = read_data(n, wire_colors, wire_to_connector)
    g, grev = sat_construct(n, connector_to_wire, wire_to_connector, connector_color)

    used = [False for _ in range(4 * n)]
    order = []

    for v in range(4 * n):
        if not used[v]:
            topsort(v)

    order.reverse()
    cid = [-1 for _ in range(4 * n)]
    color = 0

    for v in range(4 * n):
        if cid[v] == -1:
            dfs2(v, color)
            color += 1

    ans = [-1 for _ in range(2*n)]
    flaq = True
    for v in range(2 * n):
        if cid[v] == cid[v + 2 * n]:
            sys.stdout.write('NO')
            flaq = False
            break
        elif cid[v] < cid[v + 2 * n]:
            ans[v] = 0
        else:
            ans[v] = 1

    if flaq:
        if not any(ans):
            return tuple(['NO', 234234234])
        else:
            ans_2 = [-1 for _ in range(n)]

            for i in range(2 * n):
                if ans[i] == 1:
                    ans_2[wire_to_connector[i]] = i

            return ('YES', ans_2)


def gen_test(wnum, colors=None, num_colors=None):
    if colors is None:
        num_colors = wnum if num_colors is None else num_colors
        assert num_colors > 0
        colors = np.random.randint(0, num_colors, (wnum,))

    chosen_1 = np.random.choice(2 * wnum, wnum, replace=False)
    to_choose = np.random.permutation(np.setdiff1d(np.arange(2 * wnum), chosen_1))

    connectors = np.zeros(2 * wnum, dtype=int)

    for ind, w in enumerate(chosen_1):
        connectors[w] = int(ind)
    for ind, w in enumerate(to_choose):
        connectors[w] = int(ind)
    return wnum, list(colors), list(connectors)


def test_check(wnum, test, ans):
    _, cols, cons = test
    ans_, sol = ans
    if ans_ == "NO":
        print("No solution")
        return
    for i, s in enumerate(sol):
        if cons[s] != i:
            print(f"U can't use that con: {s} with that wire: {i}")
            return

        next_con = (s + 1) % (2 * wnum)

        if next_con in sol[i:]:
            if cols[i] == cols[cons[next_con]]:
                print(f"Invalid solution trying to connect: {s} and {next_con}]")
                return
        prev_con = (s - 1) % (2 * wnum)

        if prev_con in sol[i:]:
            if cols[i] == cols[cons[prev_con]]:
                print(f"Invalid solution trying to connect: {s} and {prev_con}]")
                return


for i in range(5):
    test = gen_test(3)
    n, wire_colors, wire_to_connector = test
    print("Look at test:")
    print(wire_colors)
    print(wire_to_connector)
    print("Here is the answer:")
    ans = main(n, wire_colors, wire_to_connector)
    print(ans)
    print("CHECK SOLUTION")
    print(test_check(n, test, ans))
