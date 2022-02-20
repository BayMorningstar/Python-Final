def organizationtext():
    surname =[]
    name =[]
    ID = []
    file1 = open("student.txt","r",encoding="utf-8")
    for x in file1:
        a = x.split()
        ID.append(a[0])
        surname.append(a[2])
        name.append(a[1])
    file1.close()
    list1 = [ID,surname,name]
    return list1
class Student():
    def __init__(self):
        self.studentid = organizationtext()[0]
        self.studentname = organizationtext()[2]
        self.studentsurname = organizationtext()[1]
    def Studentid(self,studentnumber):
        a = self.studentid.index(studentnumber)  
        studentname = self.studentname[a]
        studentsurname = self.studentsurname[a]
        return studentname + " " + studentsurname 
def organizationanswer():
    answersheet = []
    ID = []
    booktype = []
    placements = []
    file2 = open("answer.txt","r")
    for x in file2:
        placement = []
        a = x.split()
        ID.append(a[0])
        booktype.append(a[1])
        answersheet.append(a[2])
        placement.append(a[3:])
        for x in placement:
            placements.append(x)
    file2.close()
    list2 = [ID,booktype,answersheet,placements]
    return list2
def calculationscore(studentid):
    get_info_from_organizationanswer_func = organizationanswer() #[ID,booktype,answersheet,placements]
    ID = get_info_from_organizationanswer_func[0].index(studentid)
    answersheet1 = []
    file3 = open("key.txt","r",)
    for x in file3:
        a = x.split()
        answersheet1.append(a[0])
    file3.close()
    if get_info_from_organizationanswer_func[1][ID] == "A":
        BT = 0
    if get_info_from_organizationanswer_func[1][ID] == "B":
        BT = 1
    x = 0
    a = 0
    b = 0
    c = 0
    for h in get_info_from_organizationanswer_func[2][ID]:
        if h == answersheet1[BT][x]:
            a +=1
        elif h == "-":
            b +=1
        else :
            c +=1
        x +=1
    reducenumber = a - (c/4)
    point = (a - (c/4)) * 15
    list3 = [reducenumber,point,a,b,c,get_info_from_organizationanswer_func[1][ID]]
    return list3
def Calculate_all_student_point_by_First_list():
    scorelist = []
    get_info_from_organizationtext_func = organizationtext() #[ID,surname,name]
    for studentid in get_info_from_organizationtext_func[0]:
        scorelist.append(calculationscore(studentid)[1])
    return scorelist
def Sort_Student_By_Score():
    Sorted_Score_List_by_id = []
    list_by_score = []
    get_info_from_organizationtext_func = organizationtext() #[ID,surname,name]
    First_list = Calculate_all_student_point_by_First_list()
    Sorted_Student_Point_list = First_list
    Sorted_Student_Point_list.sort(reverse=True)
    for score in Sorted_Student_Point_list:
        Find_line_by_score = First_list.index(score)
        Student_id = get_info_from_organizationtext_func[0][Find_line_by_score]
        Student_name = Student()
        Student_info = [Student_id,Student_name.Studentid(Student_id),score]
        list_by_score.append(Student_info)
        Sorted_Score_List_by_id.append(Student_id)
        Sorted_Student_Point_list.pop(Find_line_by_score)
    return [Sorted_Score_List_by_id,list_by_score]
def Key(x):
  return x[2]
def placement():
    studentinuniversity = []
    all_university_names_chosed_by_the_student = []
    universitynumber = []
    universityname = []
    universitypoint = []
    universitycapacity = []
    studentnotuniversity = []
    Student_Id_Highest_to_lowest_Score_List = Sort_Student_By_Score()[0]
    file4 = open("university.txt","r",encoding="utf-8")
    for x in file4:
        a = x.split(",")
        universitynumber.append(a[0])
        universityname.append(a[1])
        universitypoint.append(a[2])
        universitycapacity.append(int(a[3]))
    file4.close()
    organizationanswer1 = organizationanswer()
    for x in universityname:
        studentinuniversity.append([x])
    for studentid in Student_Id_Highest_to_lowest_Score_List:
        University_name_chosen_by_the_student = []
        m = 0
        n = len(organizationanswer1[3][0])
        ID = organizationanswer1[0].index(studentid)
        for x in organizationanswer1[3][ID]:
            f = universitynumber.index(x)
            University_name_chosen_by_the_student.append(universityname[f])
            if m == 0:
                    if int(universitypoint[f]) <= calculationscore(studentid)[1]:
                        if universitycapacity[f] > 0:
                            p = universitycapacity.pop(f)
                            universitycapacity.insert(f,(p-1))
                            a = Student()
                            studentinuniversity[f].append(a.Studentid(organizationanswer1[0][ID]))
                            m += 1
                            n += 1
            n = n - 1
            if n == 0:
                a = Student()
                studentnotuniversity.append(a.Studentid(organizationanswer1[0][ID]))
        all_university_names_chosed_by_the_student.append(University_name_chosen_by_the_student)
    return [studentnotuniversity,studentinuniversity,all_university_names_chosed_by_the_student,universityname,universitypoint]
