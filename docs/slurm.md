# Slurm <!-- {docsify-ignore} -->
This page serves as point of introduction to understanding and making best use of Slurm. 

Slurm is a scheduler is a free and open-source job scheduler for Linux and Unix-like kernels, used by many supercomputers and computer clusters.

Slurm serves the purpose of being the scheduler of jobs and the manager of the resources on both, MERCED and Pinnacles clusters. It does it in three ways: 
- Provides exclusive and/or non-exclusive access to the resources on the compute nodes to the users for a certain amount of time. 
- Provides a framework to start, execute, and check the work on the set of allocated compute nodes.
- Slurm manages the queue of pending jobs based on the availability of resources.



## Slurm Commands <!-- {docsify-ignore} -->

Basic Slurm Commands to interact via the command line interface with the queueing and resource scheduler/ 
The table below shows the list and descriptions of the mostly used Slurm commands.


| Commands   | Syntax                        | Description                                              |
|------------|-------------------------------|----------------------------------------------------------|
| `sbatch`   | `sbatch <jobname>`             | Submit a batch script to Slurm for processing.           |
| `squeue`   | `squeue --me`                   | Show information about your job(s) in the queue. The command when run without the `--me` flag, shows all jobs in the queue. |
| `srun`     | `srun <option>`  | Please see our example [here](interact_job.md) for using srun in interactive session.|
| `skill/scancel` | `scancel <job-id>`        | End or cancel a queued job.|
| `sinfo`    | `sinfo`                       | Get information about the resources on available nodes that make up the HPC cluster. |

## `sbatch` Command <!-- {docsify-ignore} -->

The `sbatch` command is used to sumbit job scripts to the Slurm scheduler to be placed on the respective queue and to then begin when the requested resources are available. 

Here is an example of using `sbatch` to submit a job file to the job scheduler. 

> `sbatch <batchscript>`


