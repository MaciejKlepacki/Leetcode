class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        value = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        for i in range(13):
            num_of_times = num // value[i][0]
            result += value[i][1]*num_of_times
            num -= num_of_times * value[i][0]
        return result

        