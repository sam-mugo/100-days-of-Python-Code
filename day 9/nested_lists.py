if __name__ == '__main__':
    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        student_grades.append([name, score])
        
        
    scores = [el[1] for el in student_grades]
    score_set = set(scores)
    unique_scores = list(score_set)

    lowest = min(unique_scores)
    unique_scores.remove(lowest)
    
    student_grades.sort()
    for i in student_grades:
        lowest2 = min(unique_scores)
        if i[1] == lowest2:
            print(i[0])