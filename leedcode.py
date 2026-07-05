class solution(object):
    def twosum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    break

        return result

userinput = input("fdf:").split(",")

nums = []

for item in userinput:
    nums.append(int(item))

target=int(input("enter the number"))

solve = solution()
answer = solve.twosum(nums, target)
print("Output:", answer)
