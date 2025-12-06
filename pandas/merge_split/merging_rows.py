import pandas as pd
import json

with open("merge_split\data.json") as f:
    data = json.load(f)

customers = pd.DataFrame(data["customers"])
orders = pd.DataFrame(data["orders"])
products = pd.DataFrame(data["products"])
print("-------------------------------------")
print(customers)

print("-------------------------------------")
print(orders)
print("-------------------------------------")
print(products)

customer_orders = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)

order_products = pd.merge(
    orders,
    products,
    on="product_id",
    how="inner"
)

full_data = customers.merge(orders, on="customer_id") \
                     .merge(products, on="product_id")

cross_customer_orders = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="cross"
)


print("-------------------------------------")
print(customer_orders)

print("-------------------------------------")
print(order_products)
print("-------------------------------------")
print(full_data)
print(cross_customer_orders)