# High Performance Computing at UC Merced
There are two HPC clusters at UC Merced, MERCED and Pinnacles Cluster. Both clusters employ  the [Slurm](https://slurm.schedmd.com/) job scheduler to schedule to manage queued and running jobs. 


## Pinnacles cluster 
The NSF-MRI funded Pinnacles cluster is available for all faculty projects __at no cost!__ Pinnacles features newer generation of Intel Xeon Gold 6330 CPU processors and NVIDIA Tesla A100 v4 40GB HBM2 GPUs. 

Pinnacles cluster has RedHat Operating System.



### Pinnacles Facility statement <!-- {docsify-ignore} -->

The NSF-MRI grant number #2019144 funded Pinnacles cluster is available for all faculty projects at no cost. 

Pinnacles cluster has the following compute node configurations: 
* 40 regular Compute nodes with 2XIntel-28-Core Xeon Gold 6330 2.0GHz - 205W, each with 256GB RAM. 
* 4 High Memory nodes with 2x Intel 28-Core Xeon Gold 6330 2.0GHz CPUs and 1TB RAM for large memory calculations.
* 8 GPU nodes, and each one of the nodes has 2X NVIDIA Tesla A100 PCIe v4 40GB HBM2 Passive Single GPU.
Pinnacles also has ~92TB NFS Fast Scratch Storage space for accessing large data with low latency and 1.5PB of usable long-term storage.

All above nodes are interconnected via HDR InfiniBand w/ RDMA for fast (100Gbits/s) and low latency (sub ms) data transfer.

Relative proximity and extent of availability: The Pinnacles cluster is managed by the Office of Information Technology at UC Merced and technical support and training opportunities are available. It is available for
all faculty projects at no cost. 


## MERCED cluster 

MERCED (Multi-Environment Research Computer for Exploration and
Discovery) Cluster is a 2096 core Linux based high performance computing
cluster. The MERCED cluster runs with the [CentOS](https://www.centos.org/).

!> MERCED cluster is a recharge-service model.

Recharge Service on MERCED cluster describes that all jobs ran on MERCED are billed based on calculated and used  core-hours. 


### MERCED Facility statement <!-- {docsify-ignore} -->

MERCED is a general-purpose computing cluster located in the server facility (see computing facilities [section](README.md)). The cluster consists of a login node, 65 compute nodes, and 15 high memory nodes. Total CPU counts is 1872.

### MERCED Recharge Service 

In order to minimize disruptions to computational research on MERCED cluster, the Provost’s office has provided bridge funding for all MERCED cluster PIs for core-hour usage on MERCED through June 30, 2024


__Faculty PIs__: Please ensure that the user accounts are active and provide the COA# [here](https://merced-my.sharepoint.com/personal/yyu49_ucmerced_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fyyu49%5Fucmerced%5Fedu%2FDocuments%2FMERCED%5Frecharge&ct=1639436999554&or=OWA%2DNT&cid=61ce730a%2D0df2%2Dd438%2D7bdf%2Dbe138cf58c23) before EOB __12/21/2021__. 
Email schadalapaka@ucmerced.edu for instructions.

What is the unit of cost service? MERCED cluster cycles will be charged by **core-hours<sup>(1)</sup>**.

(1)  A core-hour is a single compute core<sup>(2)</sup> used for one hour (a core-hour) and 2G of RAM. The total cost in core-hours for a complete computation is:
```text
Total Cost ($) = # of core-hours x Duration (wall clock hours) x (cost per core-hour)
```
!> **For UC users, the cost per core-hour is $0.01, and the cost for non-UC external users is $0.02.**

(2)  A core is an individual processor: the part of a computer that executes programs. (The MERCED cluster has about 3100 cores.)

### MERCED - Recharge Questions

>Q:I have a lot of work on MERCED, but do not want to pay the Recharge rate, what are my options?

All work that was stored on MERCED can be accessed and be used on Pinnacles cluster for **Free**.
User's can always obtain access to other free compute resources such as our new NSF-MRI Pinnacles cluster, and [ACCESS](https://access-ci.org/) resources. CIRT can provide consultation for how to access these resources. Schedule a consultation [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

>Q: How to include CIRT managed charged services into budget statement? 

The faculties plan to include the budget for CIRT-managed charged services in the budget statement. Please list it under the category of 'Other Direct Costs.' For example, purchased HPC storage services can be allocated to the 'Materials/Supplies: MERCED HPC storage and maintenance' category within the 'Other Direct Costs' section.