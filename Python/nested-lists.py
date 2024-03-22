# Ubaydullo Asatullaev
# ubaydullohazard@gmail.com

if __name__ == '__main__':
    students = []  # empty lists
    scores=[]
    for _ in range(int(input())):
        name = input() 
        score = float(input())
        student = [name, score] 
        students.append(student)  # sort unique scores in ascending order
        scores.append(score) 
    secondlowg = sorted(set(scores))[1]  # select second element from sorted list
    output = sorted([student[0] for student in students if student[1] == secondlowg])   # list, stores student name which student score equal secondlowg, loop goes through each item of in students list.
    
    print("\n".join(output))  
    #"".join() - it takes list, and joins them into single string, and places "" between each element.and
    
    
    # for name in output:
    #     print(name)
        

# Problem
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
