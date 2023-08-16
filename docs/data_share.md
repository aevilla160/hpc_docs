# Sharing Data with Other Users
This page presents ways to share data with other users on the HPC clusters. Note that the word "group" on this page always refers to Unix groups and not research groups.

## Unix Permissions
Every file and directory has read, write and execute permissions associated with it. These permissons dictate what and who has access to the file or directory and what level of access it has. The owner is you, the group is the group of people asscociated with the PI that you are apart of, and other is every other user outside the unix group. Many times others refers to every other user on the HPC clusters that are not apart of the group the current user is associated with nor other group members 

| Permission | Meaning | Meaning for directories | 
| -------------------- | ---------------- | ----------------- |
| read (r)	 | Contents of file can be viewed and displayed | Contents of directory can be listed and viewed|
| write (w) | File can be modified or deleted | Files can be created in or deleted from directory | 
| execute (x) | File can be run like a program | Directory can be entered (i.e., the cd command works) |

There are also octal or numerical counterparts to the above permissions. The numbers are added together to achieve the same effect as using any cobination of the letters. 
| Permission | Meaning | Meaning for directories | 
| -------------------- | ---------------- | ----------------- |
| 4 | Contents of file can be viewed and displayed | Contents of directory can be listed and viewed|
| 2 | File can be modified or deleted | Files can be created in or deleted from directory | 
| 1 | File can be run like a program | Directory can be entered (i.e., the cd command works) |



## Unix Special Permissions
Special permissions make up the fourth access level in addition to user, group, and other. Special permissions allow for additional privileges over the standard permissions. There are special permissions option for **user**,**group** and **other** options. 


### Set owner User ID(SUID) <!-- {docsify-ignore} -->
The special permission for the user access level has a single function: A file with SUID always executes as the user who owns the file, regardless of the user passing the command.

To locate the state of this special permission, look for an ‘s’ instead of an ‘x’ in the executable bit of the file permissions.

### Set Group User ID(SGID) <!-- {docsify-ignore} -->
This special permission has a couple of functions to change how directories and/or files are accessed from a group level. 
1. If set on a file, it allows the file to be executed as the group that owns the file.

2. If set on a directory, any files created in the directory will have their group ownership set to that of the directory owner

The use of special permissions at the group level are immensely helpful for groups who are constantly collaborating and sharing directoires and files with eachother. The use of this level of special permissions also ensures that all following-created files and sub-directories are shared with the group as well without having to redo and edit sharing permissions. 


To locate the setgid bit, look for an ‘s’ in the group section of the file permissions, as shown in the example below.

    -rwxrwsr-x 1427 August 14 2023 sample_file

To set the setgid bit, use the following command:

    chmod g+s 

To remove the setgid bit, use the following command.

    chmod g-s

### Sticky Bit <!-- {docsify-ignore} -->
Sticky Bit does not affect individual files. However, at the directory level, it restricts file deletion. Only the owner (and root) of a file can remove the file within that directory. If the sticky bit is being edited in symbolic mode then simply add `+t` preceding to the permissions.



## Setting Special Permissions
To set special permissions on a file or directory we will use one of the two methods shared below(octal or numerical) with use of the `chmod` command. 

Using the numerical method, we pass a fourth, preceding digit in our chmod command. The digit used is calculated similarly to the standard permission digits:

    Start at 0
    SUID = 4
    SGID = 2
    Sticky = 1

Example Below

1. Navigate to the directory that will have special permissions. 
2.  Next execute the following command to edit group permissions `chmod 2### directory/` or for a file `chmod 2### file.txt`

Where `2` is representing that special permissions are being set for the group

Example Template: `chmod -R $### directory/`. 

`$` - Represents the numerical number that sets the special permission. `#` - Represents the permission being inputted(r,w,x). `-R` is used here as we want to apply the changes recursivly, meaning that the changes should impact the sub-directories and files inside the directory.




## The `chmod` Command
The `chmod` command allows user to change the access mode of a file or directory.
The syntax follows 
`chmod <usertype>=<permission> file`

To change the access of directory use the following syntax: 
`chmod -R <usertype>=<permission> directory`

Where `usertype` is a variable that represents different inputs:

| usertype | meaning | 
| -------------- | --------------|
| u | represents the user |
| g | represents the group | 
| o | represnets other | 

Example of changing the permission of a directory: 

To view the current permisions of a given file or directory use:
`ls -ld <file/directory>`

The output should look similar to this: 

    drwxr-xr-x 2 <owner> <group> 10 Jul 28 14:47 permissions/

The permissions will be shown in an order of user, then group and then other(everyone else) or global. In the output above the user has read, write and excutable access. The group has read and executable access. Everyonelse on the cluster has read and executable access. 


Now the command `chmod -R  u=rwx,g=---, o=--- permissions/` will be executed and will update the permssions of the group the user is asscoiated with and everyone to not have read, write or execute access of the directory, `permissions/`. 

To view the changes and ensure they are accurate run the comamnd ls -ld 

The output should look similar to this:

    drwx------ 2 <user> <group> 10 Jul 28 14:47 permissions/ 

From this we can see that the first `rwx` correlate to the user and the empty dashes represents that the group and everyone else has lost access to the directory. 

## Public and Group-Readable Directories
It is common adjust the permissions that the group has on the file or directory.

To see what group you are apart of run the command: `groups`

Run the `groups` command to see your group(s):
Ex. output 

    ucm_test

To edit the permissions to your group run the command: 
    `chmod [options] g=<permissions> <file>`
Or
    `chmod [options] <123> file `
