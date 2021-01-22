import os
from os import path
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def makedir():
    try:
        os.system('mkdir bin\\books bin\\users bin\\accounts' if os.name=='nt' else 'mkdir bin\\books bin\\users bin\\accounts')
        open('bin\\users\\user-info.txt','a').close()
        open('bin\\books\\book-info.txt','a').close()
        open('bin\\books\\reserved_book.txt','a').close()
        open('bin\\books\\returned_book.txt','a').close()
        open('bin\\books\\borrowed_book.txt','a').close()
        open('bin\\accounts\\fine.txt','a').close()
        open('bin\\credential.txt','a').close()
        if path.exists('bin\\config.txt'):
            pass
        else:
            with open('bin\\config.txt','a') as f:
                f.write('USERID-USID10000\n')
                f.write('BOOKID-BKID10000\n')
                f.write('BOROID-BRID10000\n')
                f.write('RESVID-RSID10000\n')
        cls()
    finally:
        pass