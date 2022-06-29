import json
import sys

import requests


class PopulaPortal(object):

    base_url = "http://localhost:8080/Plone/++api++"
    username = "admin"
    password = "admin"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    token = ""

    # Authenticate
    def __init__(self):
        response = requests.post(
            f"{self.base_url}/@login",
            headers=self.headers,
            json={"login": self.username, "password": self.password},
        )

        if response.status_code == 200:
            self.token = response.json()["token"]
            self.headers["Authorization"] = f"Bearer {self.token}"
            print(f"Autenticado! Token: {self.token}")
        else:
            raise ValueError("Usuário ou/e senha inválidos")

    def create_doc(self, obj, path="/"):
        """{
            "@type": "Document",
            "title": "My Document"
        }"""
        url = f"{self.base_url}{path}"

        obj_id = obj["id"]
        obj_url = f"{url}/{obj_id}"
        response = requests.post(
            obj_url,
            headers=self.headers,
            json=obj,
        )
        if response.status_code == 404:
            # Content does not exist yet, create
            response = requests.post(
                url,
                headers=self.headers,
                json=obj,
            )
            if response.status_code > 299:
                print(f"ERROR: {response.text}")
                return
            data = response.json()
            path = data["@id"]
            print(f"Created {path}")
            url = f"{path}/@workflow/publish"
            requests.post(url, headers=self.headers)
        elif response.status_code in (200, 301, 302, 308):
            # Content exists
            data = response.json()
            review_state = data.get("review_state")
            obj_url = data["@id"]
            if review_state == "private":
                requests.post(f"{obj_url}/@workflow/publish", headers=self.headers)
                print(f"Published {obj_url}")
            response = requests.patch(
                obj_url,
                headers=self.headers,
                json=obj,
            )
            print(f"Updated {obj_url}")
        else:
            # oops
            print(f"ERROR: {url} {response.text}")


if __name__ == "__main__":

    portal = PopulaPortal()
    novo = {
        "@type": "Document",
        "id": "campus",
        "title": "Campus",
        "description": "Lista de Campus da UFT",
    }
    portal.create_doc(novo)

    contents = [
        ("palmas", "Palmas", "palmas"),
        ("miracema", "Miracema", "miracema"),
    ]

for id_, title, city in contents:
    portal.create_doc(
        path="/campus",
        obj={
            "@type": "campus",
            "id": id_,
            "title": title,
            "description": f"Campus da UFT em {title}",
            "city": city,
            "email": f"{city}@uft.edu.br",
        },
    )
