def main():

    moves_lst = list()

    bool_menu = True
    
    while bool_menu == True:

        func_menu()
        
        usr_option = input()
        option = int(usr_option)

        if option == 1:

            add_move(moves_lst)

        elif option == 2:

            show_moves(moves_lst)

        elif option == 3:

            print(sum_moves(moves_lst))
            

        elif option == 4:

            print(categorize_moves(moves_lst))
        
        elif option == 5:
            bool_menu = False

        elif option > 5 and option <= 0:
            print("Please select a valid option")

        else:
            print("Please select a valid option")




    return None

def func_menu():
        print(''' Welcome, Please choose an option:
        1. Add a movement
        2. See all movements
        3. See total spending
        4. Show spending by category
        5. Exit
        ''')

        return None

def add_move(lst):

    new_move = dict()
    move_desc = check_desc()
    move_amt = check_amt()
    move_cat = check_cat()
    move_date = input("Date: ")

    new_move["desc"] = move_desc
    new_move["amount"] = float(move_amt)
    new_move["category"] = move_cat
    new_move["date"] = move_date

    lst.append(new_move)

    return lst
    
def show_moves(lst):

    all_moves = enumerate(lst, start=1)
    for index, move in all_moves:
        print(index, move)

    return None


def sum_moves(lst):

    counter = 0.0

    for item in lst:
        counter += item["amount"]

    return counter

def categorize_moves(lst):

    categories = dict()

    for item in lst:
        if item["category"] not in categories:
            categories[item["category"]] = item["amount"]

        else:
            categories[item["category"]] += item["amount"]

    return categories

def check_desc():
    
    check = True

    while check == True:
        desc = input("Description: ")
        empty_check = desc.isspace()
        if not(desc) or empty_check:
            print("You can't add a move without a description, please try again")
        else:
            check = False

    return desc

def check_amt():

    check = True

    while check == True:
        amt = input("Amount: ")
        amt = float(amt)

        if amt < 0:
            print("You can't add an ammount lower than zero, please try again")
        else:
            check = False

    return amt

        

def check_cat():

    check = True

    while check == True:
        cat = input("Category: ")
        empty_check = cat.isspace()
        if not(cat) or empty_check:
            print("You can't add a move without a category, please try again")
        else:
            check = False

    return cat

main()

