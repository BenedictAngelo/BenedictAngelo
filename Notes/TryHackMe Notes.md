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

---
## Penetration testing notes

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

---
### Content Discovery
**Robots.txt**

The robots.txt file is a document that tells search engines which pages they are and aren't allowed to show on their search engine results or ban specific search engines from crawling the website altogether. It can be common practice to restrict certain website areas so they aren't displayed in search engine results. These pages may be areas such as administration portals or files meant for the website's customers. This file gives us a great list of locations on the website that the owners don't want us to discover as penetration testers.

**Sitemap.xml**

Unlike the robots.txt file, which restricts what search engine crawlers can look at, the sitemap.xml file gives a list of every file the website owner wishes to be listed on a search engine. These can sometimes contain areas of the website that are a bit more difficult to navigate to or even list some old webpages that the current site no longer uses but are still working behind the scenes.

**Wappalyzer**

Wappalyzer ([https://www.wappalyzer.com/](https://www.wappalyzer.com/)) is an online tool and browser extension that helps identify what technologies a website uses, such as frameworks, Content Management Systems (CMS), payment processors and much more, and it can even find version numbers as well.

**Wayback Machine**

The Wayback Machine ([https://archive.org/web/](https://archive.org/web/)) is a historical archive of websites that dates back to the late 90s. You can search a domain name, and it will show you all the times the service scraped the web page and saved the contents. This service can help uncover old pages that may still be active on the current website.

**GitHub**

To understand GitHub, you first need to understand Git. Git is a **version control system** that tracks changes to files in a project. Working in a team is easier because you can see what each team member is editing and what changes they made to files. When users have finished making their changes, they commit them with a message and then push them back to a central location (repository) for the other users to then pull those changes to their local machines. GitHub is a hosted version of Git on the internet. Repositories can either be set to public or private and have various access controls. You can use GitHub's search feature to look for company names or website names to try and locate repositories belonging to your target. Once discovered, you may have access to source code, passwords or other content that you hadn't yet found.

**S3 Buckets**

S3 Buckets are a storage service provided by Amazon AWS, allowing people to save files and even static website content in the cloud accessible over HTTP and HTTPS. The owner of the files can set access permissions to either make files public, private and even writable. Sometimes these access permissions are incorrectly set and inadvertently allow access to files that shouldn't be available to the public. The format of the S3 buckets is http(s)://**{name}.**[**s3.amazonaws.com**](http://s3.amazonaws.com/) where {name} is decided by the owner, such as [tryhackme-assets.s3.amazonaws.com](http://tryhackme-assets.s3.amazonaws.com/). S3 buckets can be discovered in many ways, such as finding the URLs in the website's page source, GitHub repositories, or even automating the process. One common automation method is by using the company name followed by common terms such as **{name}**-assets, **{name}**-www, **{name}**-public, **{name}**-private, etc.

**What is Automated Discovery?**

Automated discovery is the process of using tools to discover content rather than doing it manually. This process is automated as it usually contains hundreds, thousands or even millions of requests to a web server. These requests check whether a file or directory exists on a website, giving us access to resources we didn't previously know existed. This process is made possible by using a resource called wordlists.

  

**What are wordlists?**

Wordlists are just text files that contain a long list of commonly used words; they can cover many different use cases. For example, a password wordlist would include the most frequently used passwords, whereas we're looking for content in our case, so we'd require a list containing the most commonly used directory and file names. An excellent resource for wordlists that is preinstalled on the THM AttackBox is [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) which Daniel Miessler curates.

  

**Automation Tools**

Although there are many different content discovery tools available, all with their features and flaws, we're going to cover three which are preinstalled on our attack box, ffuf, dirb and gobuster.

---
### Subdomain Enumeration

When an SSL/TLS (Secure Sockets Layer/Transport Layer Security) certificate is created for a domain by a CA (Certificate Authority), CA's take part in what's called "Certificate Transparency (CT) logs". These are publicly accessible logs of every SSL/TLS certificate created for a domain name. The purpose of Certificate Transparency logs is to stop malicious and accidentally made certificates from being used. We can use this service to our advantage to discover subdomains belonging to a domain, sites like [https://crt.sh](https://crt.sh/) offer a searchable database of certificates that shows current and historical results.

Go to [crt.sh](https://crt.sh/) and search for the domain name **tryhackme.com**, find the entry that was logged at **2020-12-26** and enter the domain below to answer the question.

Search engines contain trillions of links to more than a billion websites, which can be an excellent resource for finding new subdomains. Using advanced search methods on websites like Google, such as the `site: filter`, can narrow the search results. For example, `site:*.domain.com -site:www.domain.com` would only contain results leading to the domain name domain.com but exclude any links to www.domain.com; therefore, it shows us only subdomain names belonging to domain.com.

**Bruteforce DNS (Domain Name System) Enumeration**

- By attempting tens, hundreds, thousands, or even millions of **unique subdomains from a pre-defined list** of frequently used subdomains, and it automates it with a tool to speed up the procedure.

Tool:   
• **dnsrecon**If you're running Kali Linux, it's already pre-installed, and you can go to the "terminal" and type "**dnsrecon**" to see how to use it.



![](https://miro.medium.com/v2/resize:fit:700/1*w_By_v7mxCiFxGkAxjsWwA.png)



![](https://miro.medium.com/v2/resize:fit:394/1*xre0IWWQ28OPkrrksJe-8g.png)

It expedites the process of discovering OSINT subdomains.

1st - Install sublist3r in Kali Linux  
• **sudo apt install sublist3r**2nd Run sublist3r  
• type: **sublist3r**

Subdomains aren’t usually hosted in DNS results that are publicly accessible, such as:

- development versions of a web application
- administration portals

DNS records can be **stored on a private DNS server** or on the **developer’s workstations** in the **/etc/hosts** file (or **c:\windows\system32\drivers\etc\hosts file for Windows users**), which translates domain names to IP addresses.

Web servers can host numerous websites from a single server. • When a client requests a website, the server determines which website the client wants based on the **Host Header**.

What we can do:

- Make use of this **host header by modifying it and checking the response** to see whether we’ve discovered a new website, and it’s very similar to DNS Brute Force in that it uses a tool to seek it out and automates the process.

Tool:  
• **ffuf**It comes pre-installed with Kali LinuxExample:   
• **ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://<domain name/ip address>**Switches:  
**-w** > wordlist  
**-H** > adds/edits a header  
**-u** > url  
**-fs** > tells ffuf to ignore any results that are of the specified size

**[Question 6.1] What is the first subdomain discovered?**

![](https://miro.medium.com/v2/resize:fit:664/1*BnMAPCi4UN0u7r89YKiFDw.png)

ffuf -w namelist.txt -H “Host: FUZZ.acmeitsupport.thm” -u http://<IP address>

Notice that there are numerous reports with the “Size” of “2395” and that you should then filter out the “2395” to see what the result could be.

Method: • ffuf -w namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u [http://10.10.186.57](http://10.10.186.57/) **-fs 2395**By including the switch "-fs" and the value "2395," it will filter and eliminate all of the "2395"


![](https://miro.medium.com/v2/resize:fit:700/1*snYTebPbNAJg5QqgxdNm0w.png)

![](https://miro.medium.com/v2/resize:fit:700/1*RuB6F1FD3OKgxHmMiaUqWg.png)






---












*Reference: https://tryhackme.com/room/pentestingfundamentals*


##### Back to [README](../README.md) Mainpage


