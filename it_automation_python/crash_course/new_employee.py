# this code is used for creating id and email for the new employee

def create_id(month, years, time):
    id_employee = month + years + time[:2] + time[3:5]
    return id_employee

def create_email(name):
    if " " in name:
        spliting_name = name.split()
        email_employee = spliting_name[0] + "." + spliting_name[1] + "@thecompany.com"
        return email_employee.lower()
    return name

month = int(input("Enter month of registration: "))
years = int(input("Enter years of registration: "))
time = str(input("Enter time of registration: "))
name = str(input("Name: "))

print(f"\n\nThe Insight Employee of {name}\n")
print(f"ID   : {create_id(month, years, time)}\nName : {name}\nEmail : {create_email(name)}")
