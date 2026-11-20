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

# Seal prediction
print("Data", client.seal_submittables(
    journal_entry="Conociendo los valores ideales para la reproduccion de bacterias que consumen PET (P. sakaiensis), ajustamos las condiciones del entorno, y alimentamos paulatinamente las bacterias. A pesar de que estaban concentradas en un unico nucleo, cuando observabamos la vitalidad bajar, filtrabamos el medio para contrarestar el descenso",
    key_insights="pH fijado en 7.97, temp. en 37C, basado en condiciones ideales para P. sakaiensis",
    submittable_url="https://github.com/saltachin/BioReto-26"
))