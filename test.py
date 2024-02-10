# Run main.py and then run this script.

import requests

id = requests.put("localhost:5000", params={"note": "Test note"})["result"]
assert requests.get("localhost:5000", params={"id": id})["result"]=="Test note"
assert requests.get("localhost:5000", params={"id": "wsufusfhkdsjkjhfk"})["error"]
assert not requests.post("localhost:5000", params={"id": id, "note": "Another test note"})["error"]
assert requests.get("localhost:5000", params={"id": id})["result"]=="Another test note"
assert requests.delete("localhost:5000", params={"id": id})["result"]=="Another test note"
assert requests.delete("localhost:5000", params={"id": "kjzsdjksdf"})["error"]
assert requests.get("localhost:5000", params={"id": id})["error"]
