def gradingStudents(grades):
    ngrade=[]
    for i in grades:
        if i%5>=3 and i>35:ngrade.append(i+(5-(i%5)))
        else:ngrade.append(i)
    return ngrade

            
