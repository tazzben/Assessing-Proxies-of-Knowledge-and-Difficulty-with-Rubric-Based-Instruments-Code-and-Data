## README

The files in this directory were used to perform the analysis in the paper "Assessing Proxies of Knowledge and Difficulty with Rubric-Based Instruments."  The SSRN version of the paper is available at: https://dx.doi.org/10.2139/ssrn.4194935. The paper is forthcoming in the Southern Economic Journal.

The files are as follows:

1. Project1DataFallOnly <- Rubric data for Project 1 during the fall semester
2. Project1DataSpringOnly <- Rubric data for Project 1 during the spring semester
3. Project4DataFallOnly <- Rubric data for Project 4 during the fall semester
4. Project4DataSpringOnly <- Rubric data for Project 4 during the spring semester
5. Project1.py <- Python code to run the analysis for Project 1
6. Project4.py <- Python code to run the analysis for Project 4
7. combineAndCompare.py <- Python code to run the analysis for the 3 common rubric rows between Project 1 and Project 4
8. KDE.py and KDEMarginal.py <- Python code to produce KDE plots.  Note, that these files are dependent on the output of the Project1.py, Project4.py, and combineAndCompare.py files.
9. mw.py <- Perform the MW test based on the output of combineAndCompare.py
10. timeToCalc.py <- Python code to determine the time to calculate estimates based on class size
11. TimePlot.py <- Python code to produce the plot based on the output of timeToCalc.py