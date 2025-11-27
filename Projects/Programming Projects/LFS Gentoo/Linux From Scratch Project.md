# Linux From Scratch Project

## Objective
Learning Linux from scratch by installing and compiling a [^2]Gentoo OS at a Virtual machine (VirtualBox), from zero, to everything.



### Skills Learned

- **Linux Fundamentals** - Learning Linux from ground up by building and compiling a Gentoo OS
- **Bash/Shell** - Learning the skeletal building of Linux by te help of wiki from Linux From Scratch wiki

### Tools Used

- Bash/Shell

## Steps
---

 ### 1. Download the Minimal Gentoo ISO file at: https://www.gentoo.org/downloads/, and set up in Virtual Box, refer to: [Mini Homelab](../../Homelab%20Projects/Mini%20Homelab.md).

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

![](../../../Image%20dump/LFS%20dump/screenshot_27112025_095202.jpg)
![](../../../Image%20dump/LFS%20dump/screenshot_27112025_100809.jpg)

- Immediately dropped into GUI installer, press `CTRL + ALT + F1` to go into [^1]==TTY== or open the console and type `chvt 1` to access TTY 1.

---
*Reference: https://www.linuxfromscratch.org/lfs/view/stable/index.html *


##### Back to [README](../../../README.md) Mainpage



[^1]: In Linux, TTY stands for teletypewriter, a term originating from early physical devices used for text-based communication with computers. Today, it refers to a virtual terminal system that allows users to interact with the operating system through text input and output, serving as a fundamental component of Unix-like systems. Each terminal session, whether a physical console or a virtual one accessed via SSH or a GUI terminal emulator, is represented by a TTY device file, such as /dev/tty1 for virtual consoles or /dev/pts/0 for pseudo-terminals used in remote sessions.

[^2]: Gentoo Linux is a free, open-source Linux distribution built using the Portage package management system, which compiles software from source code tailored to the user's specific hardware and preferences. Unlike binary distributions that provide pre-compiled software, Gentoo emphasizes customization, performance optimization, and user control by compiling packages locally, often resulting in faster and more efficient systems. It is described as a "meta-distribution" due to its high adaptability, allowing users to create highly unique and personalized configurations.
