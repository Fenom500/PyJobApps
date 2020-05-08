import JobAppScraper
import SearchResultsScraper
import DataHandling


Bot = SearchResultsScraper.ZipRecruiterBot()

Search_terms = ["Python Automation"]
Locations = ["Hayward", "San Francisco"]


for term in Search_terms:
    for location in Locations:
        # SQL Initialization Code
        db = DataHandling.Database(term, location)
        db.create_table()
        Bot.set_search(term, location)
        Bot.load_all_search_results()
        all_job_postings = Bot.return_all_job_postings()

        for link in all_job_postings:
            try:
                job = JobAppScraper.JobPosting(link)
                table_name = db.table_name
                current_search_term = term
                current_location = location
                current_title = job.job_title
                current_company = job.company
                current_job_text = job.job_text
                db.write_to_table(table_name, current_search_term, current_location, current_title, current_company, current_job_text)
                print("There is an opening for a {} at company {}".format(job.job_title, job.company))
            except Exception:
                print("Something went wrong")


Bot.shutdown(delay=60)
