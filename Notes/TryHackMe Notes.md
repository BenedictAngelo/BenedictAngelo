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

*Reference: https://tryhackme.com/room/searchskills *

### Penetration testing notes

Penetration tests can have a wide variety of objectives and targets within scope. Because of this, no penetration test is the same, and there are no one-case fits all as to how a penetration tester should approach it. 

The steps a penetration tester takes during an engagement is known as the methodology. A practical methodology is a smart one, where the steps taken are relevant to the situation at hand. For example, having a methodology that you would use to test the security of a web application is not practical when you have to test the security of a network.

  

Before discussing some different industry-standard methodologies, we should note that all of them have a general theme of the following stages:  

  

|   |   |
|---|---|
|**Stage**|**Description**|
|Information Gathering|This stage involves collecting as much publically accessible information about a target/organisation as possible, for example, OSINT and research.<br><br>**Note:** This does not involve scanning any systems.|
|Enumeration/Scanning|This stage involves discovering applications and services running on the systems. For example, finding a web server that may be potentially vulnerable.|
|Exploitation|This stage involves leveraging vulnerabilities discovered on a system or application. This stage can involve the use of public exploits or exploiting application logic.|
|Privilege Escalation|Once you have successfully exploited a system or application (known as a foothold), this stage is the attempt to expand your access to a system. You can escalate horizontally and vertically, where horizontally is accessing another account of the same permission group (i.e. another user), whereas vertically is that of another permission group (i.e. an administrator).|
|Post-exploitation|This stage involves a few sub-stages:  <br><br>**1.** What other hosts can be targeted (pivoting)<br><br>**2.** What additional information can we gather from the host now that we are a privileged user<br><br>**3.**  Covering your tracks<br><br>**4.** Reporting|

  
  

**OSSTMM**

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/72a3a5b98b737f422f58b78e11e82646.png)

[The Open Source Security Testing Methodology Manual](https://github.com/mtesauro/owasp-wte/blob/master/temp-projects/wte-docs/contents/usr/share/doc/WTE-Documentation/OSSTMM/OSSTMM.3.pdf) provides a detailed framework of testing strategies for systems, software, applications, communications and the human aspect of cybersecurity.

  

The methodology focuses primarily on how these systems, applications communicate, so it includes a methodology for:

1. Telecommunications (phones, VoIP, etc.)
2. Wired Networks
3. Wireless communications

|   |   |
|---|---|
|**Advantages**|**Disadvantages**|
|Covers various testing strategies in-depth.|The framework is difficult to understand, very detailed, and tends to use unique definitions.|
|Includes testing strategies for specific targets (I.e. telecommunications and networking)|_Intentionally left blank._|
|The framework is flexible depending upon the organisation's needs.|_Intentionally left blank._||
|The framework is meant to set a standard for systems and applications, meaning that a universal methodology can be used in a penetration testing scenario.|_Intentionally left blank._|

  

**OWASP**

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/497e56c5522ca4932d720ae5fae32845.png)

  

The "[Open Web Application Security Project](https://owasp.org/)" framework is a community-driven and frequently updated framework used solely to test the security of web applications and services.

  

The foundation regularly [writes reports](https://owasp.org/www-project-top-ten/2017/) stating the top ten security vulnerabilities a web application may have, the testing approach, and remediation.

  

|   |   |
|---|---|
|**Advantages**|**Disadvantages**|
|Easy to pick up and understand.|It may not be clear what type of vulnerability a web application has (they can often overlap).|
|Actively maintained and is frequently updated.|OWASP does not make suggestions to any specific software development life cycles.|
|It covers all stages of an engagement: from testing to reporting and remediation.|The framework doesn't hold any accreditation such as CHECK.|
|Specialises in web applications and services.|_Intentionally left blank._|

  
  

**NIST Cybersecurity Framework 1.1**

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/8e11f5fcfc8fc6429fe35682797e2a24.jpg)

  

The [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) is a popular framework used to improve an organisations cybersecurity standards and manage the risk of cyber threats. This framework is a bit of an honourable mention because of its popularity and detail.

  

The framework provides guidelines on security controls & benchmarks for success for organisations from critical infrastructure (power plants, etc.) all through to commercial.  There is a limited section on a standard guideline for the methodology a penetration tester should take.

  

  

|   |   |
|---|---|
|**Advantages**|**Disadvantages**|
|The NIST Framework is estimated to be used by 50% of American organisations by 2020.|NIST has many iterations of frameworks, so it may be difficult to decide which one applies to your organisation.|
|The framework is extremely detailed in setting standards to help organisations mitigate the threat posed by cyber threats.|The NIST framework has weak auditing policies, making it difficult to determine how a breach occurred.|
|The framework is very frequently updated.|The framework does not consider cloud computing, which is quickly becoming increasingly popular for organisations.|
|NIST provides accreditation for organisations that use this framework.|_Intentionally left blank.  <br>_|
|The NIST framework is designed to be implemented alongside other frameworks.|_Intentionally left blank.  <br>_|

  

**NCSC CAF**

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/6e10e0fd0b6020d42873c218e1d37044.png)

The [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf/caf-principles-and-guidance) (CAF) is an extensive framework of fourteen principles used to assess the risk of various cyber threats and an organisation's defences against these.

  

The framework applies to organisations considered to perform "vitally important services and activities" such as critical infrastructure, banking, and the likes. The framework mainly focuses on and assesses the following topics:

- Data security
- System security
- Identity and access control
- Resiliency
- Monitoring
- Response and recovery planning

  

|   |   |
|---|---|
|Advantages|Disadvantages|
|This framework is backed by a government cybersecurity agency.|The framework is still new in the industry, meaning that organisations haven't had much time to make the necessary changes to be suitable for it.|
|This framework provides accreditation.|The framework is based on principles and ideas and isn't as direct as having rules like some other frameworks.|
|This framework covers fourteen principles which range from security to response.|Intentionally left blank.|

*Reference: https://tryhackme.com/room/pentestingfundamentals*


##### Back to [README](../README.md) Mainpage


