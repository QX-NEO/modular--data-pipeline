import password
import re
import pandas as pd



def get_sql():
    POSTGRES_ADDRESS = password.getaddress()
    POSTGRES_PORT = password.getport()
    POSTGRES_USERNAME = password.getusername()
    POSTGRES_PASSWORD = password.getpass()
    POSTGRES_DBNAME = password.getdbname()
    postgres_str = 'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME,
                                                                                            password=POSTGRES_PASSWORD, ipaddress=POSTGRES_ADDRESS, port=POSTGRES_PORT, dbname=POSTGRES_DBNAME)
    return postgres_str

def set_header(df):
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    return df

def alter_table(df):
    set_head = set_header(df)
    remove = set_head[:-1]
    return remove

def get_postback(data):
    tags = []
    for i in data.find_all("a"):
        string_tag = str(i)
        if bool(re.search('<a href="javascript:__doPostBack', string_tag)):
            tags.append(i.next.next)
    return tags

def get_date(input):
    date = input.find("span", id = "lblDate").next.next.next.split(" ")[-1]
    return date

def prep_table(df):
    df['date'] =  pd.to_datetime(df['date'],format='%d-%b-%Y')
    df[["Indicative Value Of Aggregate Holding Of FPIS (INR CR#)", "Outstanding Position Of Govt# Securities (INR CR#)", "Sec Holdings (%)"]] = df[["Indicative Value Of Aggregate Holding Of FPIS (INR CR#)", "Outstanding Position Of Govt# Securities (INR CR#)", "Sec Holdings (%)"]].astype(float)
    df = df.drop_duplicates()
    df = df.rename(columns={"Indicative Value Of Aggregate Holding Of FPIS (INR CR#)": "IVAH", "Outstanding Position Of Govt# Securities (INR CR#)": "OPGS", "Sec Holdings (%)": "sec_holding"}, errors="raise")
    return df

def remove_sql_dups():
    query = """DELETE FROM public.modular
                WHERE  ctid NOT IN (
                    SELECT min(ctid)                   
                    FROM   public.modular
                    GROUP  BY "ISIN","Security Description","IVAH","OPGS",sec_holding,date);"""
    pd.read_sql_query(query, con= get_sql())
