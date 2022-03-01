## MERCED LOGIN NODE REBOOTED. (09/30/2020)
MERCED login node back online (11:15 am PT).

## MERCED LOGIN NODE REBOOTING. NO LOSS OF JOBS/DATA (09/30/2020)

MERCED login node is being rebooted in 15 minutes (current time 10:53 am PT). Please save your work and exit the terminal. MERCED cluster will function normally. Your submitted jobs and data will NOT be lost in the meantime. MERCED login node should be back in a couple of minutes. Apologies for the temporary interruption.


## MERCED data update (9/29/2020)
Dear MERCED Users,

We write to provide you with the latest update on the status of the data and scratch space disk array, clusterstorage.

As mentioned in our last message, the CIRT team initiated stress testing of clusterstorage with a set of user groups yesterday. Unfortunately, the load of these tests led to a system failure. The CIRT continues to work with our vendor to diagnose and correct this hardware problem.

In the meantime, please note that MERCED is operational and users may use their /home space to carry out calculations.

We appreciate your patience and will provide another update tomorrow evening.



## MERCED data update (9/28/2020)
Dear MERCED Users,

We write to provide you with the latest update on the status of the data and scratch space disk array, clusterstorage.

As mentioned on Friday, the CIRT team initiated a thorough diagnostic test system. These tests have completed without error, suggesting the hardware and/or software fixes we carried out last week may have worked.

We have begun beta testing of clusterstorage with a set of user groups.

Again, we emphasize that the physical disks in the clusterStorage remain unaffected and data kept in the data and scratch spaces remain intact.

We will provide another update tomorrow evening.



## CLUSTER STORAGE UPDATE (09/24/2020)

ALTHOUGH /data AND /scratch ARE NOT USER ACCESSIBLE, RESEARCH DATA IN THE FOLDERS IS SAFE. NO RESEARCH DATA IS LOST
USERS SHOULD BE ABLE TO USE /home PARTITION FOR THEIR SIMULATIONS WHILE CIRT TEAM FINDS A WORKAROUND/FIX
PLEASE MONITOR THIS SPACE AND MERCED [Docs News](news.md) FOR UPDATES 

OIT has confirmed that the clusterstorage connected to MERCED cluster is unstable causing /data and /scratch partitions to be unavailable. We are working on a workaround. In the meantime, you can monitor MERCED cluster updates here and on MERCED login page.


## Clusterstorage is back online (09/21/2020)
/data and /scratch partitions should be available for jobs.
CIRT Team is closely monitoring the status of clusterstorage

Please monitor this space and MERCED login page for more updates

