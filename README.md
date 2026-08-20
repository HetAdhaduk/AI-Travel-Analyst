**AI-Travel-Analyst** 
**______________________________________________________________________________________________________________________________**
The **AI Travel Analyst** is a tool made with Python. It helps people who travel find the flights. The tool looks at flight data that is not organized. It makes the data clean. It also creates things to help decide. It adds scores for each flight. These scores are for **Value** and **Comfort**. The tool gives advice that people can use. It also makes a dashboard with pictures. This dashboard helps people see how prices change with the seasons, days of the week and airlines.   
**______________________________________________________________________________________________________________________________**

**Problem Statement**  
Travelers often struggle finding the right mix between price, how long the flight takes and how comfortable it is. Flight search engines show a lot of information that can be hard to understand. The prices are different, there are stops and the classes of seats are not always clear. The purpose of this project is to get useful information, from messy flight data and rate the flights in a fair way. This helps people see if a flight is really a deal or if it's a comfortable choice.   
**______________________________________________________________________________________________________________________________**


**Installation Instructions**

1. Prerequisites:   
   Ensure the following are installed:  
* Download and install gitbash  
* Python (3.7+) installed  
* Install the required python dependencies:

  Pandas (gitbash command: pip install pandas )

  Matplotlib (gitbash command: pip install matplotlib )

  Seaborn (gitbash command: pip install seaborn )

  (Or directly install all dependencies by using gitbash command on requirement.txt file in the repository. Command: pip install \-r requirements.txt)

2. Clone the repository:(using gitbash)  
   Using the command  
   git clone  
   [https://github.com/HetAdhaduk/AI-Travel-Analyst.git](https://github.com/HetAdhaduk/AI-Travel-Analyst.git)  
   cd ai-travel-analyst  
3. Ensure the dataset is in the root folder and named ‘flight\_pricing\_dataset.csv’  
4. Run the script:  
   Python \#Ai Travel [Analyst.py](http://Analyst.py)

**______________________________________________________________________________________________________________________________**

**Dataset Used**  
The script expects a CSV file named flight\_pricing\_dataset.csv.  
While the example dataset used to generate output is  
[https://drive.google.com/file/d/1a2bCY33C7cHpVCTVz\_\_5fVobesfFTBKd/view?usp=drivesdk](https://drive.google.com/file/d/1a2bCY33C7cHpVCTVz__5fVobesfFTBKd/view?usp=drivesdk)  
**______________________________________________________________________________________________________________________________**

**Methodology**

1. **Dynamic Data Scanning:** Scans column headers and assigns them to internal variables based on keyword matching   
2. **Data Cleaning:** Cleans, categorizes and standardizes data into specific classes  
3. **Custom Scoring Algorithms:**  
* **Value Score**: Penalizes flights that are significantly more expensive or longer than the daily minimums for that route.  
* **Comfort Score**: Rewards premium cabin classes while penalizing for layovers and unusually high prices.  
4. **Visualization:** Utilizes Matplotlib and Seaborn to generate a 7-panel statistical dashboard.

**______________________________________________________________________________________________________________________________**

**Technologies Used**

* **Python 3**: Core programming language.  
* **Pandas**: For data manipulation, cleaning, and feature engineering.  
* **Matplotlib & Seaborn**: For generating statistical data visualizations.

**______________________________________________________________________________________________________________________________**

**Results**  
Upon execution, the scripts outputs directly to the terminal:

* The **Top 5 Value Flights** (best balance of speed and cost).  
* The **Top 5 Comfort Flights** (best travel experience).  
* Average pricing breakdowns by Travel Class, Stops, Season, and Day of the Week.  
* **Automated Insights & Recommendations:** Text-based tips highlighting the cheapest days to fly, the most expensive seasons, and airline recommendations.

Additionally, it generates a full-screen GUI window containing 7 distinct charts  
**______________________________________________________________________________________________________________________________**


**Challenges Faced**

* **Messy String Data:** Handling inconsistent duration formats (e.g., some missing minutes, some missing hours) required building a robust custom parsing function.  
* **Currency and Data Types:** Cleaning numeric data that included commas and multiple types of currency symbols (₹, Rs) so it could be processed as floats.  
* **Relative Scoring:** Formulating a mathematical score for "Value" required grouping by day and calculating relative penalties (comparing a flight's price/time against the daily minimums and maximums) to ensure the scores were fair across different routes.

**______________________________________________________________________________________________________________________________**

**Future Improvements**

* **API Integration:** Connect to live flight APIs instead of relying on a static CSV file.  
* **Machine Learning:** Implement a regression model (e.g., Random Forest )to predict future flight prices based on historical trends.  
* **Interactive Dashboard:** Migrate the Matplotlib visualizations to an interactive web app, allowing users to filter by their specific source and destination dynamically.

**\______________________________________________________________________________________________________________________________**

**Output Screenshots**  
Top 5 value flights:  
<img width="1126" height="204" alt="image" src="https://github.com/user-attachments/assets/66c34619-7adb-41e0-9f77-335f3b596ef6" />


Top 5 comfort flights:  
<img width="1234" height="184" alt="image" src="https://github.com/user-attachments/assets/6b3b86d3-2066-4d35-b011-4e99c3a5b5a8" />


Factor Affecting Flight Prices:  
<img width="1230" height="786" alt="image" src="https://github.com/user-attachments/assets/8d4b58f8-4620-47cf-817d-c727e14b65e7" />


Insights and Recommendations:  
<img width="1212" height="416" alt="image" src="https://github.com/user-attachments/assets/7dceb652-e456-4744-abc9-047a2629a33b" />


7 Statistical plots:  
<img width="2558" height="1524" alt="image" src="https://github.com/user-attachments/assets/36a227b7-891f-4786-86a3-330b149ac42a" />
  
**\______________________________________________________________________________________________________________________________**

**Demo Video**
https://drive.google.com/file/d/19HFycBlsWXQNzpVPjeCDS-B0QPy11HLF/view?usp=drivesdk