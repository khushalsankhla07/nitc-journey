print("Bill Split Calculator")
bill_amount = float(input())
tip_percentage = float(input())
tip_amount = (tip_percentage/100) * bill_amount
total_amount = tip_amount + bill_amount
print(f"{total_amount}")
people = int(input())
amount_per_person = total_amount/people
print(f"{amount_per_person}")