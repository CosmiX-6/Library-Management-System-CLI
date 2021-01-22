from datetime import date,datetime
import booktransaction as bt
from config import cls
class Library_Management_System:
    def __init__(self):
        pass

    def Login(self,username,password):
        flag=0
        with open('bin\\credential.txt','r') as cred:
            for line in cred:
                if username in line:
                    flag=1
                    break
        if flag==1:
            li=line.strip().split('-')
            if username==li[0] and password==li[1]:
                return True
            elif username==li[0] and password!=li[1]:
                print('Incorrect Password.')
                return False
        else:
            return False
            
    def Register(self,uname,passs):
        flag=0
        with open('bin\\credential.txt') as c:
            for line in c:
                if uname in line:
                    flag=1
                    break
        if flag==0:
            cls()
            with open('bin\\credential.txt','a') as c:
                c.write('%s-%s\n'%(uname,passs))
            print('---------------------------------')  
            print('        *User Registered*        ')
            print('---------------------------------') 
        else:
            cls()
            print('---------------------------------')  
            print('*User already exists in database*')
            print('---------------------------------')  

    class User:
        def __init__(self):
            pass
        def Verify(self,uid):
            flag=0
            with open('bin\\users\\user-info.txt') as lines:
                for line in lines:
                    if str(uid) in line:
                        li=line.strip().split('-')
                        flag=1
                        break
            if flag==1:
                return [True,li[4]]
            else:
                return [False,False]
    
    class Accounts:
        def __init__(self):
            pass

        def Calculate_fine(self,con,fine,reserve):
            day=fine
            pay=0
            interest=0
            while fine>0:
                if fine<=7:
                    pay=pay+(fine*interest)
                    fine-=fine
                else:
                    pay=pay+(fine*interest)
                    fine-=7
                interest+=1
            print('The user is fined for late submission of book.\nFine Amount : Rs '+str(pay))
            ans=input('Pay fine to return book.\nFine Paid? [Y/N] : ')
            if ans=='Y' or ans=='y':
                with open('bin\\accounts\\fine.txt','a') as f_1:
                    f_1.write('%s-%s-%s-%s-%s-%s\n'%(reserve[3],reserve[4],str(pay),str(day),reserve[7],date.today().strftime('%Y,%m,%d')))
                    Library_Management_System.Book().Return_Process(day,con,reserve)
            elif ans=='N' or ans=='n':
                return 0
            else:
                return 0                    

    class Book:
        def __init__(self):
            pass

        def Show_duedt(self):
            cls()
            print('{0:9} | {1:30} | {2:10} | {3:13} | {4:7} | {5:50} | {6}\n'.format('RES ID','FULLNAME','CONTACT','ISBN NO','USER','BOOK TITLE','DUE ON'))
            with open('bin\\books\\reserved_book.txt') as res_b:
                for i in res_b:
                    i=i.strip().split('-')
                    y1,m1,d1=map(int,i[7].split(','))
                    now=date.today().strftime('%Y,%m,%d')
                    y2,m2,d2=map(int,now.split(','))
                    delta=(date(y2,m2,d2)-date(y1,m1,d1)).days
                    if delta>=0:
                        if delta==0:
                            delta='Due Today'
                        else:
                            delta=str(delta)+' days ago'
                        print('{0:9} | {1:30} | {2:10} | {3:13} | {4:7} | {5:50} | {6}'.format(i[0],i[1].replace('_',' '),i[2],i[3],i[4],i[5].replace('_',' '),delta))

        def Show_duedt_ret(self,con):
            with open('bin\\books\\reserved_book.txt') as res_b:
                for i in res_b:
                    if str(con) in i:
                        i=i.strip().split('-')
                        y1,m1,d1=map(int,i[6].split(','))
                        now=date.today().strftime('%Y,%m,%d')
                        y2,m2,d2=map(int,now.split(','))
                        delta=(date(y2,m2,d2)-date(y1,m1,d1)).days
                        return delta
        
        def Reservation_status(self):
            with open('bin\\books\\reserved_book.txt') as lines:
                for line in lines:
                    if str(self.uid) in line:
                        self.reserve=line.strip().split('-')
                        return True
                else:
                    return False

        def Reservation_status_print(self):
            cls()
            with open('bin\\books\\reserved_book.txt') as lines:
                print('{0:9} | {1:30} | {2:10} | {3:13} | {4:7} | {5:50} | {6:10} | {7:10} |\n'.format('RES ID','FULLNAME','CONTACT','ISBN NO','USER','BOOK TITLE','ISSUED ON','EXPIRY'))
                for line in lines:
                    line=line.strip().split('-')                     
                    print('{0:9} | {1:30} | {2:10} | {3:13} | {4:7} | {5:50} | {6:10} | {7:10} |'.format(line[0],line[1].replace('_',' '),line[2],line[3],line[4],line[5].replace('_',' '),line[6].replace(',','/'),line[7].replace(',','/')))
        
        def Return_book(self,con):
            self.uid=con
            if self.Reservation_status():
                day = self.Show_duedt_ret(con)
                with open('bin\\books\\reserved_book.txt') as lines:
                    for line in lines:
                        if str(con) in line:
                            reserve=line.strip().split('-')
                            break
                if day<8:
                    self.Return_Process(day,con,reserve)
                else:
                    Library_Management_System.Accounts().Calculate_fine(con,day,reserve)
            else:
                print('-------------------------------')
                print('*No book reserved by the user*')
                print('-------------------------------')

        def Return_Process(self,day,con,reserve):
            with open('bin\\books\\reserved_book.txt','r+') as search:
                original = search.readlines()
                search.seek(0)
                for line in original:
                    if reserve[2] not in line:
                        search.write(line)
                search.truncate()
            with open('bin\\books\\book-info.txt') as f:
                for b_li in f:
                    if reserve[3] in b_li:
                        break
            b_li=b_li.strip().split('-')
            with open('bin\\books\\book-info.txt') as search:
                confdata=search.readlines()
                find=b_li[0]+'-'+b_li[1]+'-'+b_li[2]+'-'+b_li[3]+'-'+b_li[4]+'-'+b_li[5]+'-'+b_li[6]+'-'+b_li[7]
                convert=b_li[0]+'-'+b_li[1]+'-'+b_li[2]+'-'+b_li[3]+'-'+b_li[4]+'-'+b_li[5]+'-'+str(int(b_li[6])+1)+'-'+b_li[7]
            with open('bin\\books\\book-info.txt','w') as replase:
                for i in confdata:
                    if find in i:
                        i=i.replace(find,convert)
                    replase.write(i)
            with open('bin\\books\\returned_book.txt','a')as f:
                f.write('%s-%s-%s-%s\n'%(str(con),reserve[3],str(day),datetime.now().strftime('%Y,%m,%d/%H:%M:%S')))
            print('-------------------------------')
            print('* Book successfully returned * ')
            print('-------------------------------')  

        def Book_request(self,uid,bid,utype):
            self.uid=uid
            self.bid=bid
            if self.Reservation_status():
                print('Already reserved a book, please return the book before requesting new book.')
                li=self.reserve
                print('{0:10} : {1}\n{2:10} : {3}\n{4:10} : {5}\n{6:10} : {7}\n'.format('Username',li[1].replace('_',' '),'Book title',li[5].replace('_',' '),'ISBN',li[3],'Issued on',li[6].replace(',','/')))
            else:
                flag=0
                with open('bin\\books\\book-info.txt') as f:
                    for line in f:
                        if str(self.bid) in line:
                            flag=1
                            break
                if flag==1:
                    line=line.strip().split('-')
                    if int(line[6])>0:
                        if int(line[6])==1 and line[7]=='rserv':
                            if utype=='Student':
                                Permission=0
                                with open('bin\\books\\reserved_book.txt','r') as f:
                                    for f_1 in f:
                                        if str(self.bid)+'Staff' in f_1:
                                            Permission=1
                                            break
                                if Permission==1:
                                    cls()
                                    bt.bookrequest(self.uid,line)
                                else:
                                    print('Last book reserved for staff.')
                            else:
                                cls()
                                bt.bookrequest(self.uid,line)
                        else:
                            cls()
                            bt.bookrequest(self.uid,line)
                    else:
                        print('This book is all reserved.')
                else:
                    print('There\'s no such book.')

        def Renew_info():
            pass

    class Library_database:
        def __init__(self):
            pass
        def Add(self,listdata,ttype):
            if ttype=='user':
                with open('bin\\config.txt') as conf:
                    confdata=conf.readlines()
                    for c_line in confdata:
                        if 'USERID' in c_line:
                            break
                c_line=c_line.strip().split('-')
                tofind=c_line[1]
                id='USID'+str(int(c_line[1][4:])+1)
                with open('bin\\users\\user-info.txt','a') as user:
                    user.write('%s-%s_%s-%s-%d-%s\n'%(id,listdata[0],listdata[1],listdata[2],listdata[3],listdata[4]))
                with open('bin\\config.txt','w') as conf:
                    for i in confdata:
                        if 'USERID-'+tofind in i:
                            i=i.replace('USERID-'+tofind,'USERID-'+id)
                        conf.write(i)
                del conf,c_line,confdata,tofind,id,listdata,ttype
            else:
                with open('bin\\config.txt') as conf:
                    confdata=conf.readlines()
                    for c_line in confdata:
                        if 'BOOKID' in c_line:
                            break
                c_line=c_line.strip().split('-')
                tofind=c_line[1]
                id='BKID'+str(int(c_line[1][4:])+1)
                with open('bin\\books\\book-info.txt','a') as book:
                    book.write('%s-%s-%s-%s-%d-%d-%d-%s\n'%(id,listdata[0],listdata[1],listdata[2],listdata[3],listdata[4],listdata[5],listdata[6]))
                with open('bin\\config.txt','w') as conf:
                    for i in confdata:
                        if 'BOOKID-'+tofind in i:
                            i=i.replace('BOOKID-'+tofind,'BOOKID-'+id)
                        conf.write(i)
                    
        def Delete(self,find,ttype):
            if ttype=='user':
                with open('bin\\users\\user-info.txt','r+') as search:
                    original = search.readlines()
                    search.seek(0)
                    for line in original:
                        if str(find) not in line:
                            search.write(line)
                    search.truncate()
            else:
                with open('bin\\books\\book-info.txt','r+') as search:
                    original = search.readlines()
                    search.seek(0)
                    for line in original:
                        if str(find) not in line:
                            search.write(line)
                    search.truncate()
        
        def Update(self,find,convert,ttype):
            flag=0
            if ttype=='user':
                with open('bin\\users\\user-info.txt') as search:
                    confdata=search.readlines()
                    for conf in confdata:
                        if str(find) in conf:
                            flag=1
                            break
                if flag==1:
                    conf=conf.strip().split('-')
                    print('User found : ')
                    print(*conf)
                    find=conf[0]+'-'+conf[1]+'-'+conf[2]+'-'+conf[3]+'-'+conf[4]
                    with open('bin\\users\\user-info.txt','w') as replas:
                        for i in confdata:
                            if find in i:
                                i=i.replace(find,conf[0]+'-'+convert)
                            replas.write(i)
                    print('Replaced with :\n'+conf[0]+'-'+convert)
                else:
                    print('-------------------------------')
                    print('     ** User Not Found **      ')
                    print('-------------------------------')
            else:
                with open('bin\\books\\book-info.txt') as search:
                    confdata=search.readlines()
                    for conf in confdata:
                        if str(find) in conf:
                            flag=1
                            break
                if flag==1:
                    conf=conf.strip().split('-')
                    print('Book found : ')
                    print(*conf)
                    find=conf[0]+'-'+conf[1]+'-'+conf[2]+'-'+conf[3]+'-'+conf[4]+'-'+conf[5]+'-'+conf[6]+'-'+conf[7]
                    with open('bin\\books\\book-info.txt','w') as replas:
                        for i in confdata:
                            if find in i:
                                i=i.replace(find,conf[0]+'-'+convert)
                            replas.write(i)
                    print('Replaced with :\n'+conf[0]+'-'+convert)
                else:
                    print('-------------------------------')
                    print('      * Book Not Found *       ')
                    print('-------------------------------')

        def Display(self,ttype):
            if ttype=='user':
                with open('bin\\users\\user-info.txt') as f:
                    print('{0:9} | {1:31} | {2:30} | {3:10} | {4}\n'.format('USER ID','FULLNAME','EMAIL ID','CONTACT','USER TYPE'))
                    for line in f:
                        line=line.strip().split('-')
                        print('{0:9} | {1:31} | {2:30} | {3:10} | {4}'.format(line[0],line[1].replace('_',' '),line[2],line[3],line[4]))
            else:
                with open('bin\\books\\book-info.txt') as f:
                    print('{5:9} | {0:50} | {1:20} | {2:30} | {3:13} | {4}\n'.format('BOOK TITLE','AUTHOR','PUBLISHER','ISBN NO.','QUANTITY/LEFT','BOOK ID'))
                    for line in f:
                        line=line.strip().split('-')
                        print('{0:9} | {1:50} | {2:20} | {3:30} | {4:13} | {5:2} / {6:2}'.format(line[0],line[1].replace('_',' '),line[2].replace('_',' '),line[3].replace('_',' '),line[4],line[5],line[6]))
        
        def Search(self,searchid,ttype,send):
            cls()
            if ttype=='user':
                flag=0
                with open('bin\\users\\user-info.txt') as f:
                    for line in f:
                        if str(searchid) in line:
                            flag=1
                            break
                if send==0:
                    if flag==1:
                        found=line.strip().split('-')
                        print('{0:31} | {1:30} | {2:10} | {3}\n'.format('FULLNAME','EMAIL ID','CONTACT','USER TYPE'))
                        print('{0:31} | {1:30} | {2:10} | {3}'.format(found[1].replace('_',' '),found[2],found[3],found[4]))
                    else:
                        print('-------------------------------')
                        print('    * User not registered *    ')
                        print('-------------------------------')
                else:
                    if flag==1:
                        return False
                    else:
                        return True
                
            else:
                flag=0
                with open('bin\\books\\book-info.txt') as f:
                    for line in f:
                        if str(searchid) in line:
                            flag=1
                            break
                if send==0:        
                    if flag==1:
                        found=line.strip().split('-')
                        print('{0:50} | {1:20} | {2:30} | {3:13} | {4}\n'.format('BOOK TITLE','AUTHOR','PUBLISHER','ISBN NO.','QUANTITY/LEFT'))
                        print('{0:50} | {1:20} | {2:30} | {3:13} | {4:2}/{5:2}'.format(found[1].replace('_',' '),found[2].replace('_',' '),found[3].replace('_',' '),found[4],found[6],found[5]))
                    else:
                        print('-------------------------------')
                        print('    * Book not registered *    ')
                        print('-------------------------------')
                else:
                    if flag==1:
                        return False
                    else:
                        return True