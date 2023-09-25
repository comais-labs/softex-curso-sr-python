import re


class EmailNotFoundError(Exception):
  pass

def extrair_emails(texto):
  # Usando uma expressão regular para encontrar endereços de e-mail
  padrao_email = r'([A-Za-z0-9_]+@[A-Za-z0-9_]+\.[a-z]{2,3}(\.[a-z]{2})?)'
  emails_encontrados = re.findall(padrao_email, texto)
  if len(emails_encontrados)==0:
    raise EmailNotFoundError("Não encontrei emails.")
  # return emails_encontrados
  return [email[0] for email in emails_encontrados]
