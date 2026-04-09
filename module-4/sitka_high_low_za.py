import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures and low tempatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
         
        low = int(row[6])
        lows.append(low)

while True:
    print("\nWeather Menu")
    print("1. View high temperatures")
    print("2. View low temperatures")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # plot highs
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "2":
        # plot lows
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "3":
        print("Thank you for using the Sitka Weather Viewer!")
        break

    else:
        print("Invalid choice. Please try again.")
