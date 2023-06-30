## Running a Job Array  <!-- {docsify-ignore} -->
Job arrays offer a mechanism for submitting and managing collections of similar jobs quickly and easily that utliizes only one job script. Submitting a job array can be useful in many of the following ways: 

1. Having a set of code or program that needs to run many different input variables or files. 
2. Running a single program repeatedly to analyzing a single data file.
3. Running the same program multiple times with varying arguements.

Submitting a job array allows users to run jobs at the same time or have the results of the previous job output to be used as input for the next job. While the output capacity from a job array is immencse, the job configurations are the same for all jobs to be ran in the job array. 

The max number of jobs that can run at the same time is determined by the maximum number of jobs that can run on the selected partition and is different for each partition. More information about each partition on each cluster can be found here: [MERCED](get_started.md) and [Pinnacles](p_get_started.md)


## Writing a Job Array Script  <!-- {docsify-ignore} -->
Job Arrays allow for multiple jobs to run using 1 job script. This is important because all jobs in the array will have same SBATCH variables by default. It is not best use of resources to submit a job array that has drastically different jobs that require drastically different requirements(i.e. job sizes, walltime, memory needed, etc). Job arrays are best used when submitting jobs with similar requirements(i.e. job sizes, walltime, memory needed, etc).

Below is a job submission script example with an array size of 5:

```bash
#!/bin/bash
#SBATCH --nodes=1  #asked for 1 node
#SBATCH --ntasks=1  #asked for 1 core
#SBATCH --partition  short  #this job will submit to short partition. Job array job limit will be limited to 12 jobs on this partition based on maximum job submit limits.
#SBATCH --mem=1G  #this job is asked for 1G of total memory, use 0 if you want to use entire node memory
#SBATCH --job-name=test_job_array #job name
#SBATCH --array=1-5 #this job array will have an array size 1-5, 5 seperate jobs will run.
#SBATCH --time=0-00:15:00 # 15 minutes  #There will be a max run time of 15 mins for this job array to run
#SBATCH --output=array_%A-%a.qlog  #the output information of each job running will put into its respective qlog file listed as: array_JOB_ID-TASK_ID.qlog
#SBATCH --export=ALL

# # This set of instructions will ask for each job running to print the date and then it's task ID

date
printf "My SLURM_ARRAY_TASK_ID: %s\n" "$SLURM_ARRAY_TASK_ID"
```




## Files and Outputs  <!-- {docsify-ignore} -->
Job Arrays have many jobs and with each job having its own proper output and error files. In the job array script there are two new variables,  `%A` and `%a`, which may be used to name the files that catch stdin, stderr and stdout. `%A` will be replaced by the value of `SLURM_ARRAY_JOB_ID` ( first job ID of the array) and `%a` will be replaced by the value of `SLURM_ARRAY_TASK_ID` (job array index value).


## How to Submit a Job Array   <!-- {docsify-ignore} -->

When sumbitting a job array there will be a new arguement, ` --array=x-y`. The task id,`x` represents the starting index, and  the task id `y` represents the last index - 1. The complete line to submit the array job will look similar to `#SBATCH --array=x-y myjob.file`. Where `myjob.file` will be replaced by the name of your job script. 

The Task ID range specification arguments can also be configured to:

1. Submit a job array with specified-comma seperated index values. Ex. `#SBATCH --array=6,36,1296`. (6, 36 1296): total of 3 jobs.
2. Submit a job array with index values incrementing by 1. Ex. `#SBATCH --array=x-y` Range from 1-10; total of 10 jobs. 
3. Submit a job array with index values that have a step or parse value that does not equal 1. Ex. `#SBATCH --array=45-90:15`. Range from index 45-90, with an step of 15 (45,60,75,90). Total of 4 jobs to be ran. 

### Job Dependcies on Job Array   <!-- {docsify-ignore} -->
Jobs that depend on outputs of previous jobs of a job array or on the ouput of a whole job array after it is completed must declare itself as dependent using `#SBATCH --depend=<Flag>:<jobid>[IndexRange] <jobscript.file>` after the independent job array has been submitted to the scheduler. 

Below are flags that can be used to help declare the dependency of certain job(s) in the job array submission line after the first job array has been submitted to the scheduler. 

|Command | USE |
| --------| --------------- |
| after  | Flag is satisfied after all tasks in the job array start. | 
| afterany | Flag is satisfied after all tasks in the job array complete.|
| aftercorr | Satisfied after the corresponding task ID in the specified job has completed successfully | 
| afterok  | Flag is satisfied after all tasks in the job array complete successfully | 
| afternotok | Flag satisfied after all tasks in the job array complete with at least one tasks not completing successfully. | 

## Command Uses  <!-- {docsify-ignore} -->

Commands to view status of the job or other parameters are more specific when using job arrays. Below are two commands and options that are frequently used with job arrays. 

Scancel Command: 

| Command | Use |
| -------------------| ----------------------------|
| scancel [jobID]_index# | Cancels the specified job from job array |
| Scancel [jobID]_[IndexRange] | Cancels all the jobs in the index range from job array |
| scancel [jobID] | Cancels the whole job array |


Squeue Command: 
The squeue command, when used with job arrays will report all of the tasks associated with a single job record on one line and use a regular expression to indicate the "array_task_id" values. When states of individual jobs change, then those changes will also be reflected in the outpout of the `squeue` command.  Adding `--array` or `-r` to the squeue command will print one job array element per line allowing for clear states for each job in the job array.



