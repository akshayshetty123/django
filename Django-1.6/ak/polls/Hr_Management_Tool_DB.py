#!/usr/bin/python -tt
import sqlite3
import time
import os
s=[]
server_path=os.getcwd()
class DataBase: 
    def __init__(self):
        self.conn = sqlite3.connect("Hr_Management_Tool_DB.sqlite3")
        self.keyVarible="$%^)*)*hgfyv     ghfdv587&%$^%#^$#@@G B78967987908 $#^$#^$# #^^?([YINTBIUTIUYTKJNp0klghbb  k879870HGFVJYURr ut7 y i"
    	
    	
	
        pass

       
    def createSignIn_Up(self):
        try:
            self.conn.execute('''CREATE TABLE SIGNIN_TABLE
       (
	   FIRST    TEXT,
	   
       PASSWD TEXT     NOT NULL,
       SEX TEXT,
       DATE TEXT
      );''')
            print "sign in up table created"
            pass
        except sqlite3.OperationalError:
#             self.conn.execute('''ALTER TABLE Task_Detail ADD  UNIQID TEXT PRIMARY KEY NOT NULL''')
#             self.conn = sqlite3.connect(self.path)
              print "Table Task_Detail is present"
              pass
            
    def submitSignIn(self,USER,Password):
        try:
            self.createSignIn_Up()
            #s.append(USER)
            #print s
           # flag=0
            #print "enter the user name"
           # s1=raw_input()
           # for i in s:
               # if(s1==i):
                #    flag=1
               # else:
                 #   flag=0
            #if(flag==1):
                
              #  print s1,"is found "
         #   else:
              #  print s1,"is not found"
                    
	    print (USER + Password + "heloo")
	    
            self.conn.execute("INSERT INTO SIGNIN_TABLE VALUES(?,?)",
                              (USER,Password))
            self.conn.commit()
#           print "username: "+Username+" saved"
#             self.conn.close()
  #          close_caller
        except sqlite3.IntegrityError:
            print "key is present"
            pass
    def submitSignIn1(self,USER,Password,s1,s2):
        try:
            self.createSignIn_Up()
        
	    print (USER + Password +s1+s2,"heloo")
	    
            self.conn.execute("INSERT INTO SIGNIN_TABLE VALUES(?,?,?,?)",
                              (USER,Password,s1,s2))
            self.conn.commit()
#           print "username: "+Username+" saved"
#             self.conn.close()
  #          close_caller
        except sqlite3.IntegrityError:
            print "key is present"
            pass
        
    def Check1(self,USER):
        v=[]
        flag=0
        cnt=0
        cursor=self.conn.execute("""SELECT user FROM SIGNIN_TABLE""")
        for i in cursor:
           
            
            
            
            if(str(i[0])==str(USER)):
                v.append(str(i[0]))
                flag=1
                cnt=cnt+1
            else:
                continue
        
        if(flag==1):
            print USER,"found in table and total user count is" ,cnt
            

        else:
            print "not found in database"
            
        return v
    
    def Check3(self,USER):
        print USER
        conn = sqlite3.connect("Hr_Management_Tool_DB.sqlite3")
        d=USER.replace("u","",0)
        
        q="DELETE from SIGNIN_TABLE where user = "+'"'+str(d)+'"'
        print 'user name===',q
             
        cursor=conn.execute(q)
        conn.commit()
		

        print "akshay"
        
        #cursor1=self.conn.execute("""SELECT * FROM SIGNIN_TABLE""")
        cursor1="akshay"
        return cursor1

    def search(self,USER,Password):
        
        cursor=self.conn.execute("""SELECT user,password FROM SIGNIN_TABLE""")
        for i in cursor:
           
            
            
            
            if(str(i[0])==str(USER) and str(i[1])==str(Password)):
                return 1
        
            else:
                continue
        return 0

    def update(self,user,password):
        
        user=str(user)
        print user
        password=str(password)
        print password
        x=self.conn.execute('UPDATE SIGNIN_TABLE SET password=? WHERE user=?',(password, user))
        print x
        self.conn.commit()
    

