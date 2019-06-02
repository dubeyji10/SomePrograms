def problem3_3(month,day,year):
    import sys
    months=("January","February","March","April","May","June","July","August",
            "September","October","November","December")
    monthkey = int(month) - 1
    print(months[monthkey],str(day)+",",year)

problem3_3(6,23,1986)
problem3_3(6,17,2016)