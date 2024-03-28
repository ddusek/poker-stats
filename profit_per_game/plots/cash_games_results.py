import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from decimal import Decimal

class CashGamesResults:
    def __init__(self) -> None:
        self.data: list[tuple[datetime, Decimal, str]] = []
        self.cash_games_table = ["Table Rebuy", "Table Buy In", "Leave Table"]

    def add_row(self, date, amount, _type):
        if _type in self.cash_games_table:
            self.data.append((datetime.strptime(date, "%Y/%m/%d %I:%M %p"), Decimal(amount), _type))

    def show_results(self):
        dates, amounts, _ = zip(*self.data)

        # Plotting
        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.plot(dates, amounts, marker='o', linestyle='-')  # Plot the data

        # Formatting the x-axis to show the date and time properly
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d %I:%M %p'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        plt.gcf().autofmt_xdate()  # Rotation
        plt.xlabel('Date/Time')
        plt.ylabel('Balance')
        plt.title('Balance Over Time')
        plt.tight_layout()  # Adjusts subplot params so that the subplot(s) fits in to the figure area

        plt.show()
