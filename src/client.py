# REST API
import requests
import json

# REST client for interacting with the colony
class HttpClient:
    # Construct a client with a session token
    def __init__(self, host, token):
        self.host = host
        self.token = token

    # Get data from the challenge
    def __get_data__(self, endpoint):
        return requests.get(
            url=f"{self.host}/api/{endpoint}",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )

    # Perform an action upon the colony
    def __post_action__(self, payload):
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
        return self.__post_action__(
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
        response = self.__post_action__(
            payload=json.dumps({
            "tipo": "temperatura", "delta": 1 if increase else -1
        }))
        data = json.loads(response.text)
        return data["resultado"]["temperatura_fijada"]

    # Update the pH level
    def update_ph(self, increase: bool = False):
        response = self.__post_action__(
            payload=json.dumps({
            "tipo": "buffer", "delta": 1 if increase else -1
        }))
        data = json.loads(response.text)
        return data["resultado"]["buffer"]

    # Update the plastic
    def add_plastic(self, x, y):
        response = self.__post_action__(
            payload=json.dumps({
            "tipo": "plastico", "x": x, "y": y
        }))
        data = json.loads(response.text)
        return data["resultado"]["plastico_en"]

    # Filter waste
    def clean(self):
        response = self.__post_action__(
            payload=json.dumps({"tipo": "filtrar"}
        ))
        data = json.loads(response.text)
        return data["resultado"]["filtrado"]

    # Revive colony
    def revive(self):
        response = self.__post_action__(
            payload=json.dumps({"tipo": "filtrar"}
        ))
        data = json.loads(response.text)
        return data["resultado"]#["filtrado"] #CHANGEME

    # Get log of actions
    def get_actions(self):
        response = self.__get_data__(endpoint="equipo/acciones")
        data = json.loads(response.text)
        return data

    # Get missions
    def get_missions(self):
        response = self.__get_data__(endpoint="equipo/misiones")
        data = json.loads(response.text)
        return data

    # Seal a prediction for the challenge
    def seal_prediction(self, prediction):
        response = requests.post(
            url=f"{self.host}/api/equipo/prediccion",
            data=json.dumps({"prediccion": prediction}),
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )
        data = json.loads(response.text)
        return data

    # Seal the submittables for the challenge
    def seal_submittables(self, journal_entry, key_insights, submittable_url):
        response = requests.post(
            url=f"{self.host}/api/equipo/entregables",
            data=json.dumps({
                "bitacora": journal_entry,
                "ficha": key_insights,
                "solucion": submittable_url
            }),
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )
