#AI Travel Analyst
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1
print("Data loading")
df = pd.read_csv('flight_pricing_dataset.csv')
df.columns = df.columns.str.strip()  # Remove any leading/trailing whitespace from column names
df.dropna(inplace=True)  # Drop rows with missing values

col1 = 'Total_Price'
col2 = 'Total_Stops'
col3 = 'Weekday'
col4 = 'Duration'
col5 = 'Airline'
col6 = 'Passenger_Count'
col7 = 'Source'
col8 = 'Destination'
col9 = 'Booking_Channel'
col10 = 'Travel_Class'
col11 = 'Season'

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
    if 'season' in col_lower:
        col11 = col
print('Data loaded')


#2

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
df.dropna(subset=['Total_Price'], inplace=True)  # Drop rows where Price is None

def clean_passenger_count(text):
    text = str(text).strip()  # Convert to string and remove whitespace
    if text.isdigit():
        return int(text)  # Return the integer value if it's a digit
    else:
        return None  # Return None for unexpected values

df['Passenger_Count'] = df[col6].apply(clean_passenger_count)  # Apply the cleaning function to the Passenger_Count column
df.fillna({'Passenger_Count': 1}, inplace=True)  # Fill NaN values in Passenger_Count with 1
df['Price']= df['Total_Price'] / df['Passenger_Count']  # Calculate price per passenger
df['Price'] = df['Price'].round(2)  # Round the price to 2 decimal places

def clean_season(text):
    text = str(text).strip().lower()  # Convert to string, remove whitespace, and convert to lowercase
    if 'summer' in text:
        return 'Summer'
    elif 'winter' in text:
        return 'Winter'
    elif 'spring' in text:
        return 'Spring'
    elif 'autumn' in text:
        return 'Autumn'
    elif 'monsoon' in text:
        return 'Monsoon'
    else:
        return None  # Return None for unexpected values
df['Season'] = df[col11].apply(clean_season)  # Apply the cleaning function to the Season column
df.dropna(subset=['Season'], inplace=True)  # Drop rows where Season is None

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
df.dropna(subset=['Total_Stops'], inplace=True)  # Drop rows where Total_Stops is None

def clean_airline(text):
    text = str(text).strip().lower()  # Convert to string and remove whitespace
    if text:
        return text  # Return the airline name if it's not empty
    else:
        return None  # Return None for unexpected values
df['Airline'] = df[col5].apply(clean_airline)  # Apply the cleaning function to the Airline column
df.dropna(subset=['Airline'], inplace=True)  # Drop rows where Airline is None

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
df['Duration'] = df['Duration'].round(2)  # Round the Duration to 2 decimal places
df.dropna(subset=['Duration'], inplace=True)  # Drop rows where Duration is None


df['Weekday'] = df[col3].str.strip()  # Convert to string, remove whitespace, and convert to lowercase
df.dropna(subset=['Weekday'], inplace=True)  # Drop rows where Weekday is None

df['Day_Name'] = df['Weekday']

def check_weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return 'Weekend'
    else:
        return 'Weekday'
        
df['Is_Weekend'] = df['Day_Name'].apply(check_weekend)
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
df.dropna(subset=['Travel_Class'], inplace=True)  # Drop rows where Travel_Class is None

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
df.dropna(subset=['Booking_Channel'], inplace=True)  # Drop rows where Booking_Channel is None

def clean_airline(text):
    text = str(text).strip()  # Convert to string and remove whitespace
    if text:
        return text  # Return the airline name if it's not empty
    else:
        return None  # Return None for unexpected values
df['Airline'] = df[col5].apply(clean_airline)  # Apply the cleaning function to the Airline column
df.dropna(subset=['Airline'], inplace=True)  # Drop rows where Airline is None

#3

df['Daily_Min_Price'] = df.groupby(['Weekday'])['Price'].transform('min')  # Calculate the daily minimum price for each source-destination pair
df['Daily_Max_Price'] = df.groupby(['Weekday'])['Price'].transform('max')  # Calculate the daily maximum price for each source-destination pair

df['Daily_Min_Time'] = df.groupby(['Weekday'])['Duration'].transform('min')  # Calculate the daily minimum duration for each source-destination pair
df['Daily_Max_Time'] = df.groupby(['Weekday'])['Duration'].transform('max')  # Calculate the daily maximum duration for each source-destination pair

df['Comfort_by_class'] = df['Travel_Class'].map({'Economy': 2, 'Premium Economy': 6, 'Business': 8, 'First Class': 10})  # Assign comfort scores based on travel class

