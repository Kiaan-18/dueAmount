def calculate_change(amount_paid,total_bill):
    change=amount_paid-total_bill
    return change 
total_bill=2.50
amount_paid=4.00
change_to_return= calculate_change(amount_paid, total_bill)
print("The shopkeeper should return $",change_to_return)