# Singularity on Pinnacles & MERCED Clusters  <!-- {docsify-ignore} -->

Singularity functions as software that facilitates the seamless execution of containers. Containers prove advantageous by consolidating all required software and dependencies into a convenient image format. This enhances convenience in sharing and ensures portability, enabling the immediate execution of software "out of the box" within the container. 

!> NOTE: Singularity and Containers need to run on a compute node, as they can consume significant resources..

## Singularity vs Docker on High Performance Computing
Singularity is an open-source container platform created for simplicity, speed, and security. In contrast to Docker, which necessitates root privileges for container execution, Singularity is tailored for user-friendly operation in shared multiuser systems and high-performance computing (HPC) environments. It seamlessly supports all Docker images and is compatible with GPUs and MPI applications.


## Creating an image using Singularity
Load the module using the following command

 ```module load singularity```



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

```singularity shell example.sif```