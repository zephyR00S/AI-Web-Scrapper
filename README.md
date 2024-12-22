# AI-Web-Scraper

## Overview
The **AI-Web-Scraper** is a Streamlit-based application that allows users to scrape content from a web page, extract and clean the content, and query specific information using natural language parsing. This tool is ideal for extracting structured data and insights from unstructured web content.

## Features
- **URL Input:** Enter any valid website URL to scrape.
- **Content Extraction:** Automatically extracts and cleans the main body content of the web page.
- **Natural Language Parsing:** Query specific information using a customizable parser (e.g., Ollama).
- **Dynamic Results Display:** View raw and parsed results in an interactive interface.
- **Download Feature:** Save the parsed results as a text file for future reference.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- The following Python libraries:
  - `streamlit`
  - `requests`
  - `beautifulsoup4`
  - `langchain`
  - `langchain_ollama`
  -  `selenium`
  -  `lxml`
  -  `html5lib`
  -  `python-dotenv`

## Usage

1. **Enter the URL** in the sidebar to scrape a webpage.
2. **Scrape Website:**
   - Click the **Scrape Website** button to fetch and clean the content.
   - View the extracted content in the "Scraped DOM Content" section.
3. **Parse Content:**
   - Enter a query describing what you want to extract.
   - Click **Parse Content** to analyze the content based on your query.
4. **Download Results:**
   - Save the parsed content using the **Download Parsed Result** button.

## File Structure
```
AI-Web-Scrapper/
│
├── main.py                # Main Streamlit app
├── scrape.py              # Scraping logic (functions for fetching and cleaning content)
├── parse.py               # Parsing logic (Ollama integration or custom parser)
├── requirements.txt       # List of required dependencies
└── README.md              # Documentation
```

## Example Workflow
1. **Input URL:**
   ```
   https://example.com
   ```
2. **Parsed Query:**
   ```
   Extract all the headlines on the webpage.
   ```
3. **Result:**
   ```
   Headline 1: ...
   Headline 2: ...
   ```

4. **Download Output:**
   A file named `parsed_result.txt` will contain:
   ```
   Headline 1: ...
   Headline 2: ...
   ```

## Customization
- **Scraping Logic:** Customize the `scrape_site` and `extract_body_content` functions in `scrape.py` to fit your scraping needs.
- **Parser Integration:** Update the `parse_with_ollama` function in `parse.py` to use other natural language models or parsing algorithms.

## Troubleshooting
- **Invalid URL Error:** Ensure the URL is valid and the website is accessible.
- **Parser Error:** Verify your query syntax and adjust parsing logic if needed.
- **Missing Dependencies:** Run `pip install -r requirements.txt` to ensure all dependencies are installed.


## Acknowledgments
- [Streamlit](https://streamlit.io) for the interactive UI.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- [Ollama](https://ollama.ai) for natural language parsing (if applicable).


## Screenshots
![Screenshot (156)](https://github.com/user-attachments/assets/3a0e938f-26fc-46fc-b296-0da6cdd11016)
![Screenshot (157)](https://github.com/user-attachments/assets/2d3f7dc4-701c-49fb-aa84-097d5e761b37)

