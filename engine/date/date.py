#File Name: date.py (Digitas date calculator engine file)

import datetime
from calverter import Calverter


#Get current Gregorian date.
now = datetime.datetime.now()
greg_year = now.year
greg_month = now.month
greg_day = now.day
greg_weekday_number = now.weekday()


#Convert Gregorian date to Julian date.
cal = Calverter()
julian = cal.gregorian_to_jd(greg_year,greg_month,greg_day)


#Convert Julian date to Hijri date.
hijri = cal.jd_to_islamic(julian)


#Organize Hijri date to [greg_weekday_number, month_name, day_number, year] format.
hijri_year = hijri[0]
hijri_month = hijri[1]
hijri_day_number = hijri[2]
hijri_date = [greg_weekday_number, hijri_month, hijri_day_number, hijri_year]


#Convert greg_weekday_number (which are in number forms) into weekday name.
hijri_weekday = ["Al Ithnayn", "Ath Thulatha", "Al Arbia", "Al khamis",
                 "Al Jummah", "As Sabt", "Al Ahad"]

hijri_date[0] = hijri_weekday[greg_weekday_number]


#Convert hijri_month (which are in number forms) into month names.
hijri_months = ["Muharram", "Safar", "Rabi al Awwal", "Rabi ath Thani",
                "Jamada al Ula", "Jumada ath Thaniyah", "Rajab", "Shaban",
                "Ramadan", "Shawal", "Dhu al Qa'dah", "Dhu al Hijah"]

hijri_date[1] = hijri_months[hijri_month-1]


#Convert list hijri_date into a nicely formated sring
date = str(hijri_date[0]) + ", " + str(hijri_date[1]) + " " + str(hijri_date[2])+ ", " + str(hijri_date[3]) + " A.H."


#day name and month name gulo thik ache kina mahmud k jiggesh korte hobe
#next 7 days date specially weekday name check kore dekhte hobe
#google translation a dekhe pronunciation check kore nite hobe
