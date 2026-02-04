import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("C:/Users/ADMIN/Downloads/company_sales_data.csv")

months = data['month_number']
total_profit = data['total_profit']
bathing_soap = data['bathingsoap']
facewash = data['facewash']

# -----------------------------
# Exercise 1: Line Plot
# -----------------------------

plt.figure(figsize=(8,5))
plt.plot(months, total_profit)
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit Per Month")
plt.show()

# -----------------------------
# Exercise 2: Subplots
# -----------------------------

plt.figure(figsize=(8,6))

# Bathing soap subplot
plt.subplot(2,1,1)
plt.plot(months, bathing_soap)
plt.title("Bathing Soap Sales")
plt.ylabel("Sales")

# Facewash subplot
plt.subplot(2,1,2)
plt.plot(months, facewash)
plt.title("Facewash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
