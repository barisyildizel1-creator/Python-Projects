import requests
from bs4 import BeautifulSoup
import ollama

def scrape_documentation(url):
    """Scrape all text content from a documentation page"""
    try:
        # Get the webpage
        print(f"Scraping: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get all text from the page (removes HTML tags)
        page_text = soup.get_text()
        
        # Clean up extra whitespace
        clean_text = ' '.join(page_text.split())
        
        return clean_text
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def summarize_with_ai(text, library_name=""):
    """Send text to local AI for summarization"""
    prompt = f"""Analyze this {library_name} documentation and provide information for BUILDING AN APPLICATION that uses this library.

    Focus on:
    - How to import/install the library in Python code
    - Main classes and functions for programmatic use (not CLI commands)
    - Code examples for embedding in applications
    - API methods and their parameters
    - How to integrate into a Python project
    - Error handling and common issues
    - Return values and data structures
    
    IGNORE command-line usage. Focus on PROGRAMMING/API usage only.
    
    Documentation content:
    {text[:8000]}"""  # Limit to 8000 chars to avoid token limits
    
    try:
        response = ollama.generate(model='llama3.2:3b', prompt=prompt)
        return response['response']
    except Exception as e:
        print(f"Error with AI: {e}")
        return None

# Interactive usage - ask user for URL
if __name__ == "__main__":
    print("=== Documentation Summarizer ===")
    print("Enter a documentation URL to scrape and summarize for app development\n")
    
    print("💡 For best results, use URLs with programming documentation:")
    print("   - API docs (readthedocs.io, docs.python.org)")
    print("   - Library docs with code examples")
    print("   - Avoid general README pages\n")
    
    # Get URL from user
    doc_url = input("Enter documentation URL: ").strip()
    
    if not doc_url:
        print("No URL provided. Exiting...")
        exit()
    
    # Ask for library name (optional)
    library_name = input("Enter library name (optional): ").strip()
    
    print(f"\nStarting to scrape: {doc_url}")
    
    # Scrape the documentation
    doc_content = scrape_documentation(doc_url)
    
    if doc_content:
        print(f"✅ Scraped {len(doc_content)} characters")
        print("🤖 Sending to AI for programming-focused analysis...")
        
        # Get AI summary
        summary = summarize_with_ai(doc_content, library_name or "this documentation")
        
        if summary:
            print("\n" + "="*60)
            print("🎯 PROGRAMMING GUIDE:")
            print("="*60)
            print(summary)
            print("="*60)
        else:
            print("❌ Failed to get AI summary")
    else:
        print("❌ Failed to scrape documentation")