class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
        report_split = [[] for i in range(len(report))]
        for i in range(len(report)):
            tmp = report[i].split()
            report_split[i] = report_split[i] + tmp
        
        _map = {}
        
        for i in range(len(report)):
            feedback = report_split[i]
            pCount, nCount = 0, 0
            for pf in positive_feedback:
                pCount += feedback.count(pf)
            for nf in negative_feedback:
                nCount += feedback.count(nf)
            score = 3*pCount - nCount
            _map[student_id[i]] = score
        # print(_map)
            
        _mapSort = sorted(_map, key=lambda x:(-_map[x], x))
        ans = []
        for i in range(len(_mapSort)):
            ans.append(_mapSort[i])
            if i == k:
                break
        return ans