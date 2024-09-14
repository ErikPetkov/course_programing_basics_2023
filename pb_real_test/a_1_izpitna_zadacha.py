br_rows_paper = int(input())
br_rows_plat = int(input())
lit_lepilo = float(input())
percemt_discount = int(input())

total_paper_price = br_rows_paper * 5.8
total_plat_price = br_rows_plat * 7.2
total_lepilo = lit_lepilo * 1.2

total = total_paper_price + total_plat_price + total_lepilo
discount = percemt_discount / 100
total_with_discount = total - (total * discount)

print(f"{total_with_discount:.3f}")
