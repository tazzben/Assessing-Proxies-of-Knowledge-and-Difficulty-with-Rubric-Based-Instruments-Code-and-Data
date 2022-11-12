import pandas as pd
from scipy.stats import mannwhitneyu, ttest_rel


def main():
    data = pd.read_csv("StudentsProjects14.csv")
    project4 = data[data['Variable'].astype(str).str[-2:] == "_4"]
    project1 = data[data['Variable'].astype(str).str[-2:] != "_4"]
    U1, p = mannwhitneyu(project1["Average Logistic"].to_list(), project4["Average Logistic"].to_list())
    print("MW Test")
    print(U1)
    print(p)
    print("TTEST")
    t, p = ttest_rel(project1["Average Logistic"].to_list(), project4["Average Logistic"].to_list())
    print(t)
    print(p)
    U1, p = mannwhitneyu(project1["Average Marginal Logistic"].to_list(), project4["Average Marginal Logistic"].to_list())
    print("MW Test Marginal")
    print(U1)
    print(p)
    print("TTEST Marginal")
    t, p = ttest_rel(project1["Average Marginal Logistic"].to_list(), project4["Average Marginal Logistic"].to_list())
    print(t)
    print(p)
    print("Marginal Means")
    print(project1["Average Marginal Logistic"].mean())
    print(project4["Average Marginal Logistic"].mean())
    print("Logistic Means")
    print(project1["Average Logistic"].mean())
    print(project4["Average Logistic"].mean())

if __name__ == '__main__':
    main()