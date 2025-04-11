hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per hour:")
r = float(rate)

if h > 40:
    gross = (r*1.5) * (h-40) + 40*r

if h <= 40:
    gross = h * r

print(gross)
