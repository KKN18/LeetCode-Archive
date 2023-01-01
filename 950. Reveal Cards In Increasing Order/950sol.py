class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        _map = defaultdict(list)
        _map[1] = [1]
        _map[2] = [1, 2]
        _map[3] = [1, 3, 2]
        _len = len(deck)
        
        
        deck_sort = sorted(deck)
        
        def evenFunc(num):
            lst = _map[num]
            if len(lst) != 0:
                return lst
            
            ret = []
            half_num = num // 2
            halfIsEven = (half_num % 2 == 0)
            if halfIsEven:
                tmp_lst = evenFunc(half_num)
            else:
                tmp_lst = oddFunc(half_num)
            
            base = 1
            tmp_base = half_num
            tmp_idx = 0
            for i in range(num):
                if i % 2 == 0:
                    ret.append(base)
                    base += 1
                else:
                    val = tmp_lst[tmp_idx]
                    tmp_idx += 1
                    ret.append(tmp_base + val)
            return ret
                    
            
        def oddFunc(num):
            lst = _map[num]
            if len(lst) != 0:
                return lst
            
            ret = []
            half_num = num // 2 + 1
            halfIsEven = (half_num % 2 == 0)
            if halfIsEven:
                tmp_lst = evenFunc(half_num)
            else:
                tmp_lst = oddFunc(half_num)
                
            base = 1
            tmp_base = num // 2
            tmp_idx = 1
            for i in range(num):
                if i % 2 == 0:
                    ret.append(base)
                    base += 1
                else:
                    val = tmp_lst[tmp_idx]
                    tmp_idx += 1
                    ret.append(tmp_base + val)
            return ret
                    
        
        isEven = _len % 2 == 0
        if isEven:
            ret = evenFunc(_len)
        else:
            ret = oddFunc(_len)
        
        ans = []
        for i in range(_len):
            idx = ret[i] - 1
            ans.append(deck_sort[idx])
        
        return ans