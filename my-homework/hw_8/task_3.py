import random
from faker import Faker
fake = Faker()

FILE_PATH="paragraphs.txt"

def generate_and_write_paragraphs(file_path):

    with open(file_path, 'w', encoding='utf-8') as file:
        paragraphs =[]
        for _ in range(5):
            language = random.choice(['en_US', 'it_IT', 'de_DE', 'es_ES', 'fr_FR'])
            fake = Faker(language)

            paragraph = fake.paragraph()
            file.write(f"{paragraph}\n")
            paragraphs.append(paragraph)

    print(f"{paragraphs} have been written to {file_path}")

generate_and_write_paragraphs(FILE_PATH)
