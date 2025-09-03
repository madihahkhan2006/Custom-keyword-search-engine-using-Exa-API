from exa_py import Exa

exa = Exa("ad761f57-c25f-4197-88b0-46f180c08c76")

query = input("Search:")

response = exa.search(
    query,
    num_results = 10,
    type = "keyword",
    #include_domains = ["https://www.tiktok.com"],
)

for result in response.results:
    print(f"title: {result.title}")
    print(f"URL: {result.url}")
    print()