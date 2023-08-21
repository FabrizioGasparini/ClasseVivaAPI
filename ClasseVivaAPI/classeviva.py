import requests
import debug.ColoredPrinting as CP
import json
import re

# ==== Classe Principale (Utente) ===== #

class Utente:
    # === Inizializza Utente === #
    def __init__(self, uid: str, pwd: str):
        self.uid = uid
        self.pwd = pwd
        self.ident = ''
        self.token = ''

        self.is_logged_in = False

    # === Effettua il Login === #
    def login(self):
        response = requests.post(RequestURLs.login[0], headers=header, data=f'{{"ident":null,"pass":"{self.pwd}","uid":"{self.uid}"}}')

        if response.status_code == 200:
            data = json.loads(response.text)

            self.ident = re.search(r'\d+', data['ident']).group()
            self.token = data['token']
            self.is_logged_in = True

            print(f'{CP.GREEN}Login effettuato con successo.')
        else:
            print(f'{CP.RED}Errore durante il Login.')

        return response

    # === Effettua una Richiesta 'GET' === #
    def request(self, reqeust_url: tuple, params=None):
        args = (self.ident,) + (params,)

        if self.is_logged_in:
            headers = self.get_headers()

            if reqeust_url[1] == 'get':
                response = requests.get(reqeust_url[0].format(*args), headers=headers)
            else:
                response = requests.post(reqeust_url[0].format(*args), headers=headers)

            if response.status_code == 200:
                print(f'{CP.GREEN}Richiesta avvenuta con successo:')
                print(f'{CP.DEFAULT}{response.text}')
                return response
            else:
                print(f'{CP.RED}Errore durante la richiesta: {response.text}')
                return None
        else:
            print(f"{CP.RED}Errore durante la richiesta: L'utente non ha effetuato il login.")
            return None

    def get_headers(self):
        headers = header.copy()
        headers['Z-Auth-Token'] = self.token

        return headers


# ===== Default Header ===== #

header: dict[str, str] = {
    "User-Agent": "CVVS/std/4.1.7 Android/10",
    "Content-Type": "application/json",
    "Z-Dev-ApiKey": "Tg1NWEwNGIgIC0K"
}

# ===== Reqeust URLs ===== #
class RequestURLs:
    base_url: str = 'https://web.spaggiari.eu/rest/v1'
    students_url: str = f'{base_url}/students/{{}}'  # Student Ident

    absences: tuple = (f'{students_url}/absences/details', 'get')
    agenda: tuple = (f'{students_url}/agenda/all/{{}}/{{}}', 'get')  # Begin Data (YYYYMMDD) / End Date (YYYYMMDD)
    didactics: tuple = (f'{students_url}/didactics', 'get')
    schoolbooks: tuple = (f'{students_url}/schoolbooks', 'get')
    calendar: tuple = (f'{students_url}/calendar/all', 'get')
    card: tuple = (f'{students_url}/card', 'get')
    grades: tuple = (f'{students_url}/grades', 'get')
    lessons: tuple = (f'{students_url}/lessons/today', 'get')
    lessons_by_day: tuple = (f'{students_url}/lessons/{{}}', 'get') # Lessons Day (YYYYMMDD)
    notes: tuple = (f'{students_url}/notes/all', 'get')
    perioids: tuple = (f'{students_url}/perioids', 'get')
    subjects: tuple = (f'{students_url}/subjects', 'get')

    login: tuple = (f'{base_url}/auth/login', 'post')
    noticeboard: tuple = (f'{students_url}/noticeboard', 'post')
    documents: tuple = (f'{students_url}/documents', 'post')
    documents_check: tuple = (f'{students_url}/documents/check/{{}}', 'post')