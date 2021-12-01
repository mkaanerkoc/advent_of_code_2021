import pandas as pd


with open('radar_readings.txt') as readings:
  sonar_readings = readings.readlines()
  sonar_readings = pd.Series([ float(reading) for reading in sonar_readings])
  
  
task1_result, task2_result = (sonar_readings.diff() > 0).sum() , (sonar_readings.rolling(3).sum().diff() > 0).sum()

print(task1_result, task2_result)
