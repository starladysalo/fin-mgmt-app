def main():

    moves_lst = list()

    bool_menu = True
    
    while bool_menu == True:
        print(''' Welcome, Please choose an option:
            1. Add a movement
            2. See all movements
            3. See total spending
            4. Show spending by category
            5. Exit
            ''')
        
        usr_option = input()
        option = int(usr_option)

        if option == 1:

            new_move = dict()
            move_desc = input("Description: ")
            move_amt = input("Ammount: ")
            move_cat = input("Category: ")
            move_date = input("Date: ")

            new_move["desc"] = move_desc
            new_move["ammount"] = float(move_amt)
            new_move["category"] = move_cat
            new_move["date"] = move_date

            moves_lst.append(new_move)

        elif option == 2:
            all_moves = enumerate(moves_lst, start=1)
            for index, move in all_moves:
                print(index, move)

        elif option == 3:
            counter = 0.0
            for item in moves_lst:
                counter += item["ammount"]
            print("Total: ", counter)

        elif option == 4:

            categories = dict()
            for item in moves_lst:
                if item["category"] not in categories:
                    categories[item["category"]] = item["ammount"]

                else:
                    categories[item["category"]] += item["ammount"]

            print(categories)
        
        elif option == 5:
            bool_menu = False



    return None

main()

