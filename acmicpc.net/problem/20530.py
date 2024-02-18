from typing import Set, Tuple, Dict

from copy import deepcopy

Path = Tuple[int, int]
Paths = Dict[int, Set[int]]
Query = Path


def make_graph(lines: Tuple[Path]):
    paths: dict[int, set] = {}
    for line in lines:
        A, B = line
        if paths.get(A):
            paths[A].add(B)
        else:
            paths[A] = {B}
        if paths.get(B):
            paths[B].add(A)
        else:
            paths[B] = {A}
    return paths


def filter_cycle_path(_paths: Paths):
    paths = deepcopy(_paths)

    is_tree_path = True

    while (is_tree_path):
        is_tree_path = False

        for key in list(paths):
            nodes = paths[key]

            if len(nodes) == 1:
                is_tree_path = True

                leaf_parent_nodes = paths.pop(key)
                for node in leaf_parent_nodes:
                    paths[node].remove(key)
    return paths


def filter_tree_path(_paths: Paths, cycle_path: Paths):
    paths = deepcopy(_paths)
    keys = tuple(cycle_path)

    for key in keys:
        if cycle_path.get(key):
            difference = paths[key].difference(cycle_path[key])
            if len(difference) > 0:
                paths[key] = difference
            else:
                paths.pop(key)
    return paths


def is_in_same_tree(cycle_nodes: Tuple[int], tree_path: Paths, queries: Tuple[Query]) -> Tuple[bool]:
    def go(query: Query):
        start, end = query

        in_cycle = start in cycle_nodes and end in cycle_nodes
        if in_cycle:
            return False

        def search(cursor: int, history: Tuple[int]):
            if cursor == end:
                return True

            if not cursor in tree_path:
                return False

            for node in tree_path[cursor]:
                if node in history:
                    continue
                return search(node, (*history, node))

            # 시작과 끝 노드 중에 하나가 사이클 노드이다.
            return False

        return search(start, (start,))

    return tuple(map(go, queries))


test_cases = [
    {
        "raw_paths": ((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (2, 3)),
        "paths": {1: {2, 3}, 2: {1, 4, 5, 3}, 3: {1, 6, 7, 2}, 4: {2}, 5: {2}, 6: {3}, 7: {3}},
        "cycle_path": {1: {2, 3}, 2: {1, 3}, 3: {1, 2}},
        "tree_path": {2: {4, 5}, 3: {6, 7}, 4: {2}, 5: {2}, 6: {3}, 7: {3}},
        "queries": ((2, 4), (4, 5), (1, 4), (6, 2)),
        "result": (True, True, False, False)
    },
    {
        "raw_paths": ((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (2, 3), (4, 8), (4, 9), (3, 6), (3, 7)),
        "paths": {1: {2, 3}, 2: {1, 4, 5, 3}, 3: {1, 6, 7, 2}, 4: {2, 8, 9}, 5: {2}, 6: {3}, 7: {3}, 8: {4}, 9: {4}},
        "cycle_path": {1: {2, 3}, 2: {1, 3}, 3: {1, 2}},
        "tree_path": {2: {4, 5}, 3: {6, 7}, 4: {2, 8, 9}, 5: {2}, 6: {3}, 7: {3}, 8: {4}, 9: {4}},
        "queries": ((2, 4), (2, 8), (9, 8), (5, 8)),
        "result": (True, True, True, True)
    },
]


def test_make_graph():
    for test_case in test_cases:
        raw_paths = test_case["raw_paths"]
        paths = test_case["paths"]
        assert make_graph(raw_paths) == paths


def test_filter_cycle_path():
    for test_case in test_cases:
        paths = test_case["paths"]
        cycle_path = test_case["cycle_path"]
        assert filter_cycle_path(paths) == cycle_path


def test_filter_tree_path():
    for test_case in test_cases:
        paths = test_case["paths"]
        cycle_path = test_case["cycle_path"]
        tree_path = test_case["tree_path"]
        assert filter_tree_path(paths, cycle_path) == tree_path


def test_is_in_same_tree():
    from utils import check_time_limit
    wrapped = check_time_limit(is_in_same_tree, 1)

    for test_case in test_cases:
        cycle_nodes = tuple(test_case["cycle_path"].keys())
        tree_path = test_case["tree_path"]

        queries = test_case["queries"]
        queries = queries * (200000 - len(queries))

        result = test_case["result"]
        assert wrapped(cycle_nodes, tree_path, queries) == result


if __name__ == "__main__":
    from sys import stdin
    def split_line_input(): return map(int, stdin.readline().split())

    N, Q = split_line_input()
    raw_paths = tuple(tuple(split_line_input()) for __ in range(N))
    queries = tuple(tuple(split_line_input()) for __ in range(Q))

    paths = make_graph(raw_paths)
    cycle_path = filter_cycle_path(paths)
    tree_path = filter_tree_path(paths, cycle_path)

    results = is_in_same_tree(tuple(cycle_path.keys()), tree_path, queries)

    for result in results:
        print({True: 1, False: 2}[result])
