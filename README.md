# Job Search Web Scraper

This Python script is a web scraper that allows you to search for job postings on TimesJobs based on keywords and save the results in an Excel file. It utilizes the BeautifulSoup library to extract job information from the website.

## Requirements
- Python 3.x
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Pandas (`pip install pandas`)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script by executing the following command:
   ```
   python job_search_scraper.py
   ```

4. The script will prompt you to enter keywords for the job search. Please separate each keyword with a comma. For example: `python,java,web development`

5. The script will start scraping job postings from TimesJobs for the provided keywords. It will display the number of jobs scraped as it progresses.

6. Once the scraping is complete, the script will save the job data in an Excel file named `jobs.xlsx` in the project directory.

7. You can open the `jobs.xlsx` file to view the job listings, including the position, company, location, required skills, and a link to the job posting.

## Important Notes

- Please be considerate when scraping websites. Frequent and aggressive scraping may put strain on the website's server. Make sure to review the website's terms of service and robots.txt file to ensure compliance with their policies.

- This script is specifically designed for TimesJobs and may require modification if you intend to use it with other job search websites.

- The script uses basic error handling but may require further enhancements for robustness and reliability in a production environment.

- Make sure you have the required Python packages installed before running the script.

## Disclaimer

This script is provided for educational purposes and personal use. Be mindful of the legality and ethical considerations when scraping websites, and always respect the terms of service of the website you are scraping.
