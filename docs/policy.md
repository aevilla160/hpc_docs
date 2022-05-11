# Acceptable user policy for resources managed by CIRT

**Created by Yue Yu, May 2022**

## University policies
1. All PIs must fill and sign the export control [form](https://ucmerced.app.box.com/s/e6pmv4cv59tz76aat5re1kzvg23c0s09) before using clusters (MERCED and Pinnacles).
2. All users are responsible for following University of California's "[Electronic Communication Policy](https://it.ucmerced.edu/sites/it.ucmerced.edu/files/wp-content/uploads/2017/11/acceptable-use-policy.pdf)" related to computing and electronics. These include but not limited to tolerance, civility, and respect for diversity of background, gender, ethnicity, race, religion, political beliefs, sexual orientation, and physical abilities. For more policies and guidelines, please visit [here](https://it.ucmerced.edu/oit-policies-guidelines).
   

## Cluster jobs
1. Cluster jobs must be run on compute nodes. Running jobs on login nodes is prohibited, and any jobs/processes that impact the performance or functions of the login nodes or interfere with other users will be terminated and an email will be sent to the user and their PI notifying cluster usage best practices and policy. **CIRT offers “Introduction to HPC” training sessions for new HPC users. Schedule [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4)**


## Quotas and storage
1. Data quotas for [MERCED](accessMerced.md) and [Pinnacles](accessPinnacles.md) are managed by CIRT. Users should note that storage provided by CIRT is for research data only. Users are responsible for ensuring that backups of their data.
2. While CIRT makes great effort to maintain the availability and integrity of storage product, but users should keep in mind that no data storage on our managed servers have historical backups. Some data servers provide "snapshot" where data changed/delted within the snapshot window can be retrieved, but this is not guaranteed. Data in `beegfs` based file system do not have the capability for snapshots. 
3. Scratch folders on both clusters are valid only when `clusterstorage` is less than 80% full, and files will be automatically deleted when `clusterstorage` reaches the 80% space usage. It is recommended that when a batch job has completed, user should transfer the output files to somewhere safe from `scratch`. 


## Software and services
1. Software on clusters should directly support research/learning. Users are generally not restricted from downloading/compiling software under their own `HOME` directory for use in research or teaching. Users are responsible for the software they installed or compiled.
2. Users choosing to self-install software have the responsibility to use them from trustworthy sources. These might include common community repositories such as CRAN, CPAN, PyPy, and Anaconda; community-acceptable applications; or known-to-the-user software packages. Users should avoid downloading pre-compiled binaries or containers from unknown sources.
3. Requesting CIRT to install/compile software. Users may request CIRT to build/install software in system for community use. **CIRT does not have the people resources to accept all requests and must prioritize**. CIRT can also deny software installation request that is not suitable for the environment.
4. No guarantee of long-term maintenance of specific software/services. System-wide software new installation, security concerns, and other new patches add to the system evolve over time and any of these changes may result in a specific software/service to be unsupportable. Any such situation happen the corresponding software/service will be removed from the infrastructure.
