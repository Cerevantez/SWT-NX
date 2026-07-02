pfand_plastik = 0.25
pfand_glas = 0.08

anz_plastik = 1
anz_glas = 1

guthaben = anz_plastik * pfand_plastik + anz_glas * pfand_glas

print("Ihr Guthaben beträgt:", round(guthaben, 2), "€")