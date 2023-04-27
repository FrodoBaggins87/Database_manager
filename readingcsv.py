#for reading csv and storing in classes
import csv
import threading
import time
temp=0
allpeople=[]
#Defining the classes required
class departments:
    def __init__(self,form_date):
        self.formation_date=form_date
    def __str__ (self):
        return f'departments({self.formation_date})'
    def date_of_formation(self):
        return self.formation_date

class people:
    def __init__(self,n,g,dept):
        self.name=n
        self.gender=g
        self.department=dept
        allpeople.append(n)
#Students and teachers classes inherited under people

class students(people):
    def __init__(self, n, g, dept):
        super().__init__(n, g, dept)


class teachers(people):
    def __init__(self, n, g, dept):
        super().__init__(n, g, dept)

#Reading the file
with open("university_records.csv", mode ='r') as file:
    
# reading the CSV file
    csvfile = csv.reader(file)
    
    fields=next(csvfile)
    for row in csvfile:
        if row==[]:
            temp=temp+1
            continue
        elif row[0]=='Name':
            continue
        else:
            if temp==0:
                globals()[row[0]]=departments(int(row[1])) #Constructing the departments class
            elif temp==1:
                globals()[row[0].replace(" ","")]=teachers(row[0], row[1], row[3]) #Contructing Teachers class
                globals()[row[0].replace(" ","")].hod= row[2]
                globals()[row[0].replace(" ","")].join_year= row[4]
            elif temp==2:
                globals()[row[0].replace(" ","")]=students(row[0], row[1], row[3]) #Constructing students class
                globals()[row[0].replace(" ","")].yob= int(row[2])
                globals()[row[0].replace(" ","")].roll= int(row[4])
                globals()[row[0].replace(" ","")].batch= int(row[5])
                globals()[row[0].replace(" ","")].join_year= int(row[6])
                globals()[row[0].replace(" ","")].alumni_status= row[7]
            elif temp==3:
                globals()[row[0].replace(" ","")].SGPA1= float(row[2])
                globals()[row[0].replace(" ","")].SGPA2= float(row[3])
                globals()[row[0].replace(" ","")].SGPA3= float(row[4])
                globals()[row[0].replace(" ","")].SGPA4= float(row[5])
                globals()[row[0].replace(" ","")].SGPA5= float(row[6])
                globals()[row[0].replace(" ","")].SGPA6= float(row[7])
                globals()[row[0].replace(" ","")].SGPA7= float(row[8])
                globals()[row[0].replace(" ","")].SGPA8= float(row[9])
                globals()[row[0].replace(" ","")].SGPA9= float(row[10])
                globals()[row[0].replace(" ","")].SGPA10= float(row[11])
            #added student marks here

def formation_year(dep):
    dep=globals()[dep]
    print(dep.date_of_formation())

def student_or_teacher(name):
    tempsa=globals()[name.replace(" ","")]
    if isinstance(tempsa,students)==True:
        print(name,'is a student')
    elif isinstance(tempsa,teachers)==True:
        print(name,'is a teachers')
    else:
        print(name,'does not belong in the database')

def department_members(dep, pos='all'):
    if pos=='students':
        for person in allpeople:
            tempsb=globals()[person.replace(" ","")]
            if isinstance(tempsb,students)==True:
                if tempsb.department==dep:
                    print(tempsb.name)
    elif pos=='teachers':
        for person in allpeople:
            tempsb=globals()[person.replace(" ","")]
            if isinstance(tempsb,teachers)==True:
                if tempsb.department==dep:
                    print(tempsb.name)
    elif pos=='all':
        for person in allpeople:
            tempsb=globals()[person.replace(" ","")]
            if tempsb.department==dep:
                print(tempsb.name)
    else:
        print('Invalid input: Put first input as name of department and second input as "students", "teachers", or "all" ')

def Year_of_Joining(name):
    name=globals()[name.replace(" ","")]
    print(name.join_year)

def list_hod(dept):
    for person in allpeople:
        tempsc=globals()[person.replace(" ","")]
        if isinstance(tempsc,teachers)==True and tempsc.department==dept and tempsc.hod==True:
                print(tempsc.name)

def students_in_batch(bat):
    for person in allpeople:
        tempsd=globals()[person.replace(" ","")]
        if isinstance(tempsd,students)==True and tempsd.batch== bat:
            print(tempsd.name)

def alumni(dept='all'):
    if dept=='all':
        for person in allpeople:
            tempse=globals()[person.replace(" ","")]
            if isinstance(tempse,students)==True and tempse.alumni_status==True:
                print(tempse.name)
    else:
        for person in allpeople:
            tempse=globals()[person.replace(" ","")]
            if isinstance(tempse,students)==True and tempse.dapartment== dept and tempse.alumni_status==True:
                print(tempse.name)

def student_from_roll_no(rolln):
    for person in allpeople:
        tempsf=globals()[person.replace(" ","")]
        if isinstance(tempsf,students)==True and tempsf.roll==int(rolln):
            print(tempsf.name)

