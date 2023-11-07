def celcius_conversion(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def main_input():
    main_input = input("Please enter a temperature in Celsius: ")

    if main_input.endswith("C"):
        try:
            celcius = float(main_input[:-1])
            fahrenheit = celcius_conversion(celcius)
            print(f"{celcius}C is converted to {fahrenheit}F")
            
        except ValueError:
            print("Error, please enter a temperature followed by a 'C'")

    else:
        print("Error, please enter a temperature followed by a 'C'")

      
if __name__ == "__main__":
    main_input()
        
       
