import smtplib # if you want to send email we use smtp simple mail transfer protocol
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls() # coonection by server.start and fro security we use starttls i.e transpose layer security
server.login('rahulbairagiofficial@gmail.com','2017****')
server.sendmail('rahulbairagiofficial@gmail.com','aditibairagiofficial@gamil.com','Mail send from rahulcode751')
print("Mail sent")
