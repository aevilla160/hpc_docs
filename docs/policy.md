# Acceptable user policy for resources managed by CIRT

**Updated by Yue Yu, May 2022**

## University policies
1. All PIs must fill and sign the export control [form](https://ucmerced.app.box.com/s/e6pmv4cv59tz76aat5re1kzvg23c0s09) before using clusters (MERCED and Pinnacles).
2. All users are responsible for following University of California's "[Electronic Communication Policy](https://policy.ucop.edu/doc/7000470/ElectronicCommunications)" related to computing and electronics. These include but not limited to tolerance, civility, and respect for diversity of background, gender, ethnicity, race, religion, political beliefs, sexual orientation, and physical abilities.
   

## Cluster jobs
1. Cluster jobs mush be run on compute nodes. Running jobs on login nodes is prohibited, and any jobs/processes that impact the performance or functions of the login nodes or interfere with other users will be terminated and an email will be sent to the user for warnings. 


## Quotas and storage
1. Data quotas for [MERCED](accessMerced.md) and [Pinnacles](accessPinnacles.md) are managed by CIRT. Users are reminded that storage provided by CIRT is for research data only. Users are responsible for ensuring that backups of their data. 
2. While CIRT makes great effort to maintain the availability and integrity of storage product, but users should keep in mind that no data storage on our managed servers have historical backups. Some data servers provide "snapshot" where data changed/delted within the snapshot window can be retrieved, but this is not guaranteed. Data in `beegfs` based file system do not have the capability for snapshots. 
3. Scratch folders on both clusters are valid only when `clusterstorage` is less than 80% full, and files will be automatically deleted when `clusterstorage` reaches the 80% space usage. It is recommended that when a batch job has completed, user should transfer the output files to somewhere safe from `scratch`. 


## Software and services
