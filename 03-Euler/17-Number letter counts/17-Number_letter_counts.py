one_2_nine = 36
ten_2_nineteen = 70
twenty_2_ninety = 46
hundred = 7
thousand = 8
# for each hundred number --> 1 and
one_2_ninety_nine = one_2_nine + ten_2_nineteen + 10 * (twenty_2_ninety) + 8 * (one_2_nine)
all_one_to_ninety_nines = 10 * one_2_ninety_nine
num_of_letters_hundreds = 9 * 100 * hundred
And = 3
num_of_letters_ands = 9 * 99 * And
result = 100*(one_2_nine)+num_of_letters_ands + num_of_letters_hundreds + all_one_to_ninety_nines + thousand + 3 # 3 is for one thousand
print(one_2_ninety_nine)
print(all_one_to_ninety_nines)
print(num_of_letters_hundreds)
print(num_of_letters_ands)
print(result)

