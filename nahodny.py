import json


print("hihi")


print(f"""
Na jakou otázku chcete odpověď ? 
1.Jaký je rok vydaní?
2.Jaký herci hrají hlavni postavy
3.Kdo je režisér?
4.Jak dlouhý je film?
""")

with open ("interstellar.json","r", encoding="utf-8") as f:
        interstellar = json.load(f)

cislootazky = int(input("Napište číslo otázky: "))

print(cislootazky)

if cislootazky == 1:
    print(f" Rok vydání je {interstellar["rokvydani"]}.")
elif cislootazky == 2:
      print(f" Herci, kteří hrají hlavní postavy jsou: {interstellar["herci"]}.")
elif cislootazky == 3:
      print(f"Režisér je {interstellar["reziser"]}.")
elif cislootazky == 4:
      print(f" Film má {interstellar["delka"]}.")
else:
      print("Prosím vyberte platné číslo otázky.")
      