## Modules on MERCED
>Many software and library packages require specific user environment settings for successful execution or use. The Modules Environment package provides a straightforward mechanism for users to dynamically load and manage such environment settings on MERCED. For example, to load the environmental variables and other settings necessary for using the Intel compiler one executes the command `module load intel`. A complete guide to the use of Modules can be found by using the command `man module` at the command line on MERCED. Here, we outlined five basic uses of Modules, we expect users find most useful information. Most commonly, users will make use of options `avail`, `load`, `list`, `unload`, and `swap`. A table describing each of these Modules options is given below. Examples using Modules are given in a number of submission scripts shown below.

The table below shows some most commonly used `module` commands.

| Command                       | Description                                                                            |
|:------------------------------|:---------------------------------------------------------------------------------------|
| `module avail`                | This command lists all available modules                                               |
| `module load <mod_name>`      | This command loads the environment corresponding to \<mod_name>                        |
| `module list`                 | This command provides a list of all modules currently loaded into the user environment |
| `module unload <mod_name>`    | This command unloads  the environment corresponding to \<mod_name>                     |
| `module swap <mod_1> <mod_2>` | This command unloads the environment corresponding to \<mod_1> and loads to \<mod_2>   |

## Software and libraries
MERCED offers a number of software packages and libraries for all users. A catalog of software and libraries available on MERCED is provided below. The command `module avail` can be used to see a full list of available Modules Environments packages when user login to MERCED, which provides a near complete list of shared packages. Additionally, users may build code locally in one’s account so long as such codes and usage are consistent with applicable Federal law, State law, and University policies. Note that code and data placed on MERCED by a user can be shared with all members of the relevant PI user group by setting the desired read, write, and or executable permissions. For example, if a user in UC Merced Prof. Suzanne Sindi’s group has built an executable program named `our_program` that others in the group wish to use, the command `ls -l` can be used to check on the user group assignment and permissions. If the program is not assigned to the `ucm_ssindi` user group and/or the user group does not have executable permission, the owner can use the following commands from within the directory of our_program `chgrp ucm_ssindi our_program` and `chmod g+x our_program`.

