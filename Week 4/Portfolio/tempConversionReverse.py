def celcius_conversion(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def fharenheit_conversion(fharenheit):
    celcius = (fharenheit - 32) * 5/9
    return celcius

cel_temp = float(input("Please enter a temperature in Celsius: "))
fhar_temp = celcius_conversion(cel_temp)
print(f"{cel_temp}C converts to {fhar_temp}F")

fhar_temp = float(input("Please enter a temperature in Fahrenheit: "))
cel_temp = fharenheit_conversion(fhar_temp)
print(f"{fhar_temp}F converts to {cel_temp}C")