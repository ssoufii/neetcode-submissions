class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        stack = []

        for i, n in enumerate(temperatures):  #key, value

            while stack and n > temperatures[stack[-1]]:
                old_high = stack.pop()
                result[old_high] = i - old_high

            stack.append(i)

        return result



        