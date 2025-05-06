# Imports & modules
import smtplib
import datetime as dt
import random as r
import os
from dotenv import load_dotenv

load_dotenv()
now = dt.datetime.now()

# Global scope
my_email = os.getenv('my_email')
to_email = os.getenv('to_email')
password = os.getenv('password')

week_days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
months = ["janvier", "février", "mars", "avril", "mai", "juin","juillet", "août", "septembre","octobre", "novembre", "décembre"]

if now.weekday() == 1:
    # Ouvrel le fichier quotes.txt et extrait chaque ligne, les stock dans une list et saisi une citation au hasard
    with open("quotes.txt", "r") as quote_file:
        file_quotes = quote_file.readlines()
        quotes = [quote.strip('\n') for quote in file_quotes]
        random_quote = r.choice(quotes)

    # Créer le message
    msg = f"Subject:Motivation du {week_days[now.weekday()]} {now.day} {months[now.month]} {now.year}\n\n{random_quote}\n\nCordialement,\nToi même ;)"

    # Envoie le courriel
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=msg.encode('utf-8')
        )
else:
    print("Il n'y a pas d'envoi de courriel prévu pour ajourd'hui !")