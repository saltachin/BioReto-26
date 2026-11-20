# REST API
import requests
import json

# REST client for interacting with the colony
class HttpClient:
    # Construct a client with a session token
    def __init__(self, host, token):
        self.host = host
        self.token = token

    # Perform an action upon the colony
    def __do_action__(self, payload):
        return requests.post(
            url=f"{self.host}/api/equipo/accion",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )

    # Measure something from the population
    def __do_measure__(self, option):
        return self.__do_action__(
            payload=json.dumps({"tipo": option})
        )

    # Get population count
    def get_count(self):
        response = self.__do_measure__(option="medir_poblacion")
        data = json.loads(response.text)
        return data["resultado"]["poblacion_ufc"]

    # Get MHET concentration
    def get_mhet(self):
        response = self.__do_measure__(option="medir_mhet")
        data = json.loads(response.text)
        return data["resultado"]["mhet_mM"]

    # Get pH level
    def get_ph(self):
        response = self.__do_measure__(option="medir_ph")
        data = json.loads(response.text)
        return data["resultado"]["ph"]

    # Update the temperature
    def update_temp(self, increase: bool = False):
        response = self.__do_action__(
            payload=json.dumps({
            "tipo": "temperatura", "delta": 1 if increase else -1
        }))
        data = json.loads(response.text)
        return data["resultado"]["temperatura_fijada"]

    # Update the pH level
    def update_ph(self, increase: bool = False):
        response = self.__do_action__(
            payload=json.dumps({
            "tipo": "buffer", "delta": 1 if increase else -1
        }))
        data = json.loads(response.text)
        return data["resultado"]["buffer"]

    # Update the plastic
    def add_plastic(self, x, y):
        response = self.__do_action__(
            payload=json.dumps({
            "tipo": "plastico", "x": x, "y": y
        }))
        data = json.loads(response.text)
        return data["resultado"]["plastico_en"]

    # Filter waste
    def clean(self):
        response = self.__do_action__(
            payload=json.dumps({"tipo": "filtrar"}
        ))
        data = json.loads(response.text)
        return data["resultado"]["filtrado"]

    # Revive colony
    def revive(self):
        response = self.__do_action__(
            payload=json.dumps({"tipo": "filtrar"}
        ))
        data = json.loads(response.text)
        return data["resultado"]#["filtrado"] #CHANGEME

