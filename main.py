from bs4 import BeautifulSoup
import requests
import time

input_text = ''
unfamiliar_skills = []

print("Enter skills that are unfamiliar to you if no more press q")
while input_text != "q":
    input_text = input(">").lower()
    unfamiliar_skills.append(input_text)
unfamiliar_skills.pop()
def find_jobs(index):
    html_text = requests.get(url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    with open(f'posts\\{index}.txt', '+a') as f:
        for job in jobs:
            time_posted = job.find('span', class_ = 'sim-posted').text
            found_job_list = []
            if 'few' in time_posted:
                job_names = job.find('h3', class_ = "joblist-comp-name").text.replace('\n', '').replace("  ", "")
                job_skill = job.find('span', class_ = "srp-skills").text.replace('\n', '').replace("  ", "")
                more_info = job.header.h2.a['href']
                if unfamiliar_skills != []:
                    for unfamiliar_skill in unfamiliar_skills:
                        if unfamiliar_skill not in job_skill:
                            found_job = 1
                        else:
                            found_job = 0
                        found_job_list.append(found_job)
                    if 0 not in found_job_list:
                        
                        f.write(f"Job Name: {job_names} \nSkills Required are: {job_skill} \nMore info: {more_info}\n\n")
                        print(f"Stored in file {index}")
                    
                else:
                    f.write(f"Job Name: {job_names} \nSkills Required are: {job_skill} \nMore info: {more_info}\nStored in file {index}\n\n")
                    print(f"Stored in file {index}")
if __name__ == "__main__":
    index = 0
    while True:
        find_jobs(index)
        index += 1
        time_wait = 10
        print(f"Waiting for {time_wait} minutes")
        time.sleep(time_wait*60)
        