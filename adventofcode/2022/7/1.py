from dataclasses import dataclass, field as dc_field
import fileinput
from typing import Tuple


def is_cd(s: str) -> bool:
    return s.startswith('$ cd ')


def is_ls(s: str) -> bool:
    return s.startswith('$ ls')


def is_dir(s: str) -> bool:
    return s.startswith('dir ')


def parse() -> "Node":
    node = root = Node('/')
    for l in fileinput.input():
        line = l.strip()
        if is_cd(line):
            d = line.replace('$ cd ', '')
            if d == '/':
                continue
            if d == '..':
                node = node.par
                continue
            assert d != '/', 'unsupported command found: $ cd /'
            assert d not in node.children, f'{d} already present in {node.d}'
            node.children[d] = Node(d)
            node.children[d].par = node
            node = node.children[d]
            continue
        if is_ls(line):
            continue
        if is_dir(line):
            continue

        # this is a file
        node.size += int(line.split()[0])

    return root


@dataclass
class Node:
    d: str
    size: int = 0
    par: "Node" = None
    children: dict[str, "Node"] = dc_field(default_factory=dict)


def dfs_sum(node) -> Tuple[int, int]:
    """returns (running_sum, cur_dir_size)"""
    if node is None:
        return 0, 0
    rsum, size = 0, node.size
    for c in node.children.values():
        csum, csize = dfs_sum(c)
        size += csize
        rsum += csum
    if size <= 10**5:
        rsum += size
    return rsum, size


if __name__ == "__main__":
    root = parse()
    print(dfs_sum(root)[0])
