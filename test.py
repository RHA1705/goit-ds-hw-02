from faker import Faker
from faker.providers import BaseProvider

class TaskProvider(BaseProvider):
    def task(self):
        actions = ["Naprawić", "Zainstalować", "Zaktualizować", "Skonfigurować", "Zweryfikować"]
        objects = ["serwer", "bazę danych", "aplikację", "oprogramowanie", "sieć"]
        return f"{self.random_element(actions)} {self.random_element(objects)}"

fake = Faker()
fake.add_provider(TaskProvider)

# Generowanie losowych tasków
for _ in range(5):
    print(f"Task: {fake.task()}")
