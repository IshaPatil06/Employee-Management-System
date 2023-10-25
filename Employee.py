import functionsFinal
class Employee:
    def __init__(self, emp_id, emp_name, emp_contact, emp_designation, emp_department, emp_salary, emp_doj, emp_dob, emp_age, emp_gender, emp_address,emp_state, emp_city, emp_aadhar, emp_pan, emp_username, emp_pw):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_contact=emp_contact
        self.emp_designation=emp_designation
        self.emp_department=emp_department
        self.emp_salary=emp_salary
        self.emp_doj=emp_doj
        self.emp_dob=emp_dob
        self.emp_age=emp_age
        self.emp_gender=emp_gender
        self.emp_address=emp_address
        self.emp_state=emp_state
        self.emp_city=emp_city
        self.emp_aadhar=emp_aadhar
        self.emp_pan=emp_pan
        self.emp_username=emp_username
        self.emp_pw=emp_pw

    def display(self):
        print("ID: ",self.emp_id, "Name: ",self.emp_name,"Contact: ",self.emp_contact,"Designation: ",self. emp_designation, "Department: ", self.emp_department,"Salary: ", self.emp_salary,"Date of joining: ", self.emp_doj, "Date of birth: ", self.emp_dob, "Age: ", self.emp_age, "Gender: ", self.emp_gender,"Address: ", self.emp_address,"State: ",self.emp_state,"City: ", self.emp_city,"Aadhar card number: ", self.emp_aadhar,"Pan card number: ", self.emp_pan, "Username: ",self.emp_username,"Password: ",self.emp_pw)
       
       
    
emp_dataobj=[]

