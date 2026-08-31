"""
Q25. GPS Coordinates
A delivery application stores the location of a delivery point as:
(13.3409, 77.1010)
Write a Python program to extract and display the latitude and longitude separately.

Topics: Tuples, Indexing, Variables.
"""

location = (13.3409, 77.1010)

latitude = location[0]
longitude = location[1]

print("Delivery Location:", location)
print("Latitude:", latitude)
print("Longitude:", longitude)
