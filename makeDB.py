import sqlite3
conn = sqlite3.connect("covid19.db")
c = conn.cursor()

#Create Table covid_data
c.execute('''CREATE TABLE covid_data ([id] INTEGER PRIMARY KEY, [Case_Type] TEXT, [Cases] INTEGER, [Difference] INTEGER, [Date] TEXT, [Country_Region] TEXT, [Province_State] TEXT, [Admin2] TEXT, [Combined_Key] TEXT, [FIPS] INTEGER, [Lat] REAL, [Long] REAL, [Prep_Flow_Runtime] TEXT, [Table_Names] TEXT)''')

conn.commit()
