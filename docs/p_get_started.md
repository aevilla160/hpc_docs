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

The following detail consists of how to request Pinnacles cluster access. If you have questions or concerns, do not hesitate to:
* Schedule a Pinnacles consultation [here](https://arrangr.com/sarvani/facultyconsult). 

!> Who can request access for Pinnacles cluster?
* UC Merced Faculty Principal Investigators (PIs) can request access to Pinnacles cluster. All user accounts on Pinnacles cluster are associated with that of a UC Merced PI.

!> Who approves access requests to Pinnacles?
* UC Merced’s Committee on Research Computing (CoRC) meets monthly and approves/denies access requests for Pinnacles.

!> How to request for Pinnacles cluster access?

__Requesting access to Pinnacles is a 3-step process.__
1. UC Merced Principal Investigators (PIs) or other researchers request Pinnacles account [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=643ea9ff1b67a0543a003112cd4bcba3&form_id=280d8bb04f72f6006137d0af0310c7b0).
2. For new account group project applications, PIs please also make sure to complete the export control [form](https://ucmerced.app.box.com/file/827800760668?s=e6pmv4cv59tz76aat5re1kzvg23c0s09), if the PI has not done one before.
3. Once the form is completed, please attach the form to the request ticket from step 1.

?> Questions?

If you still have questions, we have put together a Pinnacles [FAQ page](pinnacles_FAQ.md) that has the most common questions received and will be keeping it up to date


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

