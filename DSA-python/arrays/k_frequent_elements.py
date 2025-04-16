nums = [4,3,3,3,3,5,6]
target = 10
final_list = []
nums_dict = {}
greatest_value = 0
k_freq = 0
for curr_index, curr_numb in enumerate(nums):
    if curr_numb in nums_dict:
        nums_dict[curr_numb] = nums_dict[curr_numb] + 1  #return here
    else:
        nums_dict[curr_numb] = 1

for curr_val, times_present in nums_dict.items():
    if times_present > greatest_value:
        greatest_value = times_present
        k_freq = curr_val
print([k_freq, greatest_value])