# БИБЛИОТЕКА REQUESTS
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    posts = response.json()
    for post in posts[:3]:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")



# БИБЛИОТЕКА PANDAS
import pandas as pd

df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv')

print("First 5 rows of the dataframe:")
print(df.head())

print("\nData description:")
print(df.describe())

print("\nAverage height by age:")
print(df.groupby('age')['height'].mean())




# БИБЛИОТЕКА MATPLOTLIB
import matplotlib.pyplot as plt

ages = df['age']
heights = df['height']

plt.scatter(ages, heights, alpha=0.5)
plt.title('Height vs Age')
plt.xlabel('Age')
plt.ylabel('Height')
plt.show()

plt.hist(heights, bins=20, alpha=0.7, color='blue')
plt.title('Distribution of Heights')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()
