print("the deli has run out of pastrami so don't order it")
sandwich_orders = ['tuna', 'pastrami', 'ham', 'cheese', 'pastrami', 'turkey', 'veggie', 'pastrami']
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)