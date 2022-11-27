from time import process_time
import pandas as pd
import ProjectAssessment as pa
import numpy as np

def main():
    df = pd.read_csv('Project1DataFallOnly.csv')
    df2 = pd.read_csv('Project1DataSpringOnly.csv')
    combined = pd.concat([df,df2], ignore_index=True)
    
    # Warm up so that njit doesn't have to compile for the first run  
    ids = combined['student'].unique().flatten().tolist()
    randomGroupIds = np.random.choice(ids, size=3, replace=False)
    s = []
    for _, i in enumerate(randomGroupIds):
        rows = combined[combined['student']==i]
        s.append(rows)
    resultData = pd.concat(s, ignore_index=True)
    pa.DisplayResults(resultData)
 
    # Start real run timing ProjectAssessment
    numStudents = [3, 5, 10, 15, 20, 25, 35, 45, 55, 65, 75, 85, 100, 115, 130, 150]
    l = []
    for num in numStudents:
        ids = combined['student'].unique().flatten().tolist()
        randomGroupIds = np.random.choice(ids, size=num, replace=False)
        s = []
        for _, i in enumerate(randomGroupIds):
            rows = combined[combined['student']==i]
            s.append(rows)
        resultData = pd.concat(s, ignore_index=True)
        t1_start = process_time() 
        print("Project 1 with " + str(num) + " Students")
        pa.DisplayResults(resultData)
        t1_end = process_time()
        tdelta = t1_end-t1_start
        l.append(tdelta)
    d = pd.DataFrame({
        'Number of Students': numStudents,
        'Time': l
    })
    d.to_csv('Project1Time.csv')

if __name__ == '__main__':
    main()