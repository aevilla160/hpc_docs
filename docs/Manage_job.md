# Job Management  <!-- {docsify-ignore} -->
Presented here are helpful tools and methods to manage  Slurm jobs, find detailed information of a job like memory usage, CPUs, and how to use job statistics/information to troubleshoot any job failure.


## Checking jobs after submission  <!-- {docsify-ignore} -->

`squeue` is a useful command that can help check the state and workload of the overall cluster as well as more specific information. Below is a table of options that can be added to view certain information. By default `squeue` will show all currently submitted and running jobs on Pinnacles.

|Command_Option | Use | 
| -------------| -----------------------|
| `-M merced ` | Shows all currently submitted jobs on MERCED |
|  `--me ` | Shows all currently jobs submitted by user |
| `--r` or `-array ` | Shows job arrays sumitted onto cluster |


!> Flags can be used together in the same line for example: `squeue -M merced --me`

## Job State  <!-- {docsify-ignore} -->
Job states are the current state of the jobs that were submitted. Some important state codes that are useful are given below: 

| State Codes | Meaning | 
| -------- | --------------------| 
| PD | Job is Pending |
| R | Running | 
| CF | Job is resources allocated and now booting up| 
 CD | Job has been completed |
| CA | Job has been cancelled explicitly | 
| CG | Job is in the process of completting and is deallocating the resources | 
| F | Job exited with Failure, a non-zero exit code is presented | 
| OOM | Nodes are out of memory | 
| S | Job has been suspended |
| TO | Job terminated upon reaching its time limit | 


## Nodelist Reasons  <!-- {docsify-ignore} -->

NodeList(Reason) helps to find on which nodes the job is currently running on. Also, in the case of PD Job state, this field will give more information about the reason why the job is in pending state. Below is a table that shows common Nodelist(reasons) and their meanings. 

| (Reason) | Meaning | 
| ---------- | ---------------| 
| (Resources) |  Job is waiting for resources to become available |
| (TimeLimit) | Job has hit it's max time limit for execution |
| (ReqNodeNotAvail) | The requested node is not curretly available | 
| (Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions) | Job is not available |
|(Priority) | One or more higher priority jobs exist for this partition or advanced reservation. | 
| (QoSJobLimit) | The job's QOS has reached its maximum job count |
| QOSResourceLimit | The job's QOS has reached some resource limit | 

##  `sacct` command  <!-- {docsify-ignore} -->
The `sacct` displays accounting data for all jobs in the cluster queue or recent history. By default, the `sacct` command diplays JobId, JobName, Partition, Account, AllocCPUS, State and ExitCode. Below are useful options that can be added to get more specific information but all options for `sacct ` can be found through executing `sacct -e` or `sacct -h`.

| Option | Meaning | 
| ---------------- | ---------------| 
| --user=<uid_or_user_list> | Displays the list of jobs currently submitted and running on the cluster of the specified user. |
| -j, --jobs=<JobID> | Displays information about the job ID inputted |
| -C, --constraints=<constraint_list> | Comma separated list to filter jobs based on what constraints/features the job requested. Multiple options will be treated as 'and' not 'or', so the job would need all constraints specified to be returned not one or the other. | 
| -h, --help | Displays all options and descriptions for `sacct` |
| -X, --allocations | Only show statistics relevant to the job allocation itself |
| -v, --verbose|  Primarily for debugging purposes, report the state of various variables during processing. |
| --name=<jobname_list> | Display jobs that have any of these name(s).|
| --state=<state_list> | Displays states depending on which state was asked to be displayed and thier associated exit code. |