def printallstudentinuniversity():
    for i in placement()[1]:
        print(i[0] ,end="\n")
        for a in i[1:]:
            print(a,end="\n")
def resulttxt():
    file4 = open("result.txt","w",encoding="utf-8")
    organizationtext1 = organizationtext()
    Get_info_from_Placement_Func = placement()[2]
    Get_info_from_Sort_Student_By_Score_func = Sort_Student_By_Score()[0] 
    for studentid in organizationtext1[0]:
        calculationscore1= calculationscore(studentid)
        ID = organizationtext1[0].index(studentid)
        Find_Line_in_Highestlist = Get_info_from_Sort_Student_By_Score_func.index(studentid)
        dataline = "ID:"+ str(organizationtext1[0][ID])+ "Name:"+ str(organizationtext1[2][ID])+ "Surname:"+ str(organizationtext1[1][ID])+ "Booktype:"+ str(calculationscore1[5])
        dataline2 = "Correct Answer:"+ str(calculationscore1[2])+ "False Answer:"+ str(calculationscore1[4])+ "Blank Answer:"+ str(calculationscore1[3])+ "Number of answers after reducing the wrong ones:"+ str(calculationscore1[0])+ "Point:"+ str(calculationscore1[1])+"University:"+"".join(Get_info_from_Placement_Func[Find_Line_in_Highestlist])
        file4.write(dataline + dataline2 + "\n")
    file4.close()
def Key1(x):
  return x[1]
def listalluniversity():
    a = []
    b = placement()[3]
    c = placement()[4]
    for x in range(len(placement()[3])):
        d  = []
        d.append(b[x])
        d.append(c[x])
        a.append(d)
    a.sort(key=Key1,reverse=True)
    return a
def listalldepertmant():
    universitydepartment1 = []
    universitydepartment2 = []
    placement1 = placement()
    for u in placement1[3]:
        a = u.split("University")
        universitydepartment1.append(a[1])
        for i in universitydepartment1:
            if i not in universitydepartment2:
                universitydepartment2.append(i)
    return universitydepartment2
def menu():
    print("----------------------------------------------------------------------")
    print("1-)Search for a student with a given id")
    print("2-)List the university/universities and departments with a maximum base points")
    print("3-)Create a file named results.txt which will have, student id, name, last name, booktype, number of correct, incorrect and blank answers, number of answers afterreducing the wrong ones based on the formula given above, score, name of theschools given as a choice")
    print("4-)List the student information (id, name, last name) sorted by their score")
    print("5-)List the students placed in every university/department. Display the name of theuniversity and the department first and then the list of students who were placeinto that department")
    print("6-)List the students who were not be able to placed anywhere")
    print("7-)List all the departments")
    print("0-)Exit")
    print("----------------------------------------------------------------------")
    p = int(input("CHOSE THE NUMBER:"))
    if p == 1:
        z = True
        x = input("please enter the your id")
        organizationtext1 = organizationtext()
        for a in organizationtext1[0]:
            if x == a:
                b = Student()
                print(b.Studentid(x))
                z = False
        if z:
            print("id not found")
        print("----------------------------------------------------------------------")
        return menu()
    if p == 2:
        for i in listalluniversity():
            print(i[0],i[1])
        print("----------------------------------------------------------------------")
        return menu()
    if p == 3:
        resulttxt()
        print("----------------------------------------------------------------------")
        return menu()
    if p == 4:
        Student_List = Sort_Student_By_Score()[1]
        for i in Student_List:
            print(i[0],i[1],i[2])
        print("----------------------------------------------------------------------")
        return menu()
    if p == 5:
        printallstudentinuniversity()
        print("----------------------------------------------------------------------")
        return menu()
    if p == 6:
        for i in placement()[0]:
            print(i,end="\n")
        print("----------------------------------------------------------------------")
        return menu()
    if p == 7:
        for i in listalldepertmant():
            print(i,end="\n")
        print("----------------------------------------------------------------------")
        return menu()   
    if  p < 1 or p > 7:
        print("please choise a number")
        print("----------------------------------------------------------------------")
        return menu()
print(Sort_Student_By_Score()[0])