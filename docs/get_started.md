## System overview
MERCED hosts 114 CPU compute nodes and 8 GPU nodes. Please be aware that
the nodes among MERCED cluster are multigenerational, meaning that the CPU
processors from different nodes are having different features, the table shows below
listed detailed node information. Users may experience relative big
performance variations when running the same jobs on different nodes.

The table below listed all MERCED cluster CPU compute nodes features, and their
processors generations.

| Nodes        | feature                                                    | RAM   | Total cores pre nodes | InifiBand (IB) |
|--------------|------------------------------------------------------------|-------|-----------------------|----------------|
| 1-18         | Haswell,avx2,E5-2650_v3, no local scratch                  | 128GB | 20                    | no             |
| 20-24        | Haswell,avx2,E5-2650_v3, no local scratch                  | 257GB | 20                    | no             |
| 26-27        | Haswell,avx2,E5-2650_v3, local scratch 447GB               | 257GB | 20                    | yes            |
| 29-32        | Haswell,avx2,E5-2650_v3, local scratch 932GB               | 128GB | 20                    | yes            |
| 33-43        | Broadwell,avx2,E5-2650_v4,local scratch 932GB              | 128GB | 24                    | yes            |
| 44           | Broadwell,avx2,E5-2650_v4,local scratch 932GB              | 112GB | 24                    | yes            |
| 45-60        | Broadwell,avx2,E5-2650_v4,local scratch 932GB              | 257GB | 24                    | yes            |
| 61-72        | Broadwell,avx2,E5-2650_v4,local scratch 447GB              | 257GB | 24                    | yes            |
| 73-76, 79-88 | Broadwell,avx2,E5-2650_v4,local scratch 932GB              | 128GB | 24                    | yes            |
| 77           | Broadwell,avx2,E5-2650_v4,no local scratch                 | 128GB | 24                    | yes            |
| 89-104       | Skylake,sse4.2,avx,avx2,avx512,Gold_6130, no local scratch | 191GB | 32                    | yes            |
| 105-114       | cascadelake,sse4.2,avx,avx2,avx512,Gold_6230, no local scratch | 191GB | 40                    | yes            |

_Note: node14, 19, 25, and 28 are no longer active._

The table below listed all GPU nodes information from MERCED cluster.

| Nodes  | feature                 | RAM   | Total cores pre nodes | InifiBand (IB) |
|--------|-------------------------|-------|-----------------------|----------------|
| g01-04 | K20m,E5-2650_v3,big_mem | 257GB | 20                    | yes            |
| g05-06 | P100,E5-2620_v4         | 128GB | 16                    | no             |
| g07-08 | rtx6000,Gold_6226R      | 190GB | 32                    | yes            |


## Requesting an account
Request an account via the UC Merced IT website Research Computing
[website](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0).
Before apply an account, please read the following information
carefully.

>What do I need to get this service?

An active faculty or student __with a faculty advisor__ can submit this
request by completing this [request
form](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0).

Each PI account has at least one user group and one queue project
associate with it, which may be used by all group members. PI’s must notify the system administration staff when students, postdoctorals, and other group members depart the University and should no longer have access to MERCED. All data stored in a user accounts will be accessible at all times by the associated PI.
>What is included?

OIT will verify the eligibility and create the appropriate account for
either a PI Group or a user. Please review the following information
prior to the consultation to help determine the best solution for your
needs:
* Faculty PIs __must__ complete and __sign__ an Export Control Attestation
[form](https://it.ucmerced.edu/sites/it.ucmerced.edu/files/page/documents/principalinvestigator.exportcontrolattestation.v2017jan23.pdf)
prior to being given access to managed systems
* Users can install any licensed software packages in their __home__
  directories on MERCED, and where appropriate for other systems. If
  you need assistance, submit a [Research Software Installation Request](https://ucmerced.service-now.com/servicehub?id=sh_form_service_page&formId=06da3f8edbfc08103c4d56f3ce9619f4)(Servers and Clusters), including on which system to install the software
* The MERCED cluster uses a queuing system for job submission.
  Priorities of jobs are assigned on a dynamic basis. Not all jobs
  submitted will begin immediately.

## How to cite
All MERCED users must agree to acknowledge the MERCED Cluster and the
supporting NSF grant (ACI-1429783) in talks, posters, manuscripts, and
other forms of dissemination relying on results obtained from time on
MERCED. An example acknowledgement section is:
```text
This research [Part of this research] was conducted using [MERCED cluster (NSF- MRI, #1429783) / Pinnacles
(NSF MRI, # 2019144) / Science DMZ (NSF- CC* #1659210)] at the Cyberinfrastructure and Research Technologies
(CIRT) at University of California, Merced.
```
From time to time the Committee on Research Computing (CoRC) may request a report of publications and presentations authored by MERCED users that have included results of calculations on MERCED. This information may be used by CoRC in advertising and report documents, future proposals, and/or other materials related to research computing at UC Merced. Failure to respond to CoRC report requests and/or failure to acknowledge MERCED usage in research dissemination may result in suspension or termination of one or more user accounts associated with the non-compliant PI’s group.

## About MERCED
A team of 17 UC Merced faculty prepared and submitted a Major Research Instrumentation (MRI) grant to the National Science Foundation (NSF) in early 2014. The NSF awarded this proposal in August 2014 (NSF Award ACI-1429783). Funding from the NSF-MRI grant and associated institutional cost sharing yields a total initial spending budget of $615,842. This MRI proposal requested support for acquisition of a high performance computing (HPC) system to support scientific computing research and training activities at UC Merced and in support of regional interactions with faculty and students at nearby institutions, including the University of the Pacific, California State University Fresno, and California State University Stanislaus. Individual research programs involving computing at UCM are especially diverse, ranging from quantum chemistry to the history of medieval China and from calculation-intensive femtosecond modeling of nanoscale friction to data-intensive statistical analysis of high-volume genomic data. As one might expect, the most advantageous computing environment for one these groups is often different than that for another. Recognizing this reality, and supporting experimentation with as-yet under-utilized hardware configurations for various applications, this funded NSF-MRI proposal supported the acquisition of the MERCED cluster. 

In further support of the involved scientific research pillars, a key role of the MERCED cluster will be to bridge the gap between the modest sized resources that can reasonably be maintained by an individual faculty-led research group and extensive national supercomputer sites such as the XSEDE system (see www.xsede.org). More specifically, we anticipate MERCED offering a number of scientific and training opportunities. These include: 
* the ability to rapidly reconfigure software and hardware as needed for specific projects; 
* the option to run very long-time calculations that cannot be easily adapted to standard queues offered at most supercomputer environments; 
* the ability to generate and analyze very large data sets locally, avoiding long communication delays; 
* the capacity to train students on a full set of computational skills needed to be competitive for jobs as independent researchers. 

We also note that demonstrated software integrity, stability, and scalability are often a required component of allocation requests at major supercomputer sites. The MERCED cluster will provide the necessary resources to carry out such validation studies locally at UC Merced. Finally, the MERCED cluster will provide outstanding support for training and education. As mentioned above, HPC related research plays an important role in the work carried out in the groups at UC Merced. In addition to our Ph.D. and postdoctoral training programs, UC Merced has an active record of undergraduate education and research. Many of the senior personnel of this proposal are also involved with REU and undergraduate research mentoring programs that focus on scientific computing. The MERCED cluster will provide an excellent resource for those programs. We also expect the MERCED cluster to be used by students taking courses related to scientific computing.



