def isAdmissibleOverpayment(prices, notes, x):
    n = len(prices)
    total = 0
    for i in range(n):
        if notes[i] == "Same as in-store":continue
        note = notes[i].split()
        if note[1] == "lower":
            diff = float(note[0][0:-1])/100
        else:
            diff = - float(note[0][0:-1])/100
        total += prices[i] - prices[i] / (1 - diff)

    if round(total, 6) <= x + 0.0:return True
    else:return False


prices = [110, 95, 70]
notes = ["10.0% higher than in-store",
 "5.0% lower than in-store",
 "Same as in-store"]
x = 5
print(isAdmissibleOverpayment(prices,notes,x))