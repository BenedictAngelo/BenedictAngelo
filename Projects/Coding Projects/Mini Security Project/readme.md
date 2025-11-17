# Mini security Project

## Objective
To create a small SQLite database containing fictional data partaining of logging activities, then using python for filtering suspicious activity then automatic logging to output and in a text file



### Skills Learned

- Python
- SQL
- Automated logging
- Bash

### Tools Used

- Python
- SQL
- Bash

## Steps
1. Creating a sample data of 5 people with attempted login (fictional).
![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_130250.jpg)

- Creating a a file for generating database using python with SQLite import

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_130847.jpg)

- Created a fictional 5 subjects with varying names, devices, IPs, geolocation, status, and timestamps, with the intentional one suspicious subject that attempted a login and failed outside working hours.


![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_131132.jpg)

- Made it executable to generate the database file.

2. Run it to generate data file.

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_131602.jpg)

- Located and ran the .py file.

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_131727.jpg)

- Check if successful.

3. Creating the python file analyzer that would find suspicious activity of the subjects within the database.

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_132502.jpg)

- Created and imported SQL and defined the filename outputs

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_132613.jpg)

- Defined my parameters and added ==for== loops for filtering and conditional statement prints

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_132826.jpg)

- Created and ==echo== for an output print, and defining conditional findings of suspicious activity or no suspicious findings then a separate new SQL file for reference.

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_134333.jpg)

- Execute the ==analyzer.py==, then confirmed the 2 file outputs.

4. Look at the contents of the file outputs.

![](../../../Image%20dump/Mini%20security%20project%20dump/screenshot_17112025_134517.jpg)

- Confirmed and filtered, that =="Bon Santos"== was the suspicious that attempted login outside working hours showing his devices, IP, and location.

# END. Completed in November 16 2025


##### Back to [README](../../README.md) Mainpage




