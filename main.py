# # # У списку цілих, заповненому випадковими числами обчислити:
# # # ■ Суму негативних чисел;
# # # ■ Суму парних чисел;
# # # ■ Суму непарних чисел;
# # # ■ Добуток елементів з кратними індексами 3;
# # # ■ Добуток елементів між мінімальним та максимальним елементом;
# # # ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
# #
# # import random
# #
# # numbers_list = []
# # for _ in range(10):
# #     numbers_list.append(random.randint(-10, 10))
# #
# # print(numbers_list)
# #
# # sum_negative_numbers, sum_even_numbers, sum_odd_numbers = 0, 0, 0
# # product_multiples_index_3 = 1
# # min_element, max_element = min(numbers_list), max(numbers_list)
# # index_min_element, max_index_element = numbers_list.index(min_element), numbers_list.index(max_element)
# # product_min_max = 1
# # first_positive_num_index, last_positive_num_index = 0, 0
# # is_positive_exists = False
# # numbers_range_sum = 0
# # try:
# #     for i in range(len(numbers_list)):
# #         if numbers_list[i] < 0:
# #             sum_negative_numbers += numbers_list[i]
# #
# #         if numbers_list[i] % 2 == 0:
# #             sum_even_numbers += numbers_list[i]
# #
# #         if numbers_list[i] % 2 == 1:
# #             sum_odd_numbers += numbers_list[i]
# #
# #         if i % 3 == 0:
# #             product_multiples_index_3 *= numbers_list[i]
# #
# #     if numbers_list.index(min_element) > numbers_list.index(max_element):
# #         numbers_list[index_min_element] = max_element
# #         numbers_list[max_index_element] = min_element
# #
# #     for j in range(numbers_list.index(min_element), numbers_list.index(max_element) + 1):
# #         # В завданні не зазначено включно з min-max чи ні
# #         product_min_max *= numbers_list[j]
# #
# #     for number in numbers_list:
# #         if number > 0:
# #             is_positive_exists = True
# #
# #     if is_positive_exists:
# #         for i in range(len(numbers_list)):
# #             if numbers_list[i] > 0:
# #                 first_positive_num_index = i
# #                 break
# #
# #         for i in range(len(numbers_list) - 1, -1, -1):
# #             if numbers_list[i] > 0:
# #                 last_positive_num_index = i
# #                 break
# #
# #         if (first_positive_num_index == last_positive_num_index or
# #                 abs(first_positive_num_index - last_positive_num_index) == 1):
# #             print("No numbers in this range!")
# #         else:
# #             if first_positive_num_index > last_positive_num_index:
# #                 first_positive_num_index, last_positive_num_index = last_positive_num_index, first_positive_num_index
# #
# #             for i in range(first_positive_num_index + 1, last_positive_num_index):
# #                 numbers_range_sum += numbers_list[i]
# #
# #             print(f"Sum: {numbers_range_sum}")
# #     else:
# #         print("No positive numbers in this range!")
# #
# # except Exception as Error:
# #     print(f'ExceptionError: {Error}')
# #
# # print(f"Sum negative numbers: {sum_negative_numbers}")
# # print(f"Sum even numbers: {sum_even_numbers}")
# # print(f"Sum odd numbers: {sum_odd_numbers}")
# # print(f"Product multiples index 3: {product_multiples_index_3}")
# # print(f"Product min and max: {product_min_max}")
# # print(f"Sum between the first and last element: {numbers_range_sum}")
#
#
# # Завдання 2
# # Є список цілих, заповнений випадковими числами.
# # На підставі даних цього масиву потрібно:
# # ■ Створити список цілих, що містить лише парні числа з першого списку;
# # ■ Створити список цілих, що містить лише непарні числа з першого списку;
# # ■ Створити список цілих, що містить лише негативні числа з першого списку;
# # ■ Створити список цілих, що містить лише позитивні числа з першого списку.
#
# import random
#
# numbers_list = []
#
# for _ in range(10):
#     numbers_list.append(random.randint(-10, 10))
#
# print(numbers_list)
#
# couples_list = []
# not_even_list = []
# negative_list = []
# positive_list = []
#
# try:
#     for i in range(len(numbers_list)):
#         if numbers_list[i] % 2 == 0:
#             couples_list.append(numbers_list[i])
#         if numbers_list[i] % 2 == 1:
#             not_even_list.append(numbers_list[i])
#         if numbers_list[i] < 0:
#             negative_list.append(numbers_list[i])
#         if numbers_list[i] >= 0 and numbers_list[i]:
#             positive_list.append(numbers_list[i])
# except Exception as Error:
#     print(f"ExceptionError: {Error}")
#
# print(couples_list)
# print(not_even_list)
# print(negative_list)
# print(positive_list)