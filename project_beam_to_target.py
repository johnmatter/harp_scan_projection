#!/usr/local/bin/python3
import sys

# Per Simona's entry [1] using distances compiled by Daniel Moser [2], we can
# project the beam width from each the harps to the target as follows:
#
# width_x at target (using 3H07X) = width_x(3H07X) + 1.55 * [width_x(3H07B) - width_x(3H07A)]/1.91
# width_x at target (using 3H07A) = width_x(3H07A) + 3.46 * [width_x(3H07B) - width_x(3H07A)]/1.91
#
# [1] https://logbooks.jlab.org/entry/3768482
# [2] https://logbooks.jlab.org/entry/3764458

if (len(sys.argv)!=3):
    print("Usage: projectBeamWidthToTarget.py IHA3H07Awidth IHA3H07Bwidth ")
    sys.exit(1)

# In millimeters
try:
    IHA3H07Asigmax = float(sys.argv[1])
    IHA3H07Bsigmax = float(sys.argv[2])
except ValueError:
    raise("Input widths should be a float")
    

# In meters
distanceBetweenHarps = 1.91
distanceFromBtoTarget = 1.55
distanceFromAtoTarget = 3.46

deltaSigmax = (IHA3H07Bsigmax-IHA3H07Asigmax)

targetProjectedFromA = IHA3H07Asigmax + distanceFromAtoTarget * (deltaSigmax/distanceBetweenHarps)
targetProjectedFromB = IHA3H07Bsigmax + distanceFromBtoTarget * (deltaSigmax/distanceBetweenHarps)

print("")
print("Beam width projected to target (both harps should match)")
print("from IHA3H07A: %.4f mm" % targetProjectedFromA)
print("from IHA3H07B: %.4f mm" % targetProjectedFromB)
print("")
