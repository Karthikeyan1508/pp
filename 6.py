def pay(time, wage):
    if time > 60:
        return (40 * wage) + (20 * 1.5 * wage) + ((time - 60) * 2 * wage)
    elif time > 40:
        return (40 * wage) + ((time - 40) * 1.5 * wage)
    else:
        return time * wage

time = int(input("Enter the hours worked in last week: "))
wage = float(input("Enter wage per hour: "))

print("Your week's pay is:", pay(time, wage))
