from datetime import datetime
import re

#validating Employeeid
def validateemployeeid(employeeid):
    exp = r'^[A-Z]{3}[0-9]{4}'
    if re.match(exp, employeeid):
        return True
    else:
        return False

#validating Employee name
def validatename(name):
    l=name.split()
    if len(l)==3:
        if l[0].isalpha() and l[1].isalpha() and l[2].isalpha():
            return True
    return False

#validating mobile number
def validatemob(mobilenum):
    
    if len(mobilenum)==10:
        if mobilenum.isdigit():
            return True
    return False

#validating Designation
def validatedesignation(des):
    roles=["Manager","Data Analyst", "Accountant","Software Developer","Buisness Analyst","Software Tester","Customer Support" ]
    if des in roles:
        return True
    return False
    
def validatedepartment(dep):
    Department=["AI/ML", "HR","Automation", "Cyber Security", "Finance", "Dev Ops"]
    if dep in Department:
        return True
    return False

#validating salary
def validatesal(salary):
    if salary.isdigit():
        return True
    return False

#validating date of joining
def validatedateofjoining (dateofjoining):
    exp = r'^[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}$'
    if re.match(exp,dateofjoining):
        year=int(dateofjoining[6:10])
        month=int(dateofjoining[3:5])
        day=int(dateofjoining[0:2])
        current_date = datetime.now()
        span = (current_date.year-year)-((current_date.month, current_date.day)<(month,day))
        
        #age=int(span)
        if span>=0 and span<43:
            return True
        else:
            return False
    else:
        return None
    
#validating date of birth
def validatedateofbirth (dateofbirth):
    exp = r'^[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}$'
    if re.match (exp,dateofbirth):
        year=int(dateofbirth[6:10])
        month=int(dateofbirth[3:5])
        day=int(dateofbirth[0:2])
        current_date = datetime.now()
        age = (current_date.year-year)-((current_date.month, current_date)<(month,day))
        
        age=int(age)
        if age>18 and age<60:
            print (age)
            return True
        else:
            return False
    else:
        return None

#validating age #input is int
def validateage(age):
    age=int(age)
    if age>18 and age<60:
        return True
    return False


#validating gender #input is char
def validategender(gen):
    if gen=="M":
        return True
    elif gen=="F":
        return True
    elif gen=="O":
        return True
    else:
        return False
    


#validating state
def validatestate (state,city):
    states={"Maharashtra":["Pune","Mumbai","Nashik"],
    "Gujarat" : ["Ahmedabad", "Surat", "Vadodara"],
    "Karnataka" : ["Bangalore", "Hubli-Dharwad", "Belagavi"],
    "Delhi" : ["New Delhi"]
    }

    if state in states.keys():
        print("Valid state")
        v = states[state]
        if city in v:
            print("valid city")
            return True
            
        else:
            print("Enter valid city!")
            return False
            
    else:
        print("Enter a valid state!")
        return False
    
#validating aadhar number #input is int
def validateaadhar (aadharcardnum):
    if aadharcardnum.isdigit() and len(aadharcardnum)==12 :
        return True
    return False


#Validating pancard
def validatepan (pancardnum):
    exp=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(exp,pancardnum):
        return True
    return False

#validating username
def validateusername (usrnm):
    if len(usrnm)>4 and len(usrnm)<11:
        return True
    return False

#validating password
def validatepassword (pw):
    specialchar=['#', '$', '%', '&', '*','@','!']
    if len(pw)>8 and  len(pw)<20:
        val=True
        if not any (char.isupper() for char in pw):
            val=False
        if not any (char.islower() for char in pw):
            val=False
        if not any (char.isdigit() for char in pw):
            val=False
        if not any (char in specialchar for char in pw):
            val=False 
        if val:
            return val
    return False
