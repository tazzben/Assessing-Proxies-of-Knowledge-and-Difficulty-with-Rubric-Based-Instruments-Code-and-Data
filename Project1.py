import pandas as pd
import ProjectAssessment as pa

def main():
    df = pd.read_csv('Project1DataFallOnly.csv')
    df2 = pd.read_csv('Project1DataSpringOnly.csv')
    
    print("Project 1 with Fall Data")
    pa.SaveResults(df,rubricFile='RubricFallProject1.csv', outputFile='FallProject1.csv', studentFile='StudentsFallProject1.csv')
    
    combined = pd.concat([df,df2], ignore_index=True)
    print("Project 1 with All Data")
    pa.SaveResults(combined,rubricFile='RubricProject1.csv', outputFile='Project1.csv', studentFile='StudentsProject1.csv')

    print("Project 1 with Spring Data")
    pa.SaveResults(df2,rubricFile='RubricSpringProject1.csv', outputFile='SpringProject1.csv', studentFile='StudentsSpringProject1.csv')

if __name__ == '__main__':
    main()