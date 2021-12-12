#%% Dependencies
import requests
import pandas as pd
import time

key = '9McAdKBbyHc2bE3auHhyK7jzlBaifReb'
secret = 'T6HzmTfKxoRLAm12'
query = 'climate change'

data = []
for page in range(100): #Search returns 100 results

    print( page )
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&page={page}&api-key={key}'.format(
        key = key,
        query = query,
        page = page
    )

    resp = requests.get( url )
    try:
        arts = resp.json()['response']

        for art in arts['docs']:
            abstract = art['abstract']
            web_url = art['web_url']
            snip =  art['snippet']
            lead = art['lead_paragraph']
            headline = art['headline']['main']
            keywords = art['keywords']
            date = art['pub_date']
            
            tags = []
            location = None
            for k in keywords:
                if k['name'] == 'glocations':
                    location = k['value']
                if k['name'] == 'subject':
                    tags.append( k['value'] )
            if len(tags) > 0:
                tags = ', '.join(tags)
            
            data.append( [ date, abstract, web_url, snip, lead, headline, location, tags ] )
    except:
        continue
    time.sleep( 0.5 )
            
df = pd.DataFrame( data = data , columns = ['date','abstract', 'web_url', 'snip', 'lead', 'headline', 'location', 'tags'] )
df['date'] = pd.to_datetime( df['date'] )
df
    
#%% Convert Locations

import geocoder

gdf = df[~df['location'].isnull()]

def get_xy(dic):
    return dic['lat'],dic['lng']

gdf['loc'] = [ get_xy( geocoder.arcgis(r).json )  for i,r in gdf['location'].iteritems() ]

gdf['lat'] = [r[0]  for i,r in gdf['loc'].iteritems() ]
gdf['lon'] = [r[1]  for i,r in gdf['loc'].iteritems() ]

gdf.head()

#%% Export

df.to_json( r'C:\Users\cansu\Desktop\t\NYT_Climate.json')