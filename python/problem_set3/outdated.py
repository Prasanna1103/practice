import re

def main():
    get_outdated()
    
def get_outdated():
    monthss = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            input_date = input("Date: ").strip()
            date_month_year = re.match("(\d{1,2})/(\d{1,2})/(\d{4})$", input_date)
            
            if date_month_year:
                date,month,year = map(int,date_month_year.groups())
                
                if 1<= date <=31 and 1<= month <=12:
                    print(f"{year}-{month}-{date}")
                    break
            
            
            dd_mm_yy = re.match("([A-Za-z]+) (\d{1,2}), (\d{4})$", input_date)
            if dd_mm_yy:
                mm_name, day, year = dd_mm_yy.groups()
                
                if mm_name in monthss:
                    month = monthss.index(mm_name) + 1
                    day = int(day)
                    year = int(year)
                
                    if 1<= day <=31:
                        print(f"{year}-{month}-{day}")
                        break
                
        except ValueError:
            pass
        
        
main()                    
            
            
    
    
        