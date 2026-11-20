# ENV secrets
from dotenv import load_dotenv
from os import getenv
from client import HttpClient

# Load environment variables
load_dotenv()

# Collect host and token
host = getenv("BIO")
token = getenv("TOKEN")

print("Environment variables:")
print("HOST", host)
print("TOKEN", token)

# Construct REST client
print("Constructing client...")
client = HttpClient(host, token)
print("Done!")

# Test client
print("Data", client.get_ph())
