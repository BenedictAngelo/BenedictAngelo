# Connecting to THM VPN in Linux
Refer to [Linux Cheat Sheet](Linux%20Cheat%20Sheet.md) before installing anything.
```
sudo apt install openvpn

or

sudo pacman -S openvpn

or

sudo paru -S openvpn
```

- Use ==apt== if debian based, ==pacman== if Arch or ==paru== if AUR wrapper.

```
sudo openvpn [VPN filepath downloaded]
```
 
- Open my own Parrot OS/Kali Linux
- Then Downloaded the VPN configuration in my THM profile
- Default file path ==~/Downloads/*.ovpn==

```
ssh tryhackme@[IP address]
```

- To connect on tryhackme remote machine.

---

##### Back to [README](../README.md) Mainpage


