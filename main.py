calcultation_to_seconds = 24 
name_of_unit= "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calcultation_to_seconds} {name_of_unit}"

my_var = days_to_units(20)
print(my_var)

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
print(user_input)