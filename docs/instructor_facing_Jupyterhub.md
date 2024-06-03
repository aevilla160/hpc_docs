### 1. Getting Started
    HPC Docs
      **To Access Jupyterhub**, Please navigate to the section [How to access JupyterHub?](https://ucm-it.github.io/hpc_docs/#/jupyterhub?id=how-to-access-jupyterhub)
   - **Where to get help** (screenshot of the 2i2c launch webpage)
   - Support for JyupterHub is provided during standard operating hours: 8:00 a.m. – 5:00 p.m., Monday through Friday. Please submit a general ticket through the [UC Merced ServiceHub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

     If you're having issues accessing JupterHub, please Report a Problem at [servicehub.ucmerced.edu](https://ucmerced.service-now.com/servicehub) or call 228-HELP (4357).The same information can be found on the landing page of the JupyterHub.Please find the screenshot below for reference.

     ![](landingpage.001.png)
   - **Datascience office hours**
   - Jupyterhub/Datascience office hours every **Friday from 11:30 AM to 1:00 PM in ACS Room 365**

     Zoom Details:

     - <https://ucmerced.zoom.us/j/87915353522?pwd=bW5zV3NCNWk5d2dvVkZwaXlObHJ3dz09>
     - Meeting ID: 879 1535 3522
     - Passcode: 035925
   - Please feel free to drop by if you need help with anything from setting up your environment, or if you're just curious to learn more about more on JupyterHub. If these times don't work for you but you still require support, I encourage you to open a ServiceNow ticket [ServiceNow Request](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) .

ServiceHub requests for scheduling consultations

Please raise a general [UC Merced ServiceHub](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4)(Service Now) request for scheduling consultations 

1. Instructor-facing workflow
- **a**. **To Access Jupyterhub**, Please navigate to the section [How to access JupyterHub?](https://ucm-it.github.io/hpc_docs/#/jupyterhub?id=how-to-access-jupyterhub). (extra perios) It also contains a section about how to start the Server(Python or R) and a few other information on how to download, save, rename, and export notebooks.
- **b. What is covered in Notebook Zero?**

Notebook zero typically includes a variety of subjects and is often customized for the specific course it supports. However, there are a few consistent elements found in every notebook zero.

- code and Markdown cells
- variables and Python data types (int, float, str, bool)
- arithmetic and operators
- logical operators and keywords (and, or, not)
- if/elif/else statements
- functions and builtins
- errors

Depending on the course or module, more topics may be covered (e.g. importing libraries, iteration). While these notebooks tend to be very homogeneous.

Please find the [Zero Notebook](https://github.com/SaiUCM/Jupyterhub_Docs_Instructor/blob/main/Notebook%20Zero.ipynb) which covers the above mentioned topics and ~~also~~ it also explains how to plot the graphs using Matplotlib and Plotly libraries.

**c**. **Package Installation in Python and R**

**What are the packages pre-installed for every hub?**

The Procedure for package installation varies across different programming languages. Basic python packages such as numPy, pandas, scikit-learn, matplotlib, etc., are installed across the main Datahub. R hubs supports packages such as shiny, dplyr, tidyR, RSQLlite, etc. 

- You can use the below command for Python,

```
!pip list

```

- You can use the below command for R,

```
installed.packages()

```

Here is the list of  [Python Packages](https://github.com/berkeley-dsep-infra/datahub/blob/staging/deployments/datahub/images/default/requirements.txt) installed in [ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login) . Here is the list of [R packages](https://ucmerced.app.box.com/file/1481528927192?s=65r1rda9atblpdsxdvtyaq6exlnns9z3) of R packages installed in [ucmerced.2i2c.cloud](https://ucmerced.2i2c.cloud/hub/login)

**What should I do if I want to install more packages?**

- Use your Jupyterhub instance to install the required version of the package. Self installation of packages in your instance of hub is a temporary measure to identify dependencies. If you require a permanent solution then you need submit a [Service Now request](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) to us to install the required package(s) in your hub.
- If you want to install packages for Python in your instance, then use the following syntax,

```
pip install <package-name>

Eg: pip install numpy

```


- If you want to install packages for R in your instance, then use the following syntax,

```
install.packages("<package-name>")

Eg: install.packages("ggplot2")

```


**Pre-installed Packages**

Many Python packages have been pre-installed on JupyterHub and are available by default. To use a pre-installed package such as numpy, you can simply type the line below into a code cell.

``` 
import numpy

```

**Installing New Packages**

You can also install other packages that are not on this list. There are two methods for installation. If you will be using a package regularly in your course, we recommend using the long-term installation method.

**Temporary Installation**

Notebooks provide support for bash commands in code cells. The line below, when run in a notebook code cell, will temporarily install numpy into a user’s personal account. numpy will then be available for use while the server is running. This cell must be run every time the user’s server is restarted. Note, this is not a system-wide installation. Running the below cells will only install numpy and ggplot2 temporarily into a user’s personal account. (better highlight this)

- For python use the below code snippet
```
!pip install numpy
```

```
import numpy
```
- For R  use the below code snippet

```
install.packages("ggplot2")
```
```
library("ggplot2")
```
**Long-term installation**

*This is the recommended method for packages that will be used frequently.* If you require a permanent solution then you need to [Service Now request](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4) us to install the required package(s) in your hub.

Our Jupyterhub has two instances 1. Staging Hub(for testing the new features/updates <https://staging.ucmerced.2i2c.cloud/hub/login>) 2. Production Hub(<https://ucmerced.2i2c.cloud/hub/login>)

As in best practice, the installation will be done on staging hub first, and once validated, will be installed in the production hub.


> Before sending a request to CIRT team for installing new packages on Jupyterhub Kindly mention its Version as well

**Troubleshooting issues in the Hub**


Facing issues with your hub and want to do some basic troubleshooting before escalating issues to us? If yes, read below!

One common error is a Jupyter notebook becoming unresponsive. You will know that a notebook is unresponsive. Another type of error is a user not being able to access some part of their JupyterHub account.

We have outlined two methods below that you should try for each error type. For errors related to the execution of code, such as the notebook not running properly, you should try restarting the kernel. For errors related to access, you should try restarting the server.

**Restarting the Kernel**

If your notebook becomes unresponsive, you can try to restart the kernel. (better highlight the restart kernel in the figure below)

![](Kernel_list.002.png)

**Restarting Servers**

***Restarting Your Own Server***

All users can restart their own servers. To do so, start by going to the **Hub** **Control Panel** from the dropdown menu from File menu (highlight the hub control in the figure below)

![](status.003.png)

Once you click on Hub Control Panel.It will navigate to the page and Click the **Stop My Server** button.

![](start_server.004.png)

Once the server has stopped and the Stop My Server button is no longer visible, click the **My Serverbutton (should be Start My Server)** to restart the server.

![](startserver.005.png)

**Troubleshoot issues with Hub/Server/Code running slow**

**What should I do if my hub is running slow?**

Try these recommended options,

- Restart your kernel.
- Check whether there are a lot of open tabs. If yes, close the tabs that are not required.

**What should I do if my code is running slow?**

In general, this issue could be attributed to the varied programming practices adopted that might have slowed the operation of the hub. Check whether your code does any of the following,

- You are running an infinite loop
- Your computation/calculation is big
- You are joining tables that are too large
- You have too many notebooks open at the same time
- You are trying to show a table which is too large and as a result are crashing the browser

If they are relevant, try fixing these issues by improving the programming practices or by reducing the size of the dataset. 

If none of these above work, please <help section> (Need to insert a figure ? What is the <help section>)

**Creating assignments - Ottergrader information**

[Otter Grader](https://otter-grader.readthedocs.io/en/latest/) is a light-weight, modular open-source autograder developed by the Data Science Education Program at UC Berkeley. It is designed to grade Python and R assignments for classes at any scale by abstracting away the autograding internals in a way that is compatible with any instructor’s assignment distribution and collection pipeline.

The following steps explain how to create assignments/homework using [otter-grader](https://otter-grader.readthedocs.io/en/latest/) and Jupyterhub.

[Otter-Grader](https://otter-grader.readthedocs.io/en/latest/) parses a parent notebook containing questions, solutions, and tests to create two distribution directories: one with solutions and all tests for automatic grading and a second with no solutions and only public tests for students.

Before Creating assignments using otter-grader let’s understand the important concepts that will be helpful.

There are three different types of cell formats in Jupyter Notebooks which are

- a. Raw -→ This option will be used as plain text
- b. Markdown -→ It will be used to create the Markdown format text ex.Headers,Links,Images,text in a md format
- c. Code -→ When u change the cell type into code block, where we can write the Python or R code

You can find this option in the toolbar menu.
![](cells.006.png)
- Each of these(Code,Markdown,Raw) will have different purpose while creating assignments using otter-grader.Like 

- **Assignment Config**

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

For more information about **# ASSIGNMENT CONFIG** please refer the [documentation](https://otter-grader.readthedocs.io/en/v4.4.1/otter_assign/v1/notebook_format.html). <Specific>

**Creating Questions**

- The questions always starts with #BEGIN QUESTION and ends with #END QUESTION in between those we can create solution and test cases for that question.The following syntax will explain the question,solution and test cases format

**Question Format**

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



- Using specially-formatted Python comments, otter-grader can parse the solution cell and replace lines with ellipsis or other user-defined prompts (this behavior is described in more detail in the otter-grader docs, linked below).

**Test Cases Format**

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

![](otterq&a.007.png)

**Assignment examples**

- To see the full-fledged, Please refer to this Jupyternotebooks
- 1. [Sample Notebook1](https://github.com/SaiUCM/Jupyterhub_Docs_Instructor/blob/main/Notebook1.ipynb),
- 2.[Sample Notebook2](https://github.com/SaiUCM/Jupyterhub_Docs_Instructor/blob/main/Notebook2.ipynb)
- To understand more about creating questions, Please refer to this section in the document [Autograded Questions](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html#autograded-questions).

**otter-assign**

Once after creating the Source Notebook using otter-grader we need to generate a Student facing notebook where students can complete the assignment. To generate Student facing notebook use the command “**otter assign**“ 

```command : otter assign demo.ipynb dist ```

Now let’s break down the command. It has 3 sections as highlighted above in the command

**otter assign** -→ command to create the student facing notebook and a **Autograder zipfile** which can be used to grade the student submissions automatically using Gradescope.

**demo.ipynb** -→ It is the source notebook that instructors created using otter-grader library ,Just like the one mentioned above in Creating Questions section

**dist** → It is name of the folder where it can have both student facing Jupyter notebook which will be shared to students.The name of the folder can be anything.

For more information about otter-assign,Please refer this [section](https://otter-grader.readthedocs.io/en/latest/tutorial.html#otter-assign) in otter-grader documentation

**Delivering assignments - Github, nbgitpull**

**Github**

**What are Git and GitHub?**

Git is a version control software that tracks changes in files and allows multiple users to work on the same files in parallel smoothly. Git is often used in conjunction with [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git), a website that hosts code and files. A repository (aka repo) on [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git) holds the files for a specific project.  [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git)'s web interface also displays the information that Git tracks, such as which users are working on a file and what changes have been made to the file.

**Why should I store materials on GitHub?**

Storing materials on the  [GitHub](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git) allows you to use interact links for assignment distribution. It also allows you to use the version control features that Git provides. In general, like best practice, create two repositories 1.Private Repository and 2. Public Repository

**Private Repository:**

In this repository, instructors need to upload the source notebooks so that they remain private and inaccessible to others.

**Public Repository:**

In this repository, instructors should upload the student-facing notebooks generated using the **otter-assign** command. These notebooks can then be shared with students.

> **Note**
> Any confidential Jupyter notebooks should be uploaded to the Private Repository. Jupyter notebooks meant to be shared with students should be uploaded to the Public Repository.

**nbgitpull**

You’ll often want to distribute content (such as notebooks, scripts, sample data, etc.) to your users so they can do exercises, follow along with a lecture, or use as a starting point for their own work. This content is often constantly updated as time goes on, and needs to not overwrite your student’s work if you make an adjustment to content that has already been touched by the student. That’s where nbgitpuller comes into the picture.

nbgitpuller is already installed in the default environment for UCMerced JupyterHubs. To set up a nbgitpuller link, users must have a GitHub account. The following are the steps which will guide you to create an nbgitpuller link

[Generate nbgitpuller Link](https://ucm-it.github.io/hpc_docs/#/jupyterhub?id=generate-nbgitpuller-link)

Users can generate an nbgitpull link using the tool [nbgitpuller](https://nbgitpuller.readthedocs.io/en/latest/link.html) link, which will look like in the following screenshot:


![](nbgitpuller.008.png)

**Creating a course in Canvas and Gradescope**

**Step 1: Institutional License, GradeScope and Canvas**

GradeScope is a **paid** service that allows instructors to tie assignments back to Canvas. Once an assignment is created in Canvas and in GradeScope, a student uploads their completed notebook to GradeScope, GradeScope grades the notebook and pushes the scores back to the LMS (need explaination, you mentioned Canvas before but now LMS, which is explained in the following context, better explain LMS when it first being mentioned).

**Step 2: Documentation: Canvas and GradeScope Assigment Configuration**

[**CatCourses**](https://it.ucmerced.edu/catcourses) is UC Merced's Canvas Learning Management System (LMS). It provides a central repository for all academic course sites in which instructors can interact with and provide educational materials to their students.

To create a new course on canvas, Please follow this [documentation](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-create-a-new-course-from-the-Dashboard-as-an-instructor/ta-p/794) from canvas.

**How to create an Gradescope assignment on canvas.**

This documentation from [GradeScope](https://help.gradescope.com/article/y10z941fqs-instructor-canvas#assignment_setup) details how to configure a GradeScope course and assignments with Canvas.

1. Navigate to assignments section on the canvas and click on the new gradescope assignment

UCMerced is using Latest version of Gradecope. So Gradescope is listed in the dotted drop-down menu on the Assignments pag**e.**

![](gradescope_dropdown.009.png)

Once you click on Gradescope option from the dropdown, You will be give two options to choose as shown below.

**Assignment Type**

To begin crafting a new assignment, simply click on the 'A new Gradescope Assignment' option. This will guide you to the next step, where you'll select your assignment type. Since our aim is to grade Jupyter notebooks, opt for the 'Programming Assignment' choice.

![](assignment_settings.010.png)

then follow the **LTI 1.3** tab instructions on [GradeScope](https://help.gradescope.com/article/y10z941fqs-instructor-canvas#assignment_setup) documentation.

**Configure Autograder.**

Once after creating an assignment, it will be redirected to a page where faculty/instructors needs to upload the zip file which was created using otter-grader package using **otter assign command.**Please refer the otter-assign section (add a link to the previous session).

![](autograder.011.png)

Once after uploading a zip file which was created by instructor,Gradescope will process that which will roughly take 5-10 mins.So this is the process basically for instructors in terms of like (broken sentence),once they have generated the ZIP file they just upload it and the GRADESCOPE will build the image and then it will run the test cases for the notebook.

![](build.012.png)

Congratualtions,You have successfully created an autograder assignment using gradescope and canvas.

**Publish an Assignment**

Now the assignment will be available on canvas and will be available to students once you publish the assignment.

Open Assignments,In Course Navigation, click the **Assignments** link.Please find the screenshot for to (broken sentence) understand in a easy way.

![](status.013.png)

**Please take a look on how to[ publish assignments](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-publish-or-unpublish-an-assignment-as-an-instructor/ta-p/585) from canvas documentation. Now once the assignment is published, it will be available to students and the students can complete the assignment.**

**Note:Documentation: GradeScope Programming Assignments.**

This documentation from [GradeScope](https://help.gradescope.com/article/ujutnle52h-instructor-assignment-programming) illustrates how to tie the autograder.zip file to a GradeScope assignment to enable automatic grading. There is also a section on combining manual and autograded questions.

Note here, that we have all the autograder.zip files needed for the programming assignments, the configuration of these assignments is explained in the student facing workflow section.

**Grading and publishing grades**

Once students submitted their assignments, instructors can publish their grades from Gradescope which will then be directly reflecte in Catcourses (canvas). More information here:

<https://help.gradescope.com/article/y10z941fqs-instructor-canvas#posting_grades>

**Student facing workflow**

**How does a course look like?**

A course is automatically added into the students account based on their selection while registering for courses.Students can login into canvas using UCMerced SSO.Once login the can view all their register courses in the canvas dashaboard.

![](canvas_dashboard.014.png)

Please follow this link for more information on [courses](https://community.canvaslms.com/t5/Student-Guide/How-do-I-use-the-Course-Home-Page-as-a-student/ta-p/504) in canvas.

**How does an assignment look like?**

Students are able to access their specific course and then proceed to the assignments section. Typically, a Gradescope assignment appears similar to a standard assignment. However, students must adhere to the following steps to submit their JupyterHub assignment on Canvas.

![](creating_assignment.015.png)


In the screenshot, students can spot the upload submission button nestled in the lower right corner. Clicking on it triggers a pop-up window where students are prompted to upload their assignment as a zip file.

![](submit_assign.016.png)

After uploading the zip file, Gradescope will validate and grade the student's assignment according to the instructor's solutions.It looks something like this.

![](submit_assign1.017.png)


Upon successful submission, an email notification will be sent.

![](assign_success.018.png)

**How can I complete an assignment? (generating zip file, what does the zip file consist of)**

**How students can start-and finish their assignment?**

**How and where to submit it?**

**How to check their grades?**

1. What happens if I get errors in an assignment?
1. I am unable to submit my assignment - who should I reach out to? (same as where to get help section)


