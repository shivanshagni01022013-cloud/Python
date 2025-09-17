# Take the distance in kilometers from the user and convert it to meters, centimeters, and millimeters.

distance_km = int(input("Enter the distance in kilometers: "))
m = distance_km * 1000
cm = distance_km * 100000
mm = distance_km * 1000000

" Distance in meters: "
print(f"Distance in meters: {m}m")
print(f"Distance in centimeter: {cm}cm")
print(f"Distance in millimeters: {mm}mm")