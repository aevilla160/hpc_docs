## Our UC Merced pilot JupyterHub infrastructure is online now ! <!-- {docsify-ignore} -->
> Please go to the website at  https://ucmerced.2i2c.cloud. 

All active UC Merced students, staff and faculty should have access to the pilot hub.

If you have any questions, please free feel to contact [Sai Chandhar Annapragada](sannapragada@ucmerced.edu).

### What is JupyterHub

JupyterHub is an open source tool that lets you host a distributed Jupyter Notebook environment. With JupyterHub, users can log in to the server, and write Python code in a web browser, without having to install software on their local machine.


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

If you were not able to attend the workshop of JupyterHub, here is the recording [link](https://video.ucmerced.edu/media/JupyterHub+Workshop/1_ehe8hmux).




## Generate `nbgitpuller` link <!-- {docsify-ignore} -->
> Ensure that the `nbgitpuller` is installed into your environment

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

!> Unfortunately, `RStudio` does not support opening a specific file, and will always show the home directory. Users will have to manually navigate to the appropriate file.

### Local Jupyter versus JupyterHub

| JupyterHub | Local Jupyter Install |
|--------------| --------------------|
| Needs an internet connection | Does not need internet connection |
| Limited resources (disk and RAM) | Resources are only limited by individual computer |
| System-wide installation done by admins| You can install anything you want |
| You can only access files in your account | You can maybe access all files (if you are an admin) |
| If things break, CIRT can assist in helping fix the item | CIRT can not assist in fixing issues on local install |