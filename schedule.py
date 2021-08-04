import requests
import pandas as pd
from bs4 import BeautifulSoup
import functions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
#driver = webdriver.Chrome(ChromeDriverManager().install() 
# ^ ensures tha the correct chrome version is downloaded


def main():
    url = "https://www.ccilindia.com/FPIHome.aspx"
    response = requests.get(url)
    content = BeautifulSoup(response.text,'html.parser')
    postback_tags = functions.get_postback(content)
    first_table = pd.read_html(url)[10]
    first_table = functions.alter_table(first_table)

    path_to_chromedriver = "C:/Users/neo qi xiang/Desktop/modular/chromedriver_win32/chromedriver.exe"
    for pages in postback_tags:
        driver = webdriver.Chrome(executable_path = path_to_chromedriver)
        driver.get(url)
        elem = driver.find_element_by_link_text(pages)
        elem.click()
        driver.implicitly_wait(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tables = soup.find_all('table')
        dfs = pd.read_html(str(tables))
        df = functions.alter_table(dfs[13])
        first_table = first_table.append(df)
        driver.close()

    first_table['date'] = functions.get_date(content)
    combine_table  = functions.prep_table(first_table)
    combine_table.to_sql('modular', con= functions.get_sql(), if_exists='append', index = False)
    functions.remove_sql_dups()
    
if __name__ == "__main__" :
    main()
