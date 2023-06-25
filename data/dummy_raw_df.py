import pandas as pd
from datetime import datetime, timedelta

# Generate sample dates
order_dates = [datetime.now() - timedelta(days=x) for x in range(10, 20)]
step_dates = [[order_date - timedelta(hours=y*3) for y in range(10)] for order_date in order_dates]

# Create a list with supply chain steps
supply_chain_steps = ['Order Received', 'Materials Sourced', 'Production Started', 
                      'Production Completed', 'Quality Check', 'Dispatch from Factory', 
                      'In Transit', 'Customs Clearance', 'Received at Warehouse', 'Delivered to Customer']

# Create a list with product locations
product_locations = ['Warehouse', 'Supplier_1', 'Production_Site', 'Production_Site', 
                     'Quality_Check_Site', 'Factory_Site', 'On_Route', 'Customs', 
                     'Local_Warehouse', 'Customer_Location']

# Create a dictionary with data
data = {
    "Order_ID": [f"Ord_{i//10}" for i in range(100)],
    "Product_ID": [f"Prod_{(i//10)%3}" for i in range(100)],  # Let's assume 3 different types of furniture
    "Order_Date": [order_dates[i//10] for i in range(100)],
    "Supply_Chain_Step": supply_chain_steps*10,
    "Step_Date": [date for sublist in step_dates for date in sublist],
    "Supplier_ID": [f"Supp_{(i//10)%2}" for i in range(100)],  # Let's assume 2 different suppliers
    "Delay_Risk_Probability": [0.15 + 0.2*((i//10)%3) for i in range(100)],  # Increased delay probabilities
    "Product_Location": product_locations*10
}

# Create DataFrame
df = pd.DataFrame(data)
df.to_csv("data/raw_orders_df.csv", index=False)
