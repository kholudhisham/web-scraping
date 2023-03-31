# import libraries 
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
job_title= []
company_name =[]
location =[]
skills = []
links=[]
salary =[]
date=[]
page_num = 0
def get_data() :
    job_titles = soup.find_all("h2",{"class":"css-m604qf"})
    company_names = soup.find_all("a",{"class":"css-17s97q8"})
    locations = soup.find_all("span",{"class":"css-5wys0k"})
    job_skills = soup.find_all("div",{"class":"css-y4udm8"})
    posted_new =soup.find_all("div",{"class":"css-4c4ojb"})
    posted_old =soup.find_all("div",{"class":"css-do6t5g"})
    posted = [*posted_new ,*posted_old]


    for i in range (len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find("a").attrs['href'])
        company_name.append(company_names[i].text)
        location.append(locations[i].text)
        skills.append(job_skills[i].text) 
        date_text = posted[i].text.replace("-","").strip()
        date.append(date_text)    
while True :
    try :
        # Connect to Website and pull in data from multiple pages 
        page = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")
        src = page.content 
        soup = BeautifulSoup(src, "lxml")
        page_limit =int(soup.find("strong").text)
        if(page_num > page_limit // 15):
            print("Page Ended, Terminate")
            break
        get_data()
        page_num += 1
        print("Page Switched")
    except:
        print("Error Occured")    
        break

# Create CSV and write headers and data into the file

file_list = [job_title, company_name, location, skills, links, date]
exported = zip_longest(*file_list)
with open("C:/Users/kholud\Desktop/data analysis(udcity)/Data Analyst Portfolio/YallaKora/jobs_detailes.csv", 'w') as output_file :
    wr =csv.writer(output_file)
    wr.writerow(["Job Title","Company Name","Location", "Skills", "Link", "Date"])
    wr.writerows(exported)
print("File Created")    





