# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57

temp=56.8926
print(round(temp))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89

temp=56.8926
print(round(temp,2))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893

temp=56.8926
print(round(temp,3))

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926
# Original float
temp = 56.8926

# Convert the float to a string
temp_str = str(temp)

# Slice the string to remove the first character and concatenate '8'
# Here we're assuming you want '8' as the first character
new_str = '8' + temp_str[2:6]  # This takes '8926'

# Convert the new string back to a float
final_value = float(new_str)

print(final_value)

