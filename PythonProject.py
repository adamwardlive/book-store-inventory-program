import matplotlib
import matplotlib.pyplot as plt
import numpy as np
book_file = []
divider = "________________________________________________________________________________"
def read_file():#define new read file function
    infile = open("bookfiledata.txt")
    for row in infile:#ensures processing of each line individually
        start = 0#points to the beginning of the file
        string_builder = []#creates a temporary list builder
        if not row.startswith('#'):#ignores comments
            for index in range(len(row)):
                if row[index] == ',' or index == len(row) -1:#defines where to read to on the row
                    string_builder.append(row[start:index])
                    start = index + 1
            book_file.append(string_builder) #build list
    infile.close()
read_file()
print(divider,"\n### Book Store Inventory Program ###\n", divider)

def menu(): #menu function the user is met with at the beginning of the program featuring all functions available
    try:
        print("### Main Menu ###\n", divider) #print the function name so user knows what menu they're in
        menu_selector = 0 #define the menu selector variable
        print("[1] Output Book Titles & Details\n[2] Output Average Price Of All Books In Stock\n[3] Output Book Genre Report\n[4] Add A New Item\n[5] Book Query\n[6] Book List\n[7] Chart\n[8] Exit")
        menu_selector = int(input("Select your option:\n")) #ensures the menu selector stays in int format
    except ValueError: #excepts a value error to prevent crashing if the user enters a non-int value
        print("Error - Try Again [Option Not Defined]\n", divider)
        menu()
    else:
        if menu_selector <= 0: #if the user enters a value below or equal to 0 the menu function is recalled because this input is invalid
            print("Error - Try Again [Option Not Defined]\n", divider)
            menu()
        if menu_selector == 1:
            print_summary()
        if menu_selector == 2:
            print_summary2()
        if menu_selector == 3:
            genre_report()
        if menu_selector == 4:
            add_item()
        if menu_selector == 5:
            book_query()
        if menu_selector == 6:
            book_list()
        if menu_selector == 7:
            chart()
        if menu_selector == 8:
            exit()
        if menu_selector >= 9:
            print("Error - Try Again [Option Not Defined]\n", divider) # this is the same as the below 0 function but applies to all intgers above and equal to 9
            menu()

def back_to_main(): #back to main function which is called after each other function is completed
    back_to_main = 0
    back_to_main = input("Return to Main Menu?\n [Y] or [N]:").lower()
    if back_to_main == ('y'):
        print(divider)
        menu()

