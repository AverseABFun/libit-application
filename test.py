# Run main.py and then run this script.

import requests

id = requests.put("http://localhost:5000", params={"note": "Test note"}).json()["result"]
assert requests.get("http://localhost:5000", params={"id": id}).json()["result"]=="Test note"
assert requests.get("http://localhost:5000", params={"id": "wsufusfhkdsjkjhfk"}).json()["error"]
assert not requests.post("http://localhost:5000", params={"id": id, "note": "Another test note"}).json()["error"]
assert requests.get("http://localhost:5000", params={"id": id}).json()["result"]=="Another test note"
assert requests.delete("http://localhost:5000", params={"id": id}).json()["result"]=="Another test note"
assert requests.delete("http://localhost:5000", params={"id": "kjzsdjksdf"}).json()["error"]
assert requests.get("http://localhost:5000", params={"id": id}).json()["error"]
