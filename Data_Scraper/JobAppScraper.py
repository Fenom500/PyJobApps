import bs4 as bs
import urllib.request


class Job_Posting:

    def __init__(self, link):
        # opens web page of Job_posting Link
        self.req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        self.source = urllib.request.urlopen(self.req).read()
        self.soup = bs.BeautifulSoup(self.source, features="html.parser")
        self.job_text = self.soup.find("div", class_="jobDescriptionSection").text
        self.company = self.soup.find("span", class_="hiring_company_text t_company_name").text



sample_job_1 = "https://www.ziprecruiter.com/jobs/vector-atomic-63c83f51/embedded-programmer-entry-level-7dc73e97?job_id=0655f0a8b0ae0725fc4e5e4553a3201b"

sample = Job_Posting(sample_job_1)

print(sample.company)
