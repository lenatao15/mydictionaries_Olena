import json
    
infile = open('school_data.json', 'r')

schools = json.load(infile)

conference_numbers = [372, 108, 107, 130]

print("Report for Universities with Graduation Rate for Women over 75%")
for school in schools:
    # Filter by conference first
    conf_num = school['NCAA']['NAIA conference number football (IC2020)']
    if conf_num in conference_numbers:
        grad_rate_women = school['Graduation rate  women (DRVGR2020)']
        if grad_rate_women > 75:
            print(f"University: {school['instnm']}")
            print(f"Graduation Rate for Women: {grad_rate_women}%")
            print("-" * 30)

print("\n\n")

print("Report for Universities with Total Price for In-State Students Living Off Campus over $60,000")
for school in schools:
    # Filter by conference first
    conf_num = school['NCAA']['NAIA conference number football (IC2020)']
    if conf_num in conference_numbers:
        price_off_campus = school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']
        # Some values might be None or 0, check if it's over 60,000
        if price_off_campus and price_off_campus > 60000:
            print(f"University: {school['instnm']}")
            print(f"Total Price (Off Campus): ${price_off_campus:,.2f}")
            print("-" * 30)

infile.close()
