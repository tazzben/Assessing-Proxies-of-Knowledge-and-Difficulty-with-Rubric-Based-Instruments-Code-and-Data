import pandas as pd
import ProjectAssessment as pa

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def main():
    df = pd.read_csv('Project1DataFallOnly.csv')
    df2 = pd.read_csv('Project1DataSpringOnly.csv')
    df3 = pd.read_csv('Project4DataFallOnly.csv')
    df4 = pd.read_csv('Project4DataSpringOnly.csv')
    project1 = pd.concat([df,df2], ignore_index=True)
    project4 = pd.concat([df3,df4], ignore_index=True)
    students1 = project1['student'].unique().tolist()
    students4 = project4['student'].unique().tolist()
    students = intersection(students1, students4)
    project1 = project1[project1['student'].isin(students)]
    project4 = project4[project4['student'].isin(students)]
    project1['student'] = project1['student'].astype(str)
    project4['student'] = project4['student'].astype(str)
    project4['student'] = project4['student'].apply(lambda x: x + "_4")
    combined = pd.concat([project1,project4], ignore_index=True)
    combined = combined[combined['rubric'].isin([1,6,7])]
    print("Common Rubric Items for Project 1 and 4")
    pa.SaveResults(combined,rubricFile='RubricProjects14.csv', outputFile='Projects14.csv', studentFile='StudentsProjects14.csv')


if __name__ == '__main__':
    main()