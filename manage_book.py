import validator as vd
import library
from config import cls
ldm=library.Library_Management_System.Library_database()
lum=library.Library_Management_System.User()
lub=library.Library_Management_System.Book()
ttype='book'

def add():
    cls()
    title,auth,pubn,isbn,qnt,rstype=None,None,None,None,None,None
    while title==None:
        title = vd.entry('Title','string','book',int(50))
    while auth==None:
        auth = vd.entry('Author','string','book',int(20))
    while pubn==None:
        pubn = vd.entry('Publication','string','book',int(30))
    while isbn==None:
        isbn = vd.entry('ISBN','int','book',int(13))
    while qnt==None:
        qnt = vd.entry('Quantity','int','book',int(2))
    while rstype==None:
        rstype = vd.entry('Book type','select','book',None)
    if ldm.Search(isbn,ttype,1):
        li=[title,auth,pubn,isbn,qnt,qnt,rstype]
        ldm.Add(li,ttype)
        return True
    else:
        return 0

def search():
    cls()
    print('[ 1 ] >> Search by UID\n[ 2 ] >> Search by ISBN\n[ B ] >> back')
    choice=input('Enter a choice : ')
    if choice=='1':
        bid=0
        while int(bid)<10001 or int(bid)>99999:
            bid=input('Enter Id (Eg. 10000) : ')
        bid='BKID'+str(bid)
        ldm.Search(bid,ttype,0)
        
    elif choice=='2':
        isbn = None
        while isbn==None:
            isbn = vd.entry('ISBN','int','book',int(13))
        ldm.Search(isbn,ttype,0)
    
    elif choice=='b' or choice=='B':
        cls()
        return 0

    else:
        search()
        
def display():
    ldm.Display(ttype)

def update():
    search = None
    while search==None:
        search = vd.entry('ISBN','int','book',int(13))
    title,auth,pubn,isbn,qnt,rstype=None,None,None,None,None,None
    while title==None:
        title = vd.entry('Title','string','book',int(50))
    while auth==None:
        auth = vd.entry('Author','string','book',int(20))
    while pubn==None:
        pubn = vd.entry('Publication','string','book',int(30))
    while isbn==None:
        isbn = vd.entry('ISBN','int','book',int(13))
    while qnt==None:
        qnt = vd.entry('Quantity','int','book',int(2))
    while rstype==None:
        rstype = vd.entry('Book type','select','book',None)
    convert=title+'_'+auth+'-'+pubn+'-'+str(isbn)+'-'+str(qnt)+'-'+str(qnt)+'-'+rstype
    ldm.Update(search,convert,ttype)

def delete():
    find = None
    while find==None:
        find = vd.entry('ISBN','int','book',int(13))
    ldm.Delete(find,ttype)

def issue():
    find_user = None
    while find_user==None:
        find_user = vd.entry('Contact','int','user',int(10))
    li=lum.Verify(find_user)
    if li[0]:
        find_book = None
        while find_book==None:
            find_book = vd.entry('ISBN','int','book',int(13))
        cls()
        lub.Book_request(find_user,find_book,li[1])
    else:
        cls()
        print('-------------------------------')
        print('    * User not Registered *    ')
        print('-------------------------------')
