class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target==0 and numbers.count(0)==2:
            return [numbers.pop(0)+1,numbers.index(0)+2]
        if 0 in numbers and target in numbers:
            return sorted([numbers.index(0)+1,numbers.index(target)+1])
        for i in numbers:
            if target-i in numbers:
                if target-i==i and numbers.count(target-i)>=2:
                    return [numbers.index(i)+1,numbers.index(i)+2]
                else:
                    return [numbers.index(i)+1,numbers.index(target-i)+1]
