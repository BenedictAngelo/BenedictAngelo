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

*Reference: https://tryhackme.com/room/windowsfundamentals1xbx*

---

##### Back to [README](../README.md) Mainpage