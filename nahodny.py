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
    print({interstellar["rokvydani"]})
elif cislootazky == 2:
      print({interstellar["herci"]})
elif cislootazky == 3:
      ({interstellar["reziser"]})
elif cislootazky == 4:
      ({interstellar["delka"]})
else:
      print("Prosím vyberte platné číslo otázky")
      