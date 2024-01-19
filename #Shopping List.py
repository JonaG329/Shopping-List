#Jonathan and Dorian
#Shopping List
#1/10/24

#Functions
def intro(user, game):
    print("Hello " + user + " you are playing the game"+ game + " have a good time!")
#Function 2 (Outro)
def outro(user, game):
    print("Thank you "+ user + " for playing the game " + game + ", goodbye")
#Thank user fopr playing game using a string

intro("Jonathan and Dorian", "Shopping List")


shoppinglist = ["Milk", "Rice", "Chicken", "Apples", "Olive oil", "Bread", "Cheetos"]

def display_list():
    #Display the current shopping list
    print("Your current shopping list is", shoppinglist)


while True:
    option = int(input("What do you want to do? \nAdd a task to the to-do list  = 1  \nView the current to-do list = 2 \nMark a task as completed  = 3 \nRemove a task from the to-do list  = 4 \nExit the program = 5 \nRemoves all tasks from the list = 6 \n Sort the list alphabetically = 7 \nCount the # of Items on the list = 8 \nAction choice: "))
    if (option==1) : #adds an item to the list
        todo = input("What item would you like to add?")
        shoppinglist.append(todo)
    if (option == 2): #print the current list
        display_list()
    if (option== 3): #marks an item as done using the letter X
        ans = input("Select an item from the list to mark as done: ")
        print(ans)
        i = shoppinglist.index(ans)
        print(i)
        shoppinglist[i]=ans + " X"
        print(shoppinglist)
    if(option==4) : #removes an item from the list
        removet = input("Which item would you like to remove?")
        shoppinglist.remove(removet)
    if(option==5) : #closes the program
        print("Goodbye!")
        outro("Jonathan and Dorian", "Shopping List")
        break
    if(option==6):
        shoppinglist.clear()
    if(option==7):
        shoppinglist.sort()
    if(option==8):
        x = len(shoppinglist)
        print(x)
        

        