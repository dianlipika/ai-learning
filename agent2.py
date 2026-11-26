bill = float(input("账单金额："))
people = int(input("几个人："))
tip = bill * 0.1
total = bill + tip
print(f"含10%小费总计：{total:.2f}，每人{total/people:.2f}")
