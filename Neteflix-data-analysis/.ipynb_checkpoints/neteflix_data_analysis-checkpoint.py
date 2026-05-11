# import important libraries

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv", encoding="latin1")
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df = df.dropna(subset=['date_added'])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df = df.dropna(subset=['duration'])

# movies vs tv shows ka bar chart
type_counts = df['type'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Numbers of Movies vs Tvshows on Neteflix')
plt.xlabel('Type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('movies_VS_tvshows.png')

# content rating destributed
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,5))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%',startangle=90)
plt.title('Percentage of content Rating')
plt.tight_layout()
plt.legend()
plt.savefig('content_rating.png')
plt.show()

# movies duration distributed 
movie_df = df[df['type']=='Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize = (13, 10))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Distributation of Movie Duration')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movies_duration.png')
plt.show()

# release year vs number of shows (scatter plot)
release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.scatter(release_count.index, release_count.values, color='red')
plt.title('Release Year vs number of shows')
plt.xlabel('Release Year')
plt.ylabel('Number of shows')
plt.tight_layout()
plt.savefig('releaseYear_vs_Scatter.png')
plt.show()

# top 10 country jisne sabse jyada content diye hai
country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title('Top 10 Countris by number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_counties.png')
plt.show()

# subplots(movies vs tvshow per year)
countent_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# first subplot: movies
ax[0].plot(countent_by_year.index, countent_by_year['Movie'], color = 'blue')
ax[0].set_title('Movies Released per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# second subplot: tv shows
ax[0].plot(countent_by_year.index, countent_by_year['TV Show'], color = 'orange')
ax[0].set_title('TV Shows Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows Released Over Years')

plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')
plt.show()
