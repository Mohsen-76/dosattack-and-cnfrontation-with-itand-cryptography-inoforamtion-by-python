import os
try:
    import mysql.connector
except:
    os.system('pip install mysql-connector-python')
    
mydb=mysql.connector.connect(
    host='localhost',
    user='admin',
    password='majic',
    database='network'
)
mycursor=mydb.cursor()

def execute_(query,mess):
    try:
        mycursor.execute(query)
        mydb.commit()
        print(mess)
    except Exception as er:
        print(er)
query_update_is_block='''update info set is_block={} where ip="{}"'''
query_update_is_login='''update info set is_login={} where ip="{}"'''
query_drop_logs='''delete from logs where destination="{}" '''

menu="""
[1] create database network
---------------------------
[2] drop table info
---------------------------
[3] change block in info table
---------------------------
[4] change login in info table
---------------------------
[5] drop table logs
---------------------------
[6] drop specefic ip in log table
"""
def give_ip():
    while True:
        octed_status=False
        ip = input('enter the ip : ')
        if ip==None or ip=="" or ip=="\n":
            continue
        condition=str(ip).split('.')
        for dot in condition:
            if not dot.isdigit():
                octed_status=True
                break
        if octed_status:
            continue

        if len(condition)!=4:
            continue

        break
    return ip

def give_status():
    while True:
        num=int(input('enter one or zero : '))
        if num !=0 and num!=1:
            continue
        break
    return num

print('welcome to manage database : ')
while True:
    print(menu)
    num=int(input('enter one of number : '))
    # create database
    if num==1:
        execute_('create database network','database created')
    #drop info  
    elif num==2:
        execute_('drop table info','info table droped')
    # change block 
    elif num==3:
        ip=give_ip()
        st=give_status()
        qu_is_block=query_update_is_block.format(st,ip)
        execute_(qu_is_block,f'in ip : {ip} the field is_block is : {st}')
    # change login 
    elif num==4:
        ip=give_ip()
        st=give_status()
        qu_is_login=query_update_is_login.format(st,ip)
        execute_(qu_is_login,f'in ip : {ip} the field is_login is : {st}')
    # drop logs 
    elif num==5:
        execute_('drop table logs','droped logs')
    # drop specific ip 
    elif num==6:
        ip = give_ip()
        qu_logs=query_drop_logs.format(ip)
        execute_(qu_logs,f'ip : {ip} droped seccusfuly ...')


