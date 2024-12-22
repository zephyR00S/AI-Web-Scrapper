''' step 1 - we will create a very simple streamlit user interface ( python web application)
step 2 - grab data from the website that we want to scrape. For this purpose we will use selenium. It allows us to automate a web browser, so we can atually go to the website and grab the data we want. Once we have the content we can do some filtering on it.
Next we can pass the filtered data into a LLM. Then use that LLM to parse through the data and give us a meaningful output.
'''
import streamlit as st
from scrape import (
    scrape_site,
    extract_body_content,
    cleaned_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Streamlit UI
st.set_page_config(page_title="Web Scraper", layout="wide")
st.title("Web Scraper with Parser")


st.sidebar.header("Input Section")
url = st.sidebar.text_input("Enter URL to Scrape", placeholder="https://example.com")

if st.sidebar.button("Scrape Website"):
    if url:
        with st.spinner("Scraping the website..."):
            try:
                
                dom_content = scrape_site(url)
                body_content = extract_body_content(dom_content)
                cleaned_content = cleaned_content(body_content)

                # Storing the DOM content in Streamlit session state
                st.session_state.dom_content = cleaned_content
                st.sidebar.success("Website scraped successfully!")
            except Exception as e:
                st.sidebar.error(f"Error scraping the website: {e}")

# Display section
if "dom_content" in st.session_state:
    st.subheader("Scraped DOM Content")
    with st.expander("View Raw Content", expanded=False):
        st.text_area("DOM Content", st.session_state.dom_content, height=300)

    st.subheader("Parse Content")
    parse_description = st.text_area(
        "Tell Me What You Want To Know", placeholder="Enter your query here..."
    )

    if st.button("Parse Content"):
        if parse_description:
            with st.spinner("Parsing the content..."):
                try:
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    parsed_result = parse_with_ollama(dom_chunks, parse_description)
                    st.success("Parsing completed!")
                    st.text_area("Parsed Result", parsed_result, height=300)

                    
                    if parsed_result:
                        st.download_button(
                            label="Download Parsed Result",
                            data=parsed_result,
                            file_name="parsed_result.txt",
                            mime="text/plain",
                        )
                except Exception as e:
                    st.error(f"Error parsing the content: {e}")
else:
    # to avoid NameError
    parse_description = None





