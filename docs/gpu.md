# Building GPU Softwares on Pinnacles 
Many applications require to be built with GPU support, such as Kokkos, LAMMPS, deep learning frameworks, etc. This page will showcase how to install and build GPU-supported softwares/applications. 

The showcase will utilize the application, Kokkos, as our example application. 

## Allocating and Placement on a GPU Node

Allocating a GPU node is the first step: 

GPU nodes can be allocated via test partition (1 Hour Max TimeLimit) or via the `gpu` partition.

For shorter build times, `test` partition is a good starting point, however for longer GPU utilization allocate a node via `gpu` Queue.

To allocate a gpu node to be used interactively use the following line, `salloc --partition=<queue> --nodes=<#> --gres=gpu:X --time=<time>` where X will be replaced by 1 or 2 to denote how many GPU cards to use. 

More information can be found [here](https://ucm-it.github.io/hpc_docs/#/running_jobs) or for interactive jobs click [here](https://ucm-it.github.io/hpc_docs/#/interact_job)


Once the job has been submitted and the resources have been allocated - 

Begin to run interactively via: `run --jobid=<jobid> --pty /bin/bash`

## Checking GPU is Active 
Once placed on the GPU node, check the GPU is being used on the node you are placed on using `nvidia-smi`. If the GPU is properly activated a similar message will appear as below. 

    +-----------------------------------------------------------------------------------------+
    | NVIDIA-SMI 550.54.15              Driver Version: 550.54.15      CUDA Version: 12.4     |
    |-----------------------------------------+------------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
    |                                         |                        |               MIG M. |
    |=========================================+========================+======================|
    |   0  NVIDIA A100-PCIE-40GB          Off |   00000000:17:00.0 Off |                    0 |
    | N/A   29C    P0             35W /  250W |       0MiB /  40960MiB |      0%      Default |
    |                                         |                        |             Disabled |
    +-----------------------------------------+------------------------+----------------------+
    |   1  NVIDIA A100-PCIE-40GB          Off |   00000000:31:00.0 Off |                    0 |
    | N/A   29C    P0             37W /  250W |       0MiB /  40960MiB |      4%      Default |
    |                                         |                        |             Disabled |
    +-----------------------------------------+------------------------+----------------------+
                                                                                        
    +-----------------------------------------------------------------------------------------+
    | Processes:                                                                              |
    |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
    |        ID   ID                                                               Usage      |
    |=========================================================================================|
    |  No running processes found                                                             |
    +-----------------------------------------------------------------------------------------+

!> If a message stating that `nvidia-smi` command is not found, open a ticket [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) and state the GPU Node you are working with. 

## Installing software/application

Ensure the software has been cloned if it is from GitHub or downloaded from the original source. 

***If the Software requires `CUDA`, then `module load cuda`*** 

For the folowing demonstration of how to install a GPU-Supported appplication we will use `Kokkos`. The source can be found [here](https://github.com/kokkos/kokkos). 

`Kokkos` makes use of the `cmake` system for building of the software. 

Now to complete the building of `Kokkos`: 

1.     cmake -B kokkos_build/ -DKokkos_ENABLE_CUDA=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=.local/ -S $PWD
!> If following the line above, ensure to change the build location and install prefix to use your building and install location. 

2.      cmake --build kokkos_build/
3.      cmake --install kokkos_build/

If the build and installation were successful, `Kokkos` header files should be found in the installation location denoted in step one. 