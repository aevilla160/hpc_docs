## Borgstore(BeeGFS)
Borgstore is UC Merced's on campus data-storage center that has [HOW MUCH SIZE is the Capacity]. Borgstore is used for active,research-related data and has the capacity of 480 **terrabytes**. 


Borgstore is made up of *JKJDFJDKL* metadata server with a1U dual Xeon Skylake SP, 8x 2.5" Hotswap, 24 DIMM Sockets, IPMI, dual 10GbE-T base system and 8x 3.2TB Endurance Data Center PCIe NVMe 2.5" Solid State Drive metadata storage


### Requesting Borgstore
Borgstore is a purchasable service that can be requested [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4). Cost for active data storage is $0.05/GB/year (startup funds) and $0.06/GB/year (non-startup funds). More information can be found [here](https://it.ucmerced.edu/Research-Computing-Services).

### Accessing Borgstore

#### Accessing Data from Borgstore during scheduled job

To access data that is located in Borgstore the user must be in the Borgstore folder directory and must submit job to the scheduler from there.  If users want to submit jobs while at the Borgstore folder, the slurm option of `#SBATCH --constraint=ib` should be added to the job script. A sample job that uses this slurm option can be found [here](https://ucmerced.github.io/hpc_docs/#/running_jobs).

To run an interactive job, the job must also be ran from the borgstore directory. 

>How to check my current occupied space on Borgstore?
>
>Users can not check a detailed-breakdown of a group's users and their respective useage of the Borgstore storage. Users can check thier Groups storage usage/total using the command beegfs-ctl --getquota --gid # Users can check their ID number and Group ID # via the command id <username>.
