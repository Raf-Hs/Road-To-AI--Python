calcultation_to_seconds = 24 
name_of_unit= "hours"

def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print (type(condition_check))

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calcultation_to_seconds} {name_of_unit}"
    elif num_of_days == 0:
        return("The number is zero, so no conversion for you")
    else: 
        return("The number is negative, so no conversion for you")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

if user_input.isdigit():
    calculated_value = days_to_units(int(user_input))
    print(calculated_value)
else:
    print("Your input is not a number")
    