#!/usr/local/bin/python3
import sys

IHA3H07Asigmax = input("Width at IHA3H07A in mm: ")
IHA3H07Bsigmax = input("Width at IHA3H07B in mm: ")

try:
    IHA3H07Asigmax = float(IHA3H07Asigmax)
    IHA3H07Bsigmax = float(IHA3H07Bsigmax)
except ValueError:
    raise("Input widths should be numbers")

# Calculate difference for slope
deltaSigmax = (IHA3H07Bsigmax-IHA3H07Asigmax)

# In meters
distanceFromAtoTarget = 2.9521
distanceFromBtoTarget = 1.5468
distanceBetweenHarps = distanceFromAtoTarget - distanceFromBtoTarget

# Project to target
targetProjectedFromA = IHA3H07Asigmax + distanceFromAtoTarget * (deltaSigmax/distanceBetweenHarps)
targetProjectedFromB = IHA3H07Bsigmax + distanceFromBtoTarget * (deltaSigmax/distanceBetweenHarps)

# Determine appropriate rasterDiameter size
goodWidth = True
widthInMicrons = int(targetProjectedFromA*1e3)
if widthInMicrons > 500:
    goodWidth = False
    rasterDiameter = -1
if widthInMicrons in range(400,500):
    rasterDiameter = 4.0
if widthInMicrons in range(300,400):
    rasterDiameter = 4.5
if widthInMicrons < 300:
    rasterDiameter = 5.0
    
# Display results
print("")
print("Beam width projected to target (both harps should match)")
print("From IHA3H07A: %.4f" % targetProjectedFromA)
print("From IHA3H07B: %.4f" % targetProjectedFromB)
print("")
print("Raster insructions: ")
if goodWidth:
    print("Request a raster diameter of %0.2f mm" % rasterDiameter)
else:
    print("Request a smaller width from MCC.")
