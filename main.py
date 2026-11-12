print("Welcome to my Sales Data Analysis Project!")
import pandas as pd

data = pd.read_csv("sales.csv")

print(data)
data["Revenue"] = data["Quantity"] * data["Price"]

print("\nSales Revenue by Product:")
print(data)

total = data["Revenue"].sum()

print("\nTotal Sales Revenue: ₹", total)
total = data["Revenue"].sum()
print("\nTotal Sales Revenue: ₹", total)
total = data["Revenue"].sum()
print("\nTotal Sales Revenue: ₹", total)
highest = data.loc[data["Revenue"].idxmax()]

print("\nHighest Revenue Product:")
print(highest)
lowest = data.loc[data["Revenue"].idxmin()]

print("\nLowest Revenue Product:")
print(lowest)
import matplotlib.pyplot as plt

plt.bar(data["Product"], data["Revenue"])

plt.xlabel("Products")
plt.ylabel("Revenue (INR)")
plt.title("Sales Revenue by Product")
plt.savefig("sales_chart.png")

plt.show()
totalquantity = data["Quantity"].sum()

print("\nTotal Products Sold:", totalquantity)
average = data["Revenue"].mean()

print("\nAverage Sales Revenue: ₹", average)
bestselling = data.loc[data["Quantity"].idxmax()]

print("\nBest-Selling Product by Quantity:")
print(bestselling)
plt.figure(figsize=(8, 5))

plt.bar(data["Product"], data["Quantity"], color="orange")

plt.xlabel("Products")
plt.ylabel("Quantity Sold")
plt.title("Quantity Sold by Product")

plt.savefig("quantity_chart.png")

plt.show()
data["RevenuePercentage"] = (data["Revenue"] / total) * 100

print("\nRevenue Percentage by Product:")
print(data[["Product", "RevenuePercentage"]].round(2))
plt.figure(figsize=(8, 8))

plt.pie(
    data["Revenue"],
    labels=data["Product"],
    autopct="%1.1f%%"
)

plt.title("Revenue Distribution by Product")

plt.savefig("revenue_pie_chart.png")

plt.show()
with open("sales_report.txt", "w", encoding="utf-8") as file:
    file.write("SALES DATA ANALYSIS REPORT\n")
    file.write("==========================\n\n")

    file.write(f"Total Revenue: INR {total}\n")
    file.write(f"Total Units Sold: {totalquantity}\n")
    file.write(f"Average Revenue: INR {average:.2f}\n")

    file.write(f"\nHighest Revenue Product: {highest['Product']}\n")
    file.write(f"Lowest Revenue Product: {lowest['Product']}\n")
    file.write(f"Best-Selling Product: {bestselling['Product']}\n")

print("\nSales report generated successfully!")