
# Virtual Mini Home Lab

## Objective

The Virtual Mini Home Lab project is aimed to establish and create my very first home lab set up for a sandboxed and controlled cybersecurity practices, exercises, and projects to come. It is for documentation of setting up multiple virtual machines for the use of simulating an attacker using Security/Penetration tester Linux distros and a vulnerable OS for victim scenarios, replicating and simulating real world scenarios and Cyber security analyst and Penetration tester roles.

### Skills Learned


- Virtual machine set up.
- Linux environment familiarity and understanding.
- Home Labbing.
- Unix programming.


### Tools Used

- Virtual Box.
- Cachy OS (My main OS).
- Kali Linux OS for standard Penetration testing use.
- Parrot security OS for lightweight and stable Penetration testing/Digital Forensic use.
- Linux mint OS to simulate a vulnerable victim OS.

## Steps
### 1.  Install Virtual box in my main OS
<img width="756" height="70" alt="screenshot_11112025_202711" src="https://github.com/user-attachments/assets/6843e2c3-e65a-478c-b567-187b214c442d" />

-  "sudo pacman -Syu" to make sure my OS kernel and its packages is up to date then "sudo pacman -S virtualbox virtualbox-host-dkms dkms" to install virtualbox .(DKMS builds the modules for your current kernel and future kernel updates).

### 2.  Donwload Pre-Built VM kali linux at "https://www.kali.org/get-kali/#kali-virtual-machines"

<img width="1349" height="889" alt="screenshot_11112025_203222" src="https://github.com/user-attachments/assets/4e93d68d-c122-432d-9207-909aefdcf003" />

-  I downloaded a Virtual Box ready Kali Linux OS for easy setup and install.

### 3.  Download Parrot Security OS at "https://www.parrotsec.org/download/"

<img width="1299" height="803" alt="screenshot_11112025_203559" src="https://github.com/user-attachments/assets/32f4841a-e811-41f4-9952-a155d9090953" />

-  Click "Virtual" for virtual machine version of Parrot OS
<img width="1242" height="817" alt="screenshot_11112025_203612" src="https://github.com/user-attachments/assets/ae0e93cc-f6c8-4246-a7ab-f10eef249a10" />

-  Click the "Security" version.

<img width="1186" height="792" alt="screenshot_11112025_203623" src="https://github.com/user-attachments/assets/bd61773f-11a0-4f72-9933-a65c20a92b10" />

-  Then choose "AMD64" version for x64 bit architecture and built for PC use.

### 4.  Download Linux mint xFCE version for a lightweight version at "https://linuxmint.com/download.php"

<img width="1226" height="759" alt="screenshot_11112025_204401" src="https://github.com/user-attachments/assets/48bef35d-6dce-4a15-9561-bbd904eab70d" />

### 5.  Unzip the download files, to see the .iso or .vbox files.
### 6.  Add to each one to Virtual Box and navigate where the OS was downloaded.

<img width="1226" height="759" alt="screenshot_11112025_204401" src="https://github.com/user-attachments/assets/da5af295-3267-4b21-afa6-241d116a713f" />

-  Click Open "+" Icon then navigate and add each OS.

<img width="857" height="448" alt="screenshot_11112025_205047" src="https://github.com/user-attachments/assets/d7038c65-e071-4af4-a919-20cd69427308" />

-  Now it's listed and ready to start

### 7.  Configure the resource allocation on each OS.

<img width="1905" height="1003" alt="screenshot_11112025_205424" src="https://github.com/user-attachments/assets/a93043ee-db0f-4e9a-b683-829d3fb5ee04" />

<img width="1909" height="1025" alt="screenshot_11112025_205552" src="https://github.com/user-attachments/assets/d160d13d-f02e-4e92-80cb-3e829059c9a5" />

- I allocated 4GB ram, 4 CPU cores, 64 MB of video memory both came with dynamic virtual storage with 64GB allocated to Parrot OS and 80GB allocated for Kali Linux.

<img width="1914" height="1033" alt="screenshot_11112025_210038" src="https://github.com/user-attachments/assets/d91feecb-6036-4be6-9b37-7d8211fabab2" />

- I allocated less resources for Linux Mint with just 3GB ram, 2 CPU cores, 64 MB of video memory 25GB of virtual storage.

### 8.  Startup and fresh boot of Kali Linux.

<img width="1359" height="1026" alt="screenshot_11112025_210920" src="https://github.com/user-attachments/assets/292ec705-9fdc-4bd8-90b7-0c1eeea7f840" />

-I start Kali Linux, boot from grub, then entered default credentials user:kali pass:kali, then opened terminal to initiate "sudo apt update" to fetch updates and "sudo apt upgrade" to start the system and package upgrades.

<img width="1356" height="1027" alt="screenshot_11112025_212133" src="https://github.com/user-attachments/assets/b00c7fec-0d71-47f8-a265-5443afa6b3e0" />

-  After updates, I cleaned the system for leftover files and to delete orphaned packages.

<img width="647" height="519" alt="screenshot_11112025_213413" src="https://github.com/user-attachments/assets/4aca3202-1428-4dbe-baa7-5e53acfc6bd8" />

-  Installed an Uncomplicated firewall.

<img width="653" height="517" alt="screenshot_11112025_214210" src="https://github.com/user-attachments/assets/36feef93-9b43-41aa-9409-a49fafe71504" />

- To enable it on startup.

<img width="652" height="518" alt="screenshot_11112025_214543" src="https://github.com/user-attachments/assets/ca952fce-616c-4888-956a-a5fb036a7a43" />

-  Set up default rules.

<img width="646" height="513" alt="screenshot_11112025_214749" src="https://github.com/user-attachments/assets/39f1e939-746c-4436-afc1-076ab2348c95" />

-  Now enable the firewall and checked its status.

### 9.  Do the exact same procedure on a fresh boot Parrot OS using default user:parrot pass:parrot
### 10. Do the exact same procedure on a fresh boot Linux Mint and setting up custom user:victim pass:victim, for easy target labeling, and  not setting up a firewall, to simulate unfiltered connection and to add vulnerabilty for another attack vector.

#  END



