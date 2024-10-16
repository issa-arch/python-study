# Create a new python file stringtask.py and attempt the 5 questions below:

# 1. Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class
# name = “ JOHn .“ to “john”

# 2. Slice the below string to get you the resulting sentence:
# a. sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# b. sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton
# forces”

# 3. Split the below sentence using a semicolon i.e ; And display length of the result.
# “The lazy dog; ran so fast; it hit the wall.”

# 4. first_name=" Joh.n" last_name=" Do,e" Clean up and display Full name i.e John Doe

# 5. Having the string r = '["E","W","C"]' #Manipulate it to display EWC


# >>>>>>>>>>>> QUESTION 1 <<<<<<<<<<<
name = "  JOHn  "
clean_name = name.strip().lower()
print(clean_name)

# >>>>>>>>>>>> QUESTION 2 <<<<<<<<<<<

sentence_one = "The Dog Breed is German Shepherd"
result_one = sentence_one[8:23]
print(result_one)


# >>>>>>>>>>>> QUESTION 3 <<<<<<<<<<<

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
result_two = sentence_two[15:29]
print(result_two)


# >>>>>>>>>>>> QUESTION 4 <<<<<<<<<<<

sentence = "The lazy dog; ran so fast; it hit the wall."
split_sentence = sentence.split(';')
print(split_sentence)
print(len(split_sentence))

# >>>>>>>>>>>> QUESTION 5 <<<<<<<<<<<

first_name = " Joh,n "
last_name = "  Do,e "
clean_first_name = first_name.replace(',', '').strip().capitalize()
clean_last_name = last_name.replace(',', '').strip().capitalize()
full_name = f"{clean_first_name} {clean_last_name}"
print(full_name)

# >>>>>>>>>>>> QUESTION 6 <<<<<<<<<<<

r = ["E", "W", "C"]
result = "".join(r)
print(result)
