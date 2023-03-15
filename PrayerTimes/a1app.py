"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Fadhil Lawal
Date:   7/1/2020
"""


import a1
import MC as m
check = True
def play():
    date = m.monthconv(input("Enter Today's Date (ex.1 April 2020) : "))
    month = m.monthnum(date)
    year = m.year(date)
    adress = input("Please Enter In Your City: ")
    get = input("What Prayer Time Would You Like To Retrieve (To Retrieve All, Just Type All) : ")
    if get.lower() == 'fajr':
        print("Fajr Time Is", a1.get_fajr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    elif get.lower() == 'dhuhr':
        print("Dhuhr Time Is", a1.get_dhuhr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    elif get.lower() == 'dhur':
        print("Dhuhr Time Is", a1.get_dhuhr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    elif get.lower() == 'asr':
        print("Asr Time Is", a1.get_asr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    elif get.lower() == 'maghrib':
        print("Maghrib Time Is", a1.get_maghrib(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    elif get.lower() == 'isha':
        print("Isha Time Is", a1.get_isha(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    elif get.lower() == 'all':
        print("Fajr Time Is", a1.get_fajr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
        print("Dhuhr Time Is", a1.get_dhuhr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
        print("Asr Time Is", a1.get_asr(a1.get_json(date,a1.prayertime_response(adress,month,year))))
        print("Maghrib Time Is", a1.get_maghrib(a1.get_json(date,a1.prayertime_response(adress,month,year))))
        print("Isha Time Is", a1.get_isha(a1.get_json(date,a1.prayertime_response(adress,month,year))))
    else:
        print("Please Make Sure You Are Entering The Correct Information")

while check:
    play()
    re = input("Would You Like To Check The Times Again:(yes/no) ")
    if re.lower() != 'yes':
        print("Okay, Bye!!!")
        check = False

    
    

