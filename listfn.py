import mysql.connector as mycon
cn = mycon.connect(host='localhost',user='root',password="abcdef",database="projects")
cur = cn.cursor()
def getlist():
    global cn,cur
    print("\n*******************GET LIST**************************")
    cl = int(input("Enter the name of class: "))
    query="select * from stu where class="+str(cl)
    cour = input("Enter course: ")
    query="select * from stu where course="+'cour'
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\n *****SORRY! NO MATCHING DETAILS AVAILABLE*****")
    else:
        print("\n**************************************************")
        print('%5s'%"ID",'%15s'%'STUDENT NAME','%12s'%'ADDRESS','%10s'%'PHONE')
        print("\n**************************************************")
        count=0
        for row in results:
            print('%5s' % row[0],'%12s'%row[1],'%12s'%row[2],'%13s'%row[3])
            count+=1
        print("\n*************** TOTAL RECORD:",count,"**************")  
