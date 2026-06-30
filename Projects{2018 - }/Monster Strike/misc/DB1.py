import mysql.connector as mycon
mydb = mycon.connect(host = "localhost",user = "root",passwd = "ROOTLAP",
                             database = "kevin_the_cube")
cur = mydb.cursor()
h_sc = cur.fetchone()
cur.execute("select * from High_Score")
h_sc = cur.fetchall()
print(h_sc)
b=str(input("Enter Your Name: "))
'''a=0
        c=self.r_score
        for row in h_sc:
            if row[-1] >= c:
                a=row[0]
                continue
            elif row[-1] < c:
                a= row[0]
                break
        if a!=0:
            s = "INSERT INTO High_Score(Rank_,Name_,Score) VALUES({},'{}',{})".format(a,b,c)
            aa= "update High_Score set Rank_ =Rank_ + {} where Rank_ < {};".format(1,a)
            cur.execute(aa)
            cur.execute(s)
            mydb.commit()
        else:
            s = "INSERT INTO High_Score(Rank_,Name_,Score) VALUES({},'{}',{})".format(a+1,b,c)
            cur.execute(s)
            mydb.commit()
        cur.execute("select * from High_Score")
        h_sc = cur.fetchall()
        for row in h_sc:
            print(row)'''
        
