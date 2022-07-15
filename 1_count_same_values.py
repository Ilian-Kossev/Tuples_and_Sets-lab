input_data = input().split()
float_input_data = [float(x) for x in input_data]
unique_numbers_list = []
repetition_list = []
for number in float_input_data:
    if number not in unique_numbers_list:
        unique_numbers_list.append(number)
        count_number = float_input_data.count(number)
        repetition_list.append(count_number)
final_dict = dict(zip(unique_numbers_list, repetition_list))
for key, value in final_dict.items():
    print(f'{key:.1f} - {value} times')






