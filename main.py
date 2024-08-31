from bs4 import BeautifulSoup
import requests

html_text = requests.get(url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# jobs = soup.find_all('h3', class_ = 'joblist-comp-name')
job_name_dict = {}
for job in jobs:
    time_posted = job.find('span', class_ = 'sim-posted').text
    if 'few' in time_posted:
        job_names = job.find('h3', class_ = "joblist-comp-name").text.replace('\n', '').replace("  ", "")
        job_skill = job.find('span', class_ = "srp-skills").text.replace('\n', '').replace("  ", "")
        job_name_dict[job_names] = job_skill
# print(job_name_dict)
for key, value in job_name_dict.items():
    print(f"Job Name: {key} \nSkills Required are: {value}\n\n")