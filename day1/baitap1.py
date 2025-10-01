import datetime
age=int(input("nhap nam sinh cua ban: "))
year=datetime.datetime.now().year
your_age=year-age
print("so tuoi hien tai cua ban la: ",your_age)