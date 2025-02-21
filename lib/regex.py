import re

name = r"^[A-Z][a-zA-Z]*(?:[ '-][A-Z][a-zA-Z]*)*$"
name_regex = re.compile(name)

phone_number = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

email_address = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
