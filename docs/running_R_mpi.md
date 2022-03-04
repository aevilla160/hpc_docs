## Create a virtual environment and install R on MERCED<!-- {docsify-ignore} -->
```R
module load anaconda3
conda create -n my-R -c r r-essentials   #creates a virtual environment named my-R and installs R with some common packages
source activate my-R                     #activates the previously created virtual environment with R installed
R                                        #Start interactive R shell
install.packages(“readr”)                #This is the command to use within the interactive R shell to install new packages
```
- We have already built the environment for you, all you need to do is the following
```bash
module load anaconda3
source activate my-R
```
- The binary version of R in anaconda is just an already compiled version for linux. It should be identical to the version you would compile from source.

- Here is an example job script 
```bash
#!/bin/bash -l
#SBATCH --partition fast.q
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00
module load anaconda3
source activate my-R
Rscript Some_R_script.R
```
**Line 1**: Indicates which shell is used to execute the job script. You will likely never need to change this line

**Line 2**: This option indicates which job queue to submit your job to. There are currently three queues available that vary by how many cores you can request and how long the job will run.

**Line 3,4,5**: Indicates that we want 1 node, are going to run only a single task on that node, and

**Line 7**: This loads the anaconda module which is required to activate your R virtual environment.

**Line 8**: Activates a virtual environment call my-R, that have been previosuly created.

**Line 9**: This line is actually running the R script. RScript is recommended over R CMD BATCH.

- Assuming that you name the above script `my_Rjob.sub` you would submit it to the queue by running `sbatch my_Rjob.sub`. You can check the status of your job using `squeue -u <yourusername>`.