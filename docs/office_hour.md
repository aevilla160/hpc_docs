## First-time user log in to HPC tutorial <!-- {docsify-ignore} -->
Below is a tutorial for first-time users on how to log in to HPC cluster. The tutorial used Pinnacles as an example. If users still cannot login after watching the tutorial, feel free to open a a general consultationt ticket - Follow the steps below. 

Steps on requesting support with resetting password if users still having issues logging in after following tutorial video:
1. Go to CyberInfrastrucre & Research Technologies Service Now page. [Click Here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

2. At the bottom of the page there will be a "Request Service" button, click the button. 

3. Login with your UCM NetID and Password if prompted to do so. 

4. You will be promted with a new page that will require you to put in information including a description of the assistance you are requesting. In this case it will be resetting of password, so in the description state that you are requesting help with resetting of Remote Cluster password. 

5. When all the required fields are completed you can submit the ServiceNow Request to recieve assistance on resetting password!

Request Services & Contact Us - [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

Reset Password & Login Video Below!

<p align='center'>
<iframe width="560" height="500" src="https://www.youtube.com/embed/kfHjL9_kgQA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</p>

## Remote transfer files using `scp` command <!-- {docsify-ignore} -->
Watch the video below!
<p align='center'>
<iframe width="560" height="560" src="https://www.youtube.com/embed/G6DNWqHFC7A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</p>

## HPC Office Hour Q/A <!-- {docsify-ignore} -->
Got A Question? Feel Free to attend HPC Office Hours! Office Hours is held In-Person and via Zoom!
HPC office hours - Every Friday, 10:30 am - 12 pm, ACS Room 312  
Zoom URL:https://ucmerced.zoom.us/j/89487493900; password:895006 


### 7/21/23
>Q: My job is failing when I place it on a private partition but it runs successfully when it runs on a public partition, what could be the issue?
>
>A: Ensure that the the partition that the job is placed on has suffienent max walltime for the job to prevent a TIMEOUT job state. Private Job Partitions have unlimited wall time, so if the issue, where the job runs normally on the public partition but not on the private partition, then submit a ticket with as much information as possible so we can investigate. 

>Q: I need to jobs with data that exceeds the standard storage given in `data` & `scratch` folders, what are the options?
>
>A: Reach out to your PI and see if the PI has purchased more storage for authorized users to use and access. If PI has purchased more storage and wants to add user(s) then open a ticket to add users to the storage user group. If there is interest into obtaining more storage open a consultation ticket with CIRT to discuss purchasing into using Borgstore to access more storage. Alternatively, users can also try to breakdown their massive data into smaller pieces. This will allow smaller jobs to be ran and smaller outputs  to be produced so not all the data is needed to be stored  under the `scratch` or `data` folder at once, reducing the chance that the storage limit is reached. 

### 6/23/23
>Q: My job is getting cancelled and I am trying to access the GPU. 
>
>A: Ensure that the GPU partition is being called correctly `gpu` and that `#SBATCH --gres=gpu:X ` is implemented. Replace the X with the number of GPUs needed. 

>Q: Whats the difference between using more cores versus using more nodes?
>
>A: It is important to understand that Nodes and Cores are two different parts of an HPC cluster (two different levels). A core holds the CPU component. Multiple cores make up a node. When increasing the number of cores, the cpu or processing power per node is being increased which can help speed up jobs. Increasing the number of nodes __does not__ necessarily correlate to increase processing power. Many jobs may not be optimized for running and scaling across multiple nodes. Users trying to run across multiple nodes must implement MPI into their job so the job is optimized best for running parralelling across nodes. Please refer to the [HPC Vocab Page](hpc_vocab.md) for more information and definitions for terminology. 

>Q:How can I test whether my job is scalable for running across multiple nodes?
>
>A: It is recommended that users try using a benchmark to see if Parallelization is suitable for their job. A benchmark is testing a much smaller version of their actual job or calcuations and see whether that sample job is or can scale properly. 

>Q:Can I implement multiprocessing in my Python code. 
>
> Yes, it is recommended to read over the multiprocessing module documentation online, view it [here](https://docs.python.org/3/library/multiprocessing.html)!

>Q: Does Pinnacles have hyperthreading turned on? 
>
>A: No, Pinnacles and MERCED currently do not support hyperthreading. 

>Q: What is hyperthreading? 
>
>A: Hyperthreading is a method that allows the CPU to divide up the work among itself and complete it parallel among itself. 

>Q: I am trying to run a job on the cluster. My data utilizes python dependcies to parse through it and is located on the box cloud. Can my job run sucessfully?
>
>A: All the files and folders that the cluster needs to access needs to be transfered and present on the cluster. The cluster can not access data stored on a internet or outside cloud storage. Furthermore, to utilize python packages or dependencies one must create a conda enviroment on the cluster. More information about creating an enviroment can be found [here](conda_env.md)

>Q: How can I view the size of my data on the cluster?
>
>A: Users can use the command `du -h <filename>` to view the size of a given file or directory. 


### 6/16/23
>Q: How to install R kernel to Jupyter Lab?
>
>A: First please make sure you have R installed on your computer, if not, you can download R [here](https://cran.r-project.org/). Next, open JupyterLab, now you should be able to use R, under the terminal type `R` to get into the R environment. Once you are in the R session, please follow the steps below: 1. `install.packages("devtools")` followed by 2. `devtools::install_github("IRkernel/IRkernel")`, and finally 3. `IRkernel::installspec()`. Note: In order, the (1) install the devtools package which gets you the install_github() function, (2) install the IR Kernel from github, and (3) tell Jupyter where to find the IR Kernel. Now, when you close the JupyterLab and reopen it, you should be able to see the R kernel, more information please see [here](https://richpauloo.github.io/2018-05-16-Installing-the-R-kernel-in-Jupyter-Lab/). 

### 6/9/23
>Q: I am trying to download this folder from the cluster to my local computer but I am having issues with `rsync` - error `skipping local path`. 
>
>A: A quick bypass to this issue is to use the `scp` command to transfer files or folders from remote to local. A tutorial is posted at the top of this page. 

>Q: How can I check my groups usage of our allocated storage on Borgstore?
>
>A: Users can not check a detailed-breakdown of a group's users and their respective useage of the Borgstore storage. Users can check thier Groups storage usage/total using the command `beegfs-ctl --getquota --gid ######`. Users can check their ID number and Group ID # via the command `id <username>`.

>Q: I am having trouble accessing the Borgstore and the direcotries in the Command-Line Interface is blanking red?
>
>A: If the path displayed is flashing red and user is having issues directly accessing the Borgstore then the soft-links leading to the Borgstore are broken or outdated. It is best to open a ticket to get further assitance. Click [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) to open a ticket. 


### 6/2/23 

>Q: I'm having trouble downloading a folder or file onto the clusters and I keep getting permission denied.
>
>A:  First check whether the original author of the folder or file has given proper read (r) & write (w) access to others or groups. Use the command `ls -la` to view all permissions in your current directory or `ls -la <filename>` to view only the permissions for that specified file. To download a folder or file user must ensure that they have __read__ and __write__ access.

>Q: Can I let this folder/file download in the background?
>
>Yes users can run the download or transfer of data using `& ` at the end of their command. 


### 4/28/23
>Q: I am new to High-Performance Computing, where do I begin?
>
>A: It is highly recommended that all HPC users have knowledge of basic linux commands and understanding of how a command line interface works. If users need to brush up on basic linux commands then it is highly recommended that they view the Linux(Unix) carpentry workshops [Here!](software_carpentry.md)   
>
>Next step would be to check out the HPC Practice Session Material [Here!](hpc_training.md). Here you can look at the training material that is typically shown in the HPC workshop and even do a self-paced practice session!
>
>Finally it is highly recommended to look over sample job scripts to understand what a job is and what does a job hold. Users can view a sample job script [Here!](running_jobs.md)


### 4/14/23
>Office Hours Cancelled.
### 4/7/23
>Q: I can not login into the Central Login even though I had an account on Merced Cluster?
>
>A: Submit a password reset to gain access to the central login node. From there all data stored in the home and data folder of the Merced cluster will transfer over to Pinnacles cluster as Merced cluster is recharge model. User must also rebuild any enviroment they had built in Merced in Pinnacles. Pinnacles is the default cluster when users login to through central login. 
### 3/31/23
> NO office hour on 03/31/2023

### 3/11/23
>Q: I am new to High-Performance Computing, where do I begin?
>
>A: It is highly recommended that all HPC users have knowledge of basic linux commands and understanding of how a command line interface works. If users need to brush up on basic linux commands then it is highly recommended that they view the Linux(Unix) carpentry workshops [Here!](software_carpentry.md)   
>
>Once user is comfortable with using linux commands then it is highly recommended to look over sample job scripts to understand what a job is and what does a job hold. Users can view a sample job script [Here!](running_jobs.md)

>Q: Does Pinnacles have STATA?
>
>A: Yes, Pinnacles has STATA 17 installed.
>1. Users can see all available software on pinnacles via the command "module avail"
>2. To load a software into the enviroment "module load softare_name"
>3. To unload a module from the enviroment it is "module unload softare_name". 

### 2/24/23
>Q: How to intialzie Conda Enviroment?
>
>A:Tutorial is listed under "Running jobs" - [Click Here](conda_env.md)

>Q:My GPU node request is not being granted or running?
>
>A: Pinnacles Machine only has 8 publicly available GPU Nodes; each node has two GPU cards. Therefore, if all GPU nodes are being used then user must wait and try again later to run GPU interactive Job. 
The command "sinfo" to get information about the GPU nodes and their current usage. 


>Q: Running Gromacs with GPU on Pinnacles?
>
>A: Pinnacles only has Gromacs for CPU usage installed.

>Q:How can I monitor the state of the GPU node that is running my interactive job?
>
>A:Monitoring the state of the GPU node and seeing the usage during the interactive job can be done through the command "nvidia-smi"

>Q: Is VMD available on Pinnacles
>
>A: Yes, Pinnacles has VMD version 1.9.3. However it is recommended that users use VMD on their own local machine to get better results.




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


### 11/14/22 - 11/18/2022; 12/09/2; 1/22/23 - 2/17/23; 3/3/23; 4/21/23; 4/28/23;5/5/23; 5/12/23;5/19/23; 5/26/23; 6/30/23-7/14/23 <!-- {docsify-ignore} -->
>No Office Hour Q/A 


 




