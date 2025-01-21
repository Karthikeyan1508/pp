agencies = {
    "CBI": "Central Bureau of Investigation",
    "FBI": "Foreign Direct Investment",
    "NIA": "National Investigation Agency",
    "SSB": "Service Selection Board",
    "WBA": "Works Progress Administration"
}
print(agencies)
print("******")
print(type(agencies))

agencies["BSE"] = "Bombay Stock Exchange"
print(agencies)

agencies["SSB"] = "Social Security Administration"
print(agencies)

agencies.pop("FBI")
agencies.pop("WBA")
print(agencies)
