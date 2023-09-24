
Day_1 = float(input("Enter avg temprature of 1980 : "))
Day_2 = float(input("Enter avg temprature of 1990  : "))
Day_3 = float(input("Enter avg temprature of 2000 : "))
Day_4 = float(input("Enter avg temprature of 2010 : "))
Day_5 = float(input("Enter avg temprature of 2020 : "))

import matplotlib.pyplot as plt


days = ["1980", "1990", "2000", "2010", "2020"]
temperatures = [Day_1, Day_2, Day_3, Day_4, Day_5]


plt.figure(figsize=(8, 6))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', label='Temperature')
plt.title('Avg temprature of Decade')
plt.xlabel('Decade')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

plt.show()