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

def RunKDE(bandwidth, data):
    xinterval = np.linspace(-0.5, 0.5, 1000).tolist()
    yprojections = [CalculateKDE(x, data, bandwidth) for x in xinterval]
    return (xinterval, yprojections)


def ManageKDEProcess(bandwidth, data):
    xinterval, yprojections = RunKDE(bandwidth, data)
    return xinterval, yprojections

def CreateCompareKDEPlots(discrete=False):
    field = "Average Discrete Marginal Logistic" if discrete else "Average Marginal Logistic"
    data = pd.read_csv("StudentsProjects14.csv")
    project4 = data[data['Variable'].astype(str).str[-2:] == "_4"]
    project1 = data[data['Variable'].astype(str).str[-2:] != "_4"]
    bandwidths = [2.5*Silvermans(project1[field]), 2.5*Silvermans(project4[field])]
    dataset = [project1[field],project4[field]]
    labels = ['Project 1', 'Project 4']
    linetypes = ['-','--']
    r = []
    for index, d in enumerate(dataset):
        r.append(ManageKDEProcess(bandwidths[index], d))
    plt.figure()
    # plt.xlim(0,1)
    ax = plt.axes()
    ax.set_ylabel('Density')
    if discrete:
        ax.set_xlabel(r'Average Change in Probability of Failure')
    else:
        ax.set_xlabel(r'Average Change in Probability of Failure ($p_i(q_j,s_i)$)')   
    for index, result in enumerate(r):
        xinterval, yprojections = result
        ax.plot(xinterval, yprojections, label=labels[index], color='black', linestyle=linetypes[index])
    plt.vlines(project1[field].mean(), 0, 3, color='black', linestyles='-')
    plt.vlines(project4[field].mean(), 0, 3, color='black', linestyles='--')
    ax.legend()
    if discrete:
        plt.savefig('KDEChangeCompareCurveDiscrete.pdf')
    else:
        plt.savefig('KDEChangeCompareCurve.pdf')

def ProjectKDEPlot(discrete=False):
    field = "Average Discrete Marginal Logistic" if discrete else "Average Marginal Logistic"
    data = pd.read_csv("StudentsProject1.csv")
    subdata = data[field]
    bandwidths = [2.5*Silvermans(subdata),]
    dataset = [subdata,]
    labels = ['Project 1', ]
    linetypes = ['-',]
    r = []
    for index, d in enumerate(dataset):
        r.append(ManageKDEProcess(bandwidths[index], d))
    plt.figure()
    ax = plt.axes()
    ax.set_ylabel('Density')
    if discrete:
        ax.set_xlabel(r'Average Change in Probability of Failure')
    else:
        ax.set_xlabel(r'Average Change in Probability of Failure ($p_i(q_j,s_i)$)')
    for index, result in enumerate(r):
        xinterval, yprojections = result
        ax.plot(xinterval, yprojections, label=labels[index], color='black', linestyle=linetypes[index])
    plt.vlines(subdata.mean(), 0, 4.5, color='black', linestyles='-')
    # ax.legend()
    if discrete:
        plt.savefig('KDEChangeProject1CurveDiscrete.pdf')
    else:
        plt.savefig('KDEChangeProject1Curve.pdf')


def main():
    CreateCompareKDEPlots()
    ProjectKDEPlot()
    CreateCompareKDEPlots(True)
    ProjectKDEPlot(True)

if __name__ == '__main__':
    main()