| Name                  | Version| url                                                |
|:-------------------------|:----------------------------------------------------------------|--|
|Amber|20|[website](http://ambermd.org/)|
|Anaconda|3.6.11|[website](http://www.anaconda.com/)|
|ARPACK|3.7.0|[website](https://www.caam.rice.edu/software/ARPACK/)|
|ATLAS|3.10.3|[website](http://guix.gnu.org/packages/atlas-3.10.3/)|
|bcl2fastq2|v2,20.0.422||
|BerkeleyGW|2.1|[website](https://berkeleygw.org/)|
|Cell Ranger|6.0.1	|[website](http://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger)|
|CMake|3.12.0|[website](https://cmake.org/)|
|CMUSphinx|3.0.12|[website](https://cmusphinx.github.io/)|
|CUDA|11.2,11.2.1, 5.0, 7.5, 9.0|[website](https://developer.nvidia.com/cuda-toolkit)|
|Gaussian|g09, g09-b01, b09-d01, g16, g16-b01, gdv, gdv-20150105-i02+, gdv-20150518-i03+, gdv-20160512-i06, gdv-20160804-i09, gdv-20170407-i10+, gdv-20200106-j05, gdv-20210302-j15|[website](http://gaussian.com/)|
|GCC - the GNU Compiler Collection|10.2.0, 7.2.0, 7.3.0|[website](http://gcc.gnu.org/)|
|GDAL|2.2.4|[website](https://gdal.org/)|
|gflags|master|[website](https://github.com/gflags/gflags)|
|glog|0.3.3||
|GLPK|5.0|[website](https://www.gnu.org/software/glpk/)|
|Gurobi|9.1.1|[website](https://www.gurobi.com/)|
|GROMACS|5.0.7|[website](http://www.gromacs.org/)|
|HDF5|1.10.5|[website](http://www.hdfgroup.org/solutions/hdf5/)|
|i-ADHoRe|3.0|[website](http://bioinformatics.psb.ugent.be/software/details/i--ADHoRe)|
|IBAMR|0.8.0||
|Intel|2015.0.090, 2016.3.210, 2016_Update4_modulefile, 2017.4.056(default), (mpi) 2019.9.304, parallel_studio_xe_2020||
|Java|11.0.11|[website](https://www.java.com/en/)|
|LAMMPS|2016, 22Aug2018|[website](https://www.lammps.org/)|
|Libxc|3.0.0 intel, 4.2.3|[website](https://www.tddft.org/programs/libxc/)|
|Lumerical|2020a-r7-2347-ba4b47e008|[website](http://www.lumerical.com/)|
|MATLAB|2016b, 2018b, R2020a|[website](https://www.mathworks.com/products/matlab.html)|
|MPICH|intel - 3.1.3|[website](http://www.mpich.org/)|
|MVAPICH|2-2.2|[website](http://mvapich.cse.ohio-state.edu/)|
|NCBI - BLAST|2.11.0+|[website](https://blast.ncbi.nlm.nih.gov/Blast.cgi)|
|NVIDIA HPC|20.9, 21.2 (default)|[website](https://developer.nvidia.com/hpc-sdk)|
|Octopus|8.2|[website](https://octopus.com/)|
|Open MPI|4.1.1, 1.6/gcc, 1.6/intel, 1.8/gcc, 1.8/intel, 2.0/gcc, 2.0/intel, 4.0/gcc|[website](http://www.open-mpi.org/)|
|PEAR - PHP|0.9.10|[website](http://pear.php.net/)|
|PGi|16.10, 16.4, 16.5, 16.7, 17.10(default), 17.5, 17.7, 2016, 2017|[website](https://www.pgi.com/)|
|Quantum ESPRESSO|6.1, 6.4.1, 6.6|[website](http://www.quantum-espresso.org/)|
|ScaLAPACK|2.0.2|[website](http://www.netlib.org/scalapack/)|
|Sylabs.io - Singularity|2.4.2|[website](https://sylabs.io/singularity)|
|VMD|1.9.3|[website](http://www.ks.uiuc.edu/Research/vmd/vmd-1.9.3/)|
|SRI Language Modelling Toolkit (SRILM)|gcc - 4.8.5||
|XCrySDen|1.5.60, 1.6.2|[website](http://www.xcrysden.org/)|

## Queue details
Production calculations must be run using MERCED’s queueing and scheduling system. As stated earlier, computationally intensive calculations __should never be run on the head or login node__. MERCED makes use of __Slurm__. Detailed information regarding Slurm is available from a number of online resources. This section provides a brief description of the Slurm system, an overview of the specific queueing environment employed on MERCED, and a set of example submission scripts. The table below provides a brief overview of available queues and standard maximum resource limitations.

The available queues are designed to balance use and accessibility to the cluster for all users. Three of the queues – `std.q`, `fast.q`, and `long.q` – are distinguished from one another by the required wall time of the submitted job. The fourth available queue is the `gpu.q` queue. Requesting this queue is necessary for calculations that require the access to GPUs. If a submitted job does not complete before reaching the maximum wall time limit, the queue system will terminate the calculation. In an effort to provide a balanced access to compute cycles on MERCED, the course queue resource limitations and user-level queue resource limitations become increasingly restrictive. Therefore, users are advised to use the most limiting queue that satisfies their computational needs. In other words, users __should not__ default their work to long.q. It is essential for the best use of MERCED that users develop an awareness of their resource needs.

| Queue  | Max wall time | Max cores | Description                                                  |
|:-------|:--------------|:----------|:-------------------------------------------------------------|
| test  | 1 hrs        | 40       | This queue is for testing, max job limit is 2                            |
| compute | 5 days         | 350       | This queue is for fast jobs                                  |
| long.q | 14 days       | 350       | This queue is for long-running jobs                          |
| gpu.q  | 7 days       | 350 | This queue is used to request nodes with available GPU cards |




