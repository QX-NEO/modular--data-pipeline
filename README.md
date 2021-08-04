# modular--data-pipeline
**software:**

jupyter notebook

python 3.7

postgresql

**files:**
function.py -> functions used by schedule.py and visuals.py

password.py -> sql information for connections using python

schedule.py -> to be scheduled by task manager (windows) or cron when using linux

visuals.py -> using plotly dash to visualise time series trend of Indicative Value Of Aggregate Holding of FPIS (INR CR#) for that ISIN 

populate_DB.ipynb -> used to do a initial scrapped on: https://www.ccilindia.com/FPI_ARCV.aspx


**modules used:**
plotly-express: pip install plotly-express

numpy : pip install numpy

pandas: pip install pandas

dash: pip install dash

BeautifulSoup : pip install beautifulsoup4

selenium : pip install selenium

webdriver manager: pip install webdriver-manager <- helps you to download your webdriver version


**Important:**

recommended to use postgresql

under functions.py fill in your database connection details.

**Procedures:**

1) fill in database particulars in functions.py
2) run all populate_DB.ipynb file <- this will populate your database
3) set schedule.py inside your task schedular insructions can be found here : https://www.jcchouinard.com/python-automation-using-task-scheduler/ run your script every hour/ do not need to worry about duplicates as the script will remove duplicates found
4) run the visuals.py to view time series og Indicative Value Of Aggregate Holding of FPIS (INR CR#) for that ISIN.







 


