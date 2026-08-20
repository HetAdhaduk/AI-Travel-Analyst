**Technical Documentation: AI Travel Agent**
**______________________________________________________________________________________________________________________________**
**______________________________________________________________________________________________________________________________**

1. **System Architecture:**  
   The script operates in a linear algorithm:  
* **Dynamic scanning:** Reads the CSV and uses string-matching search to identify columns regardless of exact naming conventions.  
* **Data Cleaning:** Normalizes and standardizes strings, handles missing data, and converts pricing/time into manageable formats.  
* **Feature Making:** Calculates per-passenger pricing and derives daily minimums/maximums for relative comparisons.  
* **Scoring System:** Applies specific functions to assign flights a 1-10 score for Value and Comfort.  
* **Visualization Generation:** Compiles processed data into panel Matplotlib/Seaborn dashboard.  
**______________________________________________________________________________________________________________________________**
**______________________________________________________________________________________________________________________________**

2. **Data Dictionary (Engineered Features):**  
   While the script ingests standard flight data, these features create several new columns during executions.  
   Here are the key engineered features:  
   

| Feature | Data Type | Description |
| :---- | :---- | :---- |
| Price | Float | The true cost per passenger (Total price / passenger count) |
| Duration | Integer | Total flight time converted entirely into minutes. |
| Daily\_Min\_Price/Daily\_Max\_Price | Float | The absolute lowest and highest prices recorded for that specific day of the week |
| Daily\_Min\_Time/ Daily\_Max\_Time | Integer | The shortest and longest flight durations recorded for that day of the week. |
| Value\_Score | Float | A 0-10 score evaluating cost-effectiveness and time-efficiency |
| Comfort\_Score | Float | A 0-10 score evaluating travel class, penalizing layovers and high prices. |


**______________________________________________________________________________________________________________________________**
**______________________________________________________________________________________________________________________________**

3. **Function definition and methods**  
   **Cleaning functions**  
   These functions handle raw inputs from the dataset and standardize them.  
* *clean\_price(text)*

  **Purpose:** Removes currency symbols, commas and assign inputs as floats. And returns None if cleaning fails.

*  *clean\_passenger\_count(text)*

  **Purpose:** ensures the passenger count is integer. And assigns 1 to empty fields.

* *clean\_duration(text)*

  **Purpose:** extracts hours and minutes from varying formats and returns the total flight time in minutes.

* *clean\_stops(text)*

  **Purpose:** Converts representations of layovers into an integer value.

* *clean\_travel\_class(text),clean\_season(text),clean\_booking\_channel(text)*

  **Purpose:** function that transforms raw data into clean, uniform categories.

**______________________________________________________________________________________________________________________________**

  **Scoring Algorithms**

  These functions apply the basic logic to rank the flights.

* *calculate\_value\_score(row)*

  **Purpose:** calculates a flights “Value” based on how close its price and duration are to the absolute minimums for that day.

  **Logic:** starts with a perfect score of 10\. Applies penalties based on a normalized scale (0 to 1\) for how far the price and duration deviate from daily minimum.

* *calculate\_comfort\_score(row)*

  **Purpose:** calculates a flights “Comfort” level based on cabin class and layovers.

  **Logic:** assigns a base score based on the cabin class (Economy=2, First Class=10). Deducts 0.5 points for every layover. Applies a slight penalty for high pricing to balance the score.
**______________________________________________________________________________________________________________________________**
**______________________________________________________________________________________________________________________________**

4. **Environment & Execution Notes**  
* **Missing Data Handling:** The script uses *df.dropna()* after applying cleaning functions. If a row contains malformed or empty data, the entire row is dropped to preserve the integrity of the analysis.


  