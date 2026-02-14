s, a, b = input(), '', ''
def arithmetic_operation(x, y):
   f_number, s_number = "", ""
   
   for i in range(0, len(x), 3): f_number += str(dict_of_numbers[x[i: i+3]])
   for i in range(0, len(y), 3): s_number += str(dict_of_numbers[y[i: i+3]])
   
   if '+' in s: return int(f_number) + int(s_number)
   elif '-' in s: return int(f_number) - int(s_number)
   elif '*' in s: return int(f_number) * int(s_number)

dict_of_numbers = {"ONE": 1, "TWO": 2, "THR": 3, "FOU": 4, "FIV": 5, "SIX": 6, "SEV": 7, "EIG": 8, "NIN": 9, "ZER": 0}
reverse = {value: key for key, value in dict_of_numbers.items()}

if '+' in s:
   a, b = s.split('+')
   res = arithmetic_operation(a, b)
elif '-' in s:
   a, b = s.split('-')
   res = arithmetic_operation(a, b)
elif '*' in s:
   a, b = s.split('*')
   res = arithmetic_operation(a, b)
else:
   for i in range(0, len(s), 3):
      res += str(dict_of_numbers[s[i: i+3]])

str_res = ''
for i in str(res):
   str_res += reverse[int(i)]
print(str_res)