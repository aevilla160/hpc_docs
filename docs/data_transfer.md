# Data Transfering <!-- {docsify-ignore} -->
There are many ways to transfer data between the cluster and local workspaces. Below are instructions and descriptions of two common methods of data transfer to and from the HPC cluster.

## SCP Command
The `scp` command is useful as it is an easy and versatile command that allows for two-way transferinig of data. It does not require any setup to use and is great for constantly transfering different and seperate files or directories. `scp` is a linear and basic copy and transfer of data; therefore it does not have any failsafes to prevent data loss or data corruption. `scp` is great for simple files/directories and small, compressed files.
Below are two examples using scp, one example of transfering data from remote machine to local machine, one example of transfering data from local to remote machine. 

List of relevant options that can be used with SCP: 

| Option | Use |
|---------------|--------------------------|
| -C | Compress data before transfering | 
| -p	| Save the original file’s modification/access times, and modes |
| -r | Copy recursively; used to copy and transfer directories. |
| -v | Verbose, display the operation’s execution step by step |



### Local to Remote <!-- {docsify-ignore} -->
To transfer a file from the local machine, ensure that the command is being executed in the same directory as the file or folder or explicitly state the path in the command.
The following syntax can be used to transfer a file from a local machine to the remote machine: 

`scp [options] /path/to/file user@login.rc.ucmerced.edu:/remote/path`



### Remote to Local <!-- {docsify-ignore} -->
To transfer a file from the remote machine, ensure that the command is being executed on the local machine and the path of the file or folder is  stated in the command.
The following syntax can be used to transfer a file from the remote machine to a local machine: 

`scp [options] user@login.rc.ucmerced.edu:/remote/file.txt /local/directory`


### Video tutorial of SCP Command <!-- {docsify-ignore} -->

<p align='center'>
<iframe width="560" height="500" src="https://www.youtube.com/embed/kfHjL9_kgQA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</p>

## RSYNC Command 
The `rsync` command copies files locally or over a network. However, it employs a special transfer algorithm and a few optimizations tools to make the operation a lot faster.  If the `rync` command is given the `-a` option it will copy the exact same access privledges, this is called mirroring. Usage of the `rsync` command is great when transferring larger files and directories. There are cases where the use of `rysnc` over `scp` can result in quicker transfer times as `rsync`uses an algorithm to minimize the amount of data transferred by only transferring the portions of files that have been modified.

List of options that can be used with `rsync`:

| Option | Use |
|---------------|--------------------------|
| -a | Copy same access privledges |
| -v, --verbose	| Verbose, display the operation’s execution step by step| 
| -r |  Copy recursively; used to copy and transfer directories.|
| -u | skip updating files that are newer on the recieving end |
| -n | perform a trial run with no changes made |
| -W | copy and paste whole files, rather than only updating the changes of the file|
 

### Using Rsync <!-- {docsify-ignore} -->
To Transfer files from local machine to remote machine the `rsync` command is: 

`rsync [options] local/file/path user@login.rc.ucmerced.edu:/remote/path`

To Transfer files from remote to local machine ensure the command is executed on the local machine. The `rsync` command is: 

`rsync [options] user@login.rc.ucmerced.edd:/remote/path /local/path`

**To copy folders or directories ensure `-r` option is implemented**

