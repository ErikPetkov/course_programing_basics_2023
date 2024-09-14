#•	Паламуд – 60% по-скъп от скумрията
#•	Сафрид – 80% по-скъп от цацата
#•	Миди – 7.50 лв. за килограм
midi_for_kg = 7.5
price_for_skumria_kg = float(input())
price_for_caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
kg_midi = int(input())
price_for_palamud = price_for_skumria_kg+price_for_skumria_kg*0.6
price_for_safrid = price_for_caca_kg*1.8
palamud = palamud_kg*price_for_palamud
safrid = price_for_safrid*safrid_kg
midi = midi_for_kg * kg_midi
bill  = palamud+safrid+midi
print(f"{bill:.2f}")