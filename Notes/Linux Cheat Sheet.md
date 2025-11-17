# Useful Linux Commands for daily use
---
## Update and clean-up
```
sudo apt update && sudo apt upgrade
```

- To fetch latest update list of APT package manager and go straight into upgrade

```
sudo pacman -Syu
```

- For Arch packager
---

```
sudo apt autoclean && supo apt autoremove
```

- To clean leftover files and cache and remove orphaned packages

```
sudo pacman -Rns $(pacman -Qdtq)
sudo paccache -r
paru -c
```

- ==`sudo pacman -Rns $(pacman -Qdtq)`== Cleans orphaned packages in Arch packager, run ==`pacman -Qdtq`== first to check orphaned packages, ==`paru -c`== optional for cleaning AUR cache
---
## Processes

### systemd
- Is one of the first processes that are started on boot. Any program or piece on software that we want to start will start as what is known as child process of ==systemd==

```
ps aux | grep [The name of the program]
```

- ==`ps aux`== to fetch the list of running programs in PC, then ==`|`== to pipe the output to ==`grep`==, then grep finds the similar program or name in general on the ==[The name of the program]==
- ==`fg`== to bring the chosen process into and output into the terminal.

```
top

or

htop
```

- This command list the programs running in real time, refreshes every 10 seconds, it also provides an interact-able UI actions for the programs
- -  ==SIGTERM== - Kill the process, but allow it to do some cleanup tasks beforehand
- - ==SIGKILL== - Kill the process - doesn't do any cleanup after the fact
- - ==SIGSTOP== - Stop/suspend a process


```
kill [PID]
```

- This kills the listed program pertaining to what the process ID ==[PID]==, useful to just directly and instantly stop the program.

```
systemctl [option] [service]
```

- This command interacts with the process/daemon.
- ==[option]==
- - start
- - stop
- - enable
- - disable
### System Automation
#### cron

-Is on of the processes that starts on boot and is responsible for doing a set of command during a specific set of time or every time.

==`cron`== requires 6 specific values:

| Value | Description                           |
| ----- | ------------------------------------- |
| MIN   | What minute to execute at             |
| HOUR  | What Hour to execute at               |
| DOM   | What day of the month to execute at   |
| MON   | What month of the year to execute at  |
| DOW   | What day of the week to execute at    |
| CMD   | The actual command that will executed |      |                                       |

Example:
```
0 */12 * * * cp -R /home/cmnatic/Documents /var/backups/
```

- it support wildcard ==*== if no specific value to put.
- ==`crontabs`== can be edited with ==`crontab -e`== then select an editor like ==`nano`==

---

##### Back to [README](../README.md) Mainpage
