# Linux From Scratch Project

## Objective
Learning the building blocks of installing a Linux Operating System by doing Linux from scratch by installing and compiling a [^2]Gentoo OS at a Virtual machine (VirtualBox), from zero, to everything.



### Skills Learned

- **Linux Fundamentals** - Learning Linux from ground up by building and compiling a Gentoo OS
- **Bash/Shell** - Learning the skeletal building of Linux by the help of Linux From Scratch wiki

### Tools Used

- Bash/Shell

## Steps
---

 ### 1. Download the Minimal Gentoo ISO file at: https://www.gentoo.org/downloads/, and set up in Virtual Box, refer to: [Mini Homelab](../../Homelab%20Projects/Mini%20Homelab.md).

- **Why Gentoo LiveGUI USB ISO?** - to meet the minimal host software system requirement of Linux from scratch, refer to: https://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html

![](../../../Image%20dump/LFS%20dump/screenshot_20112025_152053.jpg)

- Choose the "LiveGUI USB image" AMDx64

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_093957.jpg)

- Press "New" and add profiles to the new and to be made Gentoo OS machine, source where the .ISO file was downloaded for the "ISO image" dropdown

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_093957.jpg)

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_094509.jpg)


- Setup hardware allocation as indicated, I chose for it to borrow 6GB of RAM and 4 cores of my CPU, and allocated 50GB of storage disk, unchecked "Pre-allocate Full size" so it only eats storage dynamically, not all 50GB right on the go, then press finish.

![](../../../Image%20dump/LFS%20dump/screenshot_20112025_153231.jpg)

- Check the "UEFI" checkbox and check "3D Acceleration" and allocate 128MB of Video Memory, hit OK.
 - Then select the Gentoo profile, and press "Start"
---

### 2. Preparing the Host System

#### 2.1 Remote host control SSH and version check.

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_095202.jpg)
![](../../../Image%20dump/LFS%20dump/screenshot_27112025_100809.jpg)

- Immediately dropped into GUI installer, press `CTRL + ALT + F1` to go into [^1]==TTY== or open the console and type `chvt 1` to access TTY 1 then use `clear` to clean the console.

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_103703.jpg)

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_104218.jpg)

- Used `sudo passwd root` to change the password of root to just `1234` for the sake of this project, then used `su -` to go into root

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_110830.jpg)

- Used `rc-service sshd start` to start the ssh daemon, the used `ip a` and `ifconfig` to see the network status and the machine IP address and its listed as `10.0.2.15`

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_110845.jpg)

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_111016.jpg)

- Then configured the device network and added a rule for ==[^3]port forwarding== so that I can connect the host and SSH into the virtualbox machine

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_112047.jpg)

- Then used `ssh root@127.0.0.1` or  much better to ignore the host custom console`TERM=xterm-256color ssh -p 2222 root@127.0.0.1`  now to SSH into root of the VM, it became 127.0.0.1 because of localhost port forwarding rule set earlier, then entered the password of `1234` of VM Gentoo root.

