if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()  ## *line stores rest  of parts
        scores = list(map(float, line)) # map(float,) it applies float to each element of in list Line
        student_marks[name] = scores # [name] is key in dictionary, scores is value associated with key in dictinoary
    query_name = input() 
    
    sum1 = (sum(student_marks[query_name])/3)
    print(f"{sum1:.2f}")


# Task
# The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example
# marks key: value pairs are
# ‘alpha’:[20, 30, 40]
# ‘beta’:[30, 50, 70]
# query_name = ‘beta’
# The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.
