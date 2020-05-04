import bs4 as bs
import urllib.request


class WebPage:

    def __init__(self, target_link):
        self.link = target_link
        self.req = urllib.request.Request(self.link, headers={'User-Agent': 'Mozilla/5.0'})
        self.source = urllib.request.urlopen(self.req).read()
        self.soup = bs.BeautifulSoup(self.source, features="html.parser")


class JobPosting(WebPage):

    def __init__(self, target_link):
        super().__init__(target_link)
        self.job_text = self.soup.find("div", class_="jobDescriptionSection").text
        self.company = self.soup.find("span", class_="hiring_company_text t_company_name").text
        self.job_title = self.soup.find("h1", class_="job_title").text
        self.job_title = self.job_title.strip()

    def print_info(self):
        print("{} is hiring for the position of {}".format(self.company, self.job_title))


class SearchResults(WebPage):

    def __init__(self, target_link):
        super().__init__(target_link)
        pass
    #     self.job_posts = self.soup.find_all("a", class_="job_link t_job_link")
    #     self.post_links = []
    #     self.get_links()
    #
    # def get_links(self):
    #     for post in self.job_posts:
    #         print(post.text)


# sample_job_1 = "https://www.ziprecruiter.com/jobs/vector-atomic-63c83f51/embedded-programmer-entry-level-7dc73e97?job_id=0655f0a8b0ae0725fc4e5e4553a3201b"
# sample = JobPosting(sample_job_1)
# print(sample.job_title)

sample_search_results = "https://www.ziprecruiter.com/search?form=jobs-landing&search=entry+python&location=Hayward%2C+CA"
sample = WebPage(sample_search_results)
print(sample.soup)