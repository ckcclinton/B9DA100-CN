# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:40:08 2019

@author: clintonngan
"""
import pandas, csv

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
            reply = str(input('Do you still want to key in the transaction for another user? (y/n) ')).lower().strip()
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
    text_csv=pandas.read_csv('bills.csv')
    df=pandas.DataFrame(text_csv)
    df.groupby('provider')
    
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
        credit_bill_list = []
        debit_bill_list = []
        for row in csv_reader:
            for column, item in enumerate(row):
                if column == 5 and column[6] == 'credit':
                    converted_credit_bill = float(item)
                    credit_bill_list.append(converted_credit_bill)
                if column == 5 and column[6] == 'debit':
                    converted_debit_bill = float(item)
                    debit_bill_list.append(converted_debit_bill)
        max_credit_bill = max(credit_bill_list)
        max_debit_bill = max(debit_bill_list)
        print('Highest credit & debit bill to date is: {0}'.format(max_credit_bill).format(max_debit_bill))

def plot_company(bills):
    bills.groupby('provider').sort_values(ascending=False)[:5].plot.bar()
    
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
        if choice == '3':
            print('Bills by Date')
        if choice == '4':
            highest_bill(bills)
        if choice == '5':
            count_bills(bills)
        if choice == '6':
            print('Average Spend by Date')
        if choice == '7':
            print('Average Time b/e Bills')
        choice = input('Please enter an option:')

def process_choice(bills):
    choice = input('Please enter an option:')
    while choice != '5':
        if choice == '1':
            view_bills(bills)
        if choice == '2':
            insert_bills(bills)
        if choice == '3':
            subprocess_choice(bills)
        if choice == '4':
            plot_company(bills)
        choice = input('Please enter an option:')
        

def main():
    bills = read_bills()
    display_menu()
    process_choice(bills)
    
if __name__ == '__main__':
    main()