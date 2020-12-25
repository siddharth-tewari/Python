a = input("Fahrenheit_To_Celsius{F2C} or  Celsius_To_Fahrenheit{C2F}")
if a == "F2C":
    fahrenheit=float(input("Enter the temerature in Fahrenheit"))
    celsius=(fahrenheit-32)*5/9
    print("Your Temperature in Celcius=",celsius)
if a == "C2F":
    celsius=float(input("Enter the Temperatre in Celcius"))
    fahrenheit=celsius*(9/5)+32
    print("Your Temperature in Fahrenheit=",fahrenheit)
