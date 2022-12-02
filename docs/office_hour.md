## Q/A during the office hour <!-- {docsify-ignore} -->
### 11/04/2022
> Q: Cannot access borgstore on compute node
>
>A: Borgstore is only accessible via infiniband (IB), you need to submit a job with`#SBATCH --constraint=ib` to make sure the job is submitted to the node with IB connections.  

> Q: How to use github. 
>
>A: Github desktop app is strongly recommended. [The HPC Resources Page](software_carpentry.md) has a workshop on Version Control with GIT for git command line general tutorial.  


>Q: Need help with parallel computing?
>
>A: CIRT does not have services that help user write code such as *"how to write python parallel program based on a serial nested loop?"*. 
>Best practice is look into parallel packages such as `multiprocessing` in python, and look into the [documentation](https://docs.python.org/3/library/multiprocessing.html) for more information. 

### 11/11/2022 (Cancelled)

### 11/18/2022
>No Office Hour Q/A 

### 11/24/2022 (Cancelled)

### 12/2/2022
> Q: Can I run a sequence of jobs from one script?
>A: Yes, one can run a sequence of jobs from one script and if the jobs are >dependent on eachother then it is possible to make them dependent on one another.

>Q: Not sure if the needed software or library is on one of the HPC clusters? 
>A: Documentation website has a list of available software and libraries already downloaded onto the clusters with their specific version numbers here: [Module List](modules.md). If the  software/library you are looking for then you can always request CIRT to add the specified software/library for community use. Users choosing to self-install software have the responsibility to use them from trustworthy sources. 
### 12/9/2022 (Cancelled)

### ***No Office Hours During Winter Break(Dec.23rd to Jan. 2nd) - Office hour will resume the week of January 2, 2023.***

