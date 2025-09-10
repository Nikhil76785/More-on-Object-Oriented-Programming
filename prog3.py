class PairsElement:
    
    def two_sum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return lookup[complement], i
            lookup[num] = i
        return None

try:
    value = int(input("Enter the target number: "))
    nums = (10, 20, 30, 40, 50, 60, 70)

    res = PairsElement().two_sum(nums, value)
    if res:
        print(f"Index1 = {res[0]}, Index2 = {res[1]}")
    else:
        print("No pair found thet adds up to the given sum.")
    
except ValueError:
    print("Please enter a valid integer.")