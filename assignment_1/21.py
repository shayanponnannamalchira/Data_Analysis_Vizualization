"""
Q21. Temperature Conversion Function
Create a function that converts Celsius temperature to Fahrenheit.
Use the function to convert a list of temperatures entered by the user.

Topics: Functions, Lists, Loops, Arithmetic operators.
"""


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def main():
    n = int(input("How many temperatures do you want to convert? "))

    celsius_temps = []
    for i in range(n):
        temp = float(input(f"Enter temperature {i + 1} in Celsius: "))
        celsius_temps.append(temp)

    fahrenheit_temps = []
    for temp in celsius_temps:
        fahrenheit_temps.append(celsius_to_fahrenheit(temp))

    print("\nCelsius\tFahrenheit")
    for c, f in zip(celsius_temps, fahrenheit_temps):
        print(f"{c}\t{f:.2f}")


if __name__ == "__main__":
    main()
