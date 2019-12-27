# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:40:08 2019

@author: clintonngan
"""
from datetime import datetime, timedelta
import pandas, csv, matplotlib.pyplot as plt

def read_bills():
    return [[col.strip() for col in line.strip().split(',')] for line in open('bills.csv') if len(line) > 1]

def insert_bills(bills):
    with open('bills.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL) 
        while (1):
            provider = input('Please enter the name of the provider: ')
            customer = input('Please enter the name of the customer: ')
            year = input('Please enter the year of transaction: ')
            month = input('Please enter the month of transaction: ')
            day = input('Please enter the day of transaction: ')
            amount = float(input('Please enter the bill amount: '))
            card_type = input('Please enter the card Type (debit or credit only!): ').strip().lower()
            csv_writer.writerow([provider, customer, year, month, day, amount, card_type])
            reply = str(input('Do you still want to key in the transaction for another bill? (y/n) ')).lower().strip()
            if reply[0] == 'n':
                break
            elif reply[0] == 'y':
                continue

def count_bills(bills):
    count = 0
    for item in bills:
        count = count + 1
    print('Bills to Date: ',count)
    
def count_pie(bills):
    bills = pandas.read_csv('bills.csv')
    bills['type'].value_counts().sort_values(ascending=True).plot.pie(title='# of Bills by payment type')
    plt.show()
    
def count_pie_year(bills):
    bills = pandas.read_csv('bills.csv')
    bills['year'].value_counts().sort_values(ascending=True).plot.pie(title='# of Bills by year')
    plt.show()
        
def display_menu():
    print('Hello, Welcome to the Bill Management company')
    print('1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit')

def summary(bills):
    fields = ['year', 'amount', 'type']
    df = pandas.read_csv('bills.csv', skipinitialspace=True, usecols=fields)
    print(df.groupby(['year','type']).sum())

def avgtime_bill(bills):
    df = pandas.read_csv('bills.csv')
    df['transaction_date'] = df.year.astype(str) + '/' +  df.month.astype(str) + '/' + df.day.astype(str)
    df['transaction_date'] = pandas.to_datetime(df['transaction_date'])
    df = df.sort_values(by=['transaction_date'])
    second_time = []
    
    for index, row in df.iterrows():
        second_time.append(row['transaction_date'])
        
    second_time.pop(0)
    df = df[:-1]
    df['second_time'] = second_time
    df['time_delta'] = df['second_time'] - df['transaction_date']
    df['time_delta'] = df['time_delta'].dt.days.astype('int16')
    avg_time_delta = df['time_delta'].sum() / len(df)
    print('Average days difference between bills: {:.2f} days'.format(avg_time_delta))

def most_popular_company(bills):
    with open('bills.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        company_list=[]
        for row in csv_reader:
            for column, item in enumerate(row):
                if column == 0:
                    company_list.append(item)
        max_company = max(company_list,key=company_list.count)
        print('Most popular company is: ', max_company)

def highest_bill(bills):
    with open('bills.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        bill_list = []
        card_type_list = []
        for row in csv_reader:
            for column, item in enumerate(row):
                if column == 5:
                    converted_bill = float(item)
                    bill_list.append(converted_bill)
                if column == 6:
                    card_type_list.append(item.strip())
        card_bill_tuple = list(zip(card_type_list, bill_list))
        credit_bill_list = []
        debit_bill_list = []
        for key, value in card_bill_tuple:
            if key == 'credit':
                credit_bill_list.append(value)
            elif key == 'debit':
                debit_bill_list.append(value)
        print('Highest credit bill: {}'.format(max(credit_bill_list)))
        print('Highest debit bill: {}'.format(max(debit_bill_list)))

def plot_company(bills):
    bills = pandas.read_csv('bills.csv')
    bills['provider'].value_counts().sort_values(ascending=True).plot.barh(title='# of bills by company')
    plt.show()
    
def plot_billdate(bills):
    bills = pandas.read_csv('bills.csv')
    bills['year'].value_counts().sort_index().plot.bar(title='# of bills by year')
    plt.show()
    bills.plot.bar(x='month', y='amount', title='Scatter amount vs month')
    plt.show()
    
def plot_avgspend_year(bills):
    bills = pandas.read_csv('bills.csv')
    show_whole_chart = str(input('Do you want the entire chart with all years? (y/n): ').lower().strip())
    if show_whole_chart[0] == 'y':
        bills.groupby("year").amount.mean().sort_index(ascending=True).plot.bar(title='Average spend by year')
        plt.show()
    elif show_whole_chart[0] == 'n':
        year_input = int(input('Please enter the year: '))
        bills = bills.loc[bills['year'] == year_input]
        bills.groupby("year").amount.mean().sort_index(ascending=True).plot.bar(title='Average spend by year')
        plt.show()
        
def plot_avgspend_month(bills):
    bills = pandas.read_csv('bills.csv')
    show_whole_chart = str(input('Do you want the MONTHLY chart for a particular year? (y/n): ').lower().strip())
    if show_whole_chart[0] == 'n':
        bills.groupby("month").amount.mean().sort_index(ascending=True).plot.bar(title='Average spend by month')
        plt.show()
    elif show_whole_chart[0] == 'y':
        year_input = int(input('Please enter the year: '))
        bills = bills.loc[bills['year'] == year_input]
        bills.groupby("month").amount.mean().sort_index(ascending=True).plot.bar(title='Average spend by month for year {}'.format(year_input))
        plt.show()
    
def display_submenu():
    print('1: Summary\n2: Top Popular Companies\n3: Bills by Date\n4: Highest Amount\n5: Total Bills\n6: Average Spend by Date\n7: Average Time b/e Bills\n8: Exit')
    
def view_bills(bills):
    for bill in bills:
        print(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6])

def subprocess_choice(bills):
    display_submenu()
    choice = input('Please enter an option:')
    while choice != '8':
        if choice == '1':
            summary(bills)
        if choice == '2':
            most_popular_company(bills)
            plot_company(bills)
        if choice == '3':
            plot_billdate(bills)
        if choice == '4':
            highest_bill(bills)
        if choice == '5':
            count_pie(bills)
            count_bills(bills)
        if choice == '6':
            plot_avgspend_year(bills)
            plot_avgspend_month(bills)
        if choice == '7':
            avgtime_bill(bills)
        choice = input('Please enter an option:')
    if choice == '8':
        process_choice(bills)

def process_choice(bills):
    display_menu()
    choice = input('Please enter an option:')
    while choice != '5':
        if choice == '1':
            view_bills(bills)
        if choice == '2':
            insert_bills(bills)
        if choice == '3':
            subprocess_choice(bills)
        if choice == '4':
            avgtime_bill(bills)
        choice = input('Please enter an option:')
        

def main():
    bills = read_bills()
    process_choice(bills)
    
if __name__ == '__main__':
    main()