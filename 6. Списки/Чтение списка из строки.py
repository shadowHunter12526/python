# Ввод: 45 8 322
nums = list(map(int, input().split()))
print(nums) # [45, 8, 322]

# 1. input() -> "45 8 322"
# 2. input().split() -> "45", "8", "322"
# 3. map(int, input().split()) -> 45, 8, 322
# 4. list(map(int, input().split())) -> ["45", "8", "322"]
