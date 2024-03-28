import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from decimal import Decimal

class BalanceChanges:
    def __init__(self) -> None:
        self.data: list[tuple[datetime, Decimal]] = []

    def add_row(self, date, balance):
        self.data.append((datetime.strptime(date, "%Y/%m/%d %I:%M %p"), Decimal(balance)))

    def show_balance_changes(self):
        dates, balances = zip(*self.data)

        # Plotting
        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.plot(dates, balances, marker='o', linestyle='-')  # Plot the data

        # Formatting the x-axis to show the date and time properly
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d %I:%M %p'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        plt.gcf().autofmt_xdate()  # Rotation
        plt.xlabel('Date/Time')
        plt.ylabel('Balance')
        plt.title('Balance Over Time')
        plt.tight_layout()  # Adjusts subplot params so that the subplot(s) fits in to the figure area

        plt.show()
