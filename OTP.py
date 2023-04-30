import random
import smtplib
otp=''.join([str(random.randint(0,9)) for i in range(4)])
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sneha25gaikwad@gmail.com',password="nopkcnodrwsjmfpp")
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg=str(otp)
print("hello your otp",msg)
server.sendmail('sneha25gaikwad@gmail.com' , 'sneha2003gaikwad@gmail.com' , msg)
server.quit()