<!-- {docsify-ignore-all} -->
## The training material for "Introduction to HPC" workshop can be found below  <!-- {docsify-ignore} -->
```pdf
training_material/10_9HPCSlides_Self.pdf
```
## Practice session details   <!-- {docsify-ignore} -->
- Copy two folders to your desired directory once you log into our remote machine (Pinnacles)

```
cp -r /home/yyu49/hpc_training/script/serial .
cp -r /home/yyu49/hpc_training/script/parallel .
```
- Go to `serial` folder.

```
cd serial
ls 
```

- Under the folder you can find two files, one python script named `python_tes1.py` the other named `test_ 1task.sh`.

    - Now let's look at the files a bit closer. 

    - Review `python_test1.py` with a text editor of your choice vim, nano, or Emacs. 
    ```
    ls 
    # open the 'python_test1.py' file with text editor of your choice.
    # close when finished looking over. 

    ```

- Review the information and structure of `test_1task.sh` 
> Important to take a note of all the different aspects of the script and all the comments in the bash script. Slurm Batch scripting starts with `#SBATCH`. Comments just start with `#` 

- Now submit `test_1task.sh` script from the serial folder

``` 
sbatch test_1task.sh
squeue --me  #this command is to check your job status
```

- `squeue --me` allows user to get jobID as well as other key information about the job information that user just submitted. 
Also you can see by using `ls` when the standard output file is placed in the directory. This is a sign that the job finished, regardless of whether the job completed succesfully or failed. 

> This completes the `serial` section of this workshop. Lets start the parallel section of this workshop!

- Go to `parallel` folder

```
cd parallel 
``` 
 
- Under the `parallel` folder there will be seven files. Open `python_parallel1.py` 
    - Review `python_parallel1.py`
    -The script simply writes out a line to anther file
    -Close the script
    -`python_parallel2.py`  & `python_parallel3.py` are similar to  `python_parallel1.py`.  

- Now look at the job submission script under the parallel folder. Open `test_2tasks.sh`.
- Review the script and take note of the key differences **Remember** this is a parallel job script. Below is the description of each line in the `test_2tasks.sh` file

```
- We are asking for 1 node 
- We are stating in the next line that we want to use 3 cores of the node. 
- We are also placing this submission on the test queue 
- Max time we are giving this job is 15 minutes 
    - This is important and will vary depending on how big your script and calulations you anticpate to be. 
- Once the job is done running we are allocating the output to go under a file(s) that we create on line 7 
- The memory we are allocating(since this job is small) will be 5G. This line will vary by the needs of the user. Place 0 here if you want to access entire node memory
- We finally name this job 
- Export all, allows the job run on all of the user's loaded environment(if user does load one, otherwise will just run job on clean working enviroment)
Toward the bottom of the shell script we now begin the for-loop to run through the files. This is the code that is desired to be executed for this job submission.
```

?> Remove **#SBATCH --reservation=......** line, when running sample script outside of workshops. 

>Now submit this job script.
``` 
sbatch test_2tasks.sh
squeue --me 
```
Continue to check by using `squeue --me` to see the status of the job submission 
Also you can see by using `ls` to see when the `.stdout` file is placed in the directory. This is a sign that the job finished, regardless of whether the job completed succesfully or failed. 
>This concludes the Practice Session Workshop

## Additional Practice Material


### MPI Tutorial <!-- {docsify-ignore} -->

Under the `MPI` folder there are two files:
1. `mpi_ex.cpp`: A C++ MPI Sample Script that demonstrates the Allreduce operation.

2. `parallel_mpi.bash` A SLURM submission script that executes the selected MPI example. It also includes dependencies and loads the neccessary modules to run the MPI script successfully. 


#### Python MPI Script Walkthrough <!-- {docsify-ignore} -->
``` python 
#Import the package mpi4py 
from mpi4py import MPI

#Identifies and groups all the processes to form the communicator
comm = MPI.COMM_WORLD

#Identify and each process with a unique rank ID 
rank = comm.Get_rank()

#The local value to be held at each rank is the rank itself. 
local_val = rank

#Perform Allreduce which groups and summates all the local values from all the ranks in the group and stores the total in total_sum
total_sum = comm.allreduce(local_val, op=MPI.SUM) 

# Have rank 0 output the total_sum
if rank == 0:   
        print(f"The total is {total_sum}")

```

#### C++ MPI Script Walkthrough 

