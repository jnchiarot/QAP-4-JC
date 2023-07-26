# Program description: This program is designed to display the
#                      difference of sales on a monthly basis.
# Written by:          Jillian Chiarot
# Date written:        July 24 - 2023

# Import libraries.
import matplotlib.pyplot as plt

# Main program.
MonthsList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
MonthlySales = []
MonthsAbbList = []

# Input.
for Month in MonthsList:

    while True:
        try:
            Sales = float(input(f"Enter the total amount of sales for {Month}: "))
            break
        except ValueError:
            print("Error - Invalid input. Please enter a valid number.")
# Procesing.
    MonthlySales.append(Sales)
    MonthsAbbList.append(Month[:3])

# Output.
plt.title("Total amount of sales each month")
plt.plot(MonthsAbbList, MonthlySales, color="green", marker="o")

plt.xlabel("Months of the year")
plt.ylabel("Total sales ($)")

plt.ylim(bottom=0)  # Sets the lower limit of the y axis to zero.

plt.grid(True)
plt.legend()

plt.show()