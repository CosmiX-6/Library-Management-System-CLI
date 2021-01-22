import config as cf
import sys
import manage_user as mu
import manage_book as mb
import manage_account as ma
import library
lub=library.Library_Management_System.Book()
cf.makedir()
def onStart():    
    print('===============================')
    print('   Library Management System   ')
    print('-------------------------------')
    print('[ 1 ] >> Login\n[ 2 ] >> Register\n[ 0 ] >> Exit')
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        cf.cls()
        sys.exit('Program terminated Successfully')
    elif choice=='1':
        login()
    elif choice=='2':
        mu.register_lib()
    else:
        onStart()
    onStart()

def login():
    cf.cls()
    print('============ Login ============')
    username = input('Username : ')
    password = input('Password : ')
    if library.Library_Management_System().Login(username,password):
        cf.cls()
        print('-------------------------------')
        print('    ** Login successful **     ')
        print('-------------------------------')
        onCreate()
    else:
        cf.cls()
        print('Incorrect username or password.\nWould you like to register ? [Y/N]\n')
        ans = input('[Y/N]')
        if ans=='Y' or ans=='y':
            cf.cls()
            mu.register_lib()
        elif ans=='N' or ans=='n':
            cf.cls()
            login()
        else:
            print('Incorrect Option Selected')
            onStart()

def onCreate():
    print('===============================')
    print('   Library Management System   ')
    print('-------------------------------')
    print('1 Book Request\n2 Return Book\n3 Book Accounts\n4 User (Add/Edit)\n5 Book (Add/Edit)\nL Logout\n0 Exit')
    choice=input('_______________________________\nEnter a choice : ')
    cf.cls()
    if choice=='0':
        sys.exit('Program terminated Successfully')
    elif choice=='1':
        cf.cls()
        mb.issue()
    elif choice=='2':
        con=mu.getcontact()
        cf.cls()
        lub.Return_book(con)
    elif choice=='3':
        bookaccount()
    elif choice=='4':
        cf.cls()
        manage_user()
    elif choice=='5':
        manage_book()
    elif choice=='L' or choice=='l':
        onStart()
    else:
        cf.cls()
    onCreate()

def manage_user():
    print('===============================')
    print('       ** MANAGE USERS **      ')
    print('-------------------------------')
    print('1 Add\n2 Update\n3 Search\n4 Display\n5 Delete\nb Back')
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        sys.exit('Program terminated Successfully')
    elif choice=='1':
        if mu.add():
            cf.cls()
            print('-------------------------------')
            print('  * User added successfully *  ')
            print('-------------------------------')
        else:
            cf.cls()
            print('-------------------------------')
            print('    * User already exists *    ')
            print('-------------------------------')
    elif choice=='2':
        cf.cls()
        mu.update()
    elif choice=='3':
        cf.cls()
        mu.search()
    elif choice=='4':
        cf.cls()
        mu.display()
    elif choice=='5':
        cf.cls()
        mu.delete()
    elif choice=='b' or choice=='B':
        cf.cls()
        return 0
    else:
        cf.cls()
    manage_user()

def manage_book():
    print('===============================')
    print('       ** MANAGE BOOKS **      ')
    print('-------------------------------')
    print('1 Add\n2 Update\n3 Search\n4 Display\n5 Delete\nb Back')
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        sys.exit('Program terminated Successfully')
    elif choice=='1':
        if mb.add():
            cf.cls()
            print('-------------------------------')
            print('  * Book added successfully *  ')
            print('-------------------------------')
        else:
            cf.cls()
            print('-------------------------------')
            print('    * Book already exists *    ')
            print('-------------------------------')
    elif choice=='2':
        cf.cls()
        mb.update()
    elif choice=='3':
        cf.cls()
        mb.search()
    elif choice=='4':
        cf.cls()
        mb.display()
    elif choice=='5':
        cf.cls()
        mb.delete()
    elif choice=='b' or choice=='B':
        cf.cls()
        return 0
    else:
        cf.cls()
    manage_book()

def bookaccount():
    print('\n===============================')
    print('      ** BOOK ACCOUNTS **      ')
    print('-------------------------------')
    print('1 Reserved Book\n2 Due_Book\n3 Borrow List\n4 Returned List\n5 Fine Book\nb Back\n0 Exit')
    choice=input('_______________________________\nEnter a choice : ')
    if choice=='0':
        sys.exit('Program terminated Successfully')
    elif choice=='1':
        ma.display_res()
    elif choice=='2':
        ma.display_due()
    elif choice=='3':
        ma.display_bor()
    elif choice=='4':
        ma.display_ret()
    elif choice=='5':
        ma.display_fine()
    elif choice=='b' or choice=='B':
        cf.cls()
        return 0
    else:
        bookaccount()
    bookaccount()

onStart()