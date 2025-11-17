# Connecting to THM VPN in Linux
Refer to [Linux Cheat Sheet](Linux%20Cheat%20Sheet.md) before installing anything.
```
sudo apt install openvpn

or

sudo pacman -S openvpn

or

sudo paru -S openvpn
```

- Use ==`apt`== if debian based, ==`pacman`== if Arch or ==`paru`== if AUR wrapper.

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

# Lesson Notes
## 'Search Skills - Cyber security 101' module notes
You are familiar with Internet search engines; however, how much are you familiar with specialized search engines? By that, we refer to search engines used to find specific types of results.

### Shodan

Let’s start with [Shodan](https://www.shodan.io/), a search engine for devices connected to the Internet. It allows you to search for specific types and versions of servers, networking equipment, industrial control systems, and IoT devices. You may want to see how many servers are still running Apache 2.4.1 and the distribution across countries. To find the answer, we can search for `apache 2.4.1`, which will return the list of servers with the string “apache 2.4.1” in their headers.

![The results of searching for apache 2.4.1 on the Shodan website.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/5f04259cf9bf5b57aed2c476-1718112514634)  

Consider visiting Shodan [Search Query Examples](https://www.shodan.io/search/examples) for more examples. Furthermore, you can check [Shodan trends](https://trends.shodan.io/) for historical insights if you have a subscription.

### Censys

At first glance, [Censys](https://search.censys.io/) appears similar to Shodan. However, Shodan focuses on Internet-connected devices and systems, such as servers, routers, webcams, and IoT devices. Censys, on the other hand, focuses on Internet-connected hosts, websites, certificates, and other Internet assets. Some of its use cases include enumerating domains in use, auditing open ports and services, and discovering rogue assets within a network. You might want to check [Censys Introductory Use Cases](https://docs.censys.com/docs/ls-introductory-use-cases#/).

![The results of searching for apache 2.4.1 on the Censys website.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/5f04259cf9bf5b57aed2c476-1718112720346)  

### VirusTotal

[VirusTotal](https://www.virustotal.com/) is an online website that provides a virus-scanning service for files using multiple antivirus engines. It allows users to upload files or provide URLs to scan them against numerous antivirus engines and website scanners in a single operation. They can even input file hashes to check the results of previously uploaded files.

The screenshot below shows the result of checking the submitted file against 67 antivirus engines. Furthermore, one can check the community's comments for more insights. Occasionally, a file might be flagged as a virus or a Trojan; however, this might not be accurate for various reasons, and that's when community members can provide a more in-depth explanation.

![Checking the detection of a certain zip file on the VirusTotal website.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/5f04259cf9bf5b57aed2c476-1718112692359)  

### Have I Been Pwned

[Have I Been Pwned](https://haveibeenpwned.com/) (HIBP) does one thing; it tells you if an email address has appeared in a leaked data breach. Finding one’s email within leaked data indicates leaked private information and, more importantly, passwords. Many users use the same password across multiple platforms, if one platform is breached, their password on other platforms is also exposed. Indeed, passwords are usually stored in encrypted format; however, many passwords are not that complex and can be recovered using a variety of attacks.

![The results for an email address on the Have I Been Pwned website.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/5f04259cf9bf5b57aed2c476-1718112534973)

*Reference: https://tryhackme.com/room/searchskills*

##### Back to [README](../README.md) Mainpage