Where 123 represent: 1 = user permissions written in octal format, 2 = group permissions written in octal format and 3 = others' permissions written in octal format. 
Ex. of changing group permissions of a directory called `permissions` 
Syntax: 
` chmod -R g=--- permissions/`
Or through using number format: 
`chmod -R 700 permissions/`

NOTE: Here there is a 7 in the user permission column as the user needs atleast read access to change group permissions. The middle 0 represents that the all permissions to the group will be removed. The last 0 represents that all permissions will be removed from every other user not in the group

Sample output of before changing permissions: 

`drwxr----- 2 <user> <group> 10 Jul 28 14:47 permissions/`

Sample Output after changing permissions: 

`drwx------ 2 <user> <group> 10 Jul 28 14:47 permissions/`





## Access Control Lists and `setfacl` Command
Access control list(ACL) allows users to go beyond what is possible with group-readable directories and the `chmod` command. This is essential when not all members of your group should have access to the file/directory or when a user outside the user group needs access to the file/directory.

The `setfacl` command is used to change access of files or directories to individual users, multiple user groups or everyone on the cluster. The `setfacl` stands for "set file acl", where acl represents access control list. The `setfacl` command is great for modifying and removing users and groups from the access control list or users who can view and modify files or directories. It also updates and deletes ACL entries for each file and directory that was specified by path.


The -m (--modify) and -M (--modify-file) options modify the ACL of a file or directory. ACL entries for this operation must include permissions.

The -x (--remove) and -X (--remove-file) options remove ACL entries. It is not an error to remove an entry which does not exist. Only ACL entries without the perms field are accepted as parameters.

Options available for setfacl: 

| Option | Description |
| ---------------- | ---------------------- |
| --test | Test mode. Instead of changing the ACLs of any files, the resulting ACLs are listed. |
| -R, --recursive | Apply operations to all files and directories recursively. This option is needed if modifying the permissions of a directory. |
| -h, --help | Print a help message explaining the command line options. |

Generic `setfacl` syntax format: 

`setfacl [-options] [-x/-X OR -m/-M] [file/directory]`

### `getfacl` Command <!-- {docsify-ignore} -->
Another useful command, `getfacl`, is used often to simplify and display all users and groups that have access to a file or directory.
This command is paired great when using the `setfacl` command to access groups and users on the ACL of a file or directory.

Below is a list of a couple of options for `getfacl`

| Option | Description |
| --access | Display the file access control list. |
|-d, --default	| Display the default access control list. |
| -R, --recursive | Apply operations to all files and directories recursively. This option is needed if viewing the permissions of a directory. |
| --help | Print help explaining the command line options.| 



Generic syntax for the use of `getfacl` to list the access list control of a file: 

`getfacl <filename>`

Generic syntax for the use of `getfacl` to list the access of a direcotry and it's contents the syntax is as follows: 

`getfacl -R <direcotryname/`

Sample output of using `getfacl` is shown below: 

    # file: temppar/
    # owner: user49
    # group: user49
    user::rwx
    group::r-x
    other::r-x

    # file: temppar//serial
    # owner: user49
    # group: group49
    user::rwx
    group::r-x
    other::r-x

    # file: temppar//serial/python_test1.py
    # owner: user49
    # group: group49
    user::rwx
    group::r-x
    other::r-x

    # file: temppar//serial/test_1task.sh
    # owner: user49
    # group: group49
    user::rwx
    group::r-x
    other::r-x


    # file: temppar//testmod.txt
    # owner: user49
    # group: user49
    user::rw-
    user:guest001:rw-
    group::r--
    mask::rw-
    other::r--

It can be seen in the sample output above that there is no explicit notation for when a directory is listed as all files and directories start with the output: `file: .....`. To denote a file versus a directory is a direcotry will have a trailing `/` after it's name. Furthermore the directory will be the first output listed at the top. 

Files and Directories will have lots of their permission and ownership listed, such as: 

1. The file or directory name
2. owner username
3. group name that the owner belongs to
4. user permissions
5. other users that were explicitly given access to the folder or directory
5. group permissions
7. Mask permissions
8. other or global user permissions

 
Here is an example of using `setfacl` for an indivdual user: 

1. First list out the current permissions for the owner, group and everyone else using `getfacl <filename>`. 
Here is a sample output: 


        # file: testmod.txt
        # owner: user49
        # group: testgroup
        user::rw-
        group::r--
        other::r--

It is shown here that the file has the owner with read and write access, the group has read access and everyone else has read access.

2. Now let's say we want to share this file with one other person outside of our group. This is done through writing `setfacl -m u:test001:rw <file.txt>`.

This will produce a output similar to the output below:

    # file: testmod.txt
    # owner: owner49
    # group: group44139
    user::rw-
    user:test001:rw-
    group::r--
    mask::r--
    other::r--

With this output we can see that there is a new user who has has access to the file, the permissions are those that were specified in the `setfacl` command, read and write permissions. 

3. Now if the owner feels that user, test001, in this example, should no longer have write permissions then `setfacl` would be used again in the following manner: `setfacl -x u:<test001> <file.txt>`. **The use of a `-x` instead of a `-m` here is important as the `-x` represents removing a user completely.**

Now check the user and groups that are on the Access Control List to the file. Using `getfacl <filename>` we can see that that the user, test001, has been removed. 

Sample Output: 

    # file: testmod.txt
    # owner: user49
    # group: testgroup
    user::rw-
    group::r--
    other::r--


**Note: Add `-R` to edit the permissions of a directory**







