# Windows Fundamentals 1
## The File System 
The file system used in modern versions of  Windows  is the **New Technology File System** or simply  [NTFS](https://docs.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview) .

Before NTFS, there was  **FAT16/FAT32** (File Allocation Table) and **HPFS** (High Performance File System). 

You still see FAT partitions in use today. For example, you typically see FAT partitions in USB devices, MicroSD cards, etc.  but traditionally not on personal Windows computers/laptops or Windows servers.

NTFS is known as a journaling file system. In case of a failure, the file system can automatically repair the folders/files on disk using information stored in a log file. This function is not possible with FAT.   

NTFS addresses many of the limitations of the previous file systems; such as: 

- Supports files larger than 4GB
- Set specific permissions on folders and files
- Folder and file compression
- Encryption ( [Encryption File System](https://docs.microsoft.com/en-us/windows/win32/fileio/file-encryption) or **EFS** )

If you're running Windows, what is the file system your Windows installation is using? You can check the Properties (right-click) of the drive your operating system is installed on, typically the C drive (C:\).

  ![](https://assets.tryhackme.com/additional/win-fun1/win-file-system.gif)

You can read Microsoft's official documentation on FAT, HPFS, and NTFS [here](https://docs.microsoft.com/en-us/troubleshoot/windows-client/backup-and-storage/fat-hpfs-and-ntfs-file-systems) . 

Let's speak briefly on some features that are specific to NTFS. 

On NTFS volumes, you can set permissions that grant or deny access to files and folders.

The permissions are:

- **Full control**
- **Modify**
- **Read & Execute**
- **List folder contents**
- **Read**
- **Write**

The below image lists the meaning of each permission on how it applies to a file and a folder. (credit  [Microsoft](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727008\(v=technet.10\)?redirectedfrom=MSDN) )

![](https://assets.tryhackme.com/additional/win-fun1/ntfs-permissions1.png)

How can you view the permissions for a file or folder?

- Right-click the file or folder you want to check for permissions.
- From the context menu, select `Properties` .
- Within Properties, click on the `Security` tab.
- In the `Group or user names` list, select the user, computer, or group whose permissions you want to view.

In the below image, you can see the permissions for the `Users` group for the Windows folder. 

![](https://assets.tryhackme.com/additional/win-fun1/windows-folder-permissions.png)

Refer to the Microsoft documentation to get a better understanding of the NTFS permissions for  Special Permissions .

Another feature of NTFS is **Alternate Data Streams** ( **ADS** ).

Alternate Data Streams  (ADS) is a file attribute specific to Windows  NTFS  (New Technology File System).

Every file has at least one data stream ( `$DATA` ), and ADS allows files to contain more than one stream of data. Natively [Window Explorer](https://support.microsoft.com/en-us/windows/what-s-changed-in-file-explorer-ef370130-1cca-9dc5-e0df-2f7416fe1cb1) doesn't display ADS to the user. There are 3rd party executables that can be used to view this data, but [Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) gives you the ability to view ADS for files.

From a security perspective, malware writers have used ADS to hide data.

Not all its uses are malicious. For example, when you download a file from the Internet, there are identifiers written to ADS to identify that the file was downloaded from the Internet.

To learn more about ADS, refer to the following link from MalwareBytes [here](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/) . 

**Bonus** : If you wish to interact hands-on with ADS, I suggest exploring Day 21 of  [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2) .

*Reference: https://tryhackme.com/room/windowsfundamentals1xbx*

---

## User account and profile, and permission notes

User accounts can be one of two types on a typical local Windows system: **Administrator** & **Standard User**. 

The user account type will determine what actions the user can perform on that specific Windows system. 

- An Administrator can make changes to the system: add users, delete users, modify groups, modify settings on the system, etc. 
- A Standard User can only make changes to folders/files attributed to the user & can't perform system-level changes, such as install programs.

You are currently logged in as an Administrator. There are several ways to determine which user accounts exist on the system. 

One way is to click the `Start Menu` and type `Other User`. A shortcut to `System Settings > Other users` should appear. 

![](https://assets.tryhackme.com/additional/win-fun1/win-other-user1.png)  

If you click on it, a Settings window should now appear. See below.

![](https://assets.tryhackme.com/additional/win-fun1/win-other-user.png)  

Since you're the Administrator, you see an option to **Add someone else to this PC**.

**Note**: A Standard User will not see this option.  

Click on the local user account. More options should appear: **Change account type** and **Remove**. 

![](https://assets.tryhackme.com/additional/win-fun1/win-other-user2.png)  

Click on Change account type. The value in the drop-down box (or the highlighted value if you click the drop-down) is the current account type. 

![](https://assets.tryhackme.com/additional/win-fun1/win-other-user3.png)

When a user account is created, a profile is created for the user. The location for each user profile folder will fall under is C:\Users.

For example, the user profile folder for the user account Max will be C:\Users\Max.

The creation of the user's profile is done upon initial login. When a new user account logs in to a local system for the first time, they'll see several messages on the login screen. One of the messages, User Profile Service, sits on the login screen for a while, which is at work creating the user profile. See below.

 ![](https://assets.tryhackme.com/additional/win-fun1/win-profile-service.png)

Once logged in, the user will see a dialog box similar to the one below (again), indicating that the profile is in creation.

![](https://assets.tryhackme.com/additional/win-fun1/win-profile-service2.png)  

Each user profile will have the same folders; a few of them are:

- Desktop
- Documents
- Downloads
- Music
- Pictures

Another way to access this information, and then some, is using **Local User and Group Management**. 

Right-click on the Start Menu and click **Run**. Type `lusrmgr.msc`. See below

![](https://assets.tryhackme.com/additional/win-fun1/win-lusrmgr.gif)  

**Note**: The Run Dialog Box allows us to open items quickly. 

Back to lusrmgr, you should see two folders: **Users** and **Groups**. 

If you click on Groups, you see all the names of the local groups along with a brief description for each group. 

Each group has permissions set to it, and users are assigned/added to groups by the Administrator. When a user is assigned to a group, the user inherits the permissions of that group. A user can be assigned to multiple groups.

**Note**: If you click on **Add someone else to this PC** from **Other users**, it will open **Local Users and Management**.

---

## Useful Windows programs and commands
---
The **System Configuration** utility (`MSConfig`) is for advanced troubleshooting, and its main purpose is to help diagnose startup issues
The **Computer Management** (`compmgmt`) utility has three primary sections: System Tools, Storage, and Services and Applications.

---
The **System Information** (`msinfo32`) tool

Per Microsoft, "_Windows includes a tool called Microsoft System Information (Msinfo32.exe).  This tool gathers information about your computer and displays a comprehensive view of your hardware, system components, and software environment, which you can use to diagnose computer issues._"

The  information in **System Summary** is divided into three sections:

- **Hardware Resources**
- **Components**
- **Software Environment**

---
What is **Resource Monitor** (`resmon`)?

Per Microsoft, "_Resource Monitor displays per-process and aggregate CPU, memory, disk, and network usage information, in addition to providing details about which processes are using individual file handles and modules. Advanced filtering allows users to isolate the data related to one or more processes (either applications or services), start, stop, pause, and resume services, and close unresponsive applications from the user interface. It also includes a process analysis feature that can help identify deadlocked processes and file locking conflicts so that the user can attempt to resolve the conflict instead of closing an application and potentially losing data._"

As some of the other tools mentioned in this room, this utility is geared primarily to advanced users who need to perform advanced troubleshooting on the computer system.  

In the Overview tab, Resmon has four sections:

- **CPU**
- **Disk**
- **Network**
- **Memory**

---
The command prompt (`cmd`) can seem daunting at first, but it's really not that bad once you understand how to interact with it. 

In early operating systems, the command line was the sole way to interact with the operating system.

When the GUI (graphical user interface) was introduced, it allowed users to perform complex tasks with a few clicks of a button instead of entering commands in the command prompt. 

Even though the GUI is the primary way to interact with the operating system, a computer user can still interact via the command prompt.

Some useful basic cmd commands:
The command **hostname** will output the computer name.

![](https://assets.tryhackme.com/additional/win-fun2/hostname.png)

The command **whoami** will output the name of the logged-in user.

![](https://assets.tryhackme.com/additional/win-fun2/whoami.png)

A command used often is `ipconfig`. This command will show the network address settings for the computer.

![](https://assets.tryhackme.com/additional/win-fun2/ipconfig.png)  

Each command will have a help manual to explain the expected syntax to execute the command properly, along with any additional parameters that can be added to the command to expand its execution.

A  command to retrieve the help manual for a command is `/?`.

For example, to see the help manual for **ipconfig**, you can use the following command: `ipconfig /?`

![](https://assets.tryhackme.com/additional/win-fun2/ipconfig-help.png)  

**Note**: To clear the command prompt screen, the command is `cls`. 

The next command is `netstat`. Per the help manual, this command will display protocol statistics and current TCP/IP network connections. 

![](https://assets.tryhackme.com/additional/win-fun2/netstat.png)  

In the above image, the line within the red box shows us an example syntax for the command. 

The structure tells us the **netstat** command can be run alone or with parameters, such as `-a`,  `-b`,  `-e`, etc. 

When any of the parameters are appended to the root command, **netstat** in this case, the output changes. Play with a few to see for yourself. 

The `net` command is primarily used to manage network resources. This command supports sub-commands.

If you type **net** without a sub-command, the output will show the syntax for the root command showing a few of the sub-commands you can use.

![](https://assets.tryhackme.com/additional/win-fun2/net.png)  

For the net command, to display the help manual `/?` will not work. In this case, you need to use different syntax, which is `net help`.

![](https://assets.tryhackme.com/additional/win-fun2/net-help.png)  

So, if you wish to see the help information for `net user` , the command is `net help user`. 

![](https://assets.tryhackme.com/additional/win-fun2/net-help-user2.png)

You can use the same command to view the help information for other useful **net** sub-commands, such as **localgroup**, **use**, **share**, and **session**.

---
The **Windows Registry** (per Microsoft) is a central hierarchical database used to store information necessary to configure the system for one or more users, applications, and hardware devices.

The registry contains information that Windows continually references during operation, such as:

- Profiles for each user
- Applications installed on the computer and the types of documents that each can create
- Property sheet settings for folders and application icons
- What hardware exists on the system
- The ports that are being used.

**Warning**: The registry is for advanced computer users. Making changes to the registry can affect normal computer operations. 

There are various ways to view/edit the registry. One way is to use the **Registry Editor** (`regedit`).

---

## Active Directory

**Windows domain** is a group of users and computers under the administration of a given business. The main idea behind a domain is to centralise the administration of common components of a Windows computer network in a single repository called **Active Directory (AD)**. The server that runs the Active Directory services is known as a **Domain Controller (DC)**.


---
*Reference:*
- https://tryhackme.com/room/windowsfundamentals1xbx
- https://tryhackme.com/room/windowsfundamentals2x0x
- https://tryhackme.com/room/winadbasics

---

##### Back to [README](../README.md) Mainpage