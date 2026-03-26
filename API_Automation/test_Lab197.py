import csv
# import pandas as pd #pip install pandas

# pip install pandas
class Test_CRUD(object):
    def test_update_1(self):
        # Read the file
        with open('PythonProject_Automation/API_Automation/userdata.csv') as csvfile:
            reader= csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    # def test_update_2(self):
    #     df = pd.read_csv('PythonProject_Automation/API_Automation/userdata.csv')
    #     print(df)