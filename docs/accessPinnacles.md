## Secure shell (SSH)
The standard method for connecting to Pinnacles is by Secure Shell `ssh`
commands. Once you've requested an account you will be provided with
initial password. However, you will have to change your password on first login.

Once the account is being created on Pinnacles, the cluster can be accessed on Mac and Linux where you can use a built-in terminal application; on Windows you can use WSL or Moba XTERM to open a terminal and type the following command: 
```bash
  ssh <YourUCMercedNetID>@login.pinnacles.ucmerced.edu 
```
Note: you have to use UC, Merced campus network to connect to Pinnacles cluster. When accessing the research clusters from an off-campus location, please ensure you are logged into UC Merced VPN to access your research cluster

If you have additional questions, please submit a general request/consultation [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

## File system
Users will be placed at the HOME directory once login to Pinnacles. Each user has 30GB storage space under the `/home/<UCMID>`. 
For larger storage access, users have access to `/home/<UCMID>/data` and `/home/<UCMID>/scratch` folders, each directory will have 256 GB storage space.  
It is recommended that if users submit jobs that require large storage space or generate large output, please perform jobs under the `/home/<UCMID>/scratch` directory, where it can handle larger size of temporary IOs for the job. Users are responsible for their own data. 
For the data storage, each user has 256 GB storage space under `/home/<UCMID>/data`, and long-term data storage can be placed there.

| Directory | Size  |
|:----------|:------|
| `/home/<UCMID>/scratch`  | 256GB |
| `/home/<UCMID>/data`      | 256GB |
|`/home/<UCMID>`|30GB|

!>The `scratch` folder is deleted periodically when the overall system storage reaches 85% of capacity or higher. Usually two weeks notification will go out by list-serve and the MOTD (message of the day, message shows on the login page to Pinnacles) will detail upcoming scratch data deletions (purges).

