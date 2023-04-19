import os
import glob
import os.path


class admin:
    def __init__(self):#constructor
        self

    def Addfile(self):  # adding a new record method
        st_id = (input("Enter new student id") + ".txt")
        try:
            save_path = 'C:/Users/Administrator/OneDrive/سطح المكتب/records/'
            completeName = os.path.join(save_path,st_id)  
            f = open(completeName, 'w')
            print("Student is added successfully!")
            f.close()
        except FileExistsError:
            print("Error: student id is already exists")

    def AddSemester(self):  # adding new semester method
        st_id = (input("Enter student id") + ".txt")
        save_path = 'C:/Users/Administrator/OneDrive/سطح المكتب/records/'
        completeName = os.path.join(save_path, st_id)
        with open(completeName, "a+") as f:
            st_sem = input("Enter the new semester year")
            for line in f:
                tokens = line.split(";")  # because ';' is seperating the data in the same line
                st_sem.strip(" ")  # for easier comparing
                tokens[0].strip(" ")  # also for easier comparing and tokens[0] is always for semester year
                if (st_sem == tokens[0]):
                    print("Error: semester is already here")
                    quit()  # quitting the program
            status = True
            new = []
            while (status == True):  # it won't reach this point unless the semester is not exist in the file 

                course = input(
                        "enter course and grade and seperate them with ':' ,Note:'if you are done enter 'done''")
                if (course.lower() == 'done'):
                    status = False
                else:
                    course.upper()
                    new.append(course)
            text = st_sem + ";"
            for i in range(0, len(new)):
                text = text + new[i] + ";"
            text=text+"\n" #to write in a new line
            f.write(text)
            
            print("Addition completed successfully!")
            f.close

    def Update(self):  # update data method
        st_id = (input("Enter student id ") + ".txt")
        save_path = 'C:/Users/Administrator/OneDrive/سطح المكتب/records/'
        completeName = os.path.join(save_path, st_id)
        with open(completeName, 'r+') as f:
            st_old = input("Enter course name you want to update ")
            for line in f:
                data = line
                tokens = data.split(";")
                for i in range(1, len(tokens)):  # because tokens[0] is for semester year (it is not important here)
                    temp1 = st_old.strip(" ").upper()  # for easier comparing
                    tokens2 = tokens[i].split(":")
                    temp2 = tokens2[0].strip(" ").upper()  # also for easier comparing
                    if (temp1 == temp2):
                        new = input("Enter new grade: ")
                        f.write(data.replace(tokens2[1],new))
                        print("Update is done!")
              
            f.close()

    def statistics(self):
        st_id = (input("Enter student id") + ".txt")
        save_path = 'C:/Users/Administrator/OneDrive/سطح المكتب/records/'
        completeName = os.path.join(save_path, st_id)
        courses = {"ENCS2110": int(1), "ENCS2340": int(3), "ENCS2380": int(3), "ENCS3130": int(1),
                   "ENCS3310": int(3), "ENCS3320": int(3), "ENCS3330": int(3), "ENCS3340": int(3),
                   "ENCS3390": int(3), "ENCS4110": int(1), "ENCS4130": int(1), "ENCS4210": int(2),
                   "ENCS4300": int(3), "ENCS4310": int(3), "ENCS4320": int(3), "ENCS4330": int(3),
                   "ENCS4370": int(3), "ENCS4380": int(3), "ENCS5140": int(1), "ENCS5150": int(1),
                   "ENCS5200": int(2), "ENCS5300": int(3), "ENEE2103": int(1), "ENEE2304": int(3),
                   "ENEE2307": int(3), "ENEE2312": int(3), "ENEE2360": int(3), "ENEE3309": int(3),
                   "ENEE4113": int(1)
                   }
        allhours = int(69)
        with open(completeName, 'r') as f:
            hourstaken =int(0)
            sum = 0
            counter = 0
            remaining = ["ENCS2110", "ENCS2340", "ENCS2380", "ENCS3130",
                         "ENCS3310", "ENCS3320", "ENCS3330", "ENCS3340",
                         "ENCS3390", "ENCS4110", "ENCS4130", "ENCS4210",
                         "ENCS4300", "ENCS4310", "ENCS4320", "ENCS4330",
                         "ENCS4370", "ENCS4380", "ENCS5140", "ENCS5150",
                         "ENCS5200", "ENCS5300", "ENEE2103", "ENEE2304",
                         "ENEE2307", "ENEE2312", "ENEE2360", "ENEE3309",
                         "ENEE4113"]
            temp=["ENCS2110", "ENCS2340", "ENCS2380", "ENCS3130",
                         "ENCS3310", "ENCS3320", "ENCS3330", "ENCS3340",
                         "ENCS3390", "ENCS4110", "ENCS4130", "ENCS4210",
                         "ENCS4300", "ENCS4310", "ENCS4320", "ENCS4330",
                         "ENCS4370", "ENCS4380", "ENCS5140", "ENCS5150",
                         "ENCS5200", "ENCS5300", "ENEE2103", "ENEE2304",
                         "ENEE2307", "ENEE2312", "ENEE2360", "ENEE3309",
                         "ENEE4113"]
            for line in f:
                tokens = line.split(";")
                localsum = 0
                localcounter = 0
                for i in range(1, len(tokens)):
                    token2 = tokens[i].split(":")
                    token2[0]=str(token2[0])
                    for x in range(0,len(remaining)):
                        if(token2[0] == remaining[x]):
                            temp.remove(remaining[x])
                    num=courses.get(token2[0])
                    hourstaken = hourstaken + int(num) # to get hours taken
                    localsum = localsum + float(token2[1])
                    localcounter = localcounter + 1
                    sum = sum + float(token2[1])
                    counter = counter + 1
                localaverage = localsum / localcounter
                print("Average for semester " + tokens[0] + " is " + localaverage)
            
            average = sum / counter
            print("Avargae all times is " + average)
            print("Finished hours=" + (allhours - hourstaken))
            print("Remaining courses are:" + temp)

    def Global(self):
        counter =0 # to get students' number
        sum = 0
        courses = {"ENCS2110": int(1), "ENCS2340": int(3), "ENCS2380": int(3), "ENCS3130": int(1),
                   "ENCS3310": int(3), "ENCS3320": int(3), "ENCS3330": int(3), "ENCS3340": int(3),
                   "ENCS3390": int(3), "ENCS4110": int(1), "ENCS4130": int(1), "ENCS4210": int(2),
                   "ENCS4300": int(3), "ENCS4310": int(3), "ENCS4320": int(3), "ENCS4330": int(3),
                   "ENCS4370": int(3), "ENCS4380": int(3), "ENCS5140": int(1), "ENCS5150": int(1),
                   "ENCS5200": int(2), "ENCS5300": int(3), "ENEE2103": int(1), "ENEE2304": int(3),
                   "ENEE2307": int(3), "ENEE2312": int(3), "ENEE2360": int(3), "ENEE3309": int(3),
                   "ENEE4113": int(1)
                   }

        semSum = {}  # summation of all hours in semesters
        for filename in glob.glob('*.txt'):
            counter = counter + 1
            with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                hourstaken = 0
                localsum = 0
                localcounter = 0  # to get average for a student in all times
                for line in f:
                    tokens = line.split(";")

                    for i in range(1, len(tokens)):  # because 0 is for semester year
                        token2 = tokens[i].split(":")
                        token2[0].strip(" ").upper()
                        hourstaken = int(hourstaken + courses.get(token2[0]))  # to get hours taken
                        localsum = localsum + float(token2[1])
                        localcounter = localcounter + 1

                    if (semSum.has_key(tokens[0])):
                        temp = semSum.get(tokens[0]).split("#")#because in semSum={sem year: summation of hours#number of students , ...}
                        semSum[tokens[0]] = int(temp[0] + hourstaken) + "#" + int(
                            temp[1] + 1)  # if semester year is in semSum then add taken hours to its value
                    else:
                        semSum[tokens[0]] = int(hourstaken) +"#"+ int(1)  # if not then add it and put the value of taken hours 

                    localaverage = localsum / localcounter #for this semster and this student
                    sum = sum + localaverage
        average = sum / counter
        print("Overall students average=" + average)
        x = 0 
        for x in range(0, len(semSum)):
                    sem_list = list(semSum.keys())
                    value_list = list(semSum.values())
                    temp2 = value_list[x].split("#")
                    avgHours = temp2[0] / temp2[1]
                    print("Average hours for semester " + sem_list[x] + " is=" + avgHours)
        return "Operations done successfully!"

    def SearchAvg(self):
        op= input("Enter option: ")
        if (op == '1'):
            avg = input("Enter average: ")
            result = []
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                    sum = 0
                    counter = 0
                    for line in f:
                        tokens = line.split(";")
                        for i in range(1, len(tokens)):  # because 0 is for semester year
                            token2 = tokens[i].split(":")
                            sum = sum + float(token2[1])
                            counter = counter + 1
                        average = sum / counter
                        if (average > avg):
                            result.append(f.name + ", average=" + average)
                            print("Students that have average greater than " + avg + " are:" + result)
        elif (op == '2'):
            avg = input("Enter average: ")
            result = []
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                    sum = 0
                    counter = 0
                    for line in f:
                        tokens = line.split(";")
                        for i in range(1, len(tokens)):  # because 0 is for semester year
                            token2 = tokens[i].split(":")
                            sum = sum + float(token2[1])
                            counter = counter + 1
                        average = sum / counter
                        if (average < avg):
                            result.append(f.name + ", average=" + average)
                    print("Students that have average less than " + avg + " are:" + result)
        elif (op == '3'):
            avg = input("Enter average: ")
            result = []
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                    sum = 0
                    counter = 0
                    for line in f:
                        tokens = line.split(";")
                        for i in range(1, len(tokens)):  # because 0 is for semester year
                            token2 = tokens[i].split(":")
                            sum = sum + float(token2[1])
                            counter = counter + 1
                        average = sum / counter
                        if (average == avg):
                            result.append(f.name + ", average=" + average)
            print("Students that have the average " + avg + " are:" + result)
        else:
            print("Error: wrong option")

    def SearchH():
        op= input("Enter option: ")
        courses = {"ENCS2110": int(1), "ENCS2340": int(3), "ENCS2380": int(3), "ENCS3130": int(1),
                   "ENCS3310": int(3), "ENCS3320": int(3), "ENCS3330": int(3), "ENCS3340": int(3),
                   "ENCS3390": int(3), "ENCS4110": int(1), "ENCS4130": int(1), "ENCS4210": int(2),
                   "ENCS4300": int(3), "ENCS4310": int(3), "ENCS4320": int(3), "ENCS4330": int(3),
                   "ENCS4370": int(3), "ENCS4380": int(3), "ENCS5140": int(1), "ENCS5150": int(1),
                   "ENCS5200": int(2), "ENCS5300": int(3), "ENEE2103": int(1), "ENEE2304": int(3),
                   "ENEE2307": int(3), "ENEE2312": int(3), "ENEE2360": int(3), "ENEE3309": int(3),
                   "ENEE4113": int(1)
                   }

        if (op == '1'):
            hour = input("Enter hours: ")
            result = []
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                    hourstaken = 0
                    for line in f:
                        tokens = line.split(";")
                        for i in range(1, len(tokens)):
                            tokens2 = tokens[i].split(":")
                            tokens2[0].strip(" ").upper()
                            hourstaken = int(hourstaken + courses.get(tokens2[0]))
                        if (hourstaken > hour):
                            result.append(f.name + ", taken hours=" + hourstaken)
                    print("Students that have taken hours more than " + hour + " are:" + result)
        elif (op == '2'):
            hour = input("Enter hours: ")
            result = []
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                    hourstaken = 0
                    for line in f:
                        tokens = line.split(";")
                        for i in range(1, len(tokens)):
                            tokens2 = tokens[i].split(":")
                            tokens2[0].strip(" ").upper()
                            hourstaken = int(hourstaken + courses.get(tokens2[0]))
                        if (hourstaken < hour):
                            result.append(f.name + ", taken hours=" + hourstaken)
                    print("Students that have taken hours less than " + hour + " are:" + result)
        elif (op == '3'):
            hour = input("Enter hours: ")
            result = []
            for filename in glob.glob('*.txt'):
                with open(os.path.join(os.getcwd('C:/Users/Administrator/OneDrive/سطح المكتب/records/'), filename), 'r') as f:
                    hourstaken = 0
                    for line in f:
                        tokens = line.split(";")
                        for i in range(1, len(tokens)):
                            tokens2 = tokens[i].split(":")
                            tokens2[0].strip(" ").upper()
                            hourstaken = int(hourstaken + courses.get(tokens2[0]))
                        if (hourstaken == hour):
                            result.append(f.name + ", taken hours=" + hourstaken)
                    print("Students that have taken hours equals " + hour + " are:" + result)
        else:
            print("Error: wrong option")


