#AI Travel Analyst
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Part 1 loading the data
print("Data loading")
df = pd.read_csv('flight_pricing_dataset.csv')
df.columns = df.columns.str.strip()  # Remove any leading/trailing whitespace from column names
df.dropna(inplace=True)  # Drop rows with missing values

col1 = 'Total_Price'
col2 = 'Total_Stops'
col3 = 'Journey_Day'
col4 = 'Duration'
col5 = 'Airline'
col6 = 'Passenger_Count'
col7 = 'Source'
col8 = 'Destination'
col9 = 'Booking_Channel'
col10 = 'Travel_Class'

for col in df.columns:   #to go through all the names in a columns
    col_lower = col.lower()  # Convert column name to lowercase
    if 'price' in col_lower or 'fare' in col_lower:
        col1 = col
    if 'stop' in col_lower:
        col2 = col
    if 'day' in col_lower:
        col3 = col
    if 'duration' in col_lower or 'time' in col_lower:
        col4 = col
    if 'airline' in col_lower or 'carrier' in col_lower:
        col5 = col
    if 'passenger count' in col_lower or 'pax' in col_lower or 'count' in col_lower or 'traveler' in col_lower or 'traveller' in col_lower:
        col6 = col
    if 'source' in col_lower:
        col7 = col
    if 'destination' in col_lower:
        col8 = col
    if 'booking' in col_lower or 'channel' in col_lower or 'platform' in col_lower or 'booking channel' in col_lower:
        col9 = col
    if 'travel class' in col_lower or 'cabin' in col_lower:
        col10 = col

print('Data loaded')


#Part 2: Data cleaning

#Cleaning Price
def clean_price(text):
    text = str(text)
    text = text.replace(',', '')  # Remove commas
    text = text.replace('₹', '')  # Remove rupee signs
    text = text.replace('Rs', '')  # Remove rupee abbreviation
    text = text.strip()  # Remove leading/trailing whitespace

    try:
        return float(text) # Convert it to decimal number
    except:
        return None  # Return None if conversion fails

df['Total_Price'] = df[col1].apply(clean_price) # Apply the cleaning function to the Price column
df = df.dropna(subset=['Total_Price'], inplace=True)  # Drop rows where Price is None

def clean_passenger_count(text):
    text = str(text).strip()  # Convert to string and remove whitespace
    if text.isdigit():
        return int(text)  # Return the integer value if it's a digit
    else:
        return None  # Return None for unexpected values

df['Passenger_Count'] = df[col6].apply(clean_passenger_count)  # Apply the cleaning function to the Passenger_Count column
df.fillna({'Passenger_Count': 1}, inplace=True)  # Fill NaN values in Passenger_Count with 1
df['Price']= df['Total_Price'] / df['Passenger_Count']  # Calculate price per passenger


def clean_stops(text):
    text = str(text).strip()  # Convert to string and remove whitespace
    if "non-stop" in text or "direct" in text or "zero" in text or "0" in text:
        return 0
    elif '1' in text or 'one' in text or 'one stop' in text:
        return 1
    elif '2' in text or 'two' in text or 'two stops' in text:
        return 2
    elif '3' in text or 'three' in text or 'three stops' in text:
        return 3
    elif '4' in text or 'four' in text or 'four stops' in text:
        return 4
    else:
        return None  # Return None for unexpected values

df['Total_Stops'] = df[col2].apply(clean_stops)  # Apply the cleaning function to the Total_Stops column
df = df.dropna(subset=['Total_Stops'], inplace=True)  # Drop rows where Total_Stops is None

def clean_duration(text):
    text = str(text).strip()  # Convert to string and remove whitespace
    hours = 0
    minutes = 0

    if 'h' in text or 'hour' in text or 'hours' in text or 'hr' in text or 'hrs' in text:
        hours_part = text.split('h')[0].strip() # Extract the part before 'h' and remove whitespace
        try:
            hours = int(hours_part) # Convert it to an integer
        except ValueError:
            hours = 0

    if 'm' in text or 'min' in text or 'minutes' in text or 'mins' in text or 'minute' in text:
        minutes_part = text.split('h')[-1].split('m')[0].strip() # Extract the part after 'h' and before 'm', then remove whitespace
        try:
            minutes = int(minutes_part) 
        except ValueError:
            minutes = 0

    total_minutes = hours * 60 + minutes
    return total_minutes if total_minutes > 0 else None  # Return None for unexpected values

df['Duration'] = df[col4].apply(clean_duration)  # Apply the cleaning function to the Duration column
df = df.dropna(subset=['Duration'], inplace=True)  # Drop rows where Duration is None


df['Journey_Day'] = pd.to_datetime(df[col3], errors='coerce').dt.day  # Convert Journey_Day to datetime and extract the day
df = df.dropna(subset=['Journey_Day'], inplace=True)  # Drop rows where Journey_Day is NaN

df['Day'] = df['Journey_Day'].dt.day_name() # Extract the day from Journey_Day

def check_day(day):
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        return 'Weekday'
    elif day in ['Saturday', 'Sunday']:
        return 'Weekend'
    else:
        return None  # Return None for unexpected values
df['Day_Type'] = df['Day'].apply(check_day)  # Apply the check_day function to the Day column

def clean_travel_class(text):
    text = str(text).strip().lower()  # Convert to string, remove whitespace, and convert to lowercase
    if 'economy' in text or 'eco' in text or 'Economy' in text:
        return 'Economy'
    elif 'business' in text or 'biz' in text or 'Business' in text:
        return 'Business'
    elif 'premium economy' in text or 'Premium Economy' in text:
        return 'Premium Economy'
    elif 'first' in text or 'First Class' in text:
        return 'First Class'
    else:
        return None  # Return None for unexpected values
df['Travel_Class'] = df[col10].apply(clean_travel_class)  # Apply the cleaning function to the Travel_Class column
df = df.dropna(subset=['Travel_Class'], inplace=True)  # Drop rows where Travel_Class is None

def clean_booking_channel(text):
    text = str(text).strip().lower()  # Convert to string, remove whitespace, and convert to lowercase
    if 'online' in text or 'Website' in text or 'app' in text or 'mobile' in text or 'internet' in text or 'Mobile App' in text:
        return 'Online'
    elif 'offline' in text or 'agent' in text or 'Travel Agent' in text or 'Airport Counter' in text:
        return 'Offline'
    elif 'Third Party' in text or 'third party' in text:
        return 'Third Party'
    else:
        return None  # Return None for unexpected values
df['Booking_Channel'] = df[col9].apply(clean_booking_channel)  # Apply the cleaning function to the Booking_Channel column
df = df.dropna(subset=['Booking_Channel'], inplace=True)  # Drop rows where Booking_Channel is None

