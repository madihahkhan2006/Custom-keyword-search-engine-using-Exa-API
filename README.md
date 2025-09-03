Keyword Search Engine using Exa API

This project demonstrates how to perform keyword-based searches using the Exa API in Python. The script allows users to input any search term, fetches the top 10 relevant results from specified domains, and displays their titles and URLs in a clean format.

Features:
- Interactive Search: Prompt-based search input from the user.
- Exa API Integration: Uses Exa’s powerful search engine for keyword-based retrieval.
- Domain Filtering: Optionally limits search results to specific domains.
- Clean Output: Displays the title and URL of each result clearly.
- 
Output Example:
When prompted with a keyword like AI tools, the output might look like:
Search: AI tools
title: The Top 5 AI Tools You Should Know
URL: https://example.com/top-5-ai-tools

title: How AI is Changing the Tech Industry
URL: https://techblog.org/ai-changing-industry


Libraries Used:
- exa_py – Python client for the Exa API

API Key used through Exa

Customization:
You can adjust the search behavior by modifying these parameters:
- num_results = 10  # Number of results to return
- type = "keyword"  # Search type: 'keyword' or 'semantic'
- include_domains = ["https://www.example.com"]  # (Optional) Limit results to certain domains
- To remove the domain filter entirely, simply omit or comment out the include_domains parameter.
  
Contact:
For questions or suggestions, feel free to open an issue or contribute a pull request to improve this script.
