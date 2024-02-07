import re

phone_numbers = [
 "(123) 456-7890",
 "1234567890",
 "123.456.7890",
 "+1 123 456-7890"
]

new_numbers = []

for number in phone_numbers:
    digits  = re.findall(r'\d', number)

    are_code = ''.join(digits[-10:-7])
    first_3 = ''.join(digits[-7:-4])
    last_4 = ''.join(digits[-4:])

    new_number = f'({are_code}) {first_3}-{last_4}'
    new_numbers.append(new_number)

print(new_numbers)