``` cpp
#include <iostream>
#include <mpi.h>
#include <cmath>

using namespace std;
int main(int argc, char** argv){
        //Process Identity is represented as an integer identifier starting at 0.
        int rank;

        //Hold the size of the group for this task
        int size;
        MPI_Init(&argc, &argv);
        //Here we identify the individual ranks and the overall size(process count)
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);

        //local rank will be the local value that each worker will start with.
        int local_val = rank;

        //total summation value that will be calculated via Allreduce
        int total_sum;
        MPI_Allreduce(&local_val, &total_sum,1,  MPI_INT, MPI_SUM, MPI_COMM_WORLD);

        //Print out the overall total sum once from worker 0.
        if(rank == 0){
                cout << "The overall sum from all ranks is: " << total_sum << endl;
        }

        //Clean up all the states that are related to MPI
        MPI_Finalize();
        return 0;
}

```




#### SLURM MPI Script Walkthrough <!-- {docsify-ignore} --> 

``` bash

#!/bin/bash
#SBATCH --nodes=1  #asked for 1 node
#SBATCH --ntasks=36 #asked for 20 cores
#SBATCH --partition test  #this job will submit to test partition
#SBATCH --mem=96G  #Asks for 96G of total memory
#SBATCH --time=0-00:15:00 # 15 minutes
#SBATCH --output=test1.qlog  #the output information will put into test1.qlog file
#SBATCH --job-name=mpitest  #the job name
#SBATCH --export=ALL

whoami
#module load  Anaconda3 and a global version of MPI
module load anaconda3
module load openmpi/4.1.4-gcc-12.2.0+cuda

# Ensures we start in our home directory
cd ~


#For the CPP version we first begin with compiling the cpp binary where mpic++ is our compiler
mpic++ -o ccexample mpi_ex.cpp

#Then we execute the binary using mpirun and using 20 workers or processes. 
# each worker will be a CPU core
mpiexec -n 20 ./ccexample


``` 

Now proceed with submitting the job via `sbatch`

Once the job has been submitted and successful, you should recieve a output in `test1.qlog` file similar to the output below 

``` bash
avilla49
The overall sum from all ranks is 190

```
This concludes the MPI Script and Job Tutorial!
### Java Tutorial <!-- {docsify-ignore} --> 

Below is the sample Java script that we will be running. This script is a simple program that produces an output of "Hello World." 
``` java
public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
    }
}
```
>Remember to use `SCP Command` to transfer Java files to the remote cluster account. [Here](office_hour.md) is a tutorial on how to use SCP to transfer files/directories!

**NOTE: As per usual, the File name of the script must match with the Class name. This sample file shown above is named `App.java`.**

Review the sample job submission script below and take note of any comments. 
```  batch
#!/bin/bash
#SBATCH --nodes=1  
#SBATCH --ntasks=1
#SBATCH --partition test    #This partition can be changed from the user to best accommodate their compute needs
#SBATCH --mem=1G   
#SBATCH --time=0-00:15:00 # 15 minute
#SBATCH --output=Appout.qlog    #Here it is important to name the output/qlog file something a little more specific as there will be other files produced when the code is finished
#SBATCH --job-name=javatest     #Name of job
#SBATCH --export=ALL    

module load openjdk/17.0.5_8    #NOTE: This line is required otherwise the necessary modules to run Java will not be imported and the Job will fail. 
# Also ensure that the most current version of openjdk that is installed on Pinnacles is being used. 
javac App.java  #This line Compiles the code. Note: Replace 'App.java' with the file name of your Java script including the '.java'
java App    #This line will execute the java program. Note: Replace 'App' with the name of your Java script excluding the '.java'
```
The name of the sample job script shown above is `javajob.bat`. This file is of Batch script file type. Users can also use `.sub` files to submit jobs.

### submit a Java job <!-- {docsify-ignore} -->
you can submit the Job using 'Sbatch [Name of Job submission file]'
>Use 'squeue --me' to find key information about the job's state currently. If there is no information being presented then the job is finished.

Let's take a look at the results of the job. If the job was successful you will get two new files under your current directory. There will now be a `Filename.class` & `Filename.qlog`.
> The `.class` file is created automatically when we run the job if there is no pre-existing class file being used to run the Java script. In the automatically created `.class` file there is only computer-readable information so we can leave this file alone. 
The more important file is the `.qlog` file which will be holding the produced output of the Java script. For example, the `.qlog` file will be holding "Hello World!" which was being produced by our sample Java script. It is important to note that if the anticipated output is NOT produced the `.qlog` file will also hold the java errors, if any, that were produced.

This concludes the Java Practice Section!





