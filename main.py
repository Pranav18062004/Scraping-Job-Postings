from bs4 import BeautifulSoup
import requests

html_text = requests.get(url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    time_posted = job.find('span', class_ = 'sim-posted').text
    if 'few' in time_posted:
        job_names = job.find('h3', class_ = "joblist-comp-name").text.replace('\n', '').replace("  ", "")
        job_skill = job.find('span', class_ = "srp-skills").text.replace('\n', '').replace("  ", "")
        more_info = job.header.h2.a['href']
        print(f"Job Name: {job_names} \nSkills Required are: {job_skill} \nMore info: {more_info}\n\n")
