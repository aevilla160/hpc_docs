# Singularity on Pinnacles & MERCED Clusters

Singularity serves as a software that allows to run containers seamlessly. Containers are useful as they allow for all necessary softwares and depencies to be stored in one convienent image format. This allows for convience in sharing and having portability in the container as the softwares are ready to be ran "out of the box". 

!> NOTE: Singularity and Containers must be ran on a compute node, as they can be resource intensive.

## Singularity vs Docker on High Performance Computing
Singularity is an open source container platform designed to be simple, fast, and secure. Unlike Docker containers which requires root privileges to run containers, Singularity is designed for ease-of-use on shared multiuser systems and in high performance computing (HPC) environments. Singularity is compatible with all Docker images and it can be used with GPUs and MPI applications.


## Creating an image using Singularity
1. `module load singularity`



### Creating a ```.sigularity``` image file

Below is an example .singularity image file that will be stored in the local directory. It uses Docker as the base Furthermore it asks to pip install numpy, scipy, matplotlib, 

``` shell 
Bootstrap: docker
From: redhat:8.6

%post
    # Commands to run in the container
    apt-get update && apt-get install -y python3 python3-pip
    pip3 install numpy scipy matplotlib

%environment
    export PATH=/usr/local/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

%runscript
    # Script to run when the container is executed
    exec python3 "$@"
    # This will exectue python3 and any arguements passed in command line. 
    #The %runscript portion here defines the default action of the container when it is executed directly (e.g., via singularity run mycontainer.sif; more on this command later)


```


## Building Singularity Image 

``` singularity build my_image.sif MyDefinitionFile.def ```

## Running Singularity Image 

``` singularity exec example.sif python3 example.py ```
**Note:** Here you can pass in the scripts that you want to execute during the running of the Singularity Image.

## Executing Commands Inside a Container

``` singularity exec example.sef "Hello World" ```

## To launch interactive mode inside a Singularity Shell

!> Remember to start an interactive job before running or launching a Singularity Shell

singularity shell example.sif