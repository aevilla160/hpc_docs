> __How do I make a General Request/Consultation?🤔__

OIT provides general request services or for assessments for individuals and research groups who wish to deploy research computing and advanced cyberinfrastructure techniques (e.g. high-performance computing, visualization, advanced networking and data collaboration, and advanced technology-enhanced workflow development).
You can make a General Request/Consultation [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

>__How do I obtain an account on MERCED cluster?__

You can request a new user account on MERCED cluster [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0). All user accounts on MERCED cluster are associated with that of a faculty PI. The faculty PI should approve that the export control attestation form, follow the procedure [here](get_started.md) on file is up-to-date and/or complete a new export control attestation form.

> __How do I install software on a CIRT Managed cluster?__

* If the software package or version you need is not available in the list of provided software, you may compile and install it yourself. The recommended location for user-installed software is the $HOME path.
* If the software installation requires root (sudo) access and/or if you need further assistance installing the software, you can request service [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=b83ee9ff1b67a0543a003112cd4bcbde&form_id=0cb3dca04f7d4300b52ba1618110c7ff).

> __How do I change password on research cluster?__
* You can request for changing your password on MERCED/any CIRT managed research cluster by submitting a general research request [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).
* Please provide the name (and/or IP address) of the cluster on which you need your password updated.

>__Error Logging into research cluster/ error sshing into cluster__

* When accessing the research clusters from an off-campus location, please ensure you are logged into UC Merced VPN to access your research cluster. VPN allows faculty, students and staff to connect to research computing resources from home or other off campus networks.

* If you still run into errors logging into the cluster, please submit a general research request [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

> __My cluster jobs failed with errors, what do I do?__

Cluster jobs can fail for a variety of reasons. But preliminary diagnoses should include ensuring following
* job is not exceeding the wall-clock time specified in the job submission script / queue wall-clock limit
* job is requesting for the right memory and CPU resources on the cluster
* job is finding the right executable on the compute node
* job has the right environment variables set on the compute nodes. You can ensure that using the command: #SBATCH --export=ALL
If your jobs are still failing, then please attend the HPC office hours (Zoom link: On MERCED cluster login page; Time: Every Friday from 10:30 am to 12 noon PST) and/or submit a general research request [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

> __My jobs are running unusually slow__

* Jobs could run slower than usual for a variety of reasons. But preliminary diagnoses should include ensuring that the job is requesting for enough memory and CPU resources on the cluster
* If your jobs are still slow, then please attend the HPC office hours (Zoom link: On MERCED cluster login page; Time: Every Friday from 10:30 am to 12 noon PST) and/or submit a general research request [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

> __My job is not running how I intended it to. How do I cancel the job?__

Use `scancel < JobID>` where `< JobID>` is the job allocation number.

> __How do I schedule a consultation?__

We are happy to help you with any questions/computational needs for you and your research group. You are welcome to attend one of our HPC office hours (Zoom link: On MERCED cluster login page; Time: Every Friday from 10:30 am to 12 noon PST) and/or submit a general research request [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

> __How do I move Big Data?__

* A number of methods allow transferring data in/out of MERCED Cluster. For most cases, we recommend using [SSH-based file transfer commands](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server), such as `scp`, `sftp`, or `rsync`. They will provide the best performance for data transfers from and to campus.
* Most casual data transfers could be done through the MERCED login node, by pointing your transfer tool to merced.ucmerced.edu.However, for transferring large amounts of data, FIONAs with dedicated bandwidths can be used for scheduled, unattended data transfers. If you are looking to complete a Big Data transfer, please submit a general research request [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

> __When/where are the HPC Walk-in Clinic hours?__

Bring your laptop, your code and your questions to the clinic and get expert help, right on the spot. Experienced graduate students are encouraged to come help your peers by mentoring them in HPC tips and tricks. Faculty are also welcome to join. Among others, Yue Yu (Sr. Research Computing Facilitator) will be available to meet with and help members of the campus research computing community at these sessions.

__where__: Zoom coordinates: On MERCED cluster login page

__When__: Every Friday from 10:30 am to 12 noon


!> Recharge center FAQs

> __I have several users doing different projects, can I use different COA# for them?__

Yes, please make sure keep the COA# information updated. Each user can also have different COA#, if the user is doing multiple projects. If you have any questions, feel free to email cirt@ucmerced.edu.



>__Are the costs the same regardless of whether we purchased our own nodes or not?__

The costs and the charges are for general Slurm partitions and not for PI-owned partitions (example: amartini.q, dstrubbe.q, qsb.q, skhatri3.q). That is, if users/groups purchased nodes for MERCED and are submitting jobs on PI/Group owned queues, users will not be charged for core-hours.

>__How do we get access to the Pinnacles cluster?__

Committee on Research Computing is scheduled to meet on the Dec 10th, 2021. Once CoRC approves access policy for Pinnacles, CIRT can begin account creation process for you and your group. Your data and accounts would be the same as on MERCED and running your workflows on Pinnacles should be seamless.

>__Can I purchase core-hours in advance?__

Since recharge services are pay-per-use services, users cannot purchase core-hours in advance. However, you can purchase “condo-model” CPU/GPU compute node(s) for Pinnacles for seamless access to compute resources after Jan 1, 2022. Request for a Pinnacles condo-model purchase [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

>__Can faculty charge recharge services directly to a grant?__

Grant funds have restrictions on how the funding can be spent, and every grant is unique. So, as long as recharge service is allowable expense under the grant, then faculty can charge recharge services directly to the grant. Each grant has a unique COA#. Please ensure that your COA information is accurate in the MERCED recharge spreadsheet by emailing cirt@ucmerced.edu.

>__I do not want my research group to exceed free core-hour limit on MERCED__

The initial recharge center implementation will provide bi-weekly usage reports of their groups to faculty PIs. If at any point, faculty would like for CIRT to stop MERCED cluster access to their group, please send an email to cirt@ucmerced.edu and CIRT can stop access. 

>__I want access to free resources. How can I get access to them?__

Remember, if you stay below or at your baseline allocation, you will not incur any fees. However, you can obtain access to other free compute resources such as our new NSF-MRI Pinnacles cluster, and XSEDE resources – and my team can provide consultation for how to access these resources. Schedule a consultation [here](https://arrangr.com/sarvani/rechargemeeting).






