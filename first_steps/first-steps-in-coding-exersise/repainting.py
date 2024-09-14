protect_nailon=1.5
p_paint = 14.5
r_razreditel = 5
needed_nailon = int(input())
needed_paint = int(input())
needed_razreditel = int(input())
hours_work = int(input())
nailon = protect_nailon*(needed_nailon+2)
paint=needed_paint*(p_paint*1.1)
razreditel = r_razreditel*needed_razreditel
all_materials= nailon+paint+razreditel+0.4
mistors = (all_materials*0.3)*hours_work
end_sum = all_materials+mistors
print(end_sum)