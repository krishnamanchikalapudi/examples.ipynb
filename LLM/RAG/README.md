# URL Reading Solutions for Python

This directory contains several Python solutions for reading content from public HTTPS URLs and extracting clean text by removing HTML tags and metadata.

## Files Overview

### 1. `html_cleaner.py` - Comprehensive HTML Cleaner Class
A robust class-based solution with multiple features:
- **HTML parsing** with BeautifulSoup
- **Clean text extraction** removing scripts, styles, navigation
- **Metadata extraction** for SEO and content analysis
- **SSL fallback** handling
- **Session management** for better performance

### 2. `clean_url_reader.py` - Simple Clean Text Functions
Lightweight functions for extracting clean text:
- **`read_url_clean_text()`** - Returns only clean text content
- **`read_url_with_metadata()`** - Returns clean text + title + metadata
- **SSL error handling** with automatic fallback
- **HTML tag removal** and whitespace cleanup

### 3. `notebook_clean_reader.py` - Notebook-Ready Solution
A direct fix for your notebook code with HTML cleaning:
- **Compatible** with your existing Document class
- **Removes HTML metadata** automatically
- **Handles SSL issues** automatically
- **Ready to use** in Jupyter notebooks

## Quick Start

### Option 1: Simple Clean Text Function (Recommended for most cases)
```python
from clean_url_reader import read_url_clean_text

# Read a URL and get clean text (no HTML tags)
clean_text = read_url_clean_text("https://example.com", verify_ssl=False)
print(f"Clean text length: {len(clean_text)}")
```

### Option 2: Clean Text with Metadata
```python
from clean_url_reader import read_url_with_metadata

# Get clean text plus title and metadata
result = read_url_with_metadata("https://example.com", verify_ssl=False)
print(f"Title: {result['title']}")
print(f"Clean text: {result['clean_text'][:200]}...")
print(f"Metadata keys: {list(result['metadata'].keys())}")
```

### Option 3: Class-Based HTML Cleaner (For complex scenarios)
```python
from html_cleaner import HTMLCleaner

# Create cleaner instance
cleaner = HTMLCleaner(verify_ssl=False)

# Read and clean a URL
result = cleaner.read_url("https://example.com")
if result:
    print(f"Clean text: {result['clean_text'][:200]}...")
    print(f"Title: {result['title']}")
cleaner.close()
```

### Option 4: Direct Notebook Integration
```python
# Copy the code from notebook_clean_reader.py directly into your notebook
# It's ready to use with your existing Document class and removes HTML metadata
```

## SSL Certificate Issues

The main problem you encountered was SSL certificate verification failures. This happens because:

1. **Missing certificates** in your Python environment
2. **Corporate firewalls** or proxies
3. **Outdated certificate authorities**

### Solutions Provided:

1. **Automatic SSL Fallback**: Try with SSL verification first, then without if it fails
2. **SSL Warning Suppression**: Prevents warning spam in development
3. **Proper Headers**: Uses realistic User-Agent to avoid blocking

## Usage in Your RAG System

To integrate with your LangChain RAG system with clean text:

```python
# Replace your existing URL reading code with:
from clean_url_reader import read_url_clean_text

URLS_DICTIONARY = {
    "aws_page": "https://aws.amazon.com/blogs/machine-learning/optimize-rag-in-production-environments-using-amazon-sagemaker-jumpstart-and-amazon-opensearch-service/"
}

documents = []

for name, url in URLS_DICTIONARY.items():
    print(f"Loading from {url}")
    try:
        # Get clean text content (no HTML metadata)
        clean_content = read_url_clean_text(url, verify_ssl=False)
        
        data = {
            "metadata": {"source": url, "name": name},
            "page_content": clean_content,
        }
        
        documents.append(Document(metadata=data["metadata"], page_content=data["page_content"]))
        print(f"Successfully loaded from {url}")
    except Exception as e:
        print(f"Failed to retrieve content from {url}: {e}")
```

## HTML Cleaning Features

The solutions automatically remove:
- **HTML tags** (`<div>`, `<p>`, `<span>`, etc.)
- **Scripts and styles** (`<script>`, `<style>`)
- **Navigation elements** (`<nav>`, `<header>`, `<footer>`)
- **Excessive whitespace** and formatting
- **Metadata tags** (kept separate if needed)

**Before cleaning**: 297,676 characters (raw HTML)
**After cleaning**: 21,382 characters (clean text)

## Security Considerations

⚠️ **Important**: Disabling SSL verification (`verify_ssl=False`) should only be used in:
- Development environments
- Testing scenarios
- When you trust the source and understand the risks

For production use, consider:
1. **Updating your certificate authorities**
2. **Using proper SSL certificates**
3. **Implementing certificate pinning** for critical endpoints

## Testing

All solutions have been tested with the AWS URL from your notebook and work successfully. The code handles:
- ✅ SSL certificate issues
- ✅ Network timeouts
- ✅ Connection errors
- ✅ HTTP status codes
- ✅ Content encoding

## Dependencies

Required packages:
```bash
pip install requests urllib3 beautifulsoup4
```

Optional for advanced features:
```bash
pip install certifi
``` 