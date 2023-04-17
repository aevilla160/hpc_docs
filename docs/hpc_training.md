## The training material for "Introduction to HPC" workshop can be found below
```pdf
training_material/HPC_intro_updated_YueYu.pdf
```
## Practice session details 
- Copy two folders to your desired directory once you log into our remote machine (Pinnacles)
```
cp -r /home/yyu49/hpc_training/script/serial .
cp -r /home/yyu49/hpc_training/script/parallel .
```
- Go to `serial` folder.
```
cd serial
ls 
# open the 'python_test1.py' file with text editor of your choice 

```

- Under the folder you can find two files, one python script named `python_tes1.py` the other named `test_ 1task.sh`.

    - Now let's look at the files a bit closer. 

    - Review 'python_test1.py'
    ```
    ls 
    # open the 'python_test1.py' file with text editor of your choice.
    # close when finished looking over. 

    ```

- Review the information and structure of 'test_1task.sh' 
> Important to take note of all the different aspects of a batch script. As well refer to all the comments in the bash script. Slurm Batch scripting starts with `#SBATCH`. Comments just start with `#` 
- Exit out of `serial` folder
-Now submit `test_1task.sh` script from the serial folder
``` 
sbatch test_1task.sh
squeue --me 
```
- `squeue --me` allows user to get jobID as well as other key information about the job script that user just submitted. 
Also you can see by using `ls` to see when the stdout file is placed on the directory. This is a sign that the job finished, regardless of whether the job completed succesfully or failed. 
> This completes the `serial` section of this workshop
>Lets start the parallel section of this workshop!
- Go to `parallel` folder
```
cd parallel 
``` 
 
-Under the `parallel` folder there will be seven files. Open `python_parallel1.py` 
    - Review `python_parallel1.py`
    -The script simply writes out a line to anther file
    -Close the script
    -`python_parallel2.py`  & `python_parallel3.py` are similar to  `python_parallel1.py`.  

- Now look at the job submission script under the parallel folder. Open `test_2tasks.sh`.
- Review the script and take note of the key differences *Remember* this is a parallel job script.
```
- We are asking for 1 node 
- We are stating in the next line that we want to use 3 cores of the node. 
- We are also placing this submission on the test queue 
- Max time we are giving this job is 15 minutes 
    - This is important and will vary depending on how big your script and calulations you anticpate to be. If your not sure on the time you need its best to underestimate the time rather than overestimate. 
- Once the job is done running we are allocating the output to go under a file(s) that we create on line 7 
- The memory we are allocating(since this job is small) will be 5G. This line will vary by the needs of the user. Place 0 here if you want to access entire node memory
- We finally name this job 
- Export all, allows the job run on all of the user's loaded environment(if user does load one, otherwise will just run job on clean working enviroment)
Toward the bottom of the shell script we now begin the for-loop to run through the files. This is the code that is desired to be executed for this job submission.
```
>Now submit this job script.
``` 
sbatch test_2tasks.sh
squeue --me 
```
Continue to check by using `squeue --me` to see the state of the job submission 
Also you can see by using `ls` to see when the `.stdout` file is placed on the directory. This is a sign that the job finished, regardless of whether the job completed succesfully or failed. 
>This concludes the Practice Session Workshop



