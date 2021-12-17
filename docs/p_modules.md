## Software and libraries
Pinnacles offers a number of software packages and libraries for all users. A catalog of software and libraries available on Pinnacles is provided below. The command `module avail` can be used to see a full list of available Modules 
Environments packages when user login to Pinnacles, which provides a near complete list of shared packages. 

Additionally, users may build code locally in one’s account so long as such codes and usage are consistent with applicable Federal law, State law, and University policies. Note that code and data placed on Pinnacles by a user can be shared with all members of the relevant PI user group by setting the desired read, write, and or executable permissions. For example, if a user in UC Merced Prof. Suzanne Sindi’s group has built an executable program named `our_program` that others in the group wish to use, the command `ls -l` can be used to check on the user group assignment and permissions. If the program is not assigned to the `ucm_ssindi` user group and/or the user group does not have executable permission, the owner can use the following commands from within the directory of our_program `chgrp ucm_ssindi our_program` and `chmod g+x our_program`.

| Modules   | Version | website                              |
|:----------|:--------|:-------------------------------------|
| anaconda3 | 2021.05 | [website](https://www.anaconda.com/) |
| opencarp | 8.1 | [website](https://opencarp.org/) |
| awscli | 1.16.308 | [website](https://aws.amazon.com/cli/) |
| openmpi | 3.1.6-gcc-8.4.1, 3.1.6-intel-2021.4.0,3.1.6-nvidiahpc-21.9-0, 4.0.6-gcc-8.4.1,openmpi/4.0.6-intel-2021, 4.0.6-nvidiahpc-21.9-0,4.1.1-gcc-8.4.1, 4.1.1-intel-2021| [website](https://www.open-mpi.org/) |
| bamtools | 2.5.1 | [website](https://bioinformatics.readthedocs.io/en/latest/bamtools/) |
|  bcl2fastq2 | 2.20.0.422 | [website](https://github.com/brwnj/bcl2fastq) |
|  beast | 1.10.4 | [website](https://beast.community/) |
| beast2 | 2.6.4 | [website](https://www.beast2.org) |
| butterflypack | 2.0.0 | [website](https://github.com/liuyangzhuan/ButterflyPACK)|
| casacore | 3.4.0 | [website](https://github.com/casacore/casacore) |
| cgal | 5.0.3 | [website](https://www.cgal.org/) |
| cmake | 3.21.4 | [website](https://cmake.org/) |
| cmaq | 5.3.1| [website](https://www.epa.gov/cmaq) |
| dakota | 6.12 | [website](https://www.dakotasoft.com/) |
| dalton | 2020.0 | [website](https://daltonprogram.org/) |
| emacs | 27.2 | [website](https://www.gnu.org/s/emacs/) |
|  ffmpeg | 4.3.2 | [website](https://ffmpeg.org/) |
| gate | 9.0 | [website](https://gate-software.com/en/home-page/) |
| gcc | 8.4.1, 11.2.0 | [website](https://gcc.gnu.org/) |
| glpk | 4.65 | [website](https://www.gnu.org/software/glpk/) |
| gromacs | 2021.3 | [website](https://www.gromacs.org/) |
| gurobi | 9.5.0| [website](https://www.gurobi.com/) |
| jellyfish | 2.2.7 | [website](https://jellyfish.co/) |
| lammps | 20210310+kokkos+cuda, 20210310+user-omp+kokkos, 20210310 | [website](https://www.lammps.org/) |
| latte | 1.2.2 | [website](https://www.math.ucdavis.edu/~latte/software.php) |
| lftp | 4.8.1 | [website](https://lftp.yar.ru/) |
| mathematica | 12.3.1| [website](https://www.wolfram.com/mathematica/) |
| matlab | r2021b | [website](https://www.mathworks.com/products/matlab.html) |
| molden | 6.7 | [website](https://www3.cmbi.umcn.nl/molden/) |
| openbabel | 3.0.0 | [website](http://openbabel.org/wiki/Main_Page) |
| opencarp | 8.1 | [website](https://www.anaconda.com/) |
| orca | 5.0.1 | [website](https://orca.security/) |
| protobuf | 3.18.0 | [website](https://github.com/protocolbuffers/protobuf) |
| quantum-espresso | 6.7 | [website](http://www.quantum-espresso.org/) |
| samtools | 1.13 | [website](http://www.htslib.org/) |
| scalapack | 2.1.0 | [website](http://www.netlib.org/scalapack/) |
| vmd | 1.9.3 | [website](https://www.ks.uiuc.edu/Research/vmd/) |

## Queue details
There are 6 types of queues on Pinnacles, and each type of queue has its own configurations and policy. The details is shown in the table below.

| Queue types | Maximum wall-clock time | Default time | Max nodes | Job limits |
|:------------|:------------------------|:-------------|:----------|:-----------|
| test        | 1hr                     | 5min         | 2         | 1          |
| bigmem      | 3d                      | 1hr          | 2         | 2          |
| gpu         | 3d                      | 1hr          | 2         | 2          |
| short       | 6hr                     | 1hr          | 4         | 12         |
| medium      | 1d                      | 6hr          | 4         | 6          |
| long        | 3d                      | 1d           | 4         | 3          |

!> test queue has access to all node types. In order to test jobs on specific node types, please use Slurm `constraints` flag. 


* For example, in order to test jobs on GPU nodes, use the following line in Slurm submission script 
`#SBATCH --constraint=gpu`
Note: Access to GPUs also requires `#SBATCH --gres=gpu:X`, X represents how many resources are required. For example:
`#SBATCH--gres=gpu:2`
In order to test job on bigmem node:
`#SBATCH --constraint=bigmem`
* Short queue is the default queue. If user does not specify the partition or the queue type in the job script, the job will be submitted to the short queue
* Default time means that If users do not specify the wall-clock time, the default time will be used.
* Max node means maximum number of nodes per job, if exceed this limit, user will see `PartitionNodeLimit` on the queue for the job, and the specific job will not be picked up.
* Job limits: for each type of queues, only a limited number of jobs per user is allowed to submit, if exceed the limit, user will not be able to submit more and a message of `sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)` will appear.


