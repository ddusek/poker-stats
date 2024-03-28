import argparse
import csv
import matplotlib
from plots.balance_changes import BalanceChanges
from plots.cash_games_results import CashGamesResults


parser = argparse.ArgumentParser(description="Read and process a CSV file.")
parser.add_argument("--file", type=str, help="Path to the CSV file", required=True)

args = parser.parse_args()

csv_file_path = args.file

balance_changes = BalanceChanges()
cash_games_results = CashGamesResults()

with open(csv_file_path, mode="r", encoding="utf-8") as file:
    # Skip the first two lines as its just info about file
    next(file)
    next(file)
    next(file)

    csv_reader = csv.reader(file, delimiter=",")

    for row in csv_reader:
        date = row[0]  # Date and time
        action = row[1]  # Buy-in, leave table, register tournament etc
        table = row[2]  # Name of table
        game = row[3]  # Poker game type and buy in value
        input = row[4]  # Input money data only
        currency = row[5]
        amount = row[6]  # Either buy-in or payout amount
        starcoins = row[7]
        t_money = row[8]
        w_money = row[9]
        balance = row[10]  # Current balance on pokerstars account
        starcoins_after_transaction = row[11]
        t_money = row[12]
        w_money = row[13]

        balance_changes.add_row(date=date, balance=balance)
        cash_games_results.add_row(date=date, amount=amount, _type=action)

    balance_changes.show_balance_changes()
    cash_games_results.show_results()
