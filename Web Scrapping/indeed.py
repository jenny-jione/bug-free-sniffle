import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)
    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)
    links = pagination.find_all('a')
    # print(links)
    pages = []
    for link in links[:-1]:
        # pages.append(link.find("span").string)
        pages.append(int(link.string))
    # print(pages[-1])  # 가장 마지막 숫자(페이지)
    max_page = pages[-1]
    return max_page


def extract_job(html):

    jobTitle = html.find("h2", {"class": "jobTitle"})
    title = jobTitle.find("span").string

    if title == "new":
        title = jobTitle.find_all("span")[1].string

    company = html.find("span", {"class": "companyName"})
    company_anchor = company.find("a")

    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string

    location = html.find("div", {"class": "companyLocation"}).string
    job_id = html["data-jk"]

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class": "fs-unmask"})

    for result in results:
        job = extract_job(result)
        jobs.append(job)
  return jobs


 def get_jobs():
     last_page = get_last_page()
     indeed_jobs = extract_jobs(last_page)
     return indeed_jobs
