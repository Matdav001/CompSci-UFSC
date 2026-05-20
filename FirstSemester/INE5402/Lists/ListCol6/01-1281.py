
n = int(input())

for _ in range(n):
    # Read the number of products available
    m = int(input())
    prices = dict()
    
    # Build the price dictionary
    for _ in range(m):
        line = input().split()
        prices[line[0]] = float(line[1])
        
    # Read the number of items to be bought
    p = int(input())
    total_spent = 0.0
    
    # Calculate the total cost
    for _ in range(p):
        line = input().split()
        product_name = line[0]
        quantity = int(line[1])
        
        
        total_spent += prices[product_name] * quantity
    
    # Output the formatted result
    print(f"R$ {total_spent:.2f}")

