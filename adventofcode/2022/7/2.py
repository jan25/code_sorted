import importlib
from typing import Tuple, Optional

first = importlib.import_module("1")


def find_dir(node: first.Node, min_size: int) -> Tuple[int, Optional[int]]:
    if node is None:
        assert False, 'should never happen: node is None'

    size = node.size
    candidate = None
    for c in node.children.values():
        csize, ccandidate = find_dir(c, min_size)
        size += csize
        if ccandidate is None:
            continue
        if candidate is None or candidate > ccandidate:
            candidate = ccandidate

    if candidate is None and size >= min_size:
        candidate = size
    return size, candidate


if __name__ == "__main__":
    root = first.parse()
    free = first.dfs_sum(root)[1] - (4 * 10**7)
    print(f'To free size: {free}')
    print(find_dir(root, free))
