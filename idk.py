import smtplib
from time import sleep

# made this for fun lol
name = input('What Is Your Name: ')
age = input('What is Your Age: ')
time = input('What is your timezone: ')
country = input('Where Do You Live: ')
email = input('What is Your Email: ')
idk = 'Made by Muidreza'
print(idk)
sleep(1)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Email - To send the form on your email", "Email pass")
message = "Name = " + name + " Age = " + age + " Timezone = " + time + " Country = " + country + " Email = " + email + " Thats it!"
s.sendmail("Copy and paste the same email as above", "Email to send the form on", message)
s.quit()
print('Hey ' + name + '. Your Application Has Been Submitted! Wait For Response On Your Email!' )
sleep(3)







