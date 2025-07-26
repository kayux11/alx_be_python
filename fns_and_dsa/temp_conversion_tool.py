# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        # Prompt for temperature value
        temperature_input = input("Enter the temperature to convert: ").strip()
        
        # Try to convert input to float
        temperature = float(temperature_input)

        # Prompt for unit (C or F)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        # Specific message for numeric input errors
        if "could not convert" in str(e) or "invalid literal" in str(e):
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        else:
            raise

if __name__ == "__main__":
    try:
        main()
    except ValueError as err:
        print(err)
