class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        twenty_dollar = 0
        ten_dollar = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five_dollar += 1
            elif bills[i] == 10 and five_dollar:
                five_dollar -= 1
                ten_dollar += 1
            elif ten_dollar and five_dollar:
                ten_dollar -= 1
                five_dollar -= 1
                twenty_dollar += 1
            elif five_dollar >= 3:
                five_dollar -= 3
                twenty_dollar += 1
            else:
                return False
        return True