## System overview
Compute nodes: Compute nodes are where actual jobs run. There are three types of compute nodes on Pinnacles.
* 40 Regular memory (RM) CPU nodes with 256GB RAM
* 4 Big memory CPU nodes (bigmem) with 1TB RAM
* 8 GPU nodes with NVIDIA A100 GPUs
All nodes are interconnected via HDR InfiniBand w/ RDMA for fast (100Gbits/s) and low latency (sub ms) data transfer.

|     CPU node            | RM node                        | bigmem node                    |
|:----------------|:-------------------------------|:-------------------------------|
| Number of nodes | 40                             | 4                              |
| CPU             | 2 Intel 28 core Xeon Gold 6330 | 2 Intel 28 core Xeon Gold 6330 |
| RAM             | 256GB | 1TB|
| Node-local storage             | 1TB NVMe Data Center Solid State Drive (SSD) | 1TB NVMe Data Center Solid State Drive (SSD)|
| Network             | ConnectX-6 VPI adapter card, HDR 100 InfiniBand (100Gb/s) and 100GbE, single-port QSFP56, PCIe3/4 x16 Slot| ConnectX-6 VPI adapter card, HDR 100 InfiniBand (100Gb/s) and 100GbE, single-port QSFP56, PCIe3/4 x16 Slot|

GPU nodes: Pinnacles GPU nodes provide exceptional performance and scalability for deep learning and accelerated computing.

| GPU node     |                                                           |
|:-------------|:----------------------------------------------------------|
| Number       | 8                                                         |
| GPU per node | 2x NVIDIA Tesla A100 PCIe v4 40GB HBM2 Passive Single GPU |
| CPU          | 2x Intel 28-Core Xeon Gold 6330                           |
| RAM          | 256GB                                                     |
| Node-local storage|1TB M.2 NVMe Data Center Solid State Drive (110mm)|
|Network|ConnectX-6 VPI adapter card, HDR-100 IB (100Gb/s) and 100GbE, single-port QSFP56, PCIe3/4 x16 Slot|

## Requesting an account

Requesting access to Pinnacles is a 3-step process.
* UC Merced Principal Investigators (PIs) request consultation to access Pinnacles cluster on [OIT ServiceHub here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0). 
* CIRT schedules a computational need assessment consultation with faculty PIs and assist PIs complete Pinnacles access request form.
* PI completes Pinnacles access request form and UC Merced’s Committee on Research Computing (CoRC) receives this form and approves/denies access requests.

?> If you still have questions, we have put together a Pinnacles FAQ page that has the most common questions received and will be keeping it up to date

Before apply an account, please read the following information
carefully.

>What do I need to get this service?

An active PI or student __with a PI advisor__ can submit this
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
All Pinnacles users must agree to acknowledge the Pinnacles Cluster and the
supporting NSF grant (NSF MRI, # 2019144) in talks, posters, manuscripts, and
other forms of dissemination relying on results obtained from time on
Pinnacles. An example acknowledgement section is:
```text
This research [Part of this research] was conducted using Pinnacles
(NSF MRI, # 2019144) at the Cyberinfrastructure and Research Technologies
(CIRT) at University of California, Merced.
```
From time to time the Committee on Research Computing (CoRC) may request a report of publications and presentations authored by Pinnacles users that have included results of calculations on Pinnacles. This information may be used by CoRC in advertising and report documents, future proposals, and/or other materials related to research computing at UC Merced. 

