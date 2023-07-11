# Job Management 
Presented here are helpful tools and methods to manage  Slurm jobs, find detailed information of a job like memory usage, CPUs, and how to use job statistics/information to troubleshoot any job failure.


## Checking jobs after submission

`squeue` is a useful command that can help check the state and workload of the overall cluster as well as more specific information. Below is a table of options that can be added to view certain information. By default `squeue` will show all currently submitted and running jobs on Pinnacles.

|Command_Option | Use | 
| -------------| -----------------------|
| `-M merced ` | Shows all currently submitted jobs on MERCED |
|  `--me ` | Shows all currently jobs submitted by user |
| `--r` or `-array ` | Shows job arrays sumitted onto cluster |


>Flags can be used together in the same line for example: `squeue -M merced --me`

## Job State
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


## Nodelist Reasons 

NodeList(Reason) helps to find on which nodes the job is currently running on. Also, in the case of PD Job state, this field will give more information about the reason why the job is in pending state. Below is a table that shows common Nodelist(reasons) and their meaning. 
| (Reason) | Meaning | 
| ---------- | ---------------| 
| (Resources) |  Job is waiting for resources to become available |
| (TimeLimit) | Job has hit it's max time limit for execution |
| (ReqNodeNotAvail) | The requested node is not curretly available | 
| (Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions) | Job is not available |
|(Priority) | One or more higher priority jobs exist for this partition or advanced reservation. | 
| (QoSJobLimit) | The job's QOS has reached its maximum job count |
| QOSResourceLimit | The job's QOS has reached some resource limit | 

##  Sacct command
The `sacct` displays accounting data for all jobs in the cluster queue or recent history. By default, the sacct command diplays JobId, JobName, Partition, Account, AllocCPUS, State and ExitCode. Below are useful options that can be added to get more specific information but all options for `sacct ` can be found through executing `sacct -e` or `sacct -h`.

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

## Common Issues
Below are common issues, that can arrise when running jobs on the clusters, and associated troubleshooting methods. 

### Out of Memory Issues <!-- {docsify-ignore} -->
Jobs can fail if the memory requested for the job exceeds the actual memory needed for the job to complete successfully.
It is good practice to always check the job state and exit code with `sacct -j <JobID>`. It can be concluded that a job has had a **OUT_OF_MEMORY** error from reading the job state column. Furthermore, the output file produced by the failed job should also contain error messages that can be associated with the job running out of memory. 

### Time-Out Issues <!-- {docsify-ignore} -->
One common issue for jobs failing is if job does not complete in the allocated time. This leads to a **Time-Out** State and a `(TimeLimit)` nodelist reason. The best approach is to increase the time being allocated for the job to run, ensuring that the job does not exceed the partition's max walltime. If the job continues to fail with a **Time-Out** state then it is best to break the job down into smaller jobs,  make it into a job array or change the partition that the job is being placed onto to run and compute. 

## Other Useful Commands

|Command | Use | 
| -------------| -----------------------|
| scancel <jobid> or skill <jobid> | These commands will kill the specified job in it's current process and state. | 
| seff <job-id> |  This command can be used to find the job efficiency report for the job(s) after it has completed and exited from the queue. Some information in the report are: State, CPU & Memory Utilized, CPU & Memory Efficiency. 
