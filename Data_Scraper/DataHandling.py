import sqlite3


class Database:

    def __init__(self, search_term, location):
        self.conn = sqlite3.connect("Data_Scraper\\PostingsData.db")
        self.c = self.conn.cursor()
        self.table_name = self.get_table_name(search_term, location)

    def get_table_name(self, search_term, location):
        search_term = search_term.replace(" ", "")
        location = location.replace(" ", "")
        return search_term + location

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS {} (SearchTerm TEXT, Location TEXT, Title TEXT, Company TEXT, Post_text TEXT)""".format(self.table_name))

    def write_to_table(self, table_name, SearchTerm, Location, Title, Company, job_text):
        self.c.execute("""INSERT INTO {} VALUES( "{}", "{}", "{}", "{}", "{}")""".format(table_name, SearchTerm, Location, Title, Company, job_text))
        self.conn.commit()
        print("Information on Post Saved")

    def read_all(self):
        data = self.c.execute("""SELECT * FROM {}""".format(self.table_name))
        self.conn.commit()
        return data.fetchall()

    def shutdown(self):
        self.c.close()
        self.conn.close()

search_term = "Hello"
location = "world"


db = Database(search_term, location)
db.create_table()

db.write_to_table(db.table_name, "asdfas", "asdfas", "asdfas", "asdfas", "asdfas")

#
#
# Bot = SearchResultsScraper.ZipRecruiterBot()
#
# Bot.set_search("Entry Level Python Programmer", "Los Angeles,CA")
# Bot.load_all_search_results()
# all_job_postings = Bot.return_all_job_postings()
#
# for link in all_job_postings:
#     job = JobAppScraper.JobPosting(link)
#     print("There is an opening for a {} at company {}".format(job.job_title, job.company))
#
# Bot.shutdown(delay=60)
