def pay(time, wage):
    if time > 60:
        return 2 * time * wage  
    elif time > 40:
        return 1.5 * time * wage  
    else:
        return time * wage  
    
time = int(input("Enter the hours worked in last week: "))
wage = float(input("Enter wage per hour: "))

print("Your week's pay is:", pay(time, wage))