Users are encouraged to report any errors [here](https://ucmerced.service-now.com/hub/com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=4720dfe64f97ca002f3bd49f0310c726&sysparm_link_parent=f509c4474fde02006137d0af0310c7b8&sysparm_catalog=e0d08b13c3330100c8b837659bba8fb4&sysparm_catalog_view=catalog_Service_Catalog) in accessing /data and /scratch partitions.


## CLUSTERSTORAGE CRASHED EARLIER TODAY (09/23/2020) ***
*** CIRT TEAM IS ACTIVELY WORKING ON RESOLVING THIS ISSUE ***
*** USERS WILL NOT BE ABLE TO ACCESS /data AND /scratch BECAUSE OF THE CRASH *** *** PLEASE MONITOR THIS SPACE AND MERCED LOGIN PAGE FOR UPDATES ***


## Clusterstorage is back online (09/21/2020)
/data and /scratch partitions should be available for jobs.
CIRT team is investigating the root cause and working with vendors to diagnose the issue



## CLUSTERSTORAGE CRASHED EARLIER TODAY (09/21/2020) ***

*** CIRT TEAM IS ACTIVELY WORKING ON RESOLVING THIS ISSUE *** 
USERS WILL NOT BE ABLE TO ACCESS /data AND /scratch BECAUSE OF THE CRASH
PLEASE MONITOR THIS SPACE AND MERCED LOGIN PAGE FOR UPDATES




CLUSTERSTORAGE IS BACK ONLINE AND FUNCTIONAL 
`/DATA` AND `/SCRATCH` SHOULD BE AVAILABLE FOR JOBS 
CIRT TEAM IS FURTHER INVESTIGATING THE ROOT CAUSE
PLEASE MONITOR THIS SPACE AND [Docs News](news.md) FOR UPDATES.
***

## CLUSTERSTORAGE CRASHED EARLIER TODAY (09/17/2020) 

*** CIRT TEAM IS ACTIVELY WORKING ON RESOLVING THIS ISSUE ***
*** USERS WILL NOT BE ABLE TO ACCESS /data AND /scratch BECAUSE OF THE CRASH ***
*** PLEASE MONITOR THIS SPACE AND MERCED LOGIN PAGE FOR UPDATES ***

***

**What's new on MERCED cluster?**
* Increased capacity added new nodes on the fast.q on the cluster 
* Updated Slurm to 20.02 version which means efficient resource management -> job submission process should be the same as before
Your user quotas on
* /home = 20G
* /data + /scratch = 768G
* /qsb (if your group has access to this storage unit) = 256G

On login, you should see your quota for HOME path.
IF you are over your quota limit, you will see an asterisk on login as shown -
```shell
==============================================================================$`
`Disk quotas for user schadalapaka (uid 662):`
     `Filesystem    used   quota   limit   grace   files   quota   limit   grace`
          `/home  64950M* 20480M  20480M   5days    502k       0       0`
`==============================================================================$`
```

IF you're over quota and are unable to read/write to the HOME space, please attend one of the special HPC walk-in hours next week (Mon - Wed (Sep 14th - 16th) from 1:30 pm - 3 pm.Zoom co-ordinates on MERCED cluster login page) for CIRT team to assist you with data management process.

You should see 3 symlinks in your HOME path at this point

1. **/data (this is the new data path)**
On your HOME space, if you run  ls -al | grep data you should see
 [schadalapaka@mrcdlogin ~]$ ls -al | grep data
lrwxrwxrwx   1 schadalapaka ucm_schadalapaka         18 Apr 10  2017 data -> /data/schadalapaka
**This data path is designed for non-primary research data. For example: genome datasets downloaded from NIH can reside here.**

2.  **/scratch (this is the new scratch path)**
On your HOME space if you run ls -al | grep scratch you should see
[schadalapaka@mrcdlogin ~]$ ls -al | grep scratch
lrwxrwxrwx   1 schadalapaka ucm_schadalapaka         21 Apr 10  2017 scratch -> /scratch/schadalapaka
**THIS is where your intermediate test results with a life-span of 4 weeks can stay.**
**Scratch path is deleted every 4 weeks, so please be sure to not leave any data that's of long-term importance to you.**

3. **/olddata (this is the old data path)**
**This path will remain in your HOME path till the end of September (September 30th) - This path should have all your files and folders from /data.**
**You can compare data from this path in your /data path to verify if all the needed data is copied into the new /data path.**

4. /qsb (for those who have access)

If you have access to qsb storage, you should see this in your HOME path.

Please let us know if you have any questions/concerns.



## EXTENDING MERCED CLUSTER MAINTENANCE TO 9/10/2020

Dear Research Computing Users,
MERCED cluster will be back online and available to researchers sometime on  09/10/2020.
CIRT team is in the last leg of the upgrades - expanding capacity, implementing user quotas, final testing before we make MERCED cluster accessible to researchers.
We appreciate your patience.

## EXTENDING MERCED CLUSTER MAINTENANCE TO 9/8/2020
Dear Research Computing Users -

**The current MERCED Cluster maintenance window is extended to next Tuesday (September 8, 2020).**

The CIRT team has been making significant upgrades to MERCED including to updating the scheduling software and implementing individual disk space quotas. We will keep you posted should conditions change.

Finally, even as we work to close this maintenance window, we are reviewing our team's standard operating procedures to ensure greater accuracy in future estimates of maintenance windows.

We appreciate your patience.




## UPCOMIMG MAINTENANCE FOR MERCED CLUSTER FROM 22nd August 2020 - 30th August 2020.

MERCED cluster will be in MAINTENANCE mode from 6 am 22nd August to 10 pm 30th August. 

After the maintenance, we should have:

(a) Updated Slurm scheduler on the cluster 
(b) Implemented user quotas on the cluster

What does this mean for MERCED cluster users (you)?

(1) Jobs that cannot be completed before August 22nd will be placed in PD(pending) state by the scheduler with "Required node not available (down, drained or reserved)" message (or) squeue output shows "ReqNodeNotAvail, UnavailableNodes:mrcd[03,14]" 

(2) All jobs that are running/pending state by August 22nd at 6 am will be lost.

(3) MERCED cluster is NOT accessible during the maintenance window. Users must plan to manage their data/jobs accordingly.

Communications to and from Research Computing group to MERCED Cluster users during maintenance window:

(i) Users should watch for email updates from Research IT staff (Sarvani Chadalapaka) and/or Interim Directors for Research Computing Prof. Sindi, Prof. Hratchian to this distribution group.

(ii) Understandably, Research IT staff might not be available during the maintenance window for ad-hoc/1:1 meetings.

(iii) Once MERCED cluster is back up and operational, we will email an all-clear on this distribution group and share communications via UC Merced OIT's Official Twitter.

For any questions or concerns re. maintenance, you might reach out to schadalapaka@ucmerced.edu 

***

 
## Fixed MERCED login access via `mrcdlogin` node (August 10 2020)

All users çan now access MERCED via the login node `mrcdlogin`. The issue of hanging while attempting to log in is resolved. Users are also able to resume activity on MERCED's `JupyterHub`.

***

## Catastrophic Crash and Data Loss on QSB Storage (August 7 2020)


It appears to us that the QSB Storage Unit (`/qsb`) had fatal crashes (possibly hardware crashes) yesterday.
These events led to unfortunate irretrievable data loss from the storage unit. 
As you have known, CIRT team did not have the infrastructure capacity to do data backups from QSB Storage. 
However, as a part of our routine maintenance, we backed up a copy of data on QSB Storage from around March 18th.

At this time,
(1) CIRT team is actively working on restoring the backup data from March and making qsbstorage accessible to users while diagnosing the root cause for the crash.
(2) CIRT team is beginning to start discussions with the storage unit vendors on warranty issues and finding replacement parts as needed.

We apologize for the inconvenience.

***
## QSB Storage Unit had unexpected reboots on 08/06/2020.

CIRT team is working on identifying and resolving the issues - please see this space for updates

***

May 29 2020 7 pm
MERCED Cluster Online 
MERCED Cluster should be fully functional and operational now.

May 29 2020 4:30 pm
Update: MERCED Cluster not accessible
Update:

Facilities has addressed the water leak in SE2 and has restored power to the space. However, OIT power distribution equipment was damaged and is in the process of being replaced. 

MERCED cluster still not accessible via network.

Another update will be provided by 6pm.

***

May 29 2020
MERCED Cluster not accessible
Dear Research Computing Users,

Due to a water leak in Science and Engineering 2, Facilities has disconnected the power to the main network distribution facility, disrupting network service to the entire building. OIT is on site assessing the situation. 

What does this mean for MERCED cluster users?

MERCED Cluster is inaccessible via ssh to users. MERCED Cluster is still powered on and is running jobs but users cannot connect to the cluster to review their results or submit new jobs until the network is back online and water leak issue has been resolved.

Please keep an eye out for this email thread for updates. 
You can get official OIT updates at  https://twitter.com/ucmit .
Also, you can see MERCED cluster news on the [GitHub Docs News page](news.md).

Thank you for your patience in this time!



Please stay safe, stay indoors during this time!


***

May 18 2020
## Change in zoom-in hours schedule for Summer 2020 

Attend HPC  walk-in sessions: Every Monday and Thursday from 2 pm to 3 pm     
Zoom coordinates: On MERCED cluster login page        |



May 7 2020
## Change in zoom-in hours schedule for Spring 2020
HPC ZOOM-IN HOURS SPRING 2020 !!

The objective of walk-in sessions is to expand the use of high-performance computing on campus (including the MERCED cluster) and develop our research computing community.
These sessions are meant for answering user questions regarding the MERCED cluster or other research computing concerns.
Drop by the zoom hours, say hi to us and/or ask us HPC questions.

**When?**  10:30 am - 11:10 am (just for 05/08/2020, 05/15/2020)
Summer-2020 zoom-in sessions hours TBA.
**Where?** See MERCED cluster MoTD
All students, postdocs, staff, and faculty are welcome to attend and bring questions.
Among others, Sarvani Chadalapaka (MERCED System Administrator), and Matthias Bussonnier (Research Computing Facilitator) will be available to meet with and help members of the campus research computing community at these sessions.
See you all on Friday!
Happy Computing!

***

May 3, 2020
## Update on node failure errors
As some of you might have noticed, there was a brief outage on MERCED cluster earlier today. Research Computing staff has identified and resolved the issue along with completing the tasks associated with scheduled emergency maintenance for the cluster.
At this point, we expect MERCED to operate normally but will continue to monitor the situation closely over the weekend.
What this means for you?
You can login to the cluster and run your jobs on the cluster as usual. Please let us know if you see any issues in doing so.
***

April 28, 2020
## Node failure errors
As some of you have noticed and reported, we are having communication issues on the MERCED cluster between the compute nodes and the slurm scheduler, which allocates cluster resources. (The message in slurm error logs in these instances will indicate incorrectly that there is a "NODE FAILURE" see below for error message.)
To fix this issue, we are having to upgrade MERCED cluster kernel and the process requires us to shutdown the cluster for a 2-day period in the next week. 
What this means for you?
You might lose any unfinished jobs/pending jobs on the cluster during the shutdown. Once the cluster is back online, we can allocate you higher priorities in the queues to allow your jobs to run before others'.
We apologize for the inconvenience and appreciate your cooperation in our efforts to keep cluster healthy and operational!
Please reach out to us and let us know if there's any further concerns/questions.
Error Message:
*** JOB ID ON mrcdXY CANCELLED AT 2020-04-27TXXXX DUE TO NODE FAILURE, SEE SLURMCTLD LOG FOR DETAILS ***

***

April 23, 2020
New login node for MERCED cluster
MERCED has a new login node ! Want to help testing it ? Try            
ssh YOURUSERNAME@mrcdlogin with MERCED password and report any issues 
***

April 17, 2020
QSB Storage is Back on MERCED

Dear QSB Storage Users,

We hope you are doing well.

We are pleased to report that the QSB storage directory is once again accessible on the MERCED cluster. We encourage you to report any issues or concerns to our team.

In addition to bringing QSB storage back we added 2 Solid State Drives on QSB which should mean writing to QSB storage is a bit faster.

Finally, a note about file systems. The performance of most file systems decreases significantly when there are with huge numbers of small files. If you had a directory like this on QSB storage, your work is still there but it might have been put into a tar archive. 

Thanks to CIRT team members Matthias Bussonnier and Jeff Pedro for working to get this job done ahead of schedule.

Let us know if you have any questions.

***

**April 17, 2020**
Change in HPC walk-in hours for this week: 10:30 am - 11:30 am 
Regular timings: 10:30 am - 12 noon

***

April 15,2020
Update on MERCED Cluster VPN Access

Hi Research Computing Users,

As you might have noticed, MERCED cluster is temporarily not needing users to be on VPN to access. However, Research Computing team is working to address that issue and requiring users to be on VPN to access MERCED cluster. 

This work should not be disruptive; If you are logged into MERCED cluster today at around 5 pm, you MAY notice brief 3-5 second interruptions in connection to MERCED cluster. 

***

April 06, 2020
Update on QSB Storage

Dear Research Computing Users,                             

We hope you are doing well. We have received several questions about why QSBStorage is not currently accessible through MERCED. The Research Computing team identified malicious software running on QSBStorage so we did not mount it when we brought MERCED back on-line.

Our team is actively working to restore QSBStorage, but in order to do so safely involves migrating all data to a newer storage system, reinstalling the OS on QSBStorage and copying the data back to the storage unit.

We will keep you posted on our progress, and anticipate to have QSBStorage back online by the week of April 20th. As always, please direct any questions/comments to Co-Directors Hrant P. Hratchian and myself.

Take care and stay safe/healthy,

***

April 2, 2020
HPC Walk-In Schedule: Fridays 10:30 am - 12 noon PT. Zoom Coordinates on MERCED cluster login screen.
March 30, 2020

Cluster have been moved to the research container.
 - Original plan was week of week of March 16, 
 - COVID-19 affected time contractors could spend on site, which added delay.
 - One of the Uninterrupted Power Supply battery leaked which made the Research Container Unsafe to enter on Mon and Tue 22 and 23. 
 - Contractors finished the move on Friday 27. 
 - We finish reconfiguration and basic testing of the cluster on Monday 30th, morning and reenabled Slurm and login for everybody. 
 - Storage nodes (Medusozoa, Tibet, QSB, ....) arer nont currently guarantied to work


November 2019 Maintenance

Merced cluster was under maintenance from Nov 4th to November 11th; The research IT team was a trying to solve a number of issues; mostly: 
 - Recurrent "Node Failures" seen by jobs, especially MPI Jobs. 
 - The Memory on the head node was generating errors and triggering a number of process failure. The rate of the error log was slowing down the disk on the head node. 
 - Many OS and Software updates were 2+ years old; and were needed on the Head and Compute Node and did require many complete restart of the cluster. 

During the week the Research IT Team has done the following

- Diagnose and Replace RAM on the head node – we haven't seen any RAM error since then. 
- Update CentOS to version 7.7 (Sept 2019) on the head node and all the compute nodes with the latest version of all the available packages, both normal and security related. Update Cuda on the GPU nodes. 
- Update the firmware of all the Infiniband switches, and all the network card.
- Implement group quotas on the main /home mount point. We can change the quotas now without a reboot of the head node. 
- Configure the cluster to bring itself back online after unexpected shutdown and speedup recovery time. Previously many manual actions had to be taken for the cluster to restart – including physically going to SE2 basement to start the head node. As far as we can tell in case of unexpected cluster reboot; critical components should now come back online on their own. 
- Some Aging nodes are starting to see hard drive failure (mrcd31, mrcd14, mrcd27), we used part of mrcd14 to fix 31. Mrcd14 is now permanently retired.
- Network parameters were tweaked on the infiniband fabric and need to be tested. Some inter-nodes communication have been upgraded from 2.5Gb/s to ~20Gb/s

We are still monitoring the cluster, and unfortunately are still seeing the "Node Failures" on many of the nodes, though our experiment during the week appeared to have ruled out hardware issue. With all the OS and firmware up to date we can get back to our vendor to request advices. 

Os Updates were also necessary for the move the new research facility once we have taken possession of the new space and attach the more recent nodes to the cluster. 

Next steps

There are still a couple of maintenance task that need to be done on a couple of machines; but do not need the cluster to be powered off. In particular all the storage nodes attached to Merced need to be patched and upgraded as well, as some have not seen updates in more than 2 years as well. 

We will contact the vendors with respect to nodes failures for advice and further diagnosis. Next step will likely require to update Slurm from current version (17) to latest version (19). Updating Slurm require planning and downtime as well.

As a new login for Merced has been ordered and will need to be set-up; we think doing the Slurm update at the same time as the installation of the new login node is the most reasonable course of action. 