def print_summary(): #print summary function containing the 1.	Output a list of books titles   # and their respective details, including a summary report displaying (a) total number of book titles and  # (b) total value of books in stock.
    book_count = 0 #define the count variable
    total_value = 0 #define to total stock value variable
    price_list = []
    print(divider,"\n### Books Available ###\n", divider)
    for book in book_file:
        book_count += 1 #this increases the count variable by 1 each iteration
        book_price = float(book[4]) #converts book price into a float for use in calculations
        print(book_count,book[1],book[0],book[3],book[2],book[6],"£"+(format(book_price,'.2f'))," "+book[5]+" In Stock",sep = ' |') #prints details of each book
        total_value += float(book[4]) * float(book[5]) #calculates the stock value of that book by doing price*stock
        if not float(book[5]) == 0: #ensures that books with a stock level of 0 are not included in the average calculation
            price_list.append(float(book_price))
    average_price_final = ((sum(price_list))//book_count) #creates the average price variable by division of price list by book count
    print(divider,"\n### Summary ###\nBooks In System: ", book_count,"\nTotal Stock Value: £",(format(total_value, '.2f')),"\nAverage Book Price: £",(format(average_price_final,'.2f')),"\n",divider)
    back_to_main()

def print_summary2(): #this function is a direct copy of the first function but i've just removed some of the other print options    #Outputs average price of books in stock
    book_count = 0  # define the count variable
    total_value = 0  # define to total stock value variable
    price_list = []
    for book in book_file:
        book_count += 1  # this increases the count variable by 1 each iteration
        book_price = float(book[4])  # converts book price into a float for use in calculations
        total_value += float(book[4]) * float(book[5])  # calculates the stock value of that book by doing price*stock
        if not float(book[5]) == 0:  # ensures that books with a stock level of 0 are not included in the average calculation
            price_list.append(float(book_price))
    average_price_final = ((sum(price_list)) // book_count)
    print(divider, "\n### Summary ###\nBooks In System: ", book_count, "\nTotal Stock Value: £",(format(total_value,'.2f')), "\nAverage Book Price: £", (format(average_price_final,'.2f')), "\n", divider)
    back_to_main()

def genre_counter(gR):
    genre_count = {} #defines a new dictionary
    for genre in gR: #for each genre in the list
        if genre in genre_count: #if the genre appears in the list
            genre_count[genre] = int(genre_count[genre]) + 1 #increase the value by one
        else:
            genre_count[genre] = 1
    for key, value in genre_count.items():
        print(key.title() + ' >', value,'available') #output the dictionary in the format outlining how many books are available from the genre

def genre_report(): #3.	Output a report detailing the number of books existing in each genre type.
    print("### Genre Report ###\n",divider)
    genre_type = [] #defines the genre type list
    for book in book_file: #a for loop appending the genre of every book in the book file to a new list
        genre_type.append(book[6])
    print("Books Available In The Following Genres:")
    genre_counter(genre_type) #calls the genre count function to count the no. of genres available & outputs this value
    print(divider)
    back_to_main()

def add_item():#Option to add new book item and present a summary report displaying # (a) the increase in total number of titles in stock and   # (b) the cost difference in average price of books in stock.
    type = []
    for book in book_file:
        if not book[2] in type:
            type.append(book[2])
    book_count = 0 #define the count variable
    total_value = 0 #define to total stock value variable
    price_list = []
    for book in book_file:
        book_count += 1 #this increases the count variable by 1 each iteration
        book_price = float(book[4]) #converts book price into a float for use in calculations
        total_value += float(book[4]) * float(book[5]) #calculates the stock value of that book by doing price*stock
        if not float(book[5]) == 0: #ensures that books with a stock level of 0 are not included in the average calculation
            price_list.append(float(book_price))
    old_avg_price = ((sum(price_list))//book_count) #this calculates the average price of a book before the new book value is calculated and added to the system
    new_book = [] #define the new book variable recording in a list the details input by the user
    new_title = (" "+input("Enter Book Title:\n"))
    new_author = input("Enter Book Author:\n")
    new_genre = (" "+input("Enter Book Genre:\n"))
    new_publisher = (" "+input("Enter Book Publisher:\n"))
    new_type = (" "+(input("HB or PB?\n").lower()))
    if not new_type in type:
        print("Invalid Type, Try Again")
        add_item()
    new_cost = (input("Enter Book Cost\n"))
    new_stock = (input("Enter Book Stock\n")) #gathers user input for each required data value
    new_book.append(new_author)
    new_book.append(new_title)
    new_book.append(new_type)
    new_book.append(new_publisher)
    new_book.append(new_cost)
    new_book.append(new_stock)
    new_book.append(new_genre)
    book_file.append(new_book) #appends the newly required data to the list price
    book_count = 0  # define the count variable
    total_value = 0  # define to total stock value variable
    price_list = []
    print(divider,"\n### Database Updated ###")
    for book in book_file:
        book_count += 1  # this increases the count variable by 1 each iteration
        book_price = float(book[4])  # converts book price into a float for use in calculations
        total_value += float(book[4]) * float(book[5])  # calculates the stock value of that book by doing price*stock
        if not float(book[5]) == 0:  # ensures that books with a stock level of 0 are not included in the average calculation
            price_list.append(float(book_price))
    average_price_final = ((sum(price_list)) // book_count)
    dif_in_price = (average_price_final - old_avg_price)
    print(divider,"\n### Summary ###","\n",divider,"\nBooks In System: ",book_count,"\nAverage Book Price: £", (format(average_price_final, '.2f')),"\nOld Average Book Price: £",(format(old_avg_price, '.2f')),"\nDifference In Average Price: £",(format(dif_in_price, '.2f')),"\n",divider)
    back_to_main()

def book_query(): #5.	Query if a book title is available and present option of (a) increasing stock level or  # (b) decreasing the stock level, due to a sale.  # If the stock level is decreased to zero indicate to the user that the book is currently out of stock.
    print("### Book Query ###\n", divider)
    search = input("Input Book Name:\n").lower()
    for book in book_file:
        if search in book[1].lower():
            print("Book Found!")
            new_stock = input("Enter Stock Adjustment:\n") #takes the stock adjustment from the user
            stock_adj = float(new_stock) #converts the adjustment to a float for calculations
            old_stock = float(book[5]) #converts the stock value within the book file to a float for calculating the new updated stock
            updated_stock = stock_adj + old_stock #stock adjustment figure added to the new stock will give the updated value
            updated_stock_format = format(str(updated_stock)) #converts the new value to a string to allow compatiblity with the print summary funciton
            book.insert(5,updated_stock_format) #inserts the new value into the book file where the original stock value was located
            book.remove(book[6]) #deletes the old stock value
            print("### Update Complete ###\n",divider)
            if updated_stock <= 0:
                print("### Book Out Of Stock ###\n",divider) #informs the user that if the new value of stock is lesser than or equal to 0 that the book is out of stock
            back_to_main()
    print("Book Not Found!\n", divider)
    back_to_main()

def book_list():
    print("### Book List ###\n", divider)
    list_type = 0
    book_count = 0
    try:
        list_type = int(input("Select:\n[1]: List All Books By Genre\n[2]: List All Books By Title\n"))
    except(ValueError):
        print(divider,"\nPlease Choose An Option From The List!\n",divider)
        book_list()
    if list_type == 1:
        print("### List By Genre ###\n", divider)
        book_file_genre = sorted(book_file, key=lambda book:book[6])
        for book in book_file_genre:
            book_count += 1  # this increases the count variable by 1 each iteration
            book_price = float(book[4])  # converts book price into a float for use in calculations
            print(book_count, book[6].upper(), book[1], book[0], book[3], book[2], "£" + (format(book_price, '.2f'))," " + book[5] + " In Stock\n", divider, sep=' |')  # prints details of each book
    else:
        print("### List By Title ###\n", divider)
        book_file_title = sorted(book_file, key=lambda book:book[1])
        for book in book_file_title:
            book_count += 1  # this increases the count variable by 1 each iteration
            book_price = float(book[4])  # converts book price into a float for use in calculations
            print(book_count,  book[1], book[0], book[3], book[2],book[6], "£" + (format(book_price, '.2f')), " " + book[5] + " In Stock\n", divider, sep=' |')  # prints details of each book
    back_to_main()

def genre_count(gR):
    genre_count = {}
    genre_nos = []
    genres_new = []
    for genre in gR:
        if genre in genre_count:
            genre_count[genre] = int(genre_count[genre]) + 1
        else:
            genre_count[genre] = 1
    for key, value in genre_count.items():
        genre_nos.append(value)
        genres_new.append(key)

    ypos = np.arange(len(genres_new))
    plt.xticks(ypos,genres_new)
    plt.ylabel("Books Available in Genre")
    plt.xlabel("Genre Name")
    plt.title("Book Genre Chart")
    plt.bar(genres_new, genre_nos)
    plt.show()
    back_to_main()

def chart():
    print("### Genre Chart ###\n", divider)
    genres = []
    genre_no = 0
    i = 0
    for book in book_file:
        genres.append(book[6])
    genre_count(genres)
menu()