Example of `sacct -e`

    Account             AdminComment        AllocCPUS           AllocNodes
    AllocTRES           AssocID             AveCPU              AveCPUFreq
    AveDiskRead         AveDiskWrite        AvePages            AveRSS
    AveVMSize           BlockID             Cluster             Comment
    Constraints         ConsumedEnergy      ConsumedEnergyRaw   Container
    CPUTime             CPUTimeRAW          DBIndex             DerivedExitCode
    Elapsed             ElapsedRaw          Eligible            End
    ExitCode            Flags               GID                 Group
    JobID               JobIDRaw            JobName             Layout
    MaxDiskRead         MaxDiskReadNode     MaxDiskReadTask     MaxDiskWrite
    MaxDiskWriteNode    MaxDiskWriteTask    MaxPages            MaxPagesNode
    MaxPagesTask        MaxRSS              MaxRSSNode          MaxRSSTask
    MaxVMSize           MaxVMSizeNode       MaxVMSizeTask       McsLabel
    MinCPU              MinCPUNode          MinCPUTask          NCPUS
    NNodes              NodeList            NTasks              Partition
    Priority            QOS                 QOSRAW              Reason
    ReqCPUFreq          ReqCPUFreqGov       ReqCPUFreqMax       ReqCPUFreqMin
    ReqCPUS             ReqMem              ReqNodes            ReqTRES
    Reservation         ReservationId       Reserved            ResvCPU
    ResvCPURAW          Start               State               Submit
    SubmitLine          Suspended           SystemComment       SystemCPU
    Timelimit           TimelimitRaw        TotalCPU            TRESUsageInAve
    TRESUsageInMax      TRESUsageInMaxNode  TRESUsageInMaxTask  TRESUsageInMin
    TRESUsageInMinNode  TRESUsageInMinTask  TRESUsageInTot      TRESUsageOutAve
    TRESUsageOutMax     TRESUsageOutMaxNode TRESUsageOutMaxTask TRESUsageOutMin
    TRESUsageOutMinNode TRESUsageOutMinTask TRESUsageOutTot     UID
    User                UserCPU             WCKey               WCKeyID
    WorkDir

Below are defintions of some important fields from the above list that are helpful when troubleshooting or debugging. 

|Field | Use | 
| -------------| -----------------------|
| JobId | Shows the ID of the job |
| JobName |Name of the Job. |
| AllocCPUS | Count of allocated CPUs. Equal to NCPUS.|
| ReqCPUS | Required number of CPUS.| 
| ReqMem | Minimum memory required for the job in MB. A c in the end denotes Memory Per CPU and a n at the end represents Memory Per Node.|
| AveRSS | Average memory use of all tasks in the job.|
| MaxRSS | Maximum memory use of any task in the job. |
| Start | Initiation time of the job in the same format as End |
| End | Termination time of the job.|
| Elapsed | Time taken by the job. |
| State | State of the job.|
| ExitCode | Exit code returned by the job. |



## `scontrol` Command 
`scontrol` is a helpful command that allows to  view or configure the submitted job and it's state. scontrol is used to view or modify Slurm configuration including: job, job step, node, partition, reservation, and overall system configuration. If no command is entered on the execute line, scontrol will operate in an interactive mode and prompt for input. It will continue prompting for input and executing commands until explicitly terminated.

Use `scontrol` with the follwing syntax to retrieve useful information about the specified job

Below is an example of using scontrol to get insight about the example job. The example job failed and has its reason shown below. It is shown as `JobState=PENDING Reason=Job's_account_not_permitted_to_use_this_partition_`

    JobId=568939 ArrayJobId=568939 ArrayTaskId=1-5 JobName=test_job_array
   UserId=guest001(100232) GroupId=ucm_guests(100058) MCS_label=N/A
   Priority=4294341946 Nice=0 Account=project_ucm_guests QOS=normal
   JobState=PENDING Reason=Job's_account_not_permitted_to_use_this_partition_(short_denies_project_ucm_guests_including_project_ucm_guests) Dependency=(null)
   Requeue=0 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
   RunTime=00:00:00 TimeLimit=00:15:00 TimeMin=N/A
   SubmitTime=2023-07-14T15:13:48 EligibleTime=2023-07-14T15:13:49
   AccrueTime=2023-07-14T15:13:49
   StartTime=2023-07-14T15:14:18 EndTime=2023-07-14T15:29:18 Deadline=N/A
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2023-07-14T15:14:18 Scheduler=Main
   Partition=short AllocNode:Sid=rclogin01:132802
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList= SchedNodeList=node018
   NumNodes=1-1 NumCPUs=1 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   TRES=cpu=1,mem=1G,node=1,billing=1
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=1 MinMemoryNode=1G MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=/scratch/guest001/job_arraytest.sh
   WorkDir=/scratch/guest001
   StdErr=/scratch/guest001/array_568939-4294967294.qlog
   StdIn=/dev/null
   StdOut=/scratch/guest001/array_568939-4294967294.qlog
   Power=



