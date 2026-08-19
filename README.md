✈️ AI Travel Analyst: Flight Price Data Science Project
📌 Project Overview
The AI Travel Analyst is a data-driven Python solution designed to analyze flight pricing data, uncover the hidden factors that drive costs, and help travelers make smarter booking decisions. It goes beyond finding the "cheapest" flight by introducing a custom 1-10 Value Score that mathematically balances ticket price with travel time and layovers, recommending the genuinely best flights available.

🎯 Problem Statement
Travelers often struggle to find the best flight because booking platforms prioritize either the cheapest flight (which may have a grueling 15-hour layover) or the fastest flight (which is often exorbitantly expensive). Furthermore, rumors about "cheaper weekday flights" and "holiday price spikes" confuse consumers. This project aims to cut through the noise by mathematically scoring flights and visually proving how time, day, and layovers actually impact ticket prices.

💻 Installation Instructions
To run this project on your local machine, follow these steps:

Install Python: Ensure Python 3.7 or newer is installed on your system.

Clone/Download the Project: Place the Python script and your dataset in the same folder.

Install Required Libraries: Open your terminal or command prompt and run the following command:

Bash
pip install pandas matplotlib seaborn
Run the Code: Open the script in any Python IDE (like VS Code, PyCharm) or a Jupyter Notebook, ensure the dataset file path is correct, and run the file.

(Note: You can also run this entirely in your browser without installation using Google Colab!)

📊 Dataset Used
The project utilizes a flight pricing dataset containing historical travel data. Key features of the dataset include:

Airline: The carrier operating the flight.

Source & Destination: Departure and arrival cities.

Date of Journey: Used to extract days of the week, weekends, and peak travel days.

Duration: Total time taken for the flight.

Total Stops: Number of layovers.

Price: The cost of the ticket (can be analyzed as total cost or calculated as Price Per Person).

🔬 Methodology
This project follows a standard Data Science pipeline:

Data Cleaning: Handled missing values, removed currency symbols and commas from prices, and converted messy text data (like "2h 50m" or "non-stop") into usable math numbers using custom Python functions.

Feature Engineering:

Extracted the Day of the Week and identified Weekends.

Dynamically calculated the top 5 most expensive travel dates to flag "Peak Travel Days."

Engineered a Value Score (1-10) that normalizes the cheapest and fastest flights for every specific date.

Exploratory Data Analysis (EDA): Grouped and sorted data to find the absolute best-value flights in the dataset.

Data Visualization: Utilized Seaborn to create Boxplots, Histograms, and Bar charts to visually compare pricing distributions.

🛠️ Technologies Used
Python: The core programming language.

Pandas: For data manipulation, cleaning, and mathematical aggregations.

Matplotlib: For structuring the layout and grids of the visual dashboard.

Seaborn: For generating beautiful, statistical visualizations (Boxplots, Barplots, Histograms).

📈 Results & Key Insights
The 1-10 Value Score Works: By mathematically punishing long layovers and high costs, the tool successfully isolates "unicorn" flights that offer excellent speed for a low price, rather than just returning cheap, low-quality flights.

The Weekend Myth: Visualizing the data via Boxplots revealed exactly how the median ticket prices fluctuate between weekdays and weekends.

Holiday/Peak Spikes: The charts clearly demonstrate a massive explosion in extreme price outliers (highly expensive tickets) during peak travel days compared to normal days.

Airline Value: Grouping the Value Score by airline highlights which carriers consistently provide the best balance of time and money.

🚧 Challenges Faced
Messy Text Data: The dataset contained highly inconsistent formatting (e.g., stops written as words like "one" vs. numbers like "1", and durations formatted in multiple different ways). This required building robust custom cleaning functions.

String Math Errors: Prices contained commas and currency symbols, which caused Python to treat them as text, crashing the math functions. This was solved by aggressively stripping non-numeric characters before conversion.

Visualizing Outliers: Initial bar charts failed to show the true comparison of prices, and standard box plots were squished by extreme VIP ticket outliers. This was resolved by hiding extreme outliers (showfliers=False) to focus on the behavior of average prices.

🚀 Future Improvements
Interactive Dashboard: Upgrade the project using Streamlit to create a clickable web app where users can filter by their desired Source and Destination cities.

Machine Learning Predictor: Implement scikit-learn to train a Random Forest model capable of predicting future flight prices based on the user's input.

Live API Integration: Connect to a live flight API (like Amadeus or Skyscanner) to run the 1-10 Value Score engine on real-time flights instead of historical data.
