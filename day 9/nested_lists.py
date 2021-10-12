if __name__ == '__main__':
    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        student_grades.append([name, score])
        
    #new list containing the scores only
    scores = [el[1] for el in student_grades]
    #remove duplicate scores
    score_set = set(scores)
    #convert to a list of unique scores
    unique_scores = list(score_set)

    #find minimum score
    lowest = min(unique_scores)
    #remove min score to get min-score
    unique_scores.remove(lowest)
    
    #sort alphabetically
    student_grades.sort()
    
    for i in student_grades:
        lowest2 = min(unique_scores)
        if i[1] == lowest2:
            print(i[0])