class student(admin):

    def __init__(self):
        self
    


user = input("Enter Type Of User (Student Or Admin):")
if (user.lower() == "admin"):
    print("==========Menu=========")
    print("[1]Add a new record file")
    print("[2]Add new semester with student courses and grades")
    print("[3]Update data")
    print("[4]Student statistics")
    print("[5]Global statistics")
    print("[6]Search")
    option = input("Enter option ")
    status = False
    if (option == '1'):
        ad1 = admin()
        ad1.Addfile()
    elif (option == '2'):
        ad2 = admin()
        ad2.AddSemester()
    elif (option == '3'):
        ad3 = admin()
        ad3.Update()
    elif (option == '4'):
        ad4 = admin()
        ad4.statistics()
    elif (option == '5'):
        print("Here's the global statistics:")
        ad5 = admin()
        ad5.Global()
    elif (option == '6'):
        print("You can search for these:")
        print("[1]Based on average")
        print("[2]Based on taken hours")
        option2 = input("Enter option: ")
        if (option2 == '1'):
            print("[1]Averages greater than .....")
            print("[2]Averages less than ........")
            print("[3]Average equals ............")
            ad6 = admin()
            ad6.SearchAvg()
        elif (option2 == '2'):
            print("[1]Taken hours greater than ......")
            print("[2]Taken hours less than .........")
            print("[3]Taken hours equals ............")
            ad7 = admin()
            ad7.SearchH()
    else:
        print("Error: option is not in the menu")

elif (user.lower() == "student"):
    print("==========Menu=========")
    print("[1]Student statistics:")
    print("[2]Global statistics")
    option = input("Enter option: ")
    if (option == '1'):
        st1 = student()
        st1.statistics()
    elif (option == '2'):
        print("Here's the global statistics:")
        st2 = student()
        st2.Global()
    else:
        print("Error: wrong option")
else:
    print("Error: invalid input")