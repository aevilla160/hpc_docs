## do_IRQ messages on MERCED Cluster 02/11/2021

Hope you're doing well and are keeping safe.

As some of you might have noticed, occasionally these messages are showing up on MERCED cluster command line -

`kernel:do_IRQ: 3.179 No irq handler for vector (irq -1)`

Until we can reboot the head node during the next maintenance cycle, the "do_IRQ" messages are not a sign of any kind of issue and will not damage or impede the system if they are present and these messages can be ignored (I know they're inconvenient BUT they are not harmful).

Sorry for the inconvenience and thank you for your cooperation.

## MERCED CLUSTER RECHARGE SERVICES STARTING 1/1/2022

With the new NSF-MRI Cluster Pinnacles coming online, we are transitioning the MERCED cluster to a recharge service (effective January 1, 2022). Users will receive a monthly baseline allocation of 100 cycles and Faculty PIs will be responsible for covering costs that exceed this baseline.
 
The costs and policies for recharge were developed with consultation with the Committee on Research Computing (CoRC) and approved by the campus Recharge Committee.

**What is happening?**
Starting on January 1, 2022, each current MERCED cluster user will receive a baseline allocation of 100 core-hours(1) per month. If users stay below their baseline hours, no charge will occur. However, faculty PIs responsible for the user accounts will be charged monthly for core-hour usage over the baseline allocation.

**What is the unit and of cost service?**
MERCED cluster cycles are charged by core-hours(1).
 
(1)A core-hour is a single compute core(2) used for one hour (a core-hour) and 2G of RAM. The total cost in core-hours for a complete computation is:
 
Total Cost ($) = # of core-hours x Duration (wall clock hours) x Cost per core-hour
 
(2)A core is an individual processor: the part of a computer that executes programs. (Fun Fact: The MERCED cluster has about 3100 cores.)
 
For UC users, the cost per core-hour is $0.01 and the cost for non-UC external users is $0.02.
 
**I don’t want to pay for MERCED what are my options?**
Remember, if you stay below or at your baseline allocation, you will not incur any fees.
However, you can obtain access to other free compute resources such as our new NSF-MRI Pinnacles cluster, and XSEDE resources – and my team can provide consultation for how to access these resources.

**CLICK [HERE](rechargeFAQs.md) FOR RECHARGE CENTER FAQ **

## UNEXPECTED CRASHES ON MERCED CLUSTER (03/26/2021): FIX

The MERCED cluster is back online. JupyterHub is accessible and users can submit jobs again. We apologize for the disruption and will continue to closely monitor the MERCED cluster this weekend.
If you experience any issues, we encourage you to open a ticket to the CIRT team [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4). 

## UNEXPECTED CRASHES ON MERCED CLUSTER (03/25/2021): WORKAROUND
CIRT is determining a workaround for the MERCED cluster users while we fully restore services on the head node. JupyterHub access is disabled during this time. We encourage you monitor [GitHub Docs News page](news.md) for updates and if you experience any issues, open a ticket to the CIRT team [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4). 


CIRT is investigating unexpected crashes on MERCED cluster. Users will not be able to submit jobs until the root cause is diagnosed and resolved. We apologize for any inconvenience. We encourage you monitor [GitHub Docs News page](news.md) for updates and if you experience any issues, open a ticket to the CIRT team [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4). 

## MERCED CLUSTER UNEXPECTED REBOOT (03/25/2021)

The MERCED cluster head node rebooted unexpectedly last night. Jobs submitted to the cluster might have been impacted because of this reboot. At this time Cluster is stable and jobs can be submitted. OIT CIRT team is investigating the root cause of this reboot and impact. We apologize for any inconvenience this has caused in your work.

We encourage you monitor GitHub Docs News page for updates and if you experience any issues, open a [ticket](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) to the CIRT team here.

-CIRT Team


## MERCED Cluster maintenance 03/02/2021 - 03/04/2021
Dear Campus Research Computing Community,

Your Cyberinfrastructure and Research Technologies (CIRT) team wants you to be ready for the upcoming maintenance on the MERCED cluster in **3 Weeks**.
Details follow –

**When?**
March 2, 2021 8 am – March 4, 2021 4 pm

**What is affected?**
Access to
-   MERCED cluster
-   Jupyterhub
-   ClusterStorage
-   skstorage, Tibet, QSB, Medusozoa, Conness

**What’s new this maintenance?** 
New quotas on MERCED cluster HOME space.

**What do researchers need to do to prepare for new quotas?**

See the flow chart “New Quotas”.

![](Mar2_Flowchart.jpeg)

There are several ways to transfer your files to the staging directory:
e.g. 
`cp -R /home/{username}/* /mnt/staging-home/{username}`

Additional information on CP Command [HERE](https://www.computerhope.com/unix/ucp.htm)

Additional information on MV Command [HERE](https://www.computerhope.com/unix/umv.htm)

Additional information on RSYNC command [HERE](https://www.computerhope.com/unix/rsync.htm)

**Jobs on MERCED cluster –**

1. Pending jobs at 9 am Mar 2nd will be on HOLD-Running jobs at 9 am Mar 2nd will be SUSPENDED
2. Reservation will be in-place on all nodes

**What do researchers need to do?**

1. Build in checkpoints for any work running during this period, especially for jobs on MERCED long.q
2. If you see message “Req node not available” for your job, it is because of the reservation. Reduce your wall-clock duration in submission script and re-submit.

**Where can researchers get the maintenance cycle updates?**
Stay tuned for updates/communications in your email and [GitHub Docs News page](news.md).
Next maintenance communications before the maintenance cycle - **19th Feb, 24th Feb, and 1st March.**

**Future Maintenance Schedule:**
* Mar. 2-4, 2021 Merced
* Apr. 6-8, 2021 El Capitan
* May. 4-6, 2021 Burrata

Any questions re. MERCED cluster maintenance cycle should be addressed via ServiceNow ticket [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

Thank You,
CIRT Team



