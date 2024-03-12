# Interactive Jobs 

Interactive jobs are a useful way to debug and test code with small sample inputs before submitting scaled up input in a batch job. Interactive jobs allows users to allocate resources and work on a node directly, seeing any errors or outputs in real-time as the program runs. 

Interactive jobs can be observed as a two-part process:
1. Requesting the resources. 
2. Entering the requested resources to run programs.

Below will be a demonstration about running an interactive job

## Requesting an Interactive Job <!-- {docsify-ignore} -->

To start an interactive session: the `salloc` command allocates resources for the interactive job. Once the resources are allocated the `srun` command will be used to enter the compute node configured for the interactive node.

`salloc` comamnd template: 
    salloc --partition=<queue> --nodes=<#> --ntasks-per-node=<#> --time=<time>

Example of `salloc` command 
    salloc --partition=test --nodes=1 --ntasks-per-node=1 --time=00:15:00

**The salloc command can also be used with the `--constraint` and `--gres` to access bigmem or GPU nodes.**


## Entering the Interactive Compute Node <!-- {docsify-ignore} -->

To enter the interacive session: the `srun` command will initiate the job step under the allocated job with the provided job id.

`srun` command template: 
    srun --jobid=<jobid> --pty /bin/bash

`srun` command example 
    srun --jobid=100234 --pty /bin/bash


Once, succesffuly entered the interactive compute node, you will notice that your current ssh login wil change from rclogin to a compute node. 

Ex. 
    [user123@rclogin02 ~] will change to [user123@gnode001 ~] reflecting that I am not directly on the compute node and now able to run my experiments. 

!> Always ensure you are on the compute node before running experiments! You may cause disruptions if you are not careful and still on the login node. 
## Ending the Interactive Session <!-- {docsify-ignore} -->

!> It's important to release the allocated resources after finished using them. 

To properly exit use one of the following methods: 

- If you're logged into the node directly, simply type exit or press Ctrl+c to log out. *

- If you used srun to run commands, you can exit the shell spawned by srun to return to your original session, and then use exit or Ctrl+D. *

- To explicitly release the resources, you can use the scancel command with your job ID, which can be found using squeue.

!> * - Using one of these methods, you must still use `scancel <jobid>` to release the resources after you exited the node. 

## Useful Tips and Tricks for Interactive Session <!-- {docsify-ignore} -->

1. Ensure your connection remains active to the node during your allocated resource time. If at any point, connection to the node is lost, the running calculations may be interrupted abruptly. 

2. Use interactive sessions only for testing of programs on the smaller scale that can be scaled up in a batch job. Interative sessions are not best used when running longer, more computationally intensive work loads. 
3. Request Only What is Need: To ensure efficient use of cluster resources, request only the amount of time, memory, and compute resources necessary for your task.
4. Always check you are currently placed on the compute node before running any experiments. For any reason you are not on the compute node and begin running experiments you may cause massive disrupitons to all users on the login nodes. 
