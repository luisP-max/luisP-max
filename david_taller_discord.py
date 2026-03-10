from collections import Counter

def register_sales():
    """
    Function to register multiple sales until the user decides to stop.
    Returns a list of sales, each as a dictionary.
    """
    sales = []
    another = 'y'
    while another.lower() == 'y':
        product = input("Enter product name: ").strip()
        
        try:
            price = float(input("Enter unit price: "))
        except ValueError:
            print("Invalid input. Defaulting price to 0.0")
            price = 0.0
        
        try:
            quantity = int(input("Enter quantity sold: "))
        except ValueError:
            print("Invalid input. Defaulting quantity to 0")
            quantity = 0
        
        sales.append({'product': product, 'price': price, 'quantity': quantity})
        print(f"Sale registered: {quantity} x {product} at ${price:.2f} each.")
        
        another = input("Do you want to register another sale? (y/n): ")
    return sales

def calculate_totals(sales):
    """
    Function to calculate total quantities per product and total revenue.
    Uses Counter for efficient quantity summation.
    Returns quantities (Counter) and total_revenue (float).
    """
    quantities = Counter()
    total_revenue = 0.0
    for sale in sales:
        quantities[sale['product']] += sale['quantity']
        total_revenue += sale['price'] * sale['quantity']
    return quantities, total_revenue

def generate_summary(quantities, total_revenue):
    """
    Function to generate and print the daily sales summary.
    """
    print("=== DAILY SALES SUMMARY ===")
    for product, qty in quantities.items():
        print(f"Product: {product}")
        print(f"Total quantity sold: {qty}")
    print(f"Total revenue: ${total_revenue:.2f}")

if __name__ == "__main__":
    # Main execution: register sales, calculate totals, and generate summary
    sales = register_sales()
    quantities, total_revenue = calculate_totals(sales)
    generate_summary(quantities, total_revenue)
    print("===========================")