price_list = []
mobile_tax_list = []

print("Please note that this calculator is specific to Texarkana, TX and was last updated on 8/7/22")
print("\nPlease enter any items involving mobile device tax first.")

mobile_product = 0.00
mobile_prompt = " "
while mobile_prompt.lower() != "n":
    try:
        mobile_prompt = input("Mobile item? (y/n) ")

        if mobile_prompt.lower() == "y":
            mobile_product = float(input("Enter price: "))
        elif mobile_prompt.lower() != "n":
            print("Please enter y or n only. ")

        if mobile_product > 0:
            mobile_tax_list.append(mobile_product)
            price_list.append(mobile_product)
        else:
            print("Please enter a valid price.")
            continue

    except ValueError:
        print("Please enter a valid price.")

mobile_tax_sum = sum(mobile_tax_list)
mobile_tax_total = mobile_tax_sum * 0.02

print("\nEnter prices of non-mobile items, if none, or finished entering prices, enter '0' in at the prompt.")

price_prompt = " "
while price_prompt != "0":
    try:
        price_prompt = float(input("Enter price: "))

        if price_prompt == 0:
            break

        if price_prompt != 0 and price_prompt > 0:
            price_list.append(price_prompt)
        else:
            print("Please enter a valid price.")
            continue

    except ValueError:
        print("Please enter a valid price.")

sum_list = sum(price_list)


def total_price(price):
    std_tax = 0.0825
    tax_amount = price * std_tax
    tax_price_sum = (price + tax_amount) + mobile_tax_total
    round_total = format(tax_price_sum, ".2f")
    print("\nThe total after tax is $" + round_total)


total_price(price=sum_list)

print(total_price)
