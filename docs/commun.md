## 01/26/2023
Dear Research Computing users-

Facilities had informed us that they will be performing essential power maintenance in the SE2 building from 5:30 am -6:30 am tomorrow Jan 27th, 2023 and will require a power shutdown for most of SE-2.

While we do not expect that this will cause any significant impact to your colocated servers in SE-2 040, there is always some risk associated with power maintenance.
Should there be any further impact following this change, we will communicate it at status.ucmerced.edu.
Please open an OIT service ticket [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) if you have any additional questions.




## 01/09/2023
Dear Research Computing users –
 
Please be aware of the following important information on upcoming downtime for the MERCED cluster and changes to CIRT services starting in February 2023.
 
If you have additional questions, please do not hesitate to reach out to me via CIRT [general request](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) or [schedule](https://arrangr.com/sarvani) a consultation with me. 
 
When: January 9, 2023 to Jan 31, 2023
MERCED Cluster will be offline starting 6:30 am on 01/09/2023 until 5 pm on 01/30/2023 (3-weeks downtime).
Why: During this period, CIRT will make a number of critical hardware, software, firmware updates to the cluster.
Notes:
<ul>
<li>Any jobs still running at 6 am on  01/09/23 will be cancelled.</li>
<li>During this maintenance window, the Pinnacles cluster will be accessible to users.</li>
</ul>
Other important changes starting 1 February 2023
<ul>
<li>Borgstore will be accessible through both MERCED and Pinnacles cluster.</li>
<li>CIRT recharge services, including MERCED cluster core-hours will be renewed. You can find costs for CIRT recharge services here.</li> 
<li>In order to minimize disruptions to computational research on MERCED cluster, the Provost's office has provided bridge funding for all MERCED cluster PIs for core-hour usage on MERCED through June 30, 2024.</li>
</ul>

## 11/30/2022

Dear HPC users,
  
  MERCED cluster 1-day maintenance is completed. 
  
  <ins>**Post maintenance updates:**</ins>

  1.	Login node RAM is replaced.  Users will not see error message such as `kernel:do_IRQ: 3.179 No irq handler for vector (irq -1)` while on login node 
  2.	General partitions “long.q” and “gpu.q” are removed, the maximum wall clock time for users is now 5-day
  3.	CPU nodes mrcd01-mrcd32 are retired 




## 11/15/2022

**Subject: Upcoming MERCED cluster maintenance and changes to CIRT services**

Dear Research Computing users –
 
Please be aware of the following important information on upcoming downtime for the MERCED cluster and changes to CIRT services starting in February 2023.
 
If you have additional questions, please do not hesitate to reach out to me via CIRT general request or schedule a consultation with me - my general availability [here](https://arrangr.com/sarvani). 

MERCED Cluster Downtime

<ins>When</ins>: November 30, 2022

Cluster will be offline starting 6:30 am on **11/30/22** until the end of the day. (1-day downtime)

<ins>Why</ins>: During this time, CIRT team will re-rack, re-cable MERCED cluster HOME storage unit and replace failed RAM modules on the login node.

Notes:
<ul>
  <li>Any jobs still running at 6 am on 11/30/22 will be cancelled.</li>
  <li>During this maintenance, users will not have login access to the cluster, or any attached storage units including Borgstore.</li>
</ul>

<ins>When</ins>: January 9, 2023 to Jan 31, 2023

MERCED Cluster will be offline starting 6:30 am on 01/09/2023 until 5 pm on 01/30/2023 (3-weeks downtime).

<ins>Why:</ins> During this period, CIRT will make a number of critical hardware, software, firmware updates to the cluster.

Notes:
<ul>
<li>Any jobs still running at 6 am on  01/09/23 will be cancelled.</li>
<li>During this maintenance window, the Pinnacles cluster and Borg store will be accessible to users.</li>
 </ul>

Other important changes starting **1 February 2023**
<ul>
<li>Borgstore will be accessible through both MERCED and Pinnacles cluster.</li>
<li>CIRT recharge services, including MERCED cluster core-hours will be renewed. You can find costs for CIRT recharge services here.</li> 
<li>In order to minimize disruptions to computational research on MERCED cluster, the Provost’s office has provided bridge funding for all MERCED cluster PIs for core-hour usage on MERCED through June 30, 2024.</li>
</ul>





## 5/13/2022

**Subject: Pinnacles maintenance (06/06/2022-06/07/2022)**

Dear Research Computing Users –

CIRT will be performing regular OS and security patch upgrades on Pinnacles cluster.

<ins>When?</ins>

Monday, June 6, 2022 - Tuesday June 7, 2022.

Pinnacles cluster will be operational starting June 8, 2022.

Impact

Pinnacles cluster will be offline starting June 6, 2022.

<ins>Jobs</ins>

Please plan your jobs ahead to avoid any disruptions. We encourage you to build in checkpoints for any work running during this period.

<ins>Planning for this maintenance</ins>

1. Build in checkpoints for any work running during this period, especially for jobs on Pinnacles PI-owned/ long.q

2. If you see message “Req node not available” for your job, it is because CIRT has reserved resources for jobs to wind-down before maintenance period. If you need to run your jobs before the maintenance, reduce your wall-clock duration in submission script and re-submit.

<ins>Next Steps</ins>

CIRT will send an ALL CLEAR email after successful maintenance.


For updates during the maintenance window, we encourage you to monitor CIRT News [here](news.md).



## 4/25/2022

**Subject: CIRT Recharge Center Hiatus Continues**

Dear MERCED cluster PIs –

Hope you are doing well.

I am writing to let you know that OIT-CIRT recharge hiatus is still in effect.

We will continue to waive all costs for faculty using CIRT recharge services, including costs for using MERCED cluster core-hours, until further notice. 
As a reminder, this recharge hiatus is retroactive to January 2022.This continues to be a fluid situation, but we anticipate that costs will be waived through at least July 2022, and possibly beyond. 

Once details have been finalized, we will reach out again to inform you, and we will also provide all users with at least one month’s notice before recharges begin again.

Please note that during the recharge hiatus, CIRT will continue to monitor and record usage on the MERCED cluster toward our goal of operating as a recharge center. 
However, faculty PIs will NOT be charged for core-hour usage on MERCED until recharge begins again.

I am happy to discuss any questions you might have – you can schedule a one-on-one consultation with me [here](https://arrangr.com/sarvani/rechargemeeting).


## 3/30/2022

**Subject: Research Computing Webinar Recording**

Dear PIs –

You may be aware that OIT hosted a webinar on our research computing offerings a few weeks back. 

I know how busy you must be, so I wanted to pass along the recorded options for the webinar as a resource to share with your colleagues and students. 

Here is the link to access the webinar: https://ucm.edu/EO_ResearchComputingWebinar

The webinar discusses our on- and off-campus research computing resources, our service model, and the various trainings and consultations OIT and the library offer for grad students, postdocs, and faculty. 

It also has a Q&A section at the end that covers some other topics in some detail.

Please feel free to share the webinar recording with your colleagues and students who have questions about research computing on campus or are interested in learning more.

Thank you, and I hope you’re well!



## 2/28/2022

**Subject: CIRT Recharge Center Hiatus - Waiving Recharge Costs**

Dear MERCED cluster PIs -

 

The Cyber Infrastructure and Research Technologies (CIRT) team is aware that our recent move to a recharge model has been a pain point for some research groups, and we are working with the Provost’s office to obtain bridge funding to offset CIRT recharge costs for faculty.

 

Until this bridge funding is secured, OIT-CIRT is in an immediate recharge hiatus, retroactive to January 1, 2022. We will continue to waive all costs for faculty using CIRT recharge services, including costs for using MERCED cluster core-hours, until further notice.

 

This is a fluid situation, but we anticipate that costs will be waived through at least April 2022, and possibly beyond. Once details have been finalized, we will reach out again to inform you, and we will also provide all users with at least one month’s notice before recharges begin again.

 

Notes:

 

During the recharge hiatus, CIRT will continue to monitor and record usage on the MERCED cluster toward our goal of operating as a recharge center. Principal investigators will continue to receive monthly reports to track their group’s core-hour usage.
 

Research groups needing MERCED cluster access will continue to be required to ensure their user and COA information provided [here](https://login.microsoftonline.com/f4dfe9a3-ca78-4998-b7a7-e6d0692eace6/oauth2/authorize?client_id=00000003-0000-0ff1-ce00-000000000000&response_mode=form_post&protectedtoken=true&response_type=code%20id_token&resource=00000003-0000-0ff1-ce00-000000000000&scope=openid&nonce=74817F0D7870D6EF7E4073B97706ED2FE1030003B869546F-842C588301A4BBE35FE1718729B638B64ED1A2007B1773EA306E78C1D1272E10&redirect_uri=https%3A%2F%2Fmerced-my.sharepoint.com%2F_forms%2Fdefault.aspx&state=OD0w&claims=%7B%22id_token%22%3A%7B%22xms_cc%22%3A%7B%22values%22%3A%5B%22CP1%22%5D%7D%7D%7D&wsucxt=1&cobrandid=11bd8083-87e0-41b5-bb78-0bc43c8a8e8a&client-request-id=1b3d25a0-800a-1000-9a79-2d73fe130045) (sign-in required) is up-to-date.
 

All MERCED cluster communications and updates will be posted on the CIRT documentation website here.
 

Once again, I am happy to discuss any questions you might have – you can schedule a one-on-one consultation with me [here](https://arrangr.com/sarvani/rechargemeeting).

 
## 1/1/22-1/15/22

**Subject: MERCED cluster core-hour usage and cost report**

Dear MERCED cluster PIs –


What is new?
 

Here is the 1st MERCED cluster core-hour usage and cost report for January 01/01/22 – 01/15/22.
 

This report contains

PI group core-hour usage
Individual user core-hour usage
Core-hour usage costs
 

From 01/01/22 – 01/15/22.
 

This usage report does not factor baseline free monthly allocation of 100 core-hours per user.
 

How do I limit my group from using any more core-hours on MERCED?
 

You can request access limits for your group [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) or by responding to this email.
 

Remember, you can obtain access to other free compute resources such as our new NSF-MRI Pinnacles cluster, and XSEDE resources – and my team can provide consultation for how to access to these systems. Schedule a consultation [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0).
 

What is happening?

 

As previously announced, with the new NSF-MRI Cluster Pinnacles coming online, CIRT transitioned MERCED cluster to a recharge service effective January 1, 2022.

 

Users will receive a monthly baseline allocation of 100 core-hours and Faculty PIs will be responsible for covering costs that exceed this baseline allocation.

 

If you have questions or concerns about recharge, do not hesitate to:

Schedule a recharge center consultation here
Get into contact with me at schadalapaka@ucmerced.edu
