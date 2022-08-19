nums = [int(line.strip()) for line in open("in1")]
print(sum(b > a for a, b in zip(nums, nums[1:])))
