## Getting started about the Campus Jupyterhub

## Pedagogy and Technology
To ensure our courses are accessible to students of all majors, we aimed to use technology that is both simple and powerful. We wanted to eliminate the frustrations commonly associated with setting up and maintaining a development environment, often encountered in introductory computing courses.Students can start writing and running code immediately, without wasting time on installation or setup.

### JupyterNotebooks? <!-- {docsify-ignore} -->

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain **live code**, equations, visualizations, and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

### The `datascience` Package <!-- {docsify-ignore} -->

In addition to the computing infrastructure, another piece of the technology is the [`datascience` package](http://data8.org/datascience/). While traditional libraries such as `pandas` and `matplotlib` are powerful, they are also quite complicated, and the verbose code and documentation can intimidate those who are new to programming. The `datascience` Python package was written for use in Berkeley’s Data Science courses and aims to provide a simple but powerful set of tools for introductory students. Students that are in or have taken Data 8 will be familiar with this package as it is used throughout the course.

The package contains useful functionality for investigating and graphically displaying data. One key component of the `datascience` package is the `Tables` abstraction, which is similar to a `pandas` dataframe. The package also contains useful functionality for drawing maps and plotting.

## Introduction to Jupyter

### What are Jupyter Notebooks? <!-- {docsify-ignore} -->
### JupyterNotebooks?
Jupyter Notebook is an open-source web application that allows you to create and share documents that contain **live code**, equations, visualizations, and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

### Features <!-- {docsify-ignore} -->

  - **Interactive Environment:** Jupyter Notebooks provide an interactive computing environment where users can write and execute code in a step-by-step manner.
  - **Support for Multiple Languages:** While originally designed for Python, Jupyter Notebooks support various programming languages like Julia, Python, and R.
  - **Rich Output:** Notebooks allow the incorporation of rich media outputs such as plots, images, videos, and interactive widgets alongside code and text cells.
  - **Markdown Support:** In addition to code cells, users can include Markdown cells to write formatted text, equations (using LaTeX syntax), and even HTML for documentation or explanations.
  - **Data Visualization:** Using libraries like Matplotlib, Seaborn, users can create interactive and static visualizations directly within the notebook environment.
  - **Integration with Libraries and Tools:** Jupyter Notebooks seamlessly integrate with various data science libraries and tools such as NumPy, Pandas, SciPy, TensorFlow, and scikit-learn.

### Components <!-- {docsify-ignore} -->

- **Cells:** Notebooks are composed of individual cells that can contain either code, Markdown-formatted text, or raw content. Users can execute code cells and render Markdown cells to produce outputs.
  
  ![jupyter_Cells](./imgs/jupyter_cells.png)


- **Kernel:** Each notebook is associated with a computational kernel, which is responsible for executing code within the notebook. Different kernels support different programming languages.

  ![kernel](./imgs/kernel.png)

- **Toolbar:** The toolbar provides quick access to common actions such as running cells, saving the notebook, adding new cells, and changing cell types.

  ![toolbar](./imgs/toolbar.png)
- **Menu Bar:** The menu bar contains various options for manipulating the notebook, managing kernels, and configuring the notebook environment.

  ![menubar](./imgs/menubar.png)
- **Output Area:** Code cells display their output, including text output, error messages, and visualizations, in the output area directly below the cell.

   ![output_area](./imgs/output_area.png)

- **File Format:** Notebooks are saved in a JSON file format with the `.ipynb`

### Using Jupyter Notebooks for Data Analysis <!-- {docsify-ignore} -->

**Jupyter Notebooks** are incredibly versatile for **data analysis** projects. They allow data scientists to combine **executable code**, rich text, **visualizations**, and equations in a single document.

- **Interactive Data Exploration:** Notebooks facilitate interactive exploration of datasets, enabling quick iterations over a data preprocessing or analysis pipeline.
- **Visualization:** With support for libraries like **Matplotlib** and **Seaborn**, users can create and embed graphs directly within notebooks.
- **Collaboration and Sharing:** Notebooks can be easily shared between users, promoting collaboration on data analysis projects.


### Why does JupyterHub Exist? <!-- {docsify-ignore} -->

[Jupyterhub](https://jupyter.org/hub) JupyterHub is an open source tool that lets you host a distributed Jupyter Notebook environment. With JupyterHub, users can log in to the server, and write Python,R code in a web browser, without having to install software on their local machine.

Working on JupyterHub provides a number of benefits, especially in an introductory course:

Students never have to do any setup or installation. JupyterHub removes the burden of setting up and maintaining a development environment.

All students and instructors use the same computing environment.

Work stored in the cloud and can be accessed from any computer.

All students have access to the same compute power, regardless of the machine they are using. For example, students without personal computers can use publicly shared computers(i.e. library computers) without being at a disadvantage in the course.

### Differences from local installation <!-- {docsify-ignore} -->

| **JupyterHub** | **Local Setup** |
| :--- | :--- |
| Needs an internet connection | Does not need an internet connection |
| Limited resources \(disk and RAM\) | Unlimited resources \(limited only by your computer\) |
| System-wide installation done by admins | You can install anything you want |
| You can only access files in your account | You can maybe access all files \(if you are an admin\) |
| If things break, we fix them :\) | If things break, you have to fix them :\( |

### Overview of the Internals <!-- {docsify-ignore} -->

The first time you logs in to JupyterHub, a personal account is created for you. You will get your own filesystem so you only have access to the files in your personal account. **Modifications to files in your personal account do not affect anyone else's files.** Unless you are an admin, you cannot access another account's files. This applies to everyone working on JupyterHub, which means a given student cannot access another student's work.

### Getting Access

Anyone with UCMerced credentials has access to the JupyterHub at [ucmerced.2i2c.cloud]([https:///ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login)). If you are having difficulties with logging in, please make sure that you are using the correct JupyterHub URL and a ucmerced.edu email to login. 
      
### Where to get help
  
   ![](./imgs/landingpage.001.png)

Support for JyupterHub is provided during standard operating hours: 8:00 a.m. – 5:00 p.m., Monday through Friday. Please submit a general ticket through the [UC Merced ServiceHub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).
If you're having issues accessing JupterHub, please Report a Problem at [servicehub.ucmerced.edu](https://ucmerced.service-now.com/servicehub) or call 228-HELP (4357).The same information can be found on the landing page of the JupyterHub.

     
### Jupyterhub office hours
Jupyterhub/Datascience office hours every **Friday from 11:30 AM to 1:00 PM in ACS Room 365**

    Zoom Details:

    https://ucmerced.zoom.us/j/87915353522?pwd=bW5zV3NCNWk5d2dvVkZwaXlObHJ3dz09
    Meeting ID: 879 1535 3522
    Passcode: 035925

Please feel free to drop by if you need help with anything from setting up your environment, or if you're just curious to learn more about more on JupyterHub. If these times don't work for you but you still require support, I encourage you to open a ServiceNow ticket [UC Merced ServiceHub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) .

### ServiceHub requests for scheduling consultations

Please raise a general [UC Merced ServiceHub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) request for scheduling consultations.

### Notebook Zero

Notebook zero typically includes a variety of subjects and is often customized for the specific course it supports. However, there are a few consistent elements found in every notebook zero.

- code and Markdown cells
- variables and Python data types (int, float, str, bool)
- arithmetic and operators
- logical operators and keywords (and, or, not)
- if/elif/else statements
- functions and builtins
- errors

Depending on the course or module, more topics may be covered (e.g. importing libraries, iteration). While these notebooks tend to be very homogeneous.

Please find the [Notebook Zero](https://github.com/SaiUCM/Jupyterhub_Docs_Instructor/blob/main/Notebook%20Zero.ipynb) which covers the above mentioned topics and it also explains how to plot the graphs using Matplotlib and Plotly libraries.

### Onboarding new users to the Hub

```{note}
New to Datahub? Interested to learn more about the services offered by the hub? If yes, refer below!
```
**I am instructor planning to teach using Jupyterhub. How do I onboard myself?**

Dear Instructor, Sharing few logistical information which would make onboarding easy for you.Please follow this documentation to onboard a User to Jupyterhub.

- Documentation: You can also refer to the FAQ section of this support documentation (Curriculum Guide), where we regularly update solutions to some of the reported issues.
 
- Packages: Check whether all the needed Python/R packages and their required versions are installed in Jupyterhub.The Procedure for package installation varies across different programming languages. Basic python packages such as numPy, pandas, scikit-learn, matplotlib, etc., are installed across the main Datahub. R hubs supports packages such as shiny, dplyr, tidyR, RSQLlite, etc. Here is the list of  [Python Packages](https://ucmerced.app.box.com/s/x2eigcssqyeca9mrid3m19glfcs73j02) installed in [ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login) . Here is the list of [R packages](https://ucmerced.app.box.com/file/1481528927192?s=65r1rda9atblpdsxdvtyaq6exlnns9z3) of R packages installed in [ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login)

If you require a permanent solution then you need submit a [UCMerced Service Hub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) to us to install the required package(s) in Jupyterhub.


**How can I learn more about Datahub to onboard myself?**

If you are new to Jupyterhub and want to know more, refer [here](https://ucmerced.2i2c.cloud/hub/login). 


**What languages are supported by the hub?**

Jupyterhub primarily supports three languages - **Python, R**.


**What is the default Memory/CPU requirement for every hub?**

Jupyterhub has a memory limit of 1 GB of RAM, which should meet the teaching/research needs of most of our users. If you are interested to know more about the memory consumption in your instance, Please use the following steps,

Look at the top right corner of your Python/R notebook for the term memory. It will highlight the amount of memory you had consumed by the amount of memory provided to your instance. 


```{figure} ../imgs/memory.png
:width: 500px
:align: center
:name: Available Memory

**As an instructor what do I need to do to set up the hub for my course?**

Honestly, nothing! You are free to use the Datahub starting today. 

```{note}
We expect that all course members log in using their UC Merced email id. We also expect that you are using [nbgitpuller service](https://jupyterhub.github.io/nbgitpuller/link) to distribute materials to your class. We can help you set up the links so that you can distribute through your course website. 
```

**What instructions should I share with students at the start of the semester**
Please ask your students,

- To download and backup their files at the end of semester.
- To refrain from installing python packages via `pip install --user`. Incase, if they install packages this way it may cause issues with launching their Jupyterhub. Best way to avoid this scenario is by installing packages by requesting them via [UCMerced Service Hub request](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4)



**How do my students download their submissions as a PDF?**
We recommend that you use the following options,
 
- **For Jupyter Notebooks:** Select File -> Save and Export Notebook as -> PDF via HTML(.pdf) to get the PDF version of your notebook. 
```{figure} ../imgs/downloadhtml.PNG
:width: 500px
:align: center
:name: Downloading notebook as a PDF 
Here is where you can find the option to download the Python notebook as a PDF!
```
- **For R files:** Select File -> Knit Document -> Select the target folder -> Select the Output Format as PDF to save the PDF version of the file
 ```{figure} ../imgs/knitting.PNG
:width: 500px
:align: center
:name: Downloading R notebook as a PDF
Here is where you can find the option to download the R file!
```
```{figure} ../imgs/knittingpdf.PNG
:width: 500px
:align: center
:name: Downloading notebook as a PDF
Here is where you can find the option to specify the download format as PDF!
```


### What are the packages pre-installed in the Jupyterhub?

The Procedure for package installation varies across different programming languages. Basic python packages such as numPy, pandas, scikit-learn, matplotlib, etc., are installed across the main Datahub. R hubs supports packages such as shiny, dplyr, tidyR, RSQLlite, etc. 

You can use the following command in Python to see the list of available packages in JupyterHub.
```
!pip list

```

You can use the following command in R to see the list of available packages in JupyterHub.

```
installed.packages()

```

Here is the list of  [Python Packages](https://github.com/berkeley-dsep-infra/datahub/blob/staging/deployments/datahub/images/default/requirements.txt) installed in [ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login) . Here is the list of [R packages](https://ucmerced.app.box.com/file/1481528927192?s=65r1rda9atblpdsxdvtyaq6exlnns9z3) of R packages installed in [ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login)

### What should I do if I want to install more packages?

Use your Jupyterhub instance to install the required version of the package. Self installation of packages in your instance of hub is a temporary measure to identify dependencies. If you require a permanent solution then you need submit a [UCMerced Service Hub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) to us to install the required package(s) in your hub.

If you want to install packages for Python in your instance, then use the following syntax,

```
!pip install <package-name>

Eg: !pip install numpy

```

If you want to install packages for R in your instance, then use the following syntax,

```
install.packages("<package-name>")

Eg: install.packages("ggplot2")

```

### Pre-installed Packages

Many Python packages have been pre-installed on JupyterHub and are available by default. To use a pre-installed package such as numpy, you can simply type the line below into a code cell.

``` 
import numpy

```

### Long-term installation

*This is the recommended method for packages that will be used frequently.* If you require a permanent solution then you need to [UCMerced Service Hub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) us to install the required package(s) in your hub.

As in best practice, the installation will be done on staging hub first, and once validated, will be installed in the production hub.


> Before sending a request to CIRT team for installing new packages on Jupyterhub Kindly mention its Version as well

## Troubleshooting issues in the Hub

Facing issues with your hub and want to do some basic troubleshooting before escalating issues to us? If yes, read below!

One common error is a Jupyter notebook becoming unresponsive. You will know that a notebook is unresponsive. Another type of error is a user not being able to access some part of their JupyterHub account.

We have outlined two methods below that you should try for each error type. For errors related to the execution of code, such as the notebook not running properly, you should try restarting the kernel. For errors related to access, you should try restarting the server.

### Restarting the Kernel

If your notebook becomes unresponsive, you can try to restart the kernel

![](./imgs/Kernel_list.002.png)


### Restarting Your Own Server

All users can restart their own servers. To do this, begin by going to the **Hub** **Control Panel** from the dropdown menu from File menu.

![](./imgs/status.003.png)

Once you click on Hub Control Panel.It will navigate to the page and Click the **Stop My Server** button.

![](./imgs/start_server.004.png)

Once the server has stopped and the Stop My Server button is no longer visible, click the **My Serverbutton (should be Start My Server)** to restart the server.

![](./imgs/startserver.005.png)

## Troubleshoot issues with Hub/Server/Code running slow

### What should I do if my hub is running slow?

Try these recommended options,

- Restart your kernel.
- Check whether there are a lot of open tabs. If yes, close the tabs that are not required.

### What should I do if my code is running slow?

In general, this issue could be attributed to the varied programming practices adopted that might have slowed the operation of the hub. Check whether your code does any of the following,

- You are running an infinite loop
- Your computation/calculation is big
- You are joining tables that are too large
- You have too many notebooks open at the same time
- You are trying to show a table which is too large and as a result are crashing the browser

If they are relevant, try fixing these issues by improving the programming practices or by reducing the size of the dataset. 


## Creating assignments - Using ottergrader

[Otter Grader](https://otter-grader.readthedocs.io/en/latest/) is a light-weight, modular open-source autograder developed by the Data Science Education Program at UC Berkeley. It is designed to grade Python and R assignments for classes at any scale by abstracting away the autograding internals in a way that is compatible with any instructor’s assignment distribution and collection pipeline.

The following steps explain how to create assignments/homework using [otter-grader](https://otter-grader.readthedocs.io/en/latest/) and Jupyterhub.

[Otter-Grader](https://otter-grader.readthedocs.io/en/latest/) parses a parent notebook containing questions, solutions, and tests to create two distribution directories: one with solutions and all tests for automatic grading and a second with no solutions and only public tests for students.

Before Creating assignments using otter-grader let’s understand the important concepts that will be helpful.There are three different types of cell formats in Jupyter Notebooks which are.
- Raw -→ This option will be used as plain text
- Markdown -→ It will be used to create the Markdown format text ex.Headers,Links,Images,text in a md format
- Code -→ When u change the cell type into code block, where we can write the Python or R code

![](./imgs/cells.006.png)


### Assignment Config

In addition to various command line arguments discussed below, Otter Assign also allows you to specify various assignment generation arguments in an assignment config cell. These are very similar to the question config cells described in the next section. Assignment config, included by convention as the first cell of the notebook, places YAML-formatted configurations in a **raw cell** that begins with the comment **# ASSIGNMENT CONFIG.**

- Example
```
# ASSIGNMENT CONFIG

  solutions\_pdf: true

  export\_cell:

  instructions: "These are some submission instructions."

  generate: 

  pdf: true

  filtering: true

  pagebreaks: true

  zips: false
 ```

For more information about **# ASSIGNMENT CONFIG** please refer the [documentation](https://otter-grader.readthedocs.io/en/v4.4.1/otter_assign/v1/notebook_format.html).

### Creating Questions

- The questions always starts with #BEGIN QUESTION and ends with #END QUESTION in between those we can create solution and test cases for that question.The following syntax will explain the question,solution and test cases format

### Question Format

```
#BEGIN QUESTION (**raw cell**)
name: q1
points: 5

 ```

**Question 1:** Write a function square that returns the square of its argument.(**markdown cell)**
- #BEGIN SOLUTION(**raw cell)**
- **Here we need to write the solution,which is typically a code(CODE cell)**
- #END SOLUTION**(raw cell)**
- **#**BEGIN TESTS**(raw cell)**
- **here we need to mention our test cases.Each test case will be on a seperate code cell**
- #END TESTS**(raw cell)**
- #END QUESTION(**raw cell**)

- The BEGIN QUESTION block contains the mandatory parameter name and two optional parameters, manual andpoints.
- Immediately after the question cell should be a solution cell.

Refer the following example

```
# BEGIN SOLUTION
def sieve(n):
    """
    Generate a set of prime numbers less than or equal to a positive integer.
    """
    # BEGIN SOLUTION
    is_prime = [True for _ in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if is_prime[p]:
            for i in range(p ** 2, n + 1, p):
                is_prime[i] = False
        p += 1

    is_prime[0]= False
    is_prime[1]= False

    return set(i for i in range(n + 1) if is_prime[i])
    # END SOLUTION
# END SOLUTION

```



- Using specially-formatted Python comments, otter-grader can parse the solution cell and replace lines with ellipsis or other user-defined prompts.

### Test Cases Format

After the solution cell comes zero or more test cells, denoted by a beginning # BEGIN TESTS annotation, finishing with an ending # END TESTS annotation, and between these two lines functions that test the code. These functions’ names begin with test\_ and are marked as # HIDDEN if appropriate. The # IGNORE lines provide funcationality for the grader to call the test funcions appropriately.
```
# BEGIN TESTS

# BEGIN TESTS
def test_low_primes(sieve):
    assert sieve(1) == set()
    assert sieve(2) == {2}
    assert sieve(3) == {2, 3}

test_low_primes(sieve)  # IGNORE
# HIDDEN
def test_higher_primes(sieve):
    assert sieve(20) == {2, 3, 5, 7, 11, 13, 17, 19}
    assert sieve(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

test_higher_primes(sieve)  # IGNORE
# END TESTS
# END QUESTION
```


- To Understand more about Test Cases,Please refer this section from the documentation [TEST CASES](https://otter-grader.readthedocs.io/en/latest/test_files/python_format.html#sample-test) <Specific Ottergrader Test Cases>
- These cells will have their outputs parsed by otter-grader to generate the otter-formatted test files needed for autograding. The otter-grader docs [tutorial](https://otter-grader.readthedocs.io/en/latest/tutorial.html) <Specific>describes how to call otter-grader to parse the notebook.
- Once you have run otter-grader, you’re ready to distribute your assignment to students! The studentsubdirectoy of your output directory will contain the version of the notebook for students (with solutions removed and only public tests) and the autograder subdirectory the version *with* solutions and hidden tests.
- For more information, check out the [otter-grader documentation](https://otter-grader.readthedocs.io/en/v4.4.1/).

The following Screenshot will give a clear understading of above syntax for creating questions,solutions and test cases

![](./imgs/otterq&a.007.png)

### Assignment examples

- To see the full-fledged, Please refer to this Jupyternotebooks
- [Sample Notebook1](https://github.com/SaiUCM/Jupyterhub_Docs_Instructor/blob/main/Notebook1.ipynb),
- [Sample Notebook2](https://github.com/SaiUCM/Jupyterhub_Docs_Instructor/blob/main/Notebook2.ipynb)
- To understand more about creating questions, Please refer to this section in the document [Autograded Questions](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html#autograded-questions).

## otter-assign

Once after creating the Source Notebook using otter-grader we need to generate a Student facing notebook where students can complete the assignment. To generate Student facing notebook use the command “**otter assign**“ 

```command : otter assign demo.ipynb dist ```

Now let’s break down the command. It has 3 sections as highlighted above in the command

**otter assign** -→ command to create the student facing notebook and a **Autograder zipfile** which can be used to grade the student submissions automatically using Gradescope.

**demo.ipynb** -→ It is the source notebook that instructors created using otter-grader library ,Just like the one mentioned above in Creating Questions section

**dist** → It is name of the folder where it can have both student facing Jupyter notebook which will be shared to students.The name of the folder can be anything.

For more information about otter-assign,Please refer this [section](https://otter-grader.readthedocs.io/en/latest/tutorial.html#otter-assign) in otter-grader documentation

## Delivering assignments - Github, nbgitpull

### What is Git and GitHub?

Git is a version control software that tracks changes in files and allows multiple users to work on the same files in parallel smoothly. Git is often used in conjunction with [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git), a website that hosts code and files. A repository (aka repo) on [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git) holds the files for a specific project.  [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git)'s web interface also displays the information that Git tracks, such as which users are working on a file and what changes have been made to the file.

### Why should I store materials on GitHub?

Storing materials on the  [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git) allows you to use interact links for assignment distribution. It also allows you to use the version control features that Git provides. In general, like best practice, create two repositories 1.Private Repository and 2. Public Repository

### Private Repository:

In this repository, instructors need to upload the source notebooks so that they remain private and inaccessible to others.

### Public Repository:

In this repository, instructors should upload the student-facing notebooks generated using the **otter-assign** command. These notebooks can then be shared with students.

> **Note**
> Any confidential Jupyter notebooks should be uploaded to the Private Repository. Jupyter notebooks meant to be shared with students should be uploaded to the Public Repository.

### nbgitpull

You’ll often want to distribute content (such as notebooks, scripts, sample data, etc.) to your users so they can do exercises, follow along with a lecture, or use as a starting point for their own work. This content is often constantly updated as time goes on, and needs to not overwrite your student’s work if you make an adjustment to content that has already been touched by the student. That’s where nbgitpuller comes into the picture.

nbgitpuller is already installed in the default environment for UCMerced JupyterHubs. To set up a nbgitpuller link, users must have a GitHub account. The following are the steps which will guide you to create an nbgitpuller link

[Generate nbgitpuller Link](https://ucm-it.github.io/hpc_docs/#/jupyterhub?id=generate-nbgitpuller-link)

Users can generate an nbgitpull link using the tool [nbgitpuller](https://nbgitpuller.readthedocs.io/en/latest/link.html) link, which will look like in the following screenshot:


![](./imgs/nbgitpuller.008.png)

## Creating a course in Catcourses and Gradescope

### Step 1: Institutional License, GradeScope and Catcourses

GradeScope is a service that allows instructors to tie assignments back to Catcourses. Once an assignment is created in Catcourses and in GradeScope, a student uploads their completed notebook to GradeScope, GradeScope grades the notebook and pushes the scores back to the Catcourse.

### Step 2: Documentation: Catcourses and GradeScope Assigment Configuration

[**CatCourses**](https://it.ucmerced.edu/catcourses) is UC Merced's Canvas Learning Management System (LMS). It provides a central repository for all academic course sites in which instructors can interact with and provide educational materials to their students.

To create a new course on canvas, Please follow this [documentation](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-create-a-new-course-from-the-Dashboard-as-an-instructor/ta-p/794) from canvas.

### How to create an Gradescope assignment on Catcourses.

This documentation from [GradeScope](https://help.gradescope.com/article/y10z941fqs-instructor-canvas#assignment_setup) details how to configure a GradeScope course and assignments with Canvas.

Navigate to assignments section on the canvas and click on the new gradescope assignment.

UCMerced is using Latest version of Gradecope. So Gradescope is listed in the dotted drop-down menu on the Assignments page.
![](./imgs/gradescope_dropdown.009.png)

Once you click on Gradescope option from the dropdown, You will be give two options to choose as shown below.

### Assignment Type

To begin crafting a new assignment, simply click on the 'A new Gradescope Assignment' option. This will guide you to the next step, where you'll select your assignment type. Since our aim is to grade Jupyter notebooks, opt for the 'Programming Assignment' choice.

![](./imgs/assignment_settings.010.png)

then follow the **LTI 1.3** tab instructions on [GradeScope](https://help.gradescope.com/article/y10z941fqs-instructor-canvas#assignment_setup) documentation.

### Configure Autograder.

Once after creating an assignment, it will be redirected to a page where faculty/instructors needs to upload the zip file which was created using otter-grader package using **otter assign command.**Please refer the otter-assign section.

![](./imgs/autograder.011.png)

Once after uploading a zip file which was created by instructor,Gradescope will process that which will roughly take 5-10 mins,Once they have generated the ZIP file they just upload it and the GRADESCOPE will build the image and then it will run the test cases for the notebook.

![](./imgs/build.012.png)

Congratualtions,You have successfully created an autograder assignment using gradescope and canvas.

### Publish an Assignment

Now the assignment will be available on canvas and will be available to students once you publish the assignment.

Open Assignments,In Course Navigation, click the **Assignments** link.

![](./imgs/status.013.png)

> **Note**
> Please take a look on how to[ publish assignments](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-publish-or-unpublish-an-assignment-as-an-instructor/ta-p/585) from canvas documentation. Now once the assignment is published, it will be available to students and the students can complete the assignment.**

> **Note:
> Documentation: GradeScope Programming Assignments.

> This documentation from [GradeScope](https://help.gradescope.com/article/ujutnle52h-instructor-assignment-programming) illustrates how to tie the autograder.zip file to a GradeScope assignment to enable automatic grading. There is also a section on combining manual and autograded questions.

Note here, that we have all the autograder.zip files needed for the programming assignments, the configuration of these assignments is explained in the student facing workflow section.

### Grading and publishing grades

Once students submitted their assignments, instructors can publish their grades from Gradescope which will then be directly reflecte in Catcourses. More information here:

<https://help.gradescope.com/article/y10z941fqs-instructor-canvas#posting_grades>

## Student facing workflow

### How does a course look like?

A course is automatically added into the students account based on their selection while registering for courses.Students can login into canvas using UCMerced SSO.Once login the can view all their register courses in the canvas dashaboard.

![](./imgs/canvas_dashboard.014.png)

Please follow this link for more information on [courses](https://community.canvaslms.com/t5/Student-Guide/How-do-I-use-the-Course-Home-Page-as-a-student/ta-p/504) in canvas.

### How does an assignment look like?

Students are able to access their specific course and then proceed to the assignments section. Typically, a Gradescope assignment appears similar to a standard assignment. However, students must adhere to the following steps to submit their JupyterHub assignment on Canvas.

![](./imgs/creating_assignment.015.png)


In the screenshot, students can spot the upload submission button nestled in the lower right corner. Clicking on it triggers a pop-up window where students are prompted to upload their assignment as a zip file.

![](./imgs/submit_assign.016.png)

After uploading the zip file, Gradescope will validate and grade the student's assignment according to the instructor's solutions.It looks something like this.

![](./imgs/submit_assign1.017.png)


Upon successful submission, an email notification will be sent.

![](./imgs/assign_success.018.png)



