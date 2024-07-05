## Secure shell (SSH)
The standard method for connecting to remote machine is by Secure Shell `ssh`
commands. After 02/01/2023, we will be using centralized login, which means once user login to the login node they will be able to connect to either MERCED or Pinnacles. Users who apply for Pinnacles account can start the application [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0), and Pinnacles is free to use within campus, however, if users want to use MERCED cluster (other than test queue) they will need to provide **COA** account information starting **02/01/2023**.


## Terminal application
On Mac and Linux you can use the built-in terminal application; on
Windows you can use
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install) or [Moba
XTERM](https://mobaxterm.mobatek.net/) to open a terminal, and type the
following command, but replace `<username>` to your UCMID.
```bash
ssh <username>@login.rc.ucmerced.edu
```
!> Using `ssh` to connect to the centralized login node so that **you will be able to submit jobs to either MERCED or Pinnacles**. 

Currently, we have 3 login nodes, users are expecting to see they are placed to either `rclogin01`, `rclogin02`, or `rclogin03`. __Do not run computationally intensive processes on the login node__. File preparation/editing, compiling, simple analyses, and other low computational cost activities are appropriate on the login node, but, again, other types of work should be submitted to the cluster via the available queue system. Users may also connect to remote machine using an x-terminal (XQuarz or X11) to spawn graphics based programs such as gnuplot, gimp, _etc_. 


## X11 Forwarding
X11 is a graphics protocol that allows user to interact with the GUI from remote servers on their local resources.

Here are some examples of the different requirements that X11 needs to be enabled by the client connecting to the cluster to use X11.
### Mac Configuration <!-- {docsify-ignore} -->
Prerequisite: 
Successfully install XQuartz 

Then open XQuartz through `open -a XQuartz` in the terminal or other CLI.

Finally ssh into the cluster with using the `-X` flag added. Ex
`ssh -X <username>@login.rc.ucmerced.edu`

### Windows Configuration <!-- {docsify-ignore} -->
If using PuTTY as the SSH client, enable X11 forwarding through the PuTTY configuration settings.
1. Open PuTTY.
2. In the configuration window, navigate to the "Connection" category.
3. Expand the "SSH" category within "Connection".
4. Click on "X11".
5. Check the box labeled "Enable X11 forwarding".
6. Optionally, you can adjust other settings related to X11 forwarding as needed.
7. Save your session settings.
Connect to your remote system as usual!


## File systems and storage
In the following, we will assume you have some familiarity with linux; if you do not, feel free to book a consultation with the IT team, but a lot of resources are available on the internet.

After connecting to the cluster you can run `ls` command
to see the available content:
```bash
$ ls
data scratch
```
Once user log in,there are 2 folders (`data` and `scratch`) locate in `HOME` that user will start with.

!> MERCED and Pinnacles are now merged into one centralized system, therefore, we increased quota for `data` `scratch` and `home` folders. Please keep in mind that **there is only 7 day grace period from when hitting the soft quota**.

|Folder|soft quota|hard quota|
|--|--|--|
|`/home/<UCMID>/data`|500G|512G|
|`/home/<UCMID>/scratch`|500G|512G|
|`/home/<UCMID>/`|70G|75G|

### Checking Disk Quota and Usage  <!-- {docsify-ignore} -->

To look at your current usage amounts of `/home`, `/data` or `/scratch` use the following command 

    quota -vs 

This will output, in sections, the filesystem, space currently used, quoata, hard limit and some other pieces of information in  a more readable format. 

**Note:** To convert the outputted megabytes to gigabytes = space(MB) divided by 1024

!> To check quota limits on Borgstore, click [here](borgstore.md).

### Checking the Size of Directories and Contents <!-- {docsify-ignore} -->

To chek the size of the current directory or any directories in it use the `du` command. 

**Note:** `du` command alone will output all directories, hidden as well, in real time so it will take a few momments to finish. It is recommended to execute the command with some form of the following options to make the process more clear and consice. 

|Option| Use |
|---------------------------|----------------------|
| -h | Will display the storage values in only two values in kb,mb,gb|
|-s | summarizes the size of the whole, current directory |
| -sh <Directory> | Shows the size of the specfied sub-directory |
|  --max-depth=N | Only show the sub-directories up to N depth, where N is a number representing the max sub-directory to display | 
|--all | write counts for all files, not just directories |
| --help | Display all other options for the `du` command | 

Example demonstrating use of `du` command 

    du -h -s <directory name>

Outputs the follwing 

    35G     <directory name>


!> Users who submit jobs to MERCED and use the unified storage are expecting slower network communications. Home - Shared over 10G network from Pinnacles to Merced. connected over IB on pinnacles. Data - Shared over 10G network from Pinnacles to Merced. connected over IB on pinnacles. Scratch - Shared over 10G network from Pinnacles to Merced. connected over IB on pinnacles

* Store in `data`, all that is research grade data that need to be backed-up and safe.
* Put in `scratch`, everything that is temporary; files will be removed from scratch when the total storage hits 85% full. Use it as for jobs checkpoints or
similar. Be sure to **not** leave any data that's of important to you under `scratch`.

!>The `scratch` folder is purged periodically when the overall system storage reaches 85% of capacity or higher. Please back-up your data to somewhere safe frequently.

There are also secondary file systems attached to MERCED that are associated with particular research groups or departments. However, currently only available from login node to allow transfers to Borgstore. 

|Folder|space|
|--|--|
|`/mnt/qsb`|256G|
|`/mnt/medusozoa`|Determined by PI|
|`/mnt/conness`|Determined by PI|
|`/mnt/branchinecta`|Determined by PI|

__Do not write files directly to `/tmp` on the head node__, as this may fill up disk space on the head node and cause trouble for everyone. Instead, use your own scratch directory for temporary files. Some codes may use `/tmp` by default and need to have the appropriate scratch directory configured.

## Borgstore (BeeGFS)
Borgstore is now accessible on all nodes (MERCED and Pinnacles) with Infiniband (IB), all of the partitions contain a mixture of nodes of InfiniBand and non-InfiniBand nodes. If users want to submit jobs while at the Borgstore folder, the slurm option of `#SBATCH --constraint=ib` should be added to the job script. Example job script can be found [here](running_jobs.md). More information pertaining to Borgstore can be found [here](borgstore.md)

