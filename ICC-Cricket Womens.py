#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[12]:


url=["https://www.icc-cricket.com/rankings/womens/team-rankings/odi",
    "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting",
    "https://www.icc-cricket.com/rankings/womens/player-rankings/odi"]


# In[13]:


final_result_file_name="All Ranking List.csv"
final_result_file_name=["Ranking Type","position","player name","team name","Rating","career Best Rating","Crawl URL"]


# In[14]:


pd.DataFrame(column=final_coulmn_names).to_csv(final_result_file_name,sep="\t",index=False,encoding="utf-8")


# In[ ]:


for url in urls:
    request_object=requests.get(url,headers=headers)
    
    html_content=request_object.text
    print_content=request_object.text
    soup_object=BeautifulSoup(html_content,"lxml")
    for element in soup_object.select('[class+"ranking-pos up"],[class="ranking-pos down"]'):
        element.replace_with(BeautifulSoup("<"+elemnt.name+">"/+element.name+">","html.parser"))
        
    rankling_type=soup_object.select_one("ranking_block_title_container>h4").text
    result_file_name=ranking_type+".csv"
    
    column_name=["position","player Name","Team Name","Rating","Career Best Rating","Crawl","URL"]


# In[9]:


pd.DataFrame({})

for element in soup_object.select('table[class="table ranking-table"]tr')
 if (element.find("th")):
        continue
        data_dict=dict()
        data_dict["crawl URl"]=url
        data_dict["Ranking Type"]=ranking_type
        if(element.select_one('[class*="position"]')):
            data_dict["podition"]=element.select_one('[class*="postion"]').text


# In[ ]:




