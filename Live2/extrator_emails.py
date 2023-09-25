import glob
from extrator import extrair_emails, EmailNotFoundError

def print_emails(lista_emails):
    for email in lista_emails:
        print(email)

def extrai_emails_from_path(path="./"):
    for file_path in glob.glob(f"{path}/**/*.txt", recursive=True):
        try:
            with open(file_path) as txt_file:
                msg = txt_file.read()
                print_emails(extrair_emails(msg))
        except EmailNotFoundError:
            print(f"Nenhum email encontrado em: {file_path}")