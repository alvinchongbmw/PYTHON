
def computepay(h,r):
    if (h > 40):
        pay = h * r
        extrapay = (h - 40) * r / 2
        pay = pay + extrapay
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours:")
try:
    fhrs = float(hrs)
except:
    fhrs = -1.0
rate = input("Enter Rage:")
try:
    frate = float(rate)
except:
    frate = -1.0
p = computepay(fhrs, frate)
print("Pay:", p)