def persons_from_gender(gend,dept='all',pers='all'):
    if dept=='all' and pers=='all':
        for person in allpeople:
            tempsg=globals()[person.replace(" ","")]
            if tempsg.gender==gend:
                print(tempsg.name)
    elif dept=='all' and pers=='students':
        for person in allpeople:
            tempsg=globals()[person.replace(" ","")]
            if tempsg.gender==gend and isinstance(tempsg,students)==True:
                print(tempsg.name)
    elif dept=='all' and pers=='teachers':
        for person in allpeople:
            tempsg=globals()[person.replace(" ","")]
            if tempsg.gender==gend and isinstance(tempsg,teachers)==True:
                print(tempsg.name)
    elif pers=='students':
        for person in allpeople:
            tempsg=globals()[person.replace(" ","")]
            if tempsg.gender==gend and tempsg.department==dept and isinstance(tempsg,students)==True:
                print(tempsg.name)
    elif pers=='teachers':
        for person in allpeople:
            tempsg=globals()[person.replace(" ","")]
            if tempsg.gender==gend and tempsg.department==dept and isinstance(tempsg,teachers)==True:
                print(tempsg.name)
    else:
        print("input 'male' or 'female' in gender and correct department name in second input or leave it blank and 'students' or 'teachers' in third input or leave it blank")

def CGPA(stu):
    print(round(((globals()[stu.replace(" ","")].SGPA1 + globals()[stu.replace(" ","")].SGPA2 + globals()[stu.replace(" ","")].SGPA3+ globals()[stu.replace(" ","")].SGPA4 + globals()[stu.replace(" ","")].SGPA5 + globals()[stu.replace(" ","")].SGPA6 + globals()[stu.replace(" ","")].SGPA7 + globals()[stu.replace(" ","")].SGPA8 + globals()[stu.replace(" ","")].SGPA9 + globals()[stu.replace(" ","")].SGPA10)/10.),2))

def Pass_or_Fail(stu):
    if globals()[stu.replace(" ","")].SGPA1>=5.0 and globals()[stu.replace(" ","")].SGPA2>=5.0 and globals()[stu.replace(" ","")].SGPA3>=5.0 and globals()[stu.replace(" ","")].SGPA4>=5.0 and globals()[stu.replace(" ","")].SGPA5>=5.0 and globals()[stu.replace(" ","")].SGPA6>=5.0 and globals()[stu.replace(" ","")].SGPA7>=5.0 and globals()[stu.replace(" ","")].SGPA8>=5.0 and globals()[stu.replace(" ","")].SGPA9>=5.0 and globals()[stu.replace(" ","")].SGPA10>=5.0:
        print(globals()[stu.replace(" ","")].name, "has passed in all the semesters.")
    else: 
        print(globals()[stu.replace(" ","")].name, "has failed in one or more of the semesters")

        
#Calling functions one by one from code

#formation_year(department)
#student_or_teacher(name)
#department_members(department,position)
#Year_of_Joining(name)
#list_hod(department)
#students_in_batch(batch)
#alumni(department)
#student_from_roll_no(roll_no)
#persons_from_gender(gend,dept,person)
#CGPA(student)
#Pass_or_Fail(student)


#Remove the required function thread from comment according to need and put suitable input

#t1 = threading.Thread (target = formation_year, args = (department,))
#t2 = threading.Thread (target = student_or_teacher, args = (name,))
#t3 = threading.Thread (target = department_members, args = (department, position,))
#t4 = threading.Thread (target = Year_of_Joining, args = (name,))
#t5 = threading.Thread (target = list_hod, args = (department,))
#t6 = threading.Thread (target = students_in_batch, args = (batch,))
#t7 = threading.Thread (target = alumni, args = (department,))
#t8 = threading.Thread (target = student_from_roll_no, args = [700006])
#t9 = threading.Thread (target = persons_from_gender, args = (gend,dept,person,))
#t10 = threading.Thread (target = CGPA, args = ['Carol Schrader'])
#t11 = threading.Thread (target = Pass_or_Fail, args = (student,))


# start the required function's thread from comment 


#t1.start()
#time.sleep(0.4)
#t2.start()
#time.sleep(0.4)
#t3.start()
#time.sleep(0.4)
#t4.start()
#time.sleep(0.4)
#t5.start()
#time.sleep(0.4)
#t6.start()
#time.sleep(0.4)
#t7.start()
#time.sleep(0.4)
#t8.start()
#time.sleep(0.4)
#t9.start()
#time.sleep(0.4)
#t10.start()
#time.sleep(0.4)
#t11.start()


# join the required function's threads to the main thread


#t1.join()
#t2.join()
#t3.join()
#t4.join()
#t5.join()
#t6.join()
#t7.join()
#t8.join()
#t9.join()
#t10.join()
#t11.join()

#taking user input from command line

func_list=['formation_year', 'student_or_teacher', 'department_members', 'Year_of_Joining', 'list_hod', 'students_in_batch', 'alumni', 'student_from_roll_no', 'persons_from_gender', 'CGPA', 'Pass_or_Fail']
user_request=input("Enter name of the functions you want to use with the respective required inputs in brackets(same function can be called more than once), for using multiple functions, use '|' as the separator. Available functions are formation_year(department), student_or_teacher(name), department_members(department,position(optional argument)), Year_of_Joining(name), list_hod(department), students_in_batch(batch), alumni(department), student_from_roll_no(roll_no), persons_from_gender(gend,dept(optional argument),position(optional argument)),CGPA(student), Pass_or_Fail(student)\n")
needed_funcs=user_request.split('|')
thread_list=[]
for inp in needed_funcs:
    temp=inp.partition('(') 
    name_of_func=temp[0].lower().replace(" ","").replace("_","")
    arguments_list=temp[2][:-1].split(',')
    for a in arguments_list:
        a.strip()
    for func in func_list:
        if func.lower().replace(" ","").replace("_","")==name_of_func:
            thread_list.append(threading.Thread (target = globals()[func], args = arguments_list))
if len(thread_list)==0:
    print("Wrong name of the functions")
else: 
    for i in range(0,len(thread_list)):
        thread_list[i].start()
        time.sleep(0.3)
    for j in range(0,len(thread_list)):
        thread_list[j].join()