admin={"admin111":"admin@111"}
user={"user123":"user#123", "ASD1234":"ASD@123asd" }
ticket={}
obj1=Employee("ASD1234","A S D","1234567890","Manager","Finance","50000","20/05/2018","01/01/2001","22","M","adress","Maharashtra","Pune","123412341234","QAZXS1234W","Asd1234","ASD@123asd")
emp_dataobj.append(obj1)
while True:
    if end==1:
        break
    print("Print adm for admin \nusr for user \nend to exit")
    chh=input("Enter your choice: ")
    end=0
    if chh=="adm":
        usrnm=input("Enter username: ")
        pwd=input("Enter password: ")
        bye=0
        if usrnm in admin.keys():
            while pwd==admin[usrnm]:
                #print("Access permitted!")
                if bye==1:
                    break
                print(end="\n")
                print("Enter 1 to add details of the Employee")
                print("Enter 2 to delete details of the Employee")
                print("Enter 3 to update details of the Employee")
                print("Enter 4 to search details of the Employee")
                print("Enter 5 to display all employees' details")
                print("Enter 6 to display the employee with highest salary")
                print("Enter 7 to display the employee with lowest salary")
                print("Enter 8 to view tickets")
                print("Enter 9 to exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    while True:
                        emp_id=input("Enter Employee Id: ")
                        if functionsFinal.validateemployeeid(emp_id) :
                            break
                        else: 
                            print("Enter a valid name!")
                            
                    
                    while True:
                        emp_name=input("Enter Employee Name: ")
                        if functionsFinal.validatename(emp_name):
                            break
                        else:
                            print("Enter name in proper format!")

                    while True:
                        emp_contact=input("Enter contact details: ")

                        if functionsFinal.validatemob(emp_contact):
                            break
                        else:
                            print("Enter valid mobile number!")

                    
                    while True:
                        emp_designation=input("Enter Employee Designation: ")
                        if functionsFinal.validatedesignation(emp_designation) :
                            break
                        else: 
                            print("Enter a valid designation!")
                            
                    while True:
                        emp_department=input("Enter Employee Department: ")
                        if functionsFinal.validatedepartment(emp_department) :
                            break
                        else: 
                            print("Enter a valid department!")

                    
                    while True:
                        emp_salary=(input("Enter Employee Salary: "))
                        if functionsFinal.validatesal(emp_salary) :
                            break
                        else: 
                            print("Enter a valid salary!")

                    
                    while True:
                        emp_doj=input("Enter Employee Date of Joining (dd/mm/yyyy): ")
                        if functionsFinal.validatedateofjoining(emp_doj) :
                            break
                        else: 
                            print("Enter a valid date!")
                    
                    
                    while True:
                        emp_dob=input("Enter Employee Date of Birth (dd/mm/yyyy): ")
                        if functionsFinal.validatedateofbirth(emp_dob) :
                            break
                        else: 
                            print("Enter a valid date!")

                   
                    while True:
                        emp_age=int(input("Enter Employee Age: "))
                        if functionsFinal.validateage(emp_age) :
                            break
                        else: 
                            print("Enter a valid age!")

                    
                    while True:
                        emp_gender=input("Enter Gender:  M for male, F for female and O for Other: ")
                        if functionsFinal.validategender(emp_gender):
                            break
                        else:
                            print("Enter gender in correct format!")
                
                    
                    emp_address=input("Enter Employee Address: ")


                    
                    while True:
                        emp_state=input("Enter Employee State: ")
                        emp_city=input("Enter Employee City: ")
                        if functionsFinal.validatestate(emp_state, emp_city):
                            break

                    while True:
                        emp_aadhar=input("Enter Employee Aadhar Number: ")

                        if functionsFinal.validateaadhar(emp_aadhar):
                            break
                        else:
                            print("Enter correct aadhar number!")
                    
                    
                    while True:
                        emp_pan=input("Enter Employee PAN Number: ")
                        if functionsFinal.validatepan(emp_pan):
                            break
                        else:
                            print("Enter correct pancard number!")
                    
                    
                    while True:
                        print("Username should be between 5 to 10 letters")
                        emp_username=input("Enter Employee UserName: ")
                        if functionsFinal.validateusername(emp_username):
                            
                            print("Employee password must have atleast 1 upper case alphabet, 1 lowercase alphabet, 1 digit, 1 special character and should be above 8 characters.")
                            emp_pw=input("Enter Employee Password : ")
                            if functionsFinal.validatepassword(emp_pw):
                                user[emp_username]=emp_pw
                                break
                            else:
                                print("Enter a valid Password!")
                                
                            
                        else:
                            print("Enter valid Username!")         
                    obj=Employee(emp_id, emp_name, emp_contact, emp_designation, emp_department, emp_salary, emp_doj, emp_dob, emp_age, emp_gender, emp_address,emp_state, emp_city, emp_aadhar, emp_pan, emp_username, emp_pw)
                    emp_dataobj.append(obj)

                    print("Data added")
                if choice==2:
                    id_delete=input("Enter the Employee id to be deleted")
                    flag=True
                    for i in emp_dataobj:
                        if i.emp_id==id_delete:
                            emp_dataobj.remove(i)
                            print("Employee details deleted!")
                    if flag==True:
                        print("Employee id not found!!!")

                if choice==3:
                    print("Press A to update name of employee")
                    print("Press B to update address of employee")
                    print("Press C to update Date of Birth of employee")
                    print("Press D to update salary of employee")
                    ch=input("Enter your choice: ")
                    eid=input("Enter the Employee id: ")
                    for i in emp_dataobj:
                        if i.emp_id==eid:
                            if ch=="A":
                                nm=input("Enter the name to be updated: ")
                                i.emp_name=nm
                                print("name updated!!!")
                            elif ch=="B":
                                adr=input("Enter the address to be updated: ")
                                i.emp_address=adr
                                print("address updated")
                            elif ch=="C":
                                dob=input("Enter the date of birth to be updated: ")
                                i.emp_dob=dob
                                print("DOB Updated!")
                            elif ch=="D":
                                print("Press a to update salary of specific employee by Employee id")
                                print("Press b to update salary of all Employee working in specific department by 10%")
                                print("Press c to update the salary of all Employees")
                                c=input("Enter your choice: ")
                                if c=="a":
                                    eid1=input("Enter the Employee id: ")
                                    for i in emp_dataobj:
                                        if i.emp_id==eid1:
                                            i.emp_salary=float(i.emp_salary)
                                            i.emp_salary=i.emp_salary + i.emp_salary*0.1
                                            
                                            print("Salary of Employee is updated")
                                        else:
                                            print("Employee id not found!!!")

                                elif c=="b":
                                    d=input("Enter the Employee department: ")
                                    for i in emp_dataobj:
                                        if i.emp_department==d:
                                            i.emp_salary=float(i.emp_salary)
                                            i.emp_salary=i.emp_salary+i.emp_salary*0.1
                                            
                                            print("Salary of Employees belonging to ",d,"is updated")
                                        else:
                                            print("Department name not found!!!")

                                elif c=="c":
                                    for i in emp_dataobj:
                                        i.emp_salary=float(i.emp_salary)
                                        i.emp_salary=i.emp_salary+i.emp_salary*0.1
                                        print("Salary of all Employees is updated")
                                else:
                                    print("Invalid Choice!")
                            else:
                                print("Invalid Choice!")
                            
                        else:
                            print("Invalid Choice!")
                        
                if choice==4:
                    print("Press I to search by Employee id")
                    print("Press II to search by Employee name")
                    print("Press III to search by Employee Department")
                    sc=input("Enter your choice: ")
                    flag=True
                    if sc=="I":
                        e_id=(input("Enter the Employee Id you want to search: "))
                        for i in emp_dataobj:
                            if i.emp_id==e_id:
                                i.display()
                                flag=False
                        if flag==True:
                            print("Employee id not found!")
                    
                    elif sc=="II":
                        e_nm=input("Enter the Employee name to be searched: ")
                        for i in emp_dataobj:
                            if i.emp_name==e_nm:
                                i.display()
                                flag=False
                                
                        if flag==True:
                            print("Employee name not found!")
                    elif sc=="III":
                        e_dept=input("Enter the Department Name to be searched: ")
                        for i in emp_dataobj:
                            if i.emp_department==e_dept:
                                i.display()
                                flag=False
                                
                        if flag==True:
                            print("Department name not found!")
                            
                if choice==5:
                    for i in emp_dataobj:
                        i.display()
                       # i.display(emp_id,emp_name,emp_contact,emp_designation,emp_department,emp_salary, emp_doj, emp_dob, emp_age, emp_gender, emp_address,emp_state, emp_city, emp_aadhar, emp_pan, emp_username, emp_pw)
                
                sal=[]
                for i in emp_dataobj:
                    sal.append(i.emp_salary)
                max_value=max(sal)
                min_value=min(sal)

                if choice==6:
                    print("Highest Salary: ", max_value, )
                    for j in emp_dataobj:
                        if j.emp_salary==max_value:
                            j.display()
                    
                
                if choice==7:
                    print("Lowest Salary: ",min_value)
                    for j in emp_dataobj:
                        if j.emp_salary==min_value:
                            j.display()

                if choice==8:
                    if ticket:
                        print("Tickets: " , end="\n")
                    for tic,query in ticket.items():
                        print(tic,":", query, end="  ")

                if choice==9:
                    bye=1
                    break
        else:
            print("Invalid credentials!!!")
            

    elif chh=="usr":
        usrnm=input("Enter username: ")
        pwd=input("Enter password: ")
        bye=0
        if bye==1:
            break
        if usrnm in user.keys():
            while pwd==user[usrnm]:
                for i in emp_dataobj:
                    if i.username == usrnm and i.password == pwd:
                        print(i.emp_id," ",i.emp_name)
                #print("Access permitted!")
                
                while True:
                    print(end="\n")
                    print("DISPLAY to display all data")
                    print("SI to search by Employee id ")
                    print("SN to search by Employee name")
                    print("SD to search by Employee department ")
                    print("TICKET to raise a query to admin")
                    print("Press EXIT to exit")
                    ans=input("Enter your choice: ")
                    print(end="\n")
                    flag=True
                    
                    if ans=="DISPLAY":
                        for i in emp_dataobj:
                            print(i.emp_id," ",i.emp_name," ",i.emp_contact," ",i.emp_designation, " ",i.emp_department)
                    elif ans=="SI":
                        e_id=input("Enter employee ID to be searched: ")
                        for i in emp_dataobj:
                            if i.emp_id==e_id:
                                flag=False
                                print(i.emp_id," ",i.emp_name," ",i.emp_contact," ",i.emp_designation, " ",i.emp_department)
                        if flag==True:
                            print("Employee ID not found!")    
                    elif ans=="SN":
                        e_name=input("Enter employee Name to be searched: ")
                        for i in emp_dataobj:
                            if i.emp_name==e_name:
                                flag=False
                                print(i.emp_id," ",i.emp_name," ",i.emp_contact," ",i.emp_designation, " ",i.emp_department)
                        if flag==True:
                            print("Employee NAME not found!")   
                    elif ans=="SD":
                        dept=input("Enter Department to be searched: ")
                        for i in emp_dataobj:
                            if i.emp_department==dept:
                                flag=False
                                print(i.emp_id," ",i.emp_name," ",i.emp_contact," ",i.emp_designation, " ",i.emp_department)
                        if flag==True:
                            print("Employee department not found!") 
                    elif ans=="TICKET":
                        tic=input("Enter your employee id: ")
                        query=input("Enter your query: ")
                        ticket[tic]=query
                        
                    elif ans=="EXIT":
                        bye=1
                        break

                    else:
                        print("Invalid Choice!")
               
            
            

        else:
            print("Invalid Credentials!!!")
            break
    elif chh=="end":
        end=1

    else:
        print("Invalid Choice!!")
        break
       