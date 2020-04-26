class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        items = list(set(o[2] for o in orders))
        tables = list(set(int(o[1]) for o in orders))
        
        tableItems = defaultdict(lambda: defaultdict(int))
        for o in orders:
            tableItems[int(o[1])][o[2]] += 1
        
        rows = [[str(t), *[str(tableItems[t][i]) for i in sorted(items)]] for t in sorted(tables)]
        
        return [['Table', *sorted(items)], *rows]
