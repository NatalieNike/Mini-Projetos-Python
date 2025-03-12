from datetime import datetime

print("Qual a data de vencimento?")

user_date = input("")

def today():
    today = datetime.now()
    return today

def verify_format():
    print()

def comparison_dates(date_ref):
    if today() > date_ref:
        return True
    else:
        return False