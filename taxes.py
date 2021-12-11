income = int(input("Write income:"))
tax_map = {
    0 : [0, 15527],
    15 : [15528, 42707],
    25 : [42708, 132406],
    28 : [132407, 1000000]
}
for taxes in tax_map.keys():
    if income in range (tax_map.get(taxes)[0], (tax_map.get(taxes)[1] + 1)):
        calculated_tax = int(income * taxes / 100)
        print(f"The tax for {income} is {taxes}%. That is {calculated_tax} dollars!")