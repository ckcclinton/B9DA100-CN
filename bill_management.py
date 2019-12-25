# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:40:08 2019

@author: clintonngan
"""
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
            amount = input('Please enter the bill amount: ')
            card_type = input('Please enter the card Type (debit or credit only!): ')
            csv_writer.writerow([provider, customer, year, month, day, amount, card_type])
            reply = str(input('Do you still want to key in the transaction for another bill? (y/n) ')).lower().strip()
            if reply[0] == 'n':
                break
            elif reply[0] == 'y':
                continue
        
def count_bills(bills):
    row_count = sum(1 for row in bills)
    print('Bills to date: ', row_count)
        
def display_menu():
    print('Hello, Welcome to the Bill Management company')
    print('1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit')

def summary(bills):
    fields = ['year', 'amount', 'type']
    df = pandas.read_csv('bills.csv', skipinitialspace=True, usecols=fields)
    print(df.groupby(['year','type']).sum())

def date_col(bills):
    df = pandas.read_csv('bills.csv', skipinitialspace=True)
    tran_date = []
    df['transaction_date'] = df.year.astype(str) +'-'+ df.month.astype(str) +'-'+ df.day.astype(str)
    df['transaction_date'] = pandas.to_datetime(df['transaction_date'])
    tran_date.append(df['transaction_date'])
    print(tran_date)

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
        bill_list = []
        card_type_list = []
        for row in csv_reader:
            for column, item in enumerate(row):
                if column == 'amount':
                    converted_bill = float(item)
                    bill_list.append(converted_bill)
                if column == 'type':
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
    bills['year'].value_counts().sort_index(ascending=True).plot.bar(title='# of bills by year')
    plt.show()
    
def plot_avgspend(bills):
    bills = pandas.read_csv('bills.csv')
    bills.groupby("year").amount.mean().sort_index(ascending=True).plot.bar(title='Average spend by year')
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
            count_bills(bills)
        if choice == '6':
            plot_avgspend(bills)
        if choice == '7':
            print('Average Time b/e Bills')
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
            date_col(bills)
        choice = input('Please enter an option:')
        

def main():
    bills = read_bills()
    process_choice(bills)
    
if __name__ == '__main__':
    main()