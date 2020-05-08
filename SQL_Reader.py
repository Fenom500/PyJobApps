import Data_Scraper.DataHandling as DataHandling

Search_term = "Python Automation"
Location = "Hayward"

db = DataHandling.Database(Search_term,Location)

all_data = db.read_all()

for item in all_data:
    print(item)