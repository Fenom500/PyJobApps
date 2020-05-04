from bs4 import BeautifulSoup as bs
import urllib.request

class Job_Posting():

    def __init__(self,link):
        # opens webpage of Job_posting Link
        self.req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        self.source = urllib.request.urlopen(self.req)



sample_job_1 = "https://www.ziprecruiter.com/jobs/vector-atomic-63c83f51/embedded-programmer-entry-level-7dc73e97?job_id=0655f0a8b0ae0725fc4e5e4553a3201b"

sample = Job_Posting(sample_job_1)