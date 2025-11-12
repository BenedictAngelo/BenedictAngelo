# Useful Linux Commands for daily use
---

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

- ==sudo pacman -Rns $(pacman -Qdtq)== Cleans orphaned packages in Arch packager, run ==pacman -Qdtq== first to check orphaned packages, ==paru -c== optional for cleaning AUR cache
---

```
ps aux | grep [The name of the program]
```

- ==ps aux== to fetch the list of running programs in PC, then ==|== to pipe the output to ==grep==, then grep finds the similar program or name in general on the ==[The name of the program]==


