revenue = int(input('Enter revenue: '))
costs = int(input('Enter costs: '))
people = int(input('Enter number of people: '))
if revenue > costs:
     print('revenue>costs')
     clear_revenue = revenue - costs
     profitability = clear_revenue/revenue
     print('Revenue {} profit {}: {:.2f}' .format('your','is',profitability))
     clear_for_person = float(clear_revenue/people)
     print('Revenue per one people: %s'%clear_for_person)
else:
     print('Your company is unprofitable')