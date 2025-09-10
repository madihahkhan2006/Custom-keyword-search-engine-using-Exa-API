from exa_py import Exa

exa = Exa("")#Input own API key from Exa

#Search query
query = input("Search:")

#Results formatting
response = exa.search(
    query,
    num_results = 10,
    type = "keyword",
    #include_domains = ["https://www.tiktok.com"], this can be added if you want to search from just one domain rather than just the World Wide Web.
)

#Format and display the results
for result in response.results:
    print(f"title: {result.title}")
    print(f"URL: {result.url}")
    print()
