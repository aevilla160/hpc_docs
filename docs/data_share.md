# Sharing Data with Other Users
This page presents ways to share data with other users on the HPC clusters. Note that the word "group" on this page always refers to Unix groups and not research groups.

## Unix Permissions
Every file and directory has read, write and execute permissions associated with it. These permissons dictate what and who has access to the file or directory and what level of access it has. The user is you, the group is the group of people asscociated with the PI that you are apart of, and other is everyother user outside the unix group. Many times others refers to every other user on the HPC clusters that are not apart of the group the current user is associated with nor other group members 

| Permission | Meaning | Meaning for directories | 
| -------------------- | ---------------- | ----------------- |
| read (r)	 | Contents of file can be viewed and displayed | Contents of directory can be listed and viewed|
| write (w) | File can be modified or deleted | Files can be created in or deleted from directory | 
| execute (x) | File can be run like a program | Directory can be entered (i.e., the cd command works) |

There are also numerical counterparts to the abover permissions and the numbers are added together to achieve the same effect as using the letters. 
| Permission | Meaning | Meaning for directories | 
| -------------------- | ---------------- | ----------------- |
| 4 | Contents of file can be viewed and displayed | Contents of directory can be listed and viewed|
| 2 | File can be modified or deleted | Files can be created in or deleted from directory | 
| 1 | File can be run like a program | Directory can be entered (i.e., the cd command works) |

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

    drwxr-xr-x 2 <user> <group> 10 Jul 28 14:47 permissions/

The permissions will be shown in an order of user, then group and everyone else or global. In the output above the user has read, write and excutable access. The group has read and executable access. Everyonelse on the cluster has read and executable access. 


Now the command ` chmod -R  u=rwx,g=---, o=--- permissions/` will be executed and will update the permssions of the group the user is asscoiated with and everyone to not have read, write or execute access of the directory, `permissions/`. 

To view the changes and ensure they are accurate run the comamnd ls -ld 

The output should look similar to this:

    drwx------ 2 <user> <group> 10 Jul 28 14:47 permissions/ 
From this we can see that the first `rwx` correlate to the user and the empty dashes represents that the group and everyone else has lost access to the directory. 

## The `setfacl` Command
The `setfacl` command is used to change access of files or directories to individual users, multiple user groups or everyone on the cluster. 


**Note: Add `-R` to edit the permissions of a directory**

## Public and Group-Readable Directories
$ It is common adjust the permissions that the group has on the file or directory.

To see what group you are apart of run the command: `groups`

Run the `groups` command to see your group(s):
Ex. output 

    ucm_test

To edit the permissions to your group run the command: 
    `chmod [options] g=<permissions> <file>`
Or
    `chmod [options] <123> file `
Where 123 represent: 1 = user permissions written in number format, 2 = group permissions written in number format and 3 = others' permissions written in number format. 
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

## ACL Permissions
Let's say you want to make a directory that only people in your Unix group can use but no one else. First determine which group you are in and which groups other users are in. 




