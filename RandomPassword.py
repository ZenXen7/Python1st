import random
import array


MAX_LEN = 12


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowcase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']


combinedlist = digits + uppercase_characters + lowcase_characters + symbols


rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase_characters)
rand_lower = random.choice(lowcase_characters)
rand_symbol = random.choice(symbols)


temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(combinedlist)

	
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)


password = "\t"
for x in temp_pass_list:
		password = password + x
		
print('\n\n\n\n')
print('Your Generated Password is: \n')
print(password)
print('\n\n\n\n')
