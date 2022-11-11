## This is to find Q/A during the office hour <!-- {docsify-ignore} -->
### 11/04/2022
> Q: Cannot access borgstore on compute node
>
>A: Borgstore is only accessible via infiniband (IB), you need to submit a job with`#SBATCH --constraint=ib` to make sure the job is submitted to the node with IB connections.  

> Q: How to use github. 
>
>A: Github desktop app is strongly recommended. [The HPC Resources Page](software_carpentry.md) has a workshop on Version Control with GIT for git command line general tutorial.  


>Q: Need help with parallel computing?
>
>A: CIRT does not have services that help user write code such as *"how to write the serial code to parallel?"*. 
>Best practice is look into parallel packages such as `multiprocessing` in python, and look into the [documentation](https://docs.python.org/3/library/multiprocessing.html) for more information. 

### 11/11/2022 (Cancelled)

