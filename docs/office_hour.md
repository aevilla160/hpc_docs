## First-time user log in to HPC tutorial <!-- {docsify-ignore} -->
Below is a tutorial for first-time users on how to log in to HPC cluster. The tutorial used Pinnacles as an example. If users still cannot login after watching the tutorial, feel free to contact us [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

<p align='center'>
<iframe width="560" height="500" src="https://www.youtube.com/embed/MNGVOCpARCQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</p>

## HPC Office Hour Q/A <!-- {docsify-ignore} -->
Got A Question? Feel Free to attend HPC Office Hours!
 

### 1/27/23
> Q:How To Run Quantum Espresso utilizing GPU?
>
>A: Run it on under interactive session so you can see wheteher job is running with gpu with command "nvidia-smi" (Shows gpu usage).
>Important: *Do Not run GPU job on CPU Node*

>Q:Running Lammps with Kokkos on Cluster?
>
>A:Available Modules on cluster:   Module - "lammps/20210310+kokkos+cuda " - lammps with Kokkos with GPU enbled. 
>Module - "lammps/20210310+user-omp+kokkos"  - with kokkos and user-omp enabled. 


### 12/2/2022
> Q: Can a user run a sequence of jobs from one script?
>
>A: Yes, a user can run a sequence of jobs from one script and if the jobs are dependent on each other then it is possible to make them [dependency jobs](https://slurm.schedmd.com/sbatch.html).

>Q: Not sure if the needed software or library is on one of the HPC clusters? 
>
>A: Documentation website has a list of available software and libraries already downloaded onto the clusters with their specific version numbers here: [Merced's Module List](modules.md) and [Pinnacles' Module List](p_modules.md). For more updated information, once you login to cluster you can check the available sofware by typing `module avail`. Users choosing to self-install software/libraries have the responsibility to use them from trustworthy sources. 

>Q: Software/library requires a new or renewal of license?
>
>A: If the software/library is installed on the cluster and available for anyone to use, CIRT manages the licenses for these products. Contact CIRT if a community-open software/product does not have an active license that should have an active license. If a software is bought or licensed from a PI then PI manage the renewal of the software/library.  


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


### 11/14/22 - 11/18/2022; 12/09/2; 1/22/23
>No Office Hour Q/A 


 




