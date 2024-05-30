# Introduction <!-- {docsify-ignore} -->
Conda is a package management environment and package manager that is primarily used for open-source software packages. Conda is associated with Python and R programming languages but also supports C++ and Fortran. 

Below is documentation on installing and maintaining a Conda environment on the HPC clusters. 

## Build your own conda environment <!-- {docsify-ignore} -->
### Load and initializing conda <!-- {docsify-ignore} -->
If you have not put the `conda init` into your `.bashrc` file, then it is necessary to initialize the conda environment before using. Once users log into the HPC system, you need to type the following command
```
module load anaconda3
conda init
```
!> Note: if you get a warning messages after `conda init` command, you need to log out the HPC system, and then log back in. You will then be able to initialize the system. Once the conda environment is initialized, you will see the environment name (default one is called `base`) next be listed next to your username in the command line. 

### Edit your `.condarc` file <!-- {docsify-ignore} -->
By default,  conda stores packages in the `HOME` directory. If you want to change the default path to somewhere you desire, for example `/data/$USER/`, you can use a text editor to create a file called `.condarc` under the path `/home/$USER/.condarc` and it should contain the path to the alternative location. 

e.g.:
```
pkgs_dirs:
 - /data/$USER/conda/pkgs
```
!> More `.condarc` examples can be found [here](https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html)

### Installing and activating a `conda` environment <!-- {docsify-ignore} -->
To install `conda` environment, you can specify a prefix, which will be the path to where the environment will be installed. If you don't include `prefix`, the default path will be under your `HOME`.  Choose a descriptive name for the environment- Conda will create the directory, the directory should not already exist. For example, if you want to create a conda environment called `env_aaa` containing the packages `AAA, BBB, CCC`, and insatll it in the directory `/data/$USER/packages`, you can do following
```
conda create --prefix /data/$USER/packages/env_aaa AAA BBB CCC
```

To activate the environment, you can do:
```
conda activate /data/$USER/packages/env_aaa
```
?> If you are using the default package path, you do not need to include path to activate the environment, you can just do:
```
conda activate ENV_NAME
```




!> Note: user can also create a `YAML` file with all of the desired conda packages so that conda will find the correct configuration to solve the environment. 
The `YAML` file will contain a name, a list of Conda channels to look for the packages, and a list of all the desired packages.

Here are some sample `YAML` files:
* **[datascience.yml](_media/datascience.yml ':ignore')** - Contains many common data science programs
* **[sklearn.yml](_media/sklearn.yml ':ignore')** - Machine learning with scikit-learn
* **[biotools.yml](_media/biotools.yml ':ignore')** - Contains applications for a bioinformatics workflow


###  Using Anaconda in SLURM job scripts <!-- {docsify-ignore} -->

Conda does not know the source when it is called in a SLURM job script. To ensure conda knows the source of the environment that it will be activating during the execution of the SLURM job script,`source activate <env name>`. This will ensure SLURM to look for the called environment in the correct PATH. 

An example job script utilizing a conda environment can be found [here!](running_R_mpi.md)

!> Note using `conda activate <env name>` may result in error as `conda activate `makes the assumption that the environment is being called in the same PATH it exists, which is not the case for SLURM jobs. 

### Common Issues with Conda<!-- {docsify-ignore} -->
Without running `conda init` the commands `conda activate` and `conda deactivate` will present the following warning.

```
[tester001@rclogin01 ~]$ conda activate
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
- bash
- fish
- tcsh
- xonsh
- zsh
- powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.

```
Since `conda init` injects some logic into your .bashrc file it must be sourced. For interactive job sessions `conda init` does not need to be called as the source is already known. However this is not the case for SLURM jobs,  therefore it is important to add `source .bashrc` to the submission script to allow subsequent conda activate or conda deactivate commands to work. 




