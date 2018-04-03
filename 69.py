import requests # => ModuleNotFoundError: No module named 'requests'. Install with `pip install requests`

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])