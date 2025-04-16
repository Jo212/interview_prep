nums = [4,5,6]
target = 10
final_list = []
nums_dict = {}
for curr_index, curr_numb in enumerate(nums):
    diff = target - curr_numb
    if diff in nums_dict:
        print([nums_dict[diff] , curr_index]) #return here
    nums_dict[curr_numb] = curr_index


