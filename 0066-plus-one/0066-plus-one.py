class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        arr = []
        for i in digits:
            number += str(i)
        number = str(int(number) + 1)
        for i in number:
            arr.append(int(i))
        return arr