nums = [int(line) for line in open("in1")]
print(tuple(zip(nums, nums[3:])))
print(sum(b > a for a, b in zip(nums, nums[3:])))
