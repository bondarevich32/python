revenue = int(input('Enter your revenue: '))
costs = int(input('Enter your costs: '))

if revenue > costs:
    profit = revenue - costs
    staff = int(input('Write the number of people in the company: '))
    print("The firm's profit per one people is: {} RUB".format(profit / staff))
elif revenue < costs:
    print('Your expenses exceed your income')
elif revenue == costs:
    print('Your expenses equal your income')