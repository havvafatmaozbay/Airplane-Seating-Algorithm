# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:58:29 2021

@author: Havva Fatma
"""

filled_seats = 0
passenger_number = 30 # given passenger number
row = 0
temp_filledSeats= -1
seats = [[3,2], [4,3], [2,3], [3,4]]  #8desired input
length_seats = len(seats)


def initialize(seats):
    seats_array =[]
    for i in seats:
        rows = i[1]
        cols = i[0]
        add = []
        for i in range(rows):
            add.append([-1]*cols)
        seats_array.append(add)
    return seats_array
        
def printSeats(seats_array):
    size = len(str(passenger_number))
    rows = [x[1] for x in seats]
    cols = [x[0] for x in seats]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length_seats):
            row = ' '
            rowl = ' '
            if len(seats_array[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*size
                    rowl += ' '*size
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats_array[j][i]:
                    if k == -1:
                        row += ' '*size
                        rowl += '-'*size
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(size - len(str(k))))
                        rowl += '-'*size
                        row += '|'
                        rowl += '+'

            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))
     
        
def fill_aisle():
    
    global filled_seats
    row = 0
    temp_filledSeats = -1
    while filled_seats < passenger_number and filled_seats != temp_filledSeats:
        temp_filledSeats = filled_seats
        for i in range(length_seats):
            if seats[i][1] > row:
                if i == 0 and seats[i][0] > 1:
                    filled_seats += 1
                    aisle = seats[i][0] - 1
                    seats_array[i][row][aisle] = filled_seats
                    if filled_seats >= passenger_number:
                        break
                elif i == length_seats - 1 and seats[i][0] > 1:
                    filled_seats += 1
                    aisle = 0
                    seats_array[i][row][aisle] = filled_seats
                    if filled_seats >= passenger_number:
                        break
                else:
                    filled_seats += 1
                    aisle = 0
                    seats_array[i][row][aisle] = filled_seats
                    if filled_seats >= passenger_number:
                        break
                    if seats[i][0] > 1:
                        filled_seats += 1
                        aisle = seats[i][0] - 1
                        seats_array[i][row][aisle] = filled_seats
                        if filled_seats >= passenger_number:
                            break
        row += 1


def fill_windowSeats():
    row = 0
    global filled_seats
    global passenger_number
    temp_filledSeats = 0
    while filled_seats < passenger_number and filled_seats != temp_filledSeats:
        temp_filledSeats = filled_seats
        if seats[0][1] > row:
            filled_seats += 1
            window = 0
            seats_array[0][row][window] = filled_seats
            if filled_seats >= passenger_number:
                break
        if seats[length_seats -1][1] > row:
            filled_seats += 1
            window = seats[length_seats -1][0] - 1
            seats_array[length_seats -1][row][window] = filled_seats
            if filled_seats >= passenger_number:
                break
        row += 1

def fill_middleSeats():
    row = 0
    temp_filledSeats = 0
    global filled_seats
    while filled_seats < passenger_number and filled_seats != temp_filledSeats:
        temp_filledSeats = filled_seats
        for i in range(length_seats):
            if seats[i][1] > row:
                if seats[i][0] > 2:
                    for col in range(1, seats[i][0] - 1):
                        filled_seats += 1
                        seats_array[i][row][col] = filled_seats
                        if filled_seats >= passenger_number:
                            break
        row += 1

        

seats_array = initialize(seats)

fill_aisle()

fill_windowSeats()
fill_middleSeats()

printSeats(seats_array)    

