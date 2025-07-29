from geopy.geocoders import Nominatim
import time
import pandas as pd

def store_latitudes_longitudes():
    df = pd.read_csv("data_with_clusters.csv")
    df = pd.DataFrame({
        "location": ['Agripada', 'Andheri East', 'Andheri West', 'Bandra East', 'Bandra West', 'Bhandup East', 'Bhandup West', 'Bhayandar East', 'Bhayandar West', 'Boisar', 'Borivali East', 'Borivali West', 'Byculla', 'Chembur', 'Churchgate', 'Colaba', 'Cuffe Parade', 'Cumballa Hill', 'Dadar East', 'Dadar West', 'Dahisar East', 'Dahisar West', 'Ghatkopar East', 'Ghatkopar West', 'Girgaon', 'Goregaon East', 'Goregaon West', 'Govandi', 'Jogeshwari East', 'Jogeshwari West', 'Kamathipura', 'Kandivali East', 'Kandivali West', 'Kanjurmarg East', 'Kanjurmarg West', 'Khar West', 'Kurla East', 'Kurla West', 'Lower Parel', 'Madanpura', 'Madh', 'Mahalakshmi', 'Mahim', 'Malabar Hill', 'Malad East', 'Malad West', 'Marine Lines', 'Matunga East', 'Matunga West', 'Mazgaon', 'Mira Road East', 'Mulund East', 'Mulund West', 'Mumbai Central', 'Naigaon East', 'Nalasopara East', 'Nalasopara West', 'Palghar', 'Parel', 'Powai', 'Prabhadevi', 'Sakinaka', 'Santacruz East', 'Santacruz West', 'Sewri', 'Sion', 'Tardeo', 'Thane West', 'Vasai East', 'Vasai West', 'Vikhroli East', 'Vikhroli West', 'Vile Parle East', 'Vile Parle West', 'Virar East', 'Virar West', 'Wadala', 'Wadala East', 'Worli', 'others']
    })

    geolocator = Nominatim(user_agent="cluster_mapper")
    def geocode_location(location):
        try:
            loc = geolocator.geocode(location)
            print(f"Geocoding {location}: {loc.latitude}, {loc.longitude}")
            if loc:
                return pd.Series([loc.latitude, loc.longitude])
        except:
            return pd.Series([None, None])

    df[['latitude', 'longitude']] = df['location'].apply(geocode_location)
    df.to_csv("locations_with_latitudes_longitudes.csv", index=False)
    time.sleep(1)


df = pd.read_csv("locations_with_latitudes_longitudes.csv")
dict = {}
for index, row in df.iterrows():
    location = row['location']
    latitude = row['latitude']
    longitude = row['longitude']
    dict[location] = {'latitude': latitude, 'longitude': longitude}

print(dict)

df = pd.read_csv("data_with_clusters.csv")
df['latitude'] = df['location1'].map(lambda x: dict[x]['latitude'] if x in dict else None)
df['longitude'] = df['location1'].map(lambda x: dict[x]['longitude']if x in dict else None)
print(df[['location1', 'latitude', 'longitude']].head())
df.to_csv("data_with_latitudes_longitudes.csv", index=False)