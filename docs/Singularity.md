# Using Singularity with the Clusters
Singularity can be a useful software when you need to have multiple software packages and configurations made and distributed for other users to use and collaborate on.

Singularity acts as a software that puts all the specs(softwares, environment configuration, etc.) into a `container` that reduces the need for configuration and other distribution issues. This enhances convenience in sharing and ensures portability, enabling the immediate execution of software "out of the box" within the container.

## Building a Container for use on the Clusters
Prerequisite: Create an account with [Sylabs Cloud](https://cloud.sylabs.io/). This will allow us to create singularity images remotely. Furthermore users can also build definition files of images for other collaborators to access via the cloud. 

1. Create a definition file that contains the instructions to build a configure with the proper packages, softwares and other specs. This `.def` file ending denotes a definition file that singularity interprets as an instruction file.

Below is an example definition script that builds a container with python and some other python packages

``` shell 
Bootstrap: docker
From: python:3.8-slim

%post
    apt-get update && apt-get install -y \
            build-essential \

    pip install --upgrade pip
        pip install numpy pandas matplotlib scipy

%environment
    export PATH=/usr/local/bin:$PATH


%runscript
    exec python "$@"
``` 

2. Start an interactive session and log into the allocated compute node. For more information on running a interactive session view [here](running_jupyter.d)

!> All of the following commands must be run on a compute node as they are resource-intensive

Because users of Pinnacles and MERCED do not have sudo access, user must create their containers on Singularity's cloud base for all public containers. Refer to prerequisite material to ensure creation and access to [Sylab Cloud](https://cloud.sylabs.io/dashboard). 

3. Run the command ``singularity remote login ``. 

4. Now you will be prompted on entering an authorization token from Sylabs. Follow the below guide on generating a token. 

        
        a. Click on Access tokens from the Sylab Cloud https://cloud.sylabs.io/dashboard.

        b. Enter a simple alias to remember the purpose of creating the token

        c. Generate the token

        d. The generated token will be displayed here. 

    ![Sylab Homepage image](imgs/sylab2image.png "Sylab Homepage Image")

5. Return to the cluster and enter the following ```singularity remote login```
        
    Enter in the token displayed. 

    If successful, a message of approval should display

6. Build the singularity container from the definition file using the following command: `singularity build --remote container_name.sif definition_filee.def`

It will now begin the process of building the container and it may take a few minutes depending on the size and configurations stated in the definition file. All singularity image files will be of type `.sif`

7. The container should now be listed in the current directory.


## Interacting with Singularity Container

!> All of these commands should still be run on a compute node!

### Running a container <!-- {docsify-ignore} -->

Use the following command: `singularity run <container.sif>

Running the container, launches an instance of the container application or environment as configured in the build file. What application/environment that will launch from the container will vary. 

For example, referring to the example build file, the container that was created from that file allows for an interactive python session if the container is being run. 

### Shell Into the container <!-- {docsify-ignore} -->

Use the following command: `singularity shell <container.sif>

Running a shell places the user in an interactive command-line interface within the container. Once inside the shell users can run applications and scripts with the softwares installed in the container, test and debug scripts and access files in the container. 


### Execute a command inside container <!-- {docsify-ignore} -->

Use the following command: `singularity exec <container.sif> <command(s)>`

This allows the user to execute commands in a singularity container without having to enter the container. 

