import validator as vd
import library
from config import cls
lms=library.Library_Management_System()
ldm=library.Library_Management_System.Library_database()
ttype='user'

def getcontact():
    contact=None
    while contact==None:
        contact = vd.entry('Contact','int','user',int(10))
    return contact
    
def add():
    cls()
    fname,lname,email,contact,idtype=None,None,None,None,None
    while fname==None:
        fname = vd.entry('Firstname','char','user',int(15))
    while lname==None:
        lname = vd.entry('Lastname','char','user',int(15))
    while email==None:
        email = vd.entry('Email id','email','user',int(30))
    while contact==None:
        contact = vd.entry('Contact','int','user',int(10))
    while idtype==None:
        idtype = vd.entry('Id type','select','user',None)
    if ldm.Search(contact,ttype,1):
        li=[fname,lname,email,contact,idtype]
        ldm.Add(li,ttype)
        return True
    else:
        return 0

def search():
    cls()
    print('[ 1 ] >> Search by UID\n[ 2 ] >> Search by Contact\n[ B ] >> back')
    choice=input('Enter a choice : ')
    if choice=='1':
        uid=0
        while int(uid)<10001 or int(uid)>99999:
            uid=input('Enter Id (Eg. 10000) : ')
        uid='USID'+str(uid)
        ldm.Search(uid,ttype,0)
        
    elif choice=='2':
        contact = None
        while contact==None:
            contact = vd.entry('Contact','int','user',int(10))
        ldm.Search(contact,ttype,0)
    
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
        search = vd.entry('Contact','int','user',int(10))
    fname,lname,email,contact,idtype=None,None,None,None,None
    while fname==None:
        fname = vd.entry('Firstname','char','user',int(15))
    while lname==None:
        lname = vd.entry('Lastname','char','user',int(15))
    while email==None:
        email = vd.entry('Email id','email','user',int(30))
    while contact==None:
        contact = vd.entry('Contact','int','user',int(10))
    while idtype==None:
        idtype = vd.entry('Id type','select','user',None)
    convert=fname+'_'+lname+'-'+email+'-'+str(contact)+'-'+idtype
    ldm.Update(search,convert,ttype)

def delete():
    find = None
    while find==None:
        find = vd.entry('Contact','int','user',int(10))
    ldm.Delete(find,ttype)

def register_lib():
    print('========== Register ===========')
    uname=input('Enter username : ')
    while vd.checkstring(uname)==False:
        uname=input('Enter username : ')
    passs=input('Enter password : ')
    while vd.checkpass(passs)==False:
        passs=input('Enter password : ')
    lms.Register(uname,passs)