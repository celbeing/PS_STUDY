import sys
sys.setrecursionlimit(10000)

def find_best_computer(n, connections):
    tree = [[] for _ in range(n + 1)]
    for a, b in connections:
        tree[a].append(b)
        tree[b].append(a)

    max_score = 0
    best_node = n + 1

    def dfs(node, parent):
        size = 1
        component_sizes = []

        for neighbor in tree[node]:
            if neighbor != parent:
                child_size = dfs(neighbor, node)
                component_sizes.append(child_size)
                size += child_size

        if parent != -1:
            component_sizes.append(n - size)

        score = 1
        for comp in component_sizes:
            score *= comp if comp > 0 else 1

        nonlocal max_score, best_node
        if score > max_score or (score == max_score and node < best_node):
            max_score = score
            best_node = node

        return size

    dfs(1, -1)
    return best_node, max_score

N = int(input())
connections = [tuple(map(int, input().split())) for _ in range(N - 1)]
node, score = find_best_computer(N, connections)
print(node, score)
