price_ht = float(input("Enter the price HT of the article: "))
quantity = int(input("Enter the number of articles: "))
vat_rate = float(input("Enter the VAT rate (e.g., 0.2 for 20%): "))

price_ttc = price_ht * quantity * (1 + vat_rate)
print(f"The total price TTC is: {price_ttc:.2f}")
