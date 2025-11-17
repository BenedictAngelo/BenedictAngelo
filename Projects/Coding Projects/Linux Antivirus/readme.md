# Automated Antivirus Scanner

## Objective
Install an antivirus called ==ClamAV== with ==ClamTK== for GUI support, automate a scheduled scanner and defining the scope of the scan, with a notifier.



### Skills Learned

- **Bash scripting**: Using Bash to define and set parameters of antivirus, and to schedule scan for my desired time in my OS.

### Tools Used

- Bash (Shell)
- ClamAV and ClamTK antivirus


## Steps

### 1. Install ClamAV antivirus in my Arch distro.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_195746.jpg)

```
sudo pacman -S clamav clamtk

or

sudo apt install clamav clamtk
```

- Install command for ClamAV antivirus for Arch repo and APT repo for debian based distros.
- Additionally add ==clamtk-kde== and ==clamtk-gnome== for scheduler plugins in preference for your desktop manager. Gnome version works well with Hyprland/Wayland.

### 2. Run ClamTK to familiarize to its GUI.

```
clamtk
```

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_200832.jpg)

- It is simple already self-explanatory, but do go in the 'Settings', for additional scanning options.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_200946.jpg)

- **Scan for PUAs**- Check to scan for Potentially Unwanted Apps, not an outright malware, but malicious programs. It may result to false positives.
- **Use heuristic scanning**- Instead of just scanning for malware signatures, it also scan for irregular or suspicious patterns and behavior of codes. It may result to false positive and slows down scans.
- **Scan files beginning with a dot**- Check to scan files that starts with dot(.), or also known as hidden files.
- **Scan directories recursively**- Check to scan the folders within folders.

### 3. Script a scan.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_202407.jpg)

- Use nano in local/bin for systemctl later.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_212306.jpg))

- Make file executable, define log file location as same as ClamTK scan history location, so I view the log on ClamTK, and then define variables for scan parameters, I excluded large files such as my games and I included some system files and common home files where malware programs usually attach and runs.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_202531.jpg)

- Added notification to notify me, and to no do anything that would interrupt the scan, added my scan commands with the defined variables for neat logging.
- Added ==if/fi== and ==else== for conditional statements.
- Ctrl + o then enter to save, Ctrl + x to exit nano

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_203545.jpg)

- Make it executable.
### 4. Make it a systemd service

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_203959.jpg)

- Nano and create and custom service.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_204134.jpg)

- Gave it a description and .service name and to run after clamav service, then referenced the script made earlier

### 5. Create the systemd timer for custom scan schedule

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_204548.jpg)

- Create another service that would time the services to run.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_204824.jpg)

- Make it run every Monday 12 noon.

### 6. Enable and start the timer

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_205012.jpg)

- Now use systemctl for it to autorun the services/daemon every boot.

![](../../../Image%20dump/Linux%20Antivirus%20dump/screenshot_17112025_205136.jpg)

- Check for the service.
- Now it should work auto scans every Monday 12:00 noon, and if my PC is open, and it will notify me if its scanning.

##### Back to [README](../../../README.md) Mainpage