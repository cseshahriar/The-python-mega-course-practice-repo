def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
     
# by default python input make str
user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))

# input type test 
my_input = input("Enter some input: ")
print(type(my_input)) # return str
