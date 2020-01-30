#!/bin/python3

def get_fahrenheit():
    return float(input("Podaj temperaturę w [°F]:"))

def calculate_celsius(fahrenheit):
    return 5.0/9.0*(fahrenheit - 32.0)

def show_celsius(celsius):
    print("Temperatura w [°C]:",celsius)
    

def main():
    fahrenheit = get_fahrenheit()
    celsius = calculate_celsius(fahrenheit)
    show_celsius(celsius)

if __name__=="__main__":
    main()
