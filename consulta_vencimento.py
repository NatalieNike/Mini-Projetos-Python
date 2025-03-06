from datetime import datetime

print("Qual a data de vencimento?")

due_date = input("")

def today():
    today = datetime.now()
    return today

def verify(date_ref):
    if today() > date_ref:
        return True
    else:
        return False