## Table of Contents
- [1. What are Jupyter Notebooks?](#1-what-are-jupyter-notebooks)
  - [1.1 Features](#11-features)
  - [1.2 Components](#12-components)
- [2. What is JupyterHub?](#2-what-is-jupyterhub)
- [3. Who can use this service?](#3-who-can-use-this-service)
- [4. How to access JupyterHub?](#4-how-to-access-jupyterhub)
  - [4.1 Staging JupyterHub](#41-staging-jupyterhub)
  - [4.2 Production JupyterHub](#42-production-jupyterhub)
- [5. Create New Notebook](#5-create-new-notebook)
- [6. Rename the Notebook](#6-rename-the-notebook)
- [7. How to run a notebook?](#7-how-to-run-a-notebook)
- [8. How to add code block?](#8-how-to-add-code-block)
- [9. How to add Markdown text cells in the notebook?](#9-how-to-add-markdown-text-cells-in-the-notebook)
- [10. How to download the notebook?](#10-how-to-download-the-notebook)
- [11. How to create a new folder?](#11-how-to-create-a-new-folder)
- [12. Shared/Shared Read-Write Folder](#12-sharedshared-read-write-folder)
  - [12.1 Shared](#121-shared)
  - [12.2 Shared Read-Write](#122-shared-read-write)
- [13. Installing packages on the Hub](#13-installing-packages-on-the-hub)
  - [13.1 Is it possible to install custom packages?](#131-is-it-possible-to-install-custom-packages)
  - [13.2 What packages & libraries are available?](#132-what-packages--libraries-are-available)
- [14. nbgitpuller](#14-nbgitpuller)
  - [14.1 Put your files in a public Github Repository](#141-put-your-files-in-a-public-github-repository)
  - [14.2 Generate nbgitpuller Link](#142-generate-nbgitpuller-link)
  - [14.3 Distribute your nbgitpuller link](#143-distribute-your-nbgitpuller-link)

<!-- ## Our UC Merced pilot JupyterHub infrastructure is online now !--> <!-- {docsify-ignore} -->
<!-- > Please go to the website at  https://ucmerced.2i2c.cloud. 

All active UC Merced students, staff and faculty should have access to the Jupyterhub.

If you have any questions, please free feel to contact Sai Chandhar Annapragada (sannapragada@ucmerced.edu). -->

<!-- ### What is JupyterHub --> <!-- {docsify-ignore} -->

<!-- JupyterHub is an open source tool that lets you host a distributed Jupyter Notebook environment. With JupyterHub, users can log in to the server, and write Python code in a web browser, without having to install software on their local machine.


Working on JupyterHub provides a number of benefits, especially in an introductory course:

Students never have to do any setup or installation. JupyterHub removes the burden of setting up and maintaining a development environment.

All students and instructors use the same computing environment.

Work stored in the cloud and can be accessed from any computer.

All students have access to the same compute power, regardless of the machine they are using. For example, students without personal computers can use publicly shared computers(i.e. library computers) without being at a disadvantage in the course.

We invite the UC Merced community to use the Hub for teaching (both now and future course planning) and exploring for research!

!> This pilot hub will be online for 11 months and feedback and usage information will be used to plan for our permanent JupyterHub.

> Instructions for Accessing the Pilot JupyterHub:
1. You can login through [UC Merced SSO](https://www.cilogon.org/home)
2. You can use the default jupyterhub image or you can change the image using the [configurator](https://github.com/2i2c-org/2i2c-hubs-image). You can also create your custom user image. There is a guide about this [here](https://docs.2i2c.org/en/latest/admin/howto/environment/index.html).
3. General information about the user environment [here](https://docs.2i2c.org/en/latest/admin/howto/environment/index.html).

If you have admin access, please note that the shared folders have the same shared path. One is configured for read-write, and the other is configured for read-only. For admins, they can see both folders but can only write to the one that is write-enabled. Standard users only see a single shared directory as read-only. From a content management standpoint, admins have full access to all content and act as a single user when interacting with content. If you want to limit the access of a folder to a specific group, you can use nbgitpuller to generate a special URL for a group of users to gain access to the folder. The usage of nbgitpuller is discussed below.

If you have any additional questions accessing hub, please open a general OIT research computing ticket [here](https://ucmerced.service-now.com/servicehub?id=public_kb_article&sys_id=3c3ee9ff1b67a0543a003112cd4bcb13&form_id=06da3f8edbfc08103c4d56f3ce9619f4).

If you were not able to attend the workshop of JupyterHub, here is the recording [link](https://video.ucmerced.edu/media/JupyterHub+Workshop/1_ehe8hmux). -->




<!-- ## Generate `nbgitpuller` link --> <!-- {docsify-ignore} -->
<!-- > Ensure that the `nbgitpuller` is installed into your environment

The default environment for 2i2c JupyterHubs has `nbgitpuller` pre-installed. However, if you define a [custom environment](https://docs.2i2c.org/admin/howto/environment/#environment-image) for your hub’s users, you’ll need to ensure that nbgitpuller is installed in order for users to use it!

To install the `nbgitpull`, please follow the instruction [here](https://github.com/jupyterhub/nbgitpuller)

> If you are using the Chrome or Firefox web browser you can directly download the browser extension to generate nbgitpuller [here](https://github.com/yuvipanda/nbgitpuller-link-generator-webextension)

Once the browser extenstion is installed, your browser should have a nbgitpuller button on top, below is an example of the chrome browser with nbgitpuller extension installed.

![nbgitpuller github](imgs/nbgitpuller_browser.png "github with nbgitpuller")

> Put your content in a public GitHub repository

Create a repository on [GitHub](https://github.com/) and begin uploading your content. This repository serves as the source for the content distributed to your users. Feel free to update it as frequently as needed. While instructors should be familiar with how GitHub works, your users will never have to interact with Git directly.

> Generate an nbgitpuller link

Generate an nbgitpuller link using the browser extension when you are in the GitHub repository that you intend to share. Please refer to the figure below for guidance on how to generate the link:

![nbgitpuller web gen](imgs/nbgitpuller_gen.png "webgen with nbgitpuller")

* The URL to the hub. Upon clicking the link, users will be redirected to the hub, and content will be pulled into their home directory there. 
* The branch in the git repository where the content lives. The default specified there is `master`, although newer GitHub repositories use `main` as the default. You can find yours on the Github page of your content repository
* The default interface to open when users click this link. The default is the classic notebook, but many other apps are available
* A file to open when the link is clicked. When left empty, a directory listing with the content of the repository will be shown

!> Unfortunately, `RStudio` does not support opening a specific file, and will always show the home directory. Users will have to manually navigate to the appropriate file. -->

<!-- ### Local Jupyter versus JupyterHub --> <!-- {docsify-ignore} -->
<!--
| JupyterHub | Local Jupyter Install |
|--------------| --------------------|
| Needs an internet connection | Does not need internet connection |
| Limited resources (disk and RAM) | Resources are only limited by individual computer |
| System-wide installation done by admins| You can install anything you want |
| You can only access files in your account | You can maybe access all files (if you are an admin) |
| If things break, CIRT can assist in helping fix the item | CIRT can not assist in fixing issues on local install | -->

## 1. What are Jupyter Notebooks?

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain **live code**, equations, visualizations, and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

### 1.1 Features

- **Interactive Environment:** Jupyter Notebooks provide an interactive computing environment where users can write and execute code in a step-by-step manner.
- **Support for Multiple Languages:** While originally designed for Python, Jupyter Notebooks support various programming languages like Julia, Python, and R.
- **Rich Output:** Notebooks allow the incorporation of rich media outputs such as plots, images, videos, and interactive widgets alongside code and text cells.
- **Markdown Support:** In addition to code cells, users can include Markdown cells to write formatted text, equations (using LaTeX syntax), and even HTML for documentation or explanations.
- **Data Visualization:** Using libraries like Matplotlib, Seaborn, users can create interactive and static visualizations directly within the notebook environment.
- **Integration with Libraries and Tools:** Jupyter Notebooks seamlessly integrate with various data science libraries and tools such as NumPy, Pandas, SciPy, TensorFlow, and scikit-learn.

### 1.2 Components

- **Cells:** Notebooks are composed of individual cells that can contain either code, Markdown-formatted text, or raw content. Users can execute code cells and render Markdown cells to produce outputs.
  ![jupyter_Cells](./jupyter_cells.png)

- **Kernel:** Each notebook is associated with a computational kernel, which is responsible for executing code within the notebook. Different kernels support different programming languages.
  ![kernel](./kernel.png)

- **Toolbar:** The toolbar provides quick access to common actions such as running cells, saving the notebook, adding new cells, and changing cell types.
  ![toolbar](./toolbar.png)
- **Menu Bar:** The menu bar contains various options for manipulating the notebook, managing kernels, and configuring the notebook environment.
  ![menubar](./menu.png)
- **Output Area:** Code cells display their output, including text output, error messages, and visualizations, in the output area directly below the cell.
  ![output_area](./output_area.png)
- **File Format:** Notebooks are saved in a JSON file format with the `.ipynb`
### 1.3 Using Jupyter Notebooks for Data Analysis

**Jupyter Notebooks** are incredibly versatile for **data analysis** projects. They allow data scientists to combine **executable code**, rich text, **visualizations**, and equations in a single document.

- **Interactive Data Exploration:** Notebooks facilitate interactive exploration of datasets, enabling quick iterations over a data preprocessing or analysis pipeline.
- **Visualization:** With support for libraries like **Matplotlib** and **Seaborn**, users can create and embed graphs directly within notebooks.
- **Collaboration and Sharing:** Notebooks can be easily shared between users, promoting collaboration on data analysis projects.

<!-- Add image syntax here for a data analysis visualization example -->

## 2. What is JupyterHub?

**JupyterHub** is a multi-user version of the notebook designed for classrooms, labs, and data science teams. It allows multiple users to access Jupyter Notebooks on a centralized server, thereby facilitating collaborative projects and learning environments.

- **Accessibility:** JupyterHub can be accessed from any web browser, making computational resources available to users without the need for complex setup procedures.
- **Resource Management:** It efficiently manages computational resources, allowing system administrators to allocate resources per user or project.

## 3. Who Can Use This Service?

The **JupyterHub** service is open to a wide range of users, from **students** to **researchers** and **data scientists**. It is particularly useful for:

- **Educational Institutions:** Teachers can create a shared JupyterHub environment for their classes, enabling an interactive learning experience.
- **Research Teams:** Collaborative projects that require data analysis, computation, and visualization can benefit significantly from JupyterHub’s shared resources.

## 4. How to Access JupyterHub?

Accessing **JupyterHub** requires a network connection and a web browser. The exact steps may vary depending on the specific JupyterHub setup, but generally involve the following:

1. **Navigate to the JupyterHub URL:** This will be provided by your institution or the administrator of the JupyterHub instance.

    <!-- Add image syntax here for the JupyterHub login page -->

2. **Log in:** Use your designated credentials. This might be your institutional login or a specific account set up by your JupyterHub administrator.

3. **Start a Notebook Server:** Once logged in, you may need to select computational resources or simply click a button to start your Jupyter Notebook server.

4. **Open or Create a Notebook:** From the JupyterHub dashboard, you can access existing notebooks or create new ones.

    <!-- Add image syntax here showing the JupyterHub dashboard -->

**Note:** The exact interface and options available may vary based on the JupyterHub configuration and the resources provided by your institution or organization.
