def calcPay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else :
        return hours * rate

hours = float(raw_input("How many hours?"))
rate = float(raw_input("Hourly rate?"))


print calcPay(hours, rate)