## Common Issues  <!-- {docsify-ignore} -->
Below are common issues, that can arrise when running jobs on the clusters, and associated troubleshooting methods. 

### Out of Memory Issues <!-- {docsify-ignore} -->
Jobs can fail if the memory requested for the job exceeds the actual memory needed for the job to complete successfully.
It is good practice to always check the job state and exit code with `sacct -j <JobID>`. It can be concluded that a job has had a **OUT_OF_MEMORY** error from reading the job state column. Furthermore, the output file produced by the failed job should also contain error messages that can be associated with the job running out of memory. 

Below is a script that will result in an out of memory error. The script is running matlab but has only 1G allocated in memory toward the job. Thus results in a fail in this use case.
    #! /bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks=3    # users could ask a max of 20 or 24 cores per node depending on MERCED hardware configuration
    #SBATCH -p test
    #SBATCH --mem=1G  #Here is the reason why the job fails
    #SBATCH --time=0-00:15:00     # 15 minutes
    #SBATCH --output=regular.stdout
    #SBATCH --job-name=test
    #SBATCH --export=ALL

    module load matlab/r2021b  # OR module load matlab/matlab_2018b
    # example 1
    matlab -nodisplay -nodesktop -nosplash -r "ver; exit;"

    # example 2
    matlab -nodisplay -nodesktop -nosplash -r "license('test', 'optimization_toolbox'); exit;"

    # example 3
    matlab -nodisplay -nodesktop -nosplash -logfile /path/to/test_matlab.log < test_matlab.m

 We can check the states by using `sacct -j 568951 --format=jobid,jobname,reqcpus,reqmem,averss,maxrss,elapsed,state%20,exitcode --unit=M`. Replace the 568951 wuth the job ID that is being checked. 

    JobID           JobName  ReqCPUS     ReqMem     AveRSS     MaxRSS    Elapsed                State ExitCode
    ------------ ---------- -------- ---------- ---------- ---------- ---------- -------------------- --------
    568951             test        3      1024M                         00:00:40        OUT_OF_MEMORY    0:125
    568951.batch      batch        3               101.62M    101.62M   00:00:40        OUT_OF_MEMORY    0:125
    568951.exte+     extern        3                 0.89M      0.89M   00:00:40            COMPLETED      0:0

Using the sacct command we see that the job resulted in OOM state which allows us to debug that the issue was an memory capacity issue. 

### Time-Out Issues <!-- {docsify-ignore} -->
One common issue for jobs failing is if job does not complete in the allocated time. This leads to a **Time-Out** State and a `(TimeLimit)` nodelist reason. The best approach is to increase the time being allocated for the job to run, ensuring that the job does not exceed the partition's max walltime. If the job continues to fail with a **Time-Out** state then it is best to break the job down into smaller jobs,  make it into a job array or change the partition that the job is being placed onto to run and compute. 