!> **NOTE:** `sbatch` command is different from `SBATCH` directives. A directive is a way of specifiing how the job script should be configured in a certain aspect(i.e. max wall time, max core count, etc.). Visit [this sction](#sbatch-directives-for-job-scripts) for further information on Slurm directives. 




## Slurm Script Main Parts <!-- {docsify-ignore} -->

In creating a Slurm script, there are 4 main parts that are necessary in order for your job to be successfully processed. 

### 1) Shebang <!-- {docsify-ignore} -->

The Shebang command tells the shell (which interprets the UNIX commands) to interpret and run the Slurm script using the bash shell.

This line should always be added at the very top of your SBATCH/Slurm script.

    !/bin/bash


### 2) `SBATCH` Directives in the Script <!-- {docsify-ignore} -->

The `SBATCH` directives must be used in the following manner for Slurm to properly recognize them: 

Template:
    #SBATCH --directive

Example: 

    #SBATCH --job-name=EXAMPLEJOB
    #SBATCH --nodes=2

#### Common Directives <!-- {docsify-ignore} -->

| Option | Description | 
| ------------ | ------------- | 
|--job-name=NAME|Specifies the name of the job.|
| --partition=PARTITION | Submits the job to a specific partition. |
|--nodes=N | Requests N nodes for the job. |
| --ntasks-per-node=N | Specifies the number of tasks to launch per node.|
|--mem=MB | Requests a specific amount of memory (in megabytes). |
|--time=DAYS:HOURS:MINUTES:SECONDS | Sets a limit on the total run time of the job. |
|--output=FILE_NAME | Designates a file to capture the standard output. |
|--error=FILE_NAME| Specifies a file to capture the standard error output.|

!> Please see [directive section](#sbatch-directives-for-job-scripts) for a more complete list. 

### 3) Exporting All of the user's environment for Job: <!-- {docsify-ignore} -->

    --export=all 

This line will tell Slurm to export the current working enviroment to be used on the computing nodes to process the requested instructions. This line is important as it helps ensure consistancy across user's working enviroment and the resources' working enviroment. 

### 4) Begin to include list of commands/instructions to execute your script. <!-- {docsify-ignore} -->

Here is where you can write the commands or instructions to execute the computations or calculations desired. Below is a small example of what instructions can look like:

    pwd # Prints the working Directory
    source activate env1 # conda activates an env called env1 
    python hello.py #runs a python program called hello.py



### Job Examples <!-- {docsify-ignore} -->

More detailed job examples can be found [here](running_jobs.md)

## Slurm - Job Management <!-- {docsify-ignore} -->

Job management is critical before running or scaling jobs and computations within a HPC enviroment. We have created a manual page that can be found [here](Manage_job.md). The documentation goes over common Slurm commands that help debug job errors and overall performance using `sacct` and `scontrol`. 


## Job Arrays <!-- {docsify-ignore} -->

Job arrays offer a mechanism for submitting and managing collections of similar jobs quickly and easily that utliizes only one job script. Job arrays are great at "automating" a repetetive job script that each time may only have input changes. Click [here](job_array.md) for the job array

## SBATCH Directives for Job Scripts <!-- {docsify-ignore} -->

| Directives      | Description   |
|-----------------|---------------|
| `--job-name <jobname>`    | Specifies a name for the job allocation. The specified name will appear along with the job id number when querying running jobs on the system. The default is the name of the batch script, or just sbatch if the script is read on sbatch’s standard input. |
| `--output <filename.out>`      | Instructs Slurm to connect the batch script's standard output directly to the filename. If not specified, the default filename is `slurm-jobID.out`. |
| `--partition <partition>`   | Requests a specific partition for the resource allocation (`gpu`, `interactive`, `normal`). If not specified, the default partition is normal. |
| `--cpus-per-task=<number>` | Advises the Slurm controller that ensuing job steps will require n-cpus number of processors per task. Without this option, the controller will just try to assign one processor per task.
| `--mem-per-cpu=<number>`  | This is the minimum memory required per allocated CPU. Note: It’s highly recommended to specify `--mem-per-cpu`. If not, the default setting of 500MB will be assigned per CPU. |
| `--time=<D:H:M:S>`         | Sets a limit on the total run time of the job allocation. If the requested time limit exceeds the partition’s time limit, the job will be left in a PENDING state (possibly indefinitely). The default time limit is the partition’s default time limit. A time limit of zero requests that no time limit be imposed. The acceptable time format is days-hours:minutes:seconds.|
| `--mail-user=<email>`    | Defines user who will receive email notification of state changes as defined by `--mail-type`.                          |
| `--mail-type=<type>`    | Notifies user by email when certain event types occur. Valid type values are BEGIN, END, FAIL. The user to be notified is indicated with `--mail-user`. The values of the `--mail-type` directive can be declared in one line like so: `--mail-type BEGIN, END, FAIL` |

## Slurm Output Environment Variables <!-- {docsify-ignore} -->

When a job scheduled by Slurm starts, it needs to know some information about its execution environment. For example, It needs to know the working directory, and what nodes allocated to it. Slurm passes this information to the running job via what so-called environment variables. The following is a table of the most common-used environment variable.

| Slurm Environment Variable | Description                                       |
|----------------------------|---------------------------------------------------|
| `SLURM_CPUS_ON_NODE`       | Number of CPUs on the allocated node.             |
| `SLURM_CPUS_PER_TASK`      | Number of CPUs requested per task.                |
| `SLURM_GPUS`               | Number of GPUs requested.                         |
| `SLURM_GPUS_PER_NODE`      | Requested GPU count per allocated node.           |
| `SLURM_GPUS_PER_TASK`      | Requested GPU count per allocated task.           |
| `SLURM_JOB_ID`             | The ID of the job allocation.                     |
| `SLURM_JOB_CPUS_PER_NODE`  | Count of processors available to the job on this node. |
| `SLURM_JOB_NAME`           | Name of the job.                                  |
| `SLURM_JOB_NODELIST`       | List of nodes allocated to the job.               |
| `SLURM_JOB_NUM_NODES`      | Total number of nodes in the job's resource allocation. |
| `SLURM_JOB_PARTITION`      | Name of the partition in which the job is running.|
| `SLURM_MEM_PER_CPU`        | Minimum memory required per allocated CPU.        |
| `SLURM_MEM_PER_GPU`        | Requested memory per allocated GPU. |
| `SLURM_MEM_PER_NODE`       | Total amount of memory per node that the job needs. |
| `SLURM_NODELIST`           | List of nodes allocated to the job. |
| `SLURM_NPROCS`             | Total number of CPUs allocated |
| `SLURM_NTASKS`             | Maximum number of MPI tasks (that's processes). |
| `SLURM_NTASKS_PER_CORE`    | Number of tasks requested per core. |
| `SLURM_NTASKS_PER_GPU`     | Number of tasks requested per GPU. |
| `SLURM_NTASKS_PER_NODE`    | Number of tasks requested per node. |
| `SLURM_PRIO_PROCESS`       | The scheduling priority (nice value) at the time of job submission. This value is propagated to the spawned processes. |
| `SLURM_PROCID`             | The MPI rank (or relative process ID) of the current process. |
| `SLURM_SUBMIT_DIR`         | The directory from which SBATCH was invoked. |
| `SLURM_SUBMIT_HOST`        | The Hostname of the computer from which SBATCH was invoked. |
| `SLURM_TASK_PID`           | The process ID of the corresponding task. |




