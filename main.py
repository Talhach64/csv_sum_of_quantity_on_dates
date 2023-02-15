import csv
from dateutil import parser
import datetime

data = []
with open("test1.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)
f.close


def get_sum_of_quantity_pastDays(pastDays, current_date):
    sum_of_quantity = 0
    for row in data:
        try:
            purchase_date = parser.parse(row['Date of purchase'])
            if pastDays <= purchase_date <= current_date:
                sum_of_quantity += int(row['Quantity'])
        except Exception as e:
            print(f"Error parsing date: {row['Date of purchase']}")
    return sum_of_quantity


def get_sum_of_quantity_specificDate(specific_date):
    sum_of_quantity = 0
    for row in data:
        try:
            purchase_date = parser.parse(row['Date of purchase'])
            if purchase_date.strftime('%d-%b-%y') == specific_date:
                sum_of_quantity += int(row['Quantity'])
        except Exception as e:
            print(f"Error parsing date: {row['Date of purchase']}")
    return sum_of_quantity


user_input = input(
    "Choose '1' for number of days back from current date you want to search for OR '2' for specific date : ")
if (user_input == '1'):
    days = int(input("Enter days: "))
    pastDays = datetime.datetime.now() - datetime.timedelta(days=days)
    sum_of_quantity = get_sum_of_quantity_pastDays(
        pastDays, datetime.datetime.now())
    print(
        f"The sum of quantity for the past {days} days is: {sum_of_quantity}")

elif (user_input == '2'):
    specific_date = input(
        "Enter the specific date: ")
    try:
        specific_date = parser.parse(specific_date).strftime('%d-%b-%y')
        sum_of_quantity = get_sum_of_quantity_specificDate(specific_date)
        print(
            f"The sum of quantity for the date {specific_date} is: {sum_of_quantity}")

    except Exception as e:
        print("Error parsing input date")
    exit()

else:
    print("Invalid Input")
