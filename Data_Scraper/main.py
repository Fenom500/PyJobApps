import SearchResultsScraper
import JobAppScraper
import sqlite3


Bot = SearchResultsScraper.ZipRecruiterBot()

Bot.set_search("Entry Level Python Programmer", "Los Angeles,CA")
Bot.load_all_search_results()
all_job_postings = Bot.return_all_job_postings()

for link in all_job_postings:
    job = JobAppScraper.JobPosting(link)
    print("There is an opening for a {} at company {}".format(job.job_title, job.company))

Bot.shutdown(delay=60)