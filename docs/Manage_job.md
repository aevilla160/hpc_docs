### Job Management is a wide topic and here it is covered how to check jobs during and after complet

## Checking jobs after submission

`squeue` is a useful command that can help check the state and workload of the overall cluster as well as more specific information. Below is a table of options that can be added to view certain information.

|Command_Option | Use | 
| -------------| -----------------------|
| `squeue ` | This will allow you to see all currently submitted jobs on Pinnacles |
| `-M merced ` | Shows all currently submitted jobs on MERCED |
|  `--me ` | Shows all currently jobs submitted by user |
| `--r` or `-array ` | Shows job arrays sumitted onto cluster |


It is also important to note: flags can be used together in the same line for example, `squeue -M merced --me`

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
The `sacct` displays accounting data for all jobs in the cluster queue or recent history. By default, the sacct command diplays JobId, JobName, Partition, Account, AllocCPUS, State and ExitCode. Below are useful options that can be added to get more specific information but all options for `sacct ` can be found through executing `sacct -e`.

| Option | Meaning | 
| ---------- | ---------------| 
| --user=<uid_or_user_list> | Displays the list of jobs currently submitted and running on the cluster of the specified user. |