Below is a script that will result in an out of memory error
    #! /bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks=3    # users could ask a max of 20 or 24 cores per node depending on MERCED hardware configuration
    #SBATCH -p test
    #SBATCH --mem=10G  
    #SBATCH --time=0-00:1:00     # 1 minute, requested
    #SBATCH --output=regular.stdout
    #SBATCH --job-name=test
    #SBATCH --export=ALL

    module load matlab/r2021b  # OR module load matlab/matlab_2018b
    # example 1
    matlab -nodisplay -nodesktop -nosplash -r "ver; exit;"

    # example 2
    matlab -nodisplay -nodesktop -nosplash -r "license('test', 'optimization_toolbox'); exit;"

    # example 3
    matlab -nodisplay -nodesktop -nosplash -logfile /path/to/test_matlab.log < test_matlab.m

After submitting this script using `sbatch TOjob.sh` we see that it runs and is successfully running up until it hits its max wall time of 1 minute. This job failed because the mininimum time needed was 180 seconds as that is the time the job sleeps after running. 

Using `sacct -j <jobID> --format=jobid,jobname,reqcpus,reqmem,averss,maxrss,elapsed,state%20,exitcode --unit=M`. We get a result table that shows that the first part timed out and thus resulted in a failed, timedout and cancelled state. 

    JobID           JobName  ReqCPUS     ReqMem     AveRSS     MaxRSS    Elapsed                State ExitCode
    ------------ ---------- -------- ---------- ---------- ---------- ---------- -------------------- --------
    568963             test        3      1024M                         00:01:10              TIMEOUT      0:0
    568963.batch      batch        3                12.01M     12.01M   00:01:11            CANCELLED     0:15
    568963.exte+     extern        3                 0.90M      0.90M   00:01:10            COMPLETED      0:0
    568963.0           echo        3                 3.30M      3.30M   00:00:00            COMPLETED      0:0
    568963.1          sleep        3                 3.27M      3.27M   00:01:12            CANCELLED     0:15

Using the sacct command we see that the job resulted in `TIMEOUT` state which allows us to debug that the issue was an walltime issue issue. 

However it always important to note that sometimes a job failing not the result of one issue or error, but a combination of many errors and issues. Furthermore it is best to keep track of jobs before, during and after completion. 


## Useful proccess to follow to ensure sucessful completion of jobs <!-- {docsify-ignore} -->
1. Submit the Job
    Submit the above job and see how it runs. To submit the above job, run the following command.

        sbatch script.sh
        Submitted batch job <JOBID>

2. Watch Live Status of the Job.
    Use the `watch squeue -u <username>`. Do not include anything past the `@` in the username. Ex. `watch squeue -u guest001`. Empty Version of Live Status is below. 
        
        Every 2.0s: squeue -u guest001
        CLUSTER: pinnacles                                                          
             JOBID PARTITION     NAME     USER ST	TIME  NODES NODELIST(REASON)
> To exit the live status of the watch squeue command, press Ctrl + C

3. After the job exits from the queue, run the below sacct command to check the status of the job. 
`sacct -j <JobID> --format=jobid,jobname,elapsed,state,exitcode`

Sacct Command SampleOutput:

        JobID    JobName    Elapsed      State ExitCode
        ------------ ---------- ---------- ---------- --------
        568963             test        3      1024M                         00:01:10              TIMEOUT      0:0
        568963.batch      batch        3                12.01M     12.01M   00:01:11            CANCELLED     0:15
        568963.exte+     extern        3                 0.90M      0.90M   00:01:10            COMPLETED      0:0
        568963.0           echo        3                 3.30M      3.30M   00:00:00            COMPLETED      0:0
        568963.1          sleep        3                 3.27M      3.27M   00:01:12            CANCELLED     0:15

## Other Useful Commands  <!-- {docsify-ignore} -->

|Command | Use | 
| -------------| -----------------------|
| scancel <jobid> or skill <jobid> | These commands will kill the specified job in it's current process and state. | 
| seff <job-id> |  This command can be used to find the job efficiency report for the job(s) after it has completed and exited from the queue. Some information in the report are: State, CPU & Memory Utilized, CPU & Memory Efficiency. If the command us ysed while the job is still in the R(Running) state, this might report incorrect information.