```
cat > version-check.sh << "EOF"
`#!/bin/bash # A script to list version numbers of critical development tools  # If you have tools installed in other directories, adjust PATH here AND # in ~lfs/.bashrc (section 4.4) as well.  LC_ALL=C  PATH=/usr/bin:/bin  bail() { echo "FATAL: $1"; exit 1; } grep --version > /dev/null 2> /dev/null || bail "grep does not work" sed '' /dev/null || bail "sed does not work" sort   /dev/null || bail "sort does not work"  ver_check() {    if ! type -p $2 &>/dev/null    then       echo "ERROR: Cannot find $2 ($1)"; return 1;     fi    v=$($2 --version 2>&1 | grep -E -o '[0-9]+\.[0-9\.]+[a-z]*' | head -n1)    if printf '%s\n' $3 $v | sort --version-sort --check &>/dev/null    then       printf "OK:    %-9s %-6s >= $3\n" "$1" "$v"; return 0;    else       printf "ERROR: %-9s is TOO OLD ($3 or later required)\n" "$1";       return 1;     fi }  ver_kernel() {    kver=$(uname -r | grep -E -o '^[0-9\.]+')    if printf '%s\n' $1 $kver | sort --version-sort --check &>/dev/null    then       printf "OK:    Linux Kernel $kver >= $1\n"; return 0;    else       printf "ERROR: Linux Kernel ($kver) is TOO OLD ($1 or later required)\n" "$kver";       return 1;     fi }  # Coreutils first because --version-sort needs Coreutils >= 7.0 ver_check Coreutils      sort     8.1 || bail "Coreutils too old, stop" ver_check Bash           bash     3.2 ver_check Binutils       ld       2.13.1 ver_check Bison          bison    2.7 ver_check Diffutils      diff     2.8.1 ver_check Findutils      find     4.2.31 ver_check Gawk           gawk     4.0.1 ver_check GCC            gcc      5.4 ver_check "GCC (C++)"    g++      5.4 ver_check Grep           grep     2.5.1a ver_check Gzip           gzip     1.3.12 ver_check M4             m4       1.4.10 ver_check Make           make     4.0 ver_check Patch          patch    2.5.4 ver_check Perl           perl     5.8.8 ver_check Python         python3  3.4 ver_check Sed            sed      4.1.5 ver_check Tar            tar      1.22 ver_check Texinfo        texi2any 5.0 ver_check Xz             xz       5.0.0 ver_kernel 5.4  if mount | grep -q 'devpts on /dev/pts' && [ -e /dev/ptmx ] then echo "OK:    Linux Kernel supports UNIX 98 PTY"; else echo "ERROR: Linux Kernel does NOT support UNIX 98 PTY"; fi  alias_check() {    if $1 --version 2>&1 | grep -qi $2    then printf "OK:    %-4s is $2\n" "$1";    else printf "ERROR: %-4s is NOT $2\n" "$1"; fi } echo "Aliases:" alias_check awk GNU alias_check yacc Bison alias_check sh Bash  echo "Compiler check:" if printf "int main(){}" | g++ -x c++ - then echo "OK:    g++ works"; else echo "ERROR: g++ does NOT work"; fi rm -f a.out  if [ "$(nproc)" = "" ]; then    echo "ERROR: nproc is not available or it produces empty output" else    echo "OK: nproc reports $(nproc) logical cores are available" fi`
EOF

bash version-check.sh
```


- Copy and paste this for softwares version check, refer to: https://www.linuxfromscratch.org/lfs/view/stable/chapter02/hostreqs.html for the script.

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_114950.jpg)

- Now run the script, and confirmed that everything passes and ok.

---
#### 2.2 Disk partitioning

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_115925.jpg)

- Run `lsblk` to list block devices, and here I see the disk I want to partitioned named `sda` wit 50GB of dynamic storage I set earlier in virtualbox settings










---
*Reference: https://www.linuxfromscratch.org/lfs/view/stable/index.html *


##### Back to [README](../../../README.md) Mainpage



[^1]: In Linux, TTY stands for teletypewriter, a term originating from early physical devices used for text-based communication with computers. Today, it refers to a virtual terminal system that allows users to interact with the operating system through text input and output, serving as a fundamental component of Unix-like systems. Each terminal session, whether a physical console or a virtual one accessed via SSH or a GUI terminal emulator, is represented by a TTY device file, such as /dev/tty1 for virtual consoles or /dev/pts/0 for pseudo-terminals used in remote sessions.

[^2]: Gentoo Linux is a free, open-source Linux distribution built using the Portage package management system, which compiles software from source code tailored to the user's specific hardware and preferences. Unlike binary distributions that provide pre-compiled software, Gentoo emphasizes customization, performance optimization, and user control by compiling packages locally, often resulting in faster and more efficient systems. It is described as a "meta-distribution" due to its high adaptability, allowing users to create highly unique and personalized configurations.

[^3]: Port forwarding is a networking technique that allows external devices on the internet to connect to a specific device within a private network, such as a home or office network, by redirecting communication requests from a public IP address and port to a designated internal IP address and port. This is necessary because devices on private networks typically use private IP addresses that are not directly accessible from the internet, and routers act as gatekeepers, blocking unsolicited incoming traffic.
