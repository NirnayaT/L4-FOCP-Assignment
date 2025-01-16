import sys
import requests

if len(sys.argv) > 1:
    try:
        response = requests.get(sys.argv[1])
        print(f"Website is {'up' if response.status_code == 200 else 'down'}")
    except:
        print("Invalid URL or website is down")
else:
    print("Please provide a URL")
