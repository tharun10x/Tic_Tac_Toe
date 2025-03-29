import random as rd
import time

def comp_input(chances, data):
    print("Computer's turn..")
    chance = "0"
    #setting the range for rows and columns for the computer to decided
    inpt = rd.choice(chances)
    if inpt in chances:
        data [inpt[0]][inpt[1]] ='0' 
        chances.remove(inpt)
    elif(len(chances)==0):
        print(" over")
    time.sleep(1.5)
    display(data)
        

data = [[" "," "," " ],[" "," "," "],[" "," "," "]]
chances=[[0,0],[0,1],[0,2],
         [1,0],[1,1],[1,2],
         [2,0],[2,1],[2,2]]

def display(data):
    print("-------")
    for row in data:
        data =f"|{row[0]}|{row[1]}|{row[2]}|"
        print(data)
    print("-------")

def user_input():
    #Getting input for rows and cols
    valid = False
    time.sleep(0.5)
    print("Your turn")
    while not valid:
        row = int(input("Enter the row "))
        col = int(input("Enter the column "))
        #Checking the index range condition
        if [row,col] in chances:
            data[row][col]='X' 
            chances.remove([row,col])
            valid = True
        elif(row or col)>=3:
            print("Index out of range!!")
            print("Please enter a valid index for row or columns")
        else:
            print("That index is not avaliable")
    display(data)
       
    

display(data)
while len(chances) !=0:
    user_input()
    #now the computer must select the position for its insertion
    comp_input(chances, data)
    