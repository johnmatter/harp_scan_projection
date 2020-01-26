#!/usr/bin/python3
import sys

print("")
print("Please input the following information from the harp scans in mm")
print("")
IHA3H07ASigmaY = input("IHA3H07A, peak 2 sigma: ")
IHA3H07ASigmaX = input("IHA3H07A, peak 3 sigma: ")
IHA3H07BSigmaY = input("IHA3H07B, peak 2 sigma: ")
IHA3H07BSigmaX = input("IHA3H07B, peak 3 sigma: ")

try:
    IHA3H07ASigmaY = float(IHA3H07ASigmaY)
    IHA3H07ASigmaX = float(IHA3H07ASigmaX)
    IHA3H07BSigmaY = float(IHA3H07BSigmaY)
    IHA3H07BSigmaX = float(IHA3H07BSigmaX)
except ValueError:
    raise("Input widths should be numbers. Please try again :)")

# Calculate difference for slope
deltaSigmaX = (IHA3H07BSigmaX-IHA3H07ASigmaX)
deltaSigmaY = (IHA3H07BSigmaY-IHA3H07ASigmaY)

# In meters
distanceFromAtoTarget = 295.097
distanceFromBtoTarget = 154.659
distanceBetweenHarps = distanceFromAtoTarget - distanceFromBtoTarget

# Project to target
targetProjectedFromASigmaX = IHA3H07ASigmaX + distanceFromAtoTarget * (deltaSigmaX/distanceBetweenHarps)
targetProjectedFromBSigmaX = IHA3H07BSigmaX + distanceFromBtoTarget * (deltaSigmaX/distanceBetweenHarps)
targetProjectedFromASigmaY = IHA3H07ASigmaY + distanceFromAtoTarget * (deltaSigmaY/distanceBetweenHarps)
targetProjectedFromBSigmaY = IHA3H07BSigmaY + distanceFromBtoTarget * (deltaSigmaY/distanceBetweenHarps)

# Check that projections match within 1 um
xMatch = (round(targetProjectedFromASigmaX,3)-round(targetProjectedFromBSigmaX,3))
yMatch = (round(targetProjectedFromASigmaY,3)-round(targetProjectedFromBSigmaY,3))
if ((xMatch>=0.001) | (yMatch>=0.001)) :
    print("IHA3H07A and IHA3H07B projections do not match within 1 um. Please consult RC.")

# Which is wider, x or y?
# Not sure why, but x tends to be wider. Might be the orientation of the last quad before the harps.
# ternary operator
if (targetProjectedFromASigmaX > targetProjectedFromASigmaY):
    wideSigma = targetProjectedFromASigmaX
else:
    wideSigma = targetProjectedFromASigmaY

# Determine appropriate rasterDiameter size
goodWidth = True
widthInMicrons = int(wideSigma*1e3)
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
print("Beam width projected to target")
print("Y: %.4f" % targetProjectedFromASigmaY)
print("X: %.4f" % targetProjectedFromASigmaX)
print("")
if goodWidth:
    print("Based on harp-projected width at the target, recommend using a %0.2f mm raster diameter." % rasterDiameter)
    print("(Please confirm with RC!)")
else:
    print("Request a smaller width from MCC.")
print("")
