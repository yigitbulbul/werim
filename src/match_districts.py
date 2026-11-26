def to_gb_name(province, district):
    if district == "Merkez":
        name = province + " merkez"
    else:
        name = district
    name = name.replace("ş", "?").replace("ı", "?").replace("ğ", "?").replace("İ", "?").replace("Ş", "?")
    return name

print(to_gb_name("Tekirdağ", "Kapaklı"))
print(to_gb_name("Kırklareli", "Merkez"))
print(to_gb_name("Tekirdağ", "Çorlu"))