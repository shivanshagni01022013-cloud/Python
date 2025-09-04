celsius = int(input("Enter the temperature in Celsius: "))
fahrenheit = (9/5 * celsius) + 32
kelvin = celsius + 273

print("Original temperature -> " + str(celsius) + "°C")
print("Temperature in Fahrenheit -> " + str(round(fahrenheit, 2)) + "°F")
print("Temperature in Kelvin -> " + str(kelvin) + "K")


