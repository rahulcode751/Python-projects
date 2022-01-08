# we have to install mysql.connector using "pip install mysql.connector" command on terminal
import mysql.connector
import datetime    # pre installed
import os          # pre installed

mydate = str(datetime.date.today())
current = mydate[8:10]+mydate[5:7]
myconnection = mysql.connector.connect(
    host="localhost", user="root", password="@RANran751", database="birthdays")
cur = myconnection.cursor()
# used to execute mysql command
cur.execute(f"select *from data where bday = {current}")
list1 = cur.fetchall()  # it return rows in list
for i in list1:
    print(i)

for i in list1:
    os.system(
        f"start https://web.whatsapp.com/send?phone=+91{i[2]}^&text=happy%20Birthday%20to%20you%20{i[0]}")

# when you run this program it will open whatsapp web with correponding friend having birthdays and whose data is present in our mysql birthday database .you just have to press enter
