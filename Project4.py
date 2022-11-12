import pandas as pd
import ProjectAssessment as pa

def main():
    df = pd.read_csv('Project4DataFallOnly.csv')
    df2 = pd.read_csv('Project4DataSpringOnly.csv')
    
    print("Project 4 with Fall Data")
    pa.SaveResults(df,rubricFile='RubricFallProject4.csv', outputFile='FallProject4.csv', studentFile='StudentsFallProject4.csv')
    
    combined = pd.concat([df,df2], ignore_index=True)
    print("Project 4 with All Data")
    pa.SaveResults(combined,rubricFile='RubricProject4.csv', outputFile='Project4.csv', studentFile='StudentsProject4.csv')

    print("Project 4 with Spring Data")
    pa.SaveResults(df2,rubricFile='RubricSpringProject4.csv', outputFile='SpringProject4.csv', studentFile='StudentsSpringProject4.csv')

if __name__ == '__main__':
    main()