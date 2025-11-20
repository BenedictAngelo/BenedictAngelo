# Linux From Scratch Project

## Objective
Learning Linux from scratch by installing and compiling a Gentoo OS at a Virtual machine (VirtualBox), from zero, to everything.



### Skills Learned

- **Linux Fundamentals** - Learning Linux from ground up by building and compiling a Gentoo minimal OS
- **Bash/Shell** - Learning the skeletal building of Linux by using commands from LFS wiki

### Tools Used

- Bash/Shell

## Steps
---

 ### 1. Download the Minimal Gentoo ISO file at: https://www.gentoo.org/downloads/, and set up in Virtual Box, refer to: [Mini Homelab](../IT%20Projects/Mini%20Homelab.md).

![](../../Image%20dump/LFS%20dump/screenshot_20112025_152053.jpg)

- Choose the "Minimal Installation CD" AMDx64

![](../../Image%20dump/LFS%20dump/screenshot_20112025_152205.jpg)

- Press "New" and add profiles to the new and to be made Gentoo OS machine, source where the .ISO file was downloaded for the "ISO image" dropdown

![](../../Image%20dump/LFS%20dump/screenshot_20112025_152430.jpg)

![](../../Image%20dump/LFS%20dump/screenshot_20112025_152436.jpg)

- Setup hardware allocation as indicated, I chose for it to borrow 6GB of RAM and 4 cores of my CPU, and allocated 50GB of storage disk, unchecked "Pre-allocate Full size" so it only eats storage dynamically, not all 50GB right on the go, then press finish.

![](../../Image%20dump/LFS%20dump/screenshot_20112025_153231.jpg)

- Check the "UEFI" checkbox and check "3D Acceleration" and allocate 128MB of Video Memory, hit OK.
 - Then select the Gentoo profile, and press "Start"
---

### 2. Partitioning the VirtualBox allocated disk

![](../../Image%20dump/LFS%20dump/screenshot_20112025_154237.jpg)

- Input `gdisk /dev/sda` to initiate partition tool, press `o` to create a new ==GPT== table, then confirm with `y`
-














##### Back to [README](../../README.md) Mainpage
