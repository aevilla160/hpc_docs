# Condo Model - Pinnacles Cluster
<schedule a consulation add a link>

## Condo Model Description
Condo computing is a shared ownership model. PIs(i.e. faculty) use equipment purchase funds from grants or other sources to purchase and contribute compute resources (i.e., nodes) to the cluster. The result is a shared researcher-owned computing resource of medium to large proportions that provides access to much larger configurations than each participant purchased individually.

Under the condo model, PIs use equipment purchase funds to buy compute (CPU or GPU) nodes that will be operated as part of the cluster. Participating groups may then have dedicated use of their purchased nodes via private partitions, or they may run larger computing jobs by sharing idle nodes owned that are on the Pinnacles cluster. This allows for immediate and integrated access to a larger cluster that would typically not be available. 


Participation in the program runs the duration of the node's warranty coverage(~ 3 years).

## Contributing to Pinnacles Cluster via Condo Model

PIs can seek purchasing computing resources that are compatible with the Pinnacles Cluster. PIs can schedule a [consultation](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) with CIRT to discuss which computing resources(nodes) are compatible to be added to the Pinnacles cluster. 

When contributing to the Pinnacles cluster, PIs can expect their group to have the highest priority to their node(s) with the use of a private partition. PIs should expect to also have their nodes be publicly accessed via `test` partition.  It is expected that CIRT will house and maintain these nodes in the cluster for as long as they are under warranty.

The following tables summarize the CPU and GPU computing resources that are available for purchase in the Pinnacles condo program. 

## Compute Resources compatible with Pinnacles Cluster


### CPU 
| CPU Model	| CPU Quantity Per Node| Core Count Per Node | RAM Capacity | 
| -------- | ---- | ----------- |---------- |
| Intel 28 core Xeon Gold 6330 | 2 |56(28*2) cores | 256GB | 
| Intel 28 core Xeon Gold 6330 | 2 | 56(28*2) cores | 1TB |

Ram Capacity can be scaled up for sizes greater than 1TB. 

!> All nodes are configured with HDR100 slots. 

### GPU
| GPU Model	| GPU Card Quantity Per Node | RAM Capacity | 
| -------- | ---- | ----------- |
| Nvidia GPU | 1 - 4 cards | Varies |

!> These are estimate prices, and final price will be determined after consultation. 

## Other Associated Costs 

Other associated costs(i.e. switches, ethernet cables, etc.) will be determined upon or after consultation with CIRT. 

Below is a table with associated tasks/items and their costs. 

| Service | Unit | UC Rate |
| --------------------- | ---------------- | -------------- |  
| Infrastructure Fee (covers racks, switches, cables, etc.) | Installation | $250 | 
|EDR Infiniband (covers IB cable and IB switches). | Installation | <COST> |
|Condo CPU/GPU Operations Fee (per purchased node)  | Node/year | $500 | 

!> Costs from the table are estimates. Final costs and configurations will be shared after consultation. Annual fees covers labor to maintain the system, utilities, software licenses and other maintenance costs.


## OS, CV software license fee $??/node for `Associated Costs Section`

## Clustervisor - Cluster Management Software Licensing Cost?



## Process - Condo Model for Pinnacles Cluster

1. Consultation between CIRT and PI(s), determining the appropriate hardware
2. Work with CIRT and our primary vendor ACT to obtain the associated quotes
3. Once the quotes have been obtained and given to the PI, PI will have to work with their respective departments to purchase the hardware. CIRT asks that the PI keeps us in the loop for any questions regarding shipping and recieving and other associated tasks. 



## Queue Priority

1. Users in the associated group(s) will be given the highest priority on the node via a privat partition. 
2. CIRT will allow all users to be placed on the condo node via the `test` partition.

## Warranty

Principal Investigators (PIs) who contribute to Pinnacles by purchasing their own nodes will receive details about their nodes' warranty.

 A HPC cluster node will be considered beyond its lifetime of maintainability when the compute node warranty from the HPC cluster vendor has expired. Typically, computing resources come with a warranty of 3 years, though this duration may vary.


Below are options that CIRT offers to PIs when the nodes become out-of-warranty. 

CIRT will give the PI two options: 

1. CIRT Keeps the node(s) and merge to public partition - 

     
    PI-owned queues will cease to exist and and the nodes will be merged into general, public partition(s).


    CIRT will take the ownership of the nodes and take responsibility for the maintance and housing of the node post-warranty. CIRT will also reserve the right to retire the node(s).
   
2. CIRT returns the node to the PI

    CIRT will facilitate removing the PI node from the cluster, and
    PIs might incur costs for CIRT's time and effort on the proceess of removing the node.
    PI will be soley responslbe for the node once returned. 


## End of Maintainability 

When a node or computing resource comes to the end of it's maintabiliity where it becomes ineffective to continue to purchase parts for it, or parts are no longer produced or the QoS becomes poor, requiring lots of attention and staff oversight. We will proceed with taking it down from the cluster and offer options to the PI. 

1. CIRT Keeps the node(s) and merge to public partition - 

     
    PI-owned queues will cease to exist and and the nodes will be merged into general, public partition(s).


    CIRT will take the ownership of the nodes and take responsibility for the maintance and housing of the node post-warranty. CIRT will also reserve the right to retire the node(s).
   
2. CIRT returns the node to the PI

    CIRT will facilitate removing the PI node from the cluster, and
    PIs might incur costs for CIRT's time and effort on the proceess of removing the node.
    PI will be soley responslbe for the node once returned. 

## Condo PI-Contributor Highlight
Below is a table of PIs who have contributed nodes to the Pinnacles cluster, assisting in the growth and power of Pinnacles. 

| PI | Department |  Queue | 
| -------------- | ----------------------- | --------------- |
| Bercem Dutagaci | QSB | pi.bdutagaci |
| Changho Kim | Applied Math | pi.ckim103 |
| Henrik Larsson | Chemistry & Biochemistry | pi.larsson |
| Ashlie Martini | Mechanical Engineering | pi.amartini |
| Anna Nierenberg | Physics | pi.anierenberg |
| Aurora Pribram-Jones | Chemistry & Biochemistry | pi.apribram-jones |
| David Strubbe | Physics | pi.dstrubbe |



## Condo Department-level Contributor Highlight 
Below is a table of departments who have contributed nodes to the Pinnacles cluster, assisting in the growth and computing power of Pinnacles. 

| Department | Queue |
| ----------------- | --------------- |
| Life & Enviromental Science | dept.les |
| Applied Math | dept.appliedmath |
| Cognitive Science | dept.cogsci |
| Center for Cellular and Biomolecular Machines | grp.ccbm |

## Joining the condo program
Please reach out to CIRT to schedule a consultation via [ServiceNow](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4)
## Other Policies 
