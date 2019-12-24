# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:40:08 2019

@author: clintonngan
"""
import pandas, csv

def read_bills():
    return [[col.strip() for col in line.strip().split(',')] for line in open('bills.csv') if len(line) > 1]

def insert_bills(bills):
    with open('bills.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(input(["Provider","Customer","Year","Month","Day","Amount","debit/credit"]))
        
def count_bills(bills):
    row_count = sum(1 for row in bills)
    print('Bills to date: ', row_count)
        
def display_menu():
    print('Hello, Welcome to the Bill Management company')
    print('1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit')
    
def most_popular_company(bills):
    with open('bills.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        company_list=[]
        for row in csv_reader:
            for column, item in enumerate(row):
                if column == 0:
                    company_list.append(item)
        max_company = max(company_list)
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
    for bill in bills:
        bills.groupby(bill[0]).sort_values(ascending=False)[:5].plot.bar()
    
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
            print('Summary')
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
    insert_bills(bills)
    
if __name__ == '__main__':
    main()