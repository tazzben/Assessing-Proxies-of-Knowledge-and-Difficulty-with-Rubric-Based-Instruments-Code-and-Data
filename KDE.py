import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

CalculateDistance = lambda x, y: np.abs(x-y)
EpanechnikovWeight = lambda d: (3/4)*(1-np.power(d,2))
Silvermans = lambda x: (np.power((4*np.power(x.std(),5))/(3*x.count()),1/5))*1.5


def CalculateKDE(x, data, bandwidth):
    subsample = data.loc[((x-bandwidth) <= data) & (data <= (x+bandwidth))]
    n = data.count()
    if subsample.count()>0:
        normalizedsubsample = subsample.apply(func=CalculateDistance, args=(x,))/(bandwidth)
        density = (1/(n*bandwidth))*normalizedsubsample.apply(func=EpanechnikovWeight).sum()
        return density
    else:
        return 0

def RunKDE(bandwidth, data, marginal = False):
    if marginal:
        xinterval = np.linspace(-0.5, 0.5, 1000).tolist()
    else:
        xinterval = np.linspace(0, 1, 1000).tolist()
    yprojections = [CalculateKDE(x, data, bandwidth) for x in xinterval]
    return (xinterval, yprojections)


def ManageKDEProcess(bandwidth, data, marginal = False):
    xinterval, yprojections = RunKDE(bandwidth, data, marginal)
    return xinterval, yprojections

def CreateCompareKDEPlots():
    data = pd.read_csv("StudentsProjects14.csv")
    project4 = data[data['Variable'].astype(str).str[-2:] == "_4"]
    project1 = data[data['Variable'].astype(str).str[-2:] != "_4"]
    bandwidths = [3*Silvermans(project1["Average Logistic"]), 3*Silvermans(project4["Average Logistic"])]
    dataset = [project1["Average Logistic"],project4["Average Logistic"]]
    labels = ['Project 1', 'Project 4']
    linetypes = ['-','--']
    r = []
    for index, d in enumerate(dataset):
        r.append(ManageKDEProcess(bandwidths[index], d))
    plt.figure()
    # plt.xlim(0,1)
    ax = plt.axes()
    ax.set_ylabel('Density')
    ax.set_xlabel(r'Average Probability of Failure ($p(q_j,s_i)$)')
    for index, result in enumerate(r):
        xinterval, yprojections = result
        ax.plot(xinterval, yprojections, label=labels[index], color='black', linestyle=linetypes[index])
    plt.vlines(project1["Average Logistic"].mean(), 0, 2.5, color='black', linestyles='-')
    plt.vlines(project4["Average Logistic"].mean(), 0, 2.5, color='black', linestyles='--')
    ax.legend()
    plt.savefig('KDECompareCurve.pdf')

def ProjectKDEPlot(data, filename, h=2.5, marginal = False):
    if marginal:
        subdata = data["Average Marginal Logistic"]
    else:
        subdata = data["Average Logistic"]
    bandwidths = [2*Silvermans(subdata),]
    dataset = [subdata,]
    labels = ['Project 1', ]
    linetypes = ['-',]
    r = []
    for index, d in enumerate(dataset):
        r.append(ManageKDEProcess(bandwidths[index], d, marginal))
    plt.figure()
    ax = plt.axes()
    ax.set_ylabel('Density')
    if marginal:
        ax.set_xlabel(r'Average Change in Probability of Failure ($p_i(q_j,s_i)$)')
    else:
        ax.set_xlabel(r'Average Probability of Failure ($p(q_j,s_i)$)')
    for index, result in enumerate(r):
        xinterval, yprojections = result
        ax.plot(xinterval, yprojections, label=labels[index], color='black', linestyle=linetypes[index])
    plt.vlines(subdata.mean(), 0, h, color='black', linestyles='-')
    print(subdata.mean())
    # ax.legend()
    plt.savefig(filename)


def main():
#    CreateCompareKDEPlots()
    ProjectKDEPlot(pd.read_csv("StudentsProject1.csv"),'KDEProject1Curve.pdf',2.5)
    ProjectKDEPlot(pd.read_csv("StudentsProject1.csv"),'KDEChangeProject1Curve.pdf',5, True)
    ProjectKDEPlot(pd.read_csv("StudentsFallProject1.csv"),'KDEFallProject1Curve.pdf',3)
    ProjectKDEPlot(pd.read_csv("StudentsFallProject1.csv"),'KDEFallChangeProject1Curve.pdf', 6, True)
    ProjectKDEPlot(pd.read_csv("StudentsSpringProject1.csv"),'KDESpringProject1Curve.pdf',2.5)
    ProjectKDEPlot(pd.read_csv("StudentsSpringProject1.csv"),'KDESpringChangeProject1Curve.pdf',4.25, True)




if __name__ == '__main__':
    main()
