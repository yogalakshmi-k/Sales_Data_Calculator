
# Veda Technology - AI & ML Internship
# Task 4: Sales Data Calculator

sales = [1200, 2500, 1800, 3200, 1500, 2800, 2100]

total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)

print("SALES DATA ANALYSIS")
print("-------------------")
print("Sales Values:", sales)
print("Number of Sales:", len(sales))
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
