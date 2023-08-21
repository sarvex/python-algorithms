# Brute Force : O(n^2)
def bruteForce(nums):
  maxSum = nums[0]

  for i in range(len(nums)):
    sum = 0
    for j in range (i, len(nums)):
      sum += nums[j]
      maxSum = max(maxSum, sum)
  return maxSum

# Kadane Algorithm : O(n)
def kadanes(nums):
  maxSum = nums[0];
  sum = 0;

  for n in nums:
    sum = max(sum, 0)
    sum += n
    maxSum = max(maxSum, sum)
  return maxSum;

def slidingWindow(nums):
  maxSum = nums[0]
  sum = 0
  maxLeft, maxRight = 0, 0
  left = 0

  for right in range(len(nums)):
    if sum < 0:
      sum = 0
      left = right

    sum += nums[right]

    if sum > maxSum:
      maxSum = sum
      maxLeft, maxRight = left, right

  return [maxLeft, maxRight]

def main():
  nums = [4, -1, 2, -7, 3, 4]
  print(bruteForce(nums))
  print(kadanes(nums))
  print(slidingWindow(nums))

if __name__=="__main__":
  main()
