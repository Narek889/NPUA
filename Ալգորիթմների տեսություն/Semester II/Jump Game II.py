def jump_game_II(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        #print("i = ",i, "i+ nums[i] = ", i+nums[i], "nums[i]", nums[i], "farthest", farthest)
        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                break

    return jumps

nums = [2, 3, 1, 1, 4]
print(f'Number of jumps = {jump_game_II(nums)}')
