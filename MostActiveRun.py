import webbrowser
import time
import csv
import datetime
from datetime import datetime


def most_active_run():
    init_url = "https://www.nseindia.com/market-data/most-active-equities"
    webbrowser.open_new_tab(init_url)

    time.sleep(5)

    file_company_name = open("FILE_COMPANY_NAME_Main.txt","w")
    url= 'https://www.nseindia.com/api/live-analysis-most-active-securities?index=value&csv=true'  

    webbrowser.open_new_tab(url)

    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    day = datetime.now().day
    month = datetime.now().month
    month = months[int(month)-1]
    if int(day) < 10:
        day = "0" + str(day)
    year = datetime.now().year

    time.sleep(10)
    
    with open(f"C:\\Users\\shini\\Downloads\\MA-Equities-CM-value-{day}-{month}-{year}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            file_company_name.write(row[0]+'\n')

