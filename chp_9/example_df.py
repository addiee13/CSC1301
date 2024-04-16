import pandas as pd
dataframe = pd.DataFrame(data=[82, 100, 56],
                         columns= ["Test Scores"],
                         index = ["Exam 1","Exam 2", "Exam 3"])
print(dataframe)