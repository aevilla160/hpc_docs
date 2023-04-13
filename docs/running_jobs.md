## Running jobs on clusters

The command `sbatch` is used to submit jobs to the queue. Additional commands to work with and monitor the queue/scheduler are shown in the table below.

|Command|Description|
|--|--|
|squeue|reports the state of jobs or job steps.|
|sinfo|reports the state of partitions and nodes managed by Slurm|
|scancel|used to cancel a pending or running job or job step. It can also be used to send an arbitrary signal to all processes associated with a running job or job step.|


!>The listed queue resource limitations are based on planned limitations. Queue resource limitations may vary for specific users and user groups according to node buy-in, project needs, current resource use, and/or administrative needs. Contact the system administration team for clarification or to request a variance from standard limitations.

Typical use of the queue system begins by writing a submission script that will be handed to the queue and scheduling system. The submission script is comprised of two sections: (1) a list of SGE options and resource requirements to guide the scheduler’s assignment of the job to one or more production nodes; and (2) a standard shell script that carries out the user desired calculation. To submit a job script, for example submit `my_job.sub` to the queue, one uses the following command:
```bash
sbatch my_job.sub #if you want to submit to merced please use sbatch -M merced my_job.sub
```
!> Starting 02/01/2023 we are using the centralized login, which means upon login user can submit jobs to either MERCED or Pinnacles. Here is the sample script for `my_job.sub` for submitting jobs to MERCED

```bash
#!/bin/bash  
#SBATCH --nodes=1  #asked for 1 node
#SBATCH --ntasks=20 #asked for 20 cores
#SBATCH --partition test  #this job will submit to test partition
#SBATCH -M merced # add this flag if you want to submit jobs to MERCED cluster
#SBATCH --mem=96G  #this job is asked for 96G of total memory, use 0 if you want to use entire node memory
# #SBATCH --gres=gpu:X # uncomment this line if you need GPU access, replace X with number of GPU you need
# #SBATCH -w <selected_node> #uncomment this line if you want to select specific available node to run 
#SBATCH --time=0-00:15:00 # 15 minutes  
#SBATCH --output=test1.qlog  #the output information will put into test1.qlog file
#SBATCH --job-name=test1  #the job name
#SBATCH --export=ALL

# This submission file will run a simple set of commands. All stdout will
# be captured in test1.qlog (as specified in the Slurm command --output above).
# This job file uses a shared-memory parallel environment and requests 20
# cores (--ntasks option) on a single node(--nodes option). 
#  

whoami
```

!> Unlike MERCED, Pinnacles will be the default cluster you job can submit to, if you don't add any `#SBATCH -M merced` flag, your job will be submitted to Pinnacles automatically. Similarly, `-M merced` flag must be used within `scontrol`, `sinfo`, `sbatch`, `squeue`, `srun` etc to run on merced. Note that if you are using `mpirun` and require the job to be run on MERCED, you need to add `export SLURM_CLUSTERS=merced` to your slurm script. 


The `my_job.sub` sample script for Pinnacles is provided below, the job scripts for the two machines look quite similar, however, they have different partition names and time limits:
```bash
#!/bin/bash
##SBATCH --mail-user=UCMercedNetID@ucmerced.edu  
##SBATCH --mail-type=ALL  #uncomment the first two lines if you want to receive the email notifications
#SBATCH --nodes=1    # request only 1 node
#SBATCH --partition test      # this job will be submitted to test queue
#SBATCH --time=0-00:15:00 # 15 minute
#SBATCH --ntasks-per-node=56 # this job requests for 56 cores on a node
#SBATCH --output=my_%j.stdout    # standard output will be redirected to this file
# #SBATCH --constraint=bigmem   #uncomment this line if you need the access to the bigmem node for Pinnacles
# #SBATCH --constraint=gpu #uncomment this line if you need the access to GPU
# #SBATCH --gres=gpu:2   #uncomment this line if you need GPU access (2 GPUs)
#SBATCH --job-name=my_job    # this is your job’s name
#SBATCH --export=ALL

#  type 'man sbatch' for more information and options
#  this job will ask for 1 full CPU node (56 cores) for 10 min

# run your job
```

Note that for both MERCED and Pinnacles CPUs hyper-threading are turned off.  

> If you want to assess how busy the cluster is, please use the following

Use `sinfo` to see the nodes state and check how many nodes are being allocated (alloc) or how many nodes are available (idle)

> If you want to estimate the job starting time 

`sacct -X -j <JOBID> -o start,submit` provides information for job estimated starting time or submitted time