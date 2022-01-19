""" we will automate a script that will send an email to people on their birthdays
* there is a way to run our code habitually which is in the cloud . its free
    step 1 : go to pythonanywere.com
    step 2 : create an account and log in
    step 3 : go to Files and import all your files
    step 4 : go to consoles and click on bash  , then wait and type python (name of your main file)
    step 5 : go to tasks then add the time and the same command you run in the bash then click on add task

NOTE: provide in the csv data such us name,email,year,month,day to the person that you will send happy birthday
example:    name,email,year,month,day
            james,james@gmail.com,1995,5,18
"""


import pandas
import random
import smtplib
import datetime as dt

# create a tuple which contains today day , and month using datetime module
today = (dt.datetime.now().month, dt.datetime.now().day)

# using pandas , we must read the csv file and convert it to dictionary
birthday = pandas.read_csv("birthdays.csv")
dict_birthday = {(datarow.month, datarow.day): datarow for (index, datarow) in birthday.iterrows()}


# let's see if today(day , month) match the key
if today in dict_birthday:
    person = dict_birthday[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as l:
        content = l.read()
        content = content.replace("[NAME]", person["name"])

    # gmail infos:
    my_email = ""  # here write your gmail
    my_password = ""  # here write your password
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person["email"],
                            msg=f"Subject : Happy Birthday\n\n {content}")
