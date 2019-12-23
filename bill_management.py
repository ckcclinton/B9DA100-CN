# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:40:08 2019

@author: clintonngan
"""
import pandas

def read_bills():
    return [[col.strip() for col in line.strip().split(',')] for line in open('bills.csv') if len(line) > 1]

def write_bills(bills):
    bill_file = open('bills.csv', 'w')
    for bill in bills:
        bill_file.write(', '.join(bill) + '\n')
        
def count_bills(bills):
    row_count = sum(1 for row in bills)
    print('Bills to date: ', row_count)
        
def display_menu():
    print('Hello, Welcome to the Bill Management company')
    print('1: View Bills\n2: Insert a Bill\n3: Reports\n4: T&Cs\n5: Exit')
    
def highest_bill(bills):
    for bill in bills:
        print(max(bill[5]))

def plot_company(bills):
    bills.groupby(bills[0]).sort_values(ascending=False)[:5].plot.bar()
    
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
            print('Top Popular Companies')
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
            write_bills(bills)
        if choice == '3':
            subprocess_choice(bills)
        if choice == '4':
            plot_company(bills)
        choice = input('Please enter an option:')
        

def main():
    bills = read_bills()
    display_menu()
    process_choice(bills)
    write_bills(bills)
    
if __name__ == '__main__':
    main()