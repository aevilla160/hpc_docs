

## Modules on Pinnacles & MERCED
>Many software and library packages require specific user environment settings for successful execution or use. The Modules Environment package provides a straightforward mechanism for users to dynamically load and manage such environment settings on Pinnacles or MERCED. For example, to load the environmental variables and other settings necessary for using the Intel compiler one executes the command `module load intel`. A complete guide to the use of Modules can be found by using the command `man module` at the command line.   Here, we outlined five basic uses of Modules, we expect users find most useful information. Most commonly, users will make use of options `avail`, `load`, `list`, `unload`, and `swap`. A table describing each of these Modules options is given below.


The table below shows some most commonly used `module` commands.

| Command                       | Description                                                                            |
|:------------------------------|:---------------------------------------------------------------------------------------|
| `module avail`                | This command lists all available modules                                               |
| `module load <mod_name>`      | This command loads the environment corresponding to \<mod_name>                        |
| `module list`                 | This command provides a list of all modules currently loaded into the user environment |
| `module unload <mod_name>`    | This command unloads  the environment corresponding to \<mod_name>                     |
| `module swap <mod_1> <mod_2>` | This command unloads the environment corresponding to \<mod_1> and loads to \<mod_2>   |


Additionally, users may build code locally in one’s account so long as such codes and usage are consistent with applicable Federal law, State law, and University policies. Note that code and data placed on Pinnacles by a user can be shared with all members of the relevant PI user group by setting the desired read, write, and or executable permissions. For example, if a user in UC Merced Prof. Suzanne Sindi’s group has built an executable program named `our_program` that others in the group wish to use, the command `ls -l` can be used to check on the user group assignment and permissions. If the program is not assigned to the `ucm_ssindi` user group and/or the user group does not have executable permission, the owner can use the following commands from within the directory of our_program `chgrp ucm_ssindi our_program` and `chmod g+x our_program`.


## Software and libraries
Pinnacles offers a number of software packages and libraries for all users. A catalog of software and libraries available on Pinnacles is provided below. The command `module avail` can be used to see a full list of available Modules, Environments & packages when user login to Pinnacles, which provides a near complete list of shared packages. 

To access a list of software packages and libraries for MERCED, use the commmand `module avail -M merced` to see MERCED-only softwares & libraries. A catalog of software and libraries available on MERCED is below. 

!> Pinnacles is the default and free cluster that all users have access to and all jobs and applications run on. MERCED is the recharge-model cluster that only users that are associated with a COA nunber have access to use.


## Pinnacles Module list


| Modules   | Version | website                              |
|:----------|:--------|:-------------------------------------|
| Amber |20-devel | [website](https://ambermd.org/index.php) |
| Amber | 20 | [website](https://ambermd.org/index.php) | 
|  Anaconda3 | 2021.05 | [website](https://www.anaconda.com/) |
| AWScli | 1.16.308 | [website](https://aws.amazon.com/cli/) |
| bamtools | 2.5.1 | [website](https://bioinformatics.readthedocs.io/en/latest/bamtools/) |
| bcftools | 1.12 | [website](https://bioconda.github.io/recipes/bcftools/README.html) | 
|  bcl2fastq2 | 2.20.0.422 | [website](https://github.com/brwnj/bcl2fastq) |
| BEAST | 1.10.4 | [website](https://beast.community/) | 
| BEAST2 | 2.6.4 | [website](https://www.beast2.org/) | 
| bedtools2 | 2.6.4 | [website](https://bedtools.readthedocs.io/en/latest/index.html#) | 
| BerkeleyGW | 3.0.1-intel-mvapich2, 3.0.1-intel-2021.4.0, 3.0.1 | [website](https://berkeleygw.org/) | 
| Bowtie | 1.3.0 | [website](https://bowtie-bio.sourceforge.net/index.shtml) | 
| Bowtie2 | 2.4.2 | [website](https://bowtie-bio.sourceforge.net/bowtie2/index.shtml) |
| BRAKER | 2.1.6 | [website](https://github.com/Gaius-Augustus/BRAKER) |
| butterflypack | 2.0.0 | [website](https://github.com/liuyangzhuan/ButterflyPACK)|
| bwa-mem2 | 2.2.1 | [website](https://bioconda.github.io/recipes/bwa-mem2/README.html) |
| casacore | 3.4.0 | [website](https://github.com/casacore/casacore) |
| cgal | 5.0.3 | [website](https://www.cgal.org/) |
| cmake | 3.21.4 | [website](https://cmake.org/) |
| cmaq | 5.3.1| [website](https://www.epa.gov/cmaq) |
| COLLIER | 1.2.5 | [website](https://collier.hepforge.org/index.html) | 
| cuda | 10.2.89, 11.0.3, 11.4.0, 11.5.0, 11.8.0 | [website](https://developer.nvidia.com/cuda-toolkit) |
| Dakota | 6.12 | [website](https://www.dakotasoft.com/) |
| Dalton | 2020.0 | [website](https://daltonprogram.org/) |
| ELPA | 2021.11.001 | [website](https://xconfigure.readthedocs.io/en/latest/elpa/) |
| Emacs | 27.2 | [website](https://www.gnu.org/s/emacs/) |
| fastqc | 0.11.9 | [website]( ) | 
|  ffmpeg | 4.3.2 | [website](https://ffmpeg.org/) |
| fftw | 3.3.10-gcc.8.5.0, 3.3.10-intel-2021.4.0 | [website]( ) |
| GATE | 9.0 | [website](https://gate-software.com/en/home-page/) |
| gatk | 4.2.2 | [website](https://github.com/broadinstitute/gatk/releases) |
|Gaussian|g09, g09-b01, b09-d01, g16, g16-b01, gdv, gdv-20150105-i02+, gdv-20150518-i03+, gdv-20160512-i06, gdv-20160804-i09, gdv-20170407-i10+, gdv-20200106-j05, gdv-20210302-j15|[website](http://gaussian.com/)|
| gcc | 8.4.1, 11.2.0 | [website](https://gcc.gnu.org/) |
| git | 2.37.0 | [websit](https://git-scm.com/) | 
| glpk | 4.65 | [website](https://www.gnu.org/software/glpk/) |
| gromacs | 2021.3 | [website](https://www.gromacs.org/) |
| gnuplots | 5.4.2 | [website](http://www.gnuplot.info/) | 
| grace | 5.4.2 | [website]() | 
| GROMACS |2021.3, 2022.3|[website](http://www.gromacs.org/)|
| gsl | 2.7 | [website](https://www.gnu.org/software/gsl/) | 
| gurobi | 9.5.0| [website](https://www.gurobi.com/) |
| HDF5 |1.10.5-intel-2021.4.0 | [website](http://www.hdfgroup.org/solutions/hdf5/)|
| ibamr | .8.0-testing, .12.0-debug-cmake, .12.0-debug, .12.0-opt-cmake, .12.0-opt | [website]() | 
| intel-mkl | 2020.4.304 | [website](https://www.intel.com/content/www/us/en/docs/onemkl/get-started-guide/2023-0/overview.html) |
| intel | 2021.4.0 | [website](https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit.html#gs.zt5r3c) |
| interproscan	 | 5.54-87.0| [website](https://www.ebi.ac.uk/interpro/download/) |
| iqtree	 | 2.1.3 | [website](http://www.iqtree.org) |
| jellyfish | 2.2.7 | [website](https://jellyfish.co/) |
| julia | 1.7.3 | [website](https://discourse.julialang.org/) | 
| lammps | 20210310+kokkos+cuda, 20210310+user-omp+kokkos, 20210310, 20220107+ml - quip, 20220107, 20230208 | [website](https://www.lammps.org/) |
| latte | 1.2.2 | [website](https://www.math.ucdavis.edu/~latte/software.php) |
| lftp | 4.9.2 | [website](https://lftp.yar.ru/) |
| libtirpc | 1.1.4 | [website](https://www.linuxfromscratch.org/blfs/view/svn/basicnet/libtirpc.html) |
| localcolabfold | 1.5.1 | [website](https://github.com/YoshitakaMo/localcolabfold) |
| mathematica | 12.3.1| [website](https://www.wolfram.com/mathematica/) |
| matlab | r2021b, r2023a | [website](https://www.mathworks.com/products/matlab.html) |
| minimap2 | 2.14 | [website](https://github.com/lh3/minimap2) |
| molden | 6.7 | [website](https://www3.cmbi.umcn.nl/molden/) |
| MPICH |3.4.2-gcc-8.4.1, 3.4.2-intel-2021.4.0, 3.4.2-nvidiahpc-21.9-0 | [website](http://www.mpich.org/)|
| multiqc	 | 1.7 | [website](https://bioconda.github.io/recipes/multiqc/README.html) |
| MVAPICH |2.3.6-gcc-8.4.1, 2.3.6-intel-2021.4.0|[website](http://mvapich.cse.ohio-state.edu/)|
| ncbi-blast | 2.12.0 | [website](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) |
| netliib-lapack | 3.9.1 | [website](https://www.netlib.org/lapack/) |
| NVIDIA HPC | 21.9-0 |[website](https://developer.nvidia.com/hpc-sdk)|
| onnx | 1.10.1 | [website](https://github.com/onnx/onnx) | 
| openbabel | 3.0.0 | [website](http://openbabel.org/wiki/Main_Page) |
| openblas | 0.3.18, 0.3.21 | [website](https://www.openblas.net/) | 
| opencarp | 8.1 | [website](https://opencarp.org/) |
| openjdk | 17.0.5_8 | [website](https://github.com/openjdk/jdk) |
| openmpi |3.1.3-gcc, 3.1.6-gcc-8.4.1, 3.1.6-intel-2021.4.0,3.1.6-nvidiahpc-21.9-0,4.0-merced-test, 4.0.6-gcc-8.4.1,openmpi/4.0.6-intel-2021, 4.0.6-nvidiahpc-21.9-0,4.1.1-gcc-8.4.1, 4.1.1-intel-2021.4.0| [website](https://www.open-mpi.org/) |
| orca | 5.0.1 | [website](https://orca.security/) |
| OrthoFinder	 | 2.5.2 | [website](https://github.com/davidemms/OrthoFinder) |
| Phyluce		 | 1.6.7 | [website](https://phyluce.readthedocs.io/en/latest/installation.html) |
| picard | 2.26.2 | [website](https://github.com/broadinstitute/picard) |
| pigz | 2.7 | [website](https://github.com/madler/pigz) |
| protobuf | 3.18.0 | [website](https://github.com/protocolbuffers/protobuf) |
| quantum-espresso | 6.7-intel-test, 7.1, 7.2-gcc-openblas | [website](http://www.quantum-espresso.org/) |
| r | 4.2.2 | [website](https://www.r-project.org/) | 
| rclone | 1.59.1 | [website](https://rclone.org/) |
| repeatedmodeler | 1.0.11 | [website](https://www.repeatmasker.org/RepeatModeler/)
| samtools | 1.13 | [website](http://www.htslib.org/) |
| scalapack | 2.1.0 | [website](http://www.netlib.org/scalapack/) |
| schrodinger | 2022-1,2022-3 | [website](https://www.schrodinger.com/) |
| sickle | 1.33 | [website](https://bioweb.pasteur.fr/packages/pack@sickle@1.33) |
| Singularity | 3.8.3 | [website](https://github.com/apptainer/singularity) |
| smalt | 0.7.6 | [website]() | 
| Sombrero | 2021-08-16 | [website](https://github.com/sa2c/sombrero) | 
| Spiral | 8.2.0 | [website](http://spiral.net/index.html) | 
| srilm | 1.7.2 | [website](http://www.speech.sri.com/projects/srilm/) |
| Stata | 17 | [website](https://www.stata.com/) | 
| Stacks	 | 2.53 | [website](https://catchenlab.life.illinois.edu/stacks/) |
| Subversion | 1.14.1 | [website](https://subversion.apache.org/) | 
| Tcl | 8.5.19-gcc-8.5.0 | [website](https://www.tcl.tk/) | 
| TeraChem | 1.95 | [website](http://www.petachem.com/products.html) | 
| tk | 8.5.19-gcc-8.5.0 | [website](https://www.tcl.tk/software/tcltk/8.5.html) | 
| TransDecoder		 | 5.5.0 | [website](https://github.com/TransDecoder/TransDecoder/releases) |
| Trimmomatic | 0.39 | [website](http://www.usadellab.org/cms/?page=trimmomatic) |
| Trinity	 |2.12.0 | [website](https://github.com/trinityrnaseq/trinityrnaseq) |
| VCFtools | 0.1.14 | [website](https://vcftools.sourceforge.net/) |
| VMD |1.9.1,  1.9.3 | [website](https://www.ks.uiuc.edu/Research/vmd/) |
| wannier90 | 3.1.0 | [website](http://www.wannier.org/) |
| XCrySDen|1.5.60, 1.6.2|[website](http://www.xcrysden.org/)|

## MERCED Module list

| Name                  | Version| Website                                                |
|:-------------------------|:----------------------------------------------------------------|:------------|
|bwa-mem2|2.2.1|[website](https://bioconda.github.io/recipes/bwa-mem2/README.html)|
|BerkeleyGW|3.0.1-intel-mvapich2|[website](https://berkeleygw.org/)|
|Intel-mkl|2020.4.304|[website](https://www.intel.com/content/www/us/en/docs/onemkl/get-started-guide/2023-0/overview.html)|
|OpenMPI|4.0-merced-test|[website](https://www.open-mpi.org/)|




## Clusters Queue Information

 **The available queues are designed to balance use and accessibility to the clusters for all users. If a submitted job does not complete before reaching the maximum wall time limit, the queue system will terminate the calculation. In an effort to provide a balanced access to compute cycles on Pinnacles & MERCED, the course queue resource limitations and user-level queue resource limitations become increasingly restrictive. Therefore, users are advised to use the most limiting queue that satisfies their computational needs. In other words, users __should not__ default their work to `compute` for MERCED or `short` for Pinnacles. It is essential for the best use of the clusters that users develop an awareness of their resource needs.**:

There are 6 types of queues on Pinnacles, and each type of queue has its own configurations and policy. The details is shown in the table below.

| Queue types | Maximum wall-clock time | Default time | Max nodes | Job limits |
|:------------|:------------------------|:-------------|:----------|:-----------|
| test        | 1hr                     | 5min         | 2         | 1          |
| bigmem      | 3d                      | 1hr          | 2         | 2          |
| gpu         | 3d                      | 1hr          | 2         | 4          |
| short       | 6hr                     | 1hr          | 4         | 12         |
| medium      | 1d                      | 6hr          | 4         | 6          |
| long        | 3d                      | 1d           | 4         | 3          |



* For example, in order to test jobs on GPU nodes, use the following line in Slurm submission script 
`#SBATCH --constraint=gpu`
Note: Access to GPUs also requires `#SBATCH --gres=gpu:X`, X represents how many resources are required. For example:
`#SBATCH--gres=gpu:2`
In order to test job on bigmem node:
`#SBATCH --constraint=bigmem`
* Short queue is the default queue. If user does not specify the partition or the queue type in the job script, the job will be submitted to the short queue
* Default time means that If users do not specify the wall-clock time, the default time will be used. If job does not finish by the wall time then it will be terminated by the scheduling system.
* Max node means maximum number of nodes per job, if exceed this limit, user will see `PartitionNodeLimit` on the queue for the job, and the specific job will not be picked up.
* Job limits: for each type of queues, only a limited number of jobs per user is allowed to submit, if exceed the limit, user will not be able to submit more and a message of `sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)` will appear.


There are 3 types of queues on MERCED, and each type of queue has its own configurations and policy. The details is shown in the table below.

| Public Queues(Available to all users)| Max Wall Time | Default Time | Max Nodes per Job | Max # of jobs that can be submitted | 
| -------------------------------------|---------------|--------------|-------------------|-------------------------------------|
| bigmem | 5 days | 1 hr | 2 nodes | 6 | 
| test^ | 1 hour | 5 min. | 2 nodes | 1 |
| *compute | 5 days | 1 hr | 2 nodes | 6 | 


* <span style="color: red;"> `#SBATCH -M merced ` must always be used to submit a job to MERCED cluster</span>
* <span style="color: red;"> ^ `test` queue has access to all node types use constraints to test on specific types. </span>
* <span style="color: red;"> \* `compute` queue is the default queue for all jobs submitted  </span>

!> NOTE: MERCED cluster general queues maximum job submissions per user is set to 20 which means user can not submit more than 20 jobs at a time.

!> Production calculations must be run using the queueing and scheduling system. Computationally intensive calculations __should never be run on the head or login node__. MERCED & Pinnacles makes use of __Slurm__. Detailed information regarding Slurm is available from a number of online resources. 


