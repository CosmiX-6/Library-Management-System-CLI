from datetime import datetime,date,timedelta
def bookrequest(uid,line):
    b_li=line
    with open('bin\\users\\user-info.txt') as user:
        for line in user:
            if str(uid) in line:
                break
    u_li=line.strip().split('-')
    with open('bin\\config.txt') as conf:
        confdata=conf.readlines()
        for c_line in confdata:
            if 'BOROID' in c_line:
                break
    c_line=c_line.strip().split('-')
    tofind=c_line[1]
    id='BRID'+str(int(c_line[1][4:])+1)
    with open('bin\\books\\borrowed_book.txt','a') as br_b:
        br_b.write('%s-%s-%s-%s\n'%(id,u_li[0],b_li[0],datetime.now().strftime('%Y,%m,%d/%H:%M:%S')))
    with open('bin\\config.txt','w') as conf:
        for i in confdata:
            if 'BOROID-'+tofind in i:
                i=i.replace('BOROID-'+tofind,'BOROID-'+id)
            conf.write(i)
    with open('bin\\config.txt') as conf:
        confdata=conf.readlines()
        for c_line in confdata:
            if 'RESVID' in c_line:
                break
    c_line=c_line.strip().split('-')
    tofind=c_line[1]
    id='RSID'+str(int(c_line[1][4:])+1)
    with open('bin\\books\\reserved_book.txt','a') as br_b:
        br_b.write('%s-%s-%s-%s-%s-%s-%s-%s\n'%(id,u_li[1],u_li[3],b_li[4],u_li[4],b_li[1],date.today().strftime('%Y,%m,%d'),(date.today()+timedelta(days=7)).strftime('%Y,%m,%d')))
    with open('bin\\config.txt','w') as conf:
        for i in confdata:
            if 'RESVID-'+tofind in i:
                i=i.replace('RESVID-'+tofind,'RESVID-'+id)
            conf.write(i)
    with open('bin\\books\\book-info.txt') as search:
        confdata=search.readlines()
        find=b_li[0]+'-'+b_li[1]+'-'+b_li[2]+'-'+b_li[3]+'-'+b_li[4]+'-'+b_li[5]+'-'+b_li[6]+'-'+b_li[7]
        convert=b_li[0]+'-'+b_li[1]+'-'+b_li[2]+'-'+b_li[3]+'-'+b_li[4]+'-'+b_li[5]+'-'+str(int(b_li[6])-1)+'-'+b_li[7]
        print('-------------------------------')
        print('       ** Book Granted **      ')
        print('-------------------------------')
    with open('bin\\books\\book-info.txt','w') as replase:
        for i in confdata:
            if find in i:
                i=i.replace(find,convert)
            replase.write(i)