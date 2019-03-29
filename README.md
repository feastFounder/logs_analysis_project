Logs Analysis Project
===

by Paul Tillman - Logs Analysis Project from the Udacity Full Stack Web Developer Nanodegree
---
Project
---

**Write SQL queries to answer the following questions about a PostgreSQL database which contains the logs of a fictional newspaper’s website.**
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

**Required Libraries and Dependencies**
The project code was created using the following software:
* Python 3.7.2
* psycopg2 2.7.7
* PostgreSQL 9.5.14

This project can be run in a Vagrant managed virtual machine (VM). For this project, Vagrant and VirtualBox software were installed on the system.

**Project contents**
* Logs_Analysis.py - This the Python program that connects to the PostgreSQL database (‘news’), executes the SQL queries and displays the desired results.
* newsdata.zip - Zip file with the data that populates the PostgreSQL database named 'news'.
* README.md - Contains info about the project (also, what you’re currently reading).
* Vagrantfile - This is the configuration file for the Vagrant virtual machine.

**How to Run the Project**
Download the project zip file to your computer and unzip the file to your desired project directory.
Open the text-based interface for your operating system (terminal window, command prompt, Git Bash, etc ….) and navigate to the project directory.

**Bringing the VM up**
Open your terminal and navigate to the folder containing the Vagrant file.  Then bring up the Virtual Machine (VM) with the following command:

`vagrant up`

The first time you run this command, it may take an extra minute because Vagrant needs to download the VM image.
You can then log into the VM with the following command:

`vagrant ssh`

Navigate to the folder containing the .
Once inside the VM, navigate to the /vagrant directory, which should contain the newsdata.zip and Logs_Analysis.py files with this command:

`cd /vagrant`

First, unzip the zip file with the command:

`unzip newsdata.zip`

Then run the following command to load the logs into the database:

`psql -d news -f newsdata.sql`

**Running the reporting tool**

The logs reporting tool is executed with the following command:

`python logs_analysis.py`

The answers to the three questions should now be displayed.

**Shutting the virtual machine down**
When you are finished with the project,  press Ctrl-D to log out of it. You can shut down the virtual machine by typing this command:

`vagrant halt`

You should see something akin to 

*“Attempting to gracefully shut down the virtual machine…”* 

in your terminal.  Once this process finishes, it will be safe to shut down the terminal without leaving the virtual machine to run in the background forever and ever.