def calculate_value_score(row):
    price_diff = row['Daily_Max_Price'] - row['Daily_Min_Price']
    if price_diff == 0:
        price_penalty = 0
    else:
        price_penalty = (row['Price'] - row['Daily_Min_Price']) / price_diff  # Calculate the price penalty based on the daily min and max prices
    time_diff = row['Daily_Max_Time'] - row['Daily_Min_Time']
    if time_diff == 0:
        time_penalty = 0
    else:
        time_penalty = (row['Duration'] - row['Daily_Min_Time']) / time_diff  # Calculate the time penalty based on the daily min and max durations
    total_penalty = price_penalty + time_penalty  # Calculate the total penalty
    score = 10.0 - (total_penalty * 5.0)  # Calculate the value score
    return round(score, 1)  # Return the final value score


def calculate_comfort_score(row):
    comfort_score = row['Comfort_by_class']  # Get the comfort score based on travel class
    stop_penalty = row['Total_Stops'] * 0.5  # Calculate the stop penalty based on the number of stops
    price_penalty = (row['Price'] - row['Daily_Min_Price']) / (row['Daily_Max_Price'] - row['Daily_Min_Price']) * 2.0 if row['Daily_Max_Price'] != row['Daily_Min_Price'] else 0  # Calculate the price penalty based on the daily min and max prices
    return round(comfort_score - stop_penalty - price_penalty, 1)  # Return the final comfort score

df['Value_Score'] = df.apply(calculate_value_score, axis=1)  # Apply the calculate_value_score function to each row
df['Comfort_Score'] = df.apply(calculate_comfort_score, axis=1)

airline_avg_scores1 = df.groupby('Airline')[['Value_Score']].mean().reset_index()  # Calculate the average Value_Score and Comfort_Score for each airline
airline_avg_scores1['Value_Score'] = airline_avg_scores1['Value_Score'].round(2)  # Round the Value_Score to 2 decimal places
airline_avg_scores2 = df.groupby('Airline')[['Comfort_Score']].mean().reset_index()  # Calculate the average Comfort_Score for each airline
airline_avg_scores2['Comfort_Score'] = airline_avg_scores2['Comfort_Score'].round(2)  # Round the Comfort_Score to 2 decimal places

print("Top 5 Value Flights:")
best_value_flights = df.sort_values(by='Value_Score', ascending=False).head(5)  # Get the top 5 flights based on Value_Score
print(best_value_flights[[col5, 'Source', 'Destination', 'Price', 'Duration', 'Total_Stops', 'Travel_Class', 'Value_Score']])  # Print the relevant columns of the top 5 flights
print("\nTop 5 Comfort Flights:")
best_comfort_flights = df.sort_values(by='Comfort_Score', ascending=False).head(5)  # Get the top 5 flights based on Comfort_Score
print(best_comfort_flights[[col5, 'Source', 'Destination', 'Price', 'Duration', 'Total_Stops', 'Travel_Class', 'Comfort_Score']])  # Print the relevant columns of the top 5 flights

#4
sns.set_theme(style="whitegrid")
plt.figure(figsize=(20, 22))

plt.subplot(4, 2, 1)
sns.histplot(df['Season'], bins=20, color='lightblue')  # Create a histogram for Season
plt.title('Seasonal Distribution of Flights')  # Set the title of the plot
    
plt.subplot(4, 2, 2)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.boxplot(x='Day_Name', y='Price', hue='Day_Name', data=df, order=days, palette="Set2", legend=False, showfliers=False)  # Create a boxplot for Price by Day_Name
plt.title('Price Distribution by Day')  # Set the title of the plot

plt.subplot(4, 2, 3)
sns.barplot(x='Value_Score', y='Airline', data=airline_avg_scores1, palette="Set2")  # Create a bar plot for average Value_Score by Airline
plt.title('Average Value Score by Airline')  # Set the title of the plot

plt.subplot(4, 2, 4)
sns.barplot(x='Comfort_Score', y='Airline', data=airline_avg_scores2, palette="Set2")  # Create a bar plot for average Comfort_Score by Airline
plt.title('Average Comfort Score by Airline')  # Set the title of the plot

plt.subplot(4, 2, 5)
sns.histplot(df['Booking_Channel'], bins=20, color='lightgreen')  # Create a histogram for Booking_Channel
plt.title('Preferred Booking Channel')  # Set the title of the plot

plt.subplot(4, 2, 6)
sns.histplot(df['Travel_Class'], bins=20, color='lightcoral')  # Create a histogram for Travel_Class
plt.title('Preferred Travel Class')  # Set the title of the plot

plt.subplot(4, 2, 7)
sns.boxplot(x='Total_Stops', y='Price', hue='Total_Stops', data=df, palette="Set2", legend=False, showfliers=False)  # Create a boxplot for Price by Total_Stops
plt.title('Price Distribution by Total Stops')  # Set the title of the plot 

plt.subplots_adjust(
    left=0.159, 
    bottom=0.05, 
    right=0.933, 
    top=0.938, 
    wspace=0.289, 
    hspace=0.43
)
plt.show()  # Display all the plots


