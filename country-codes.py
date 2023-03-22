import csv

# open the file to read from
f = open("email-domains.csv", "r")  

 # create empty dictionary
d = {}  

# loop through each email to sort
for line in f:
    domain_end = line.replace("\n","").split("@")
    domain_end = domain_end[1].split(".")
    domain_end = domain_end[-1]
    if domain_end in d:
        d[domain_end][1] += 1
    else:
        if domain_end == "af":
            d[domain_end] = ["Afghanistan",1]
        elif domain_end == "aq":
            d[domain_end] = ["Antarctica",1]
        elif domain_end == "au":
            d[domain_end] = ["Australia",1]
        elif domain_end == "by":
            d[domain_end] = ["Belarus",1]
        elif domain_end == "be":
            d[domain_end] = ["Belgium",1]
        elif domain_end == "bw":
            d[domain_end] = ["Botswana",1]
        elif domain_end == "ca":
            d[domain_end] = ["Canada",1]
        elif domain_end == "ch":
            d[domain_end] = ["Switzerland",1]
        elif domain_end == "cn":
            d[domain_end] = ["China",1]
        elif domain_end == "de":
            d[domain_end] = ["Germany",1]
        elif domain_end == "dk":
            d[domain_end] = ["Denmark",1]
        elif domain_end == "fi":
            d[domain_end] = ["Finland",1]
        elif domain_end == "fr":
            d[domain_end] = ["France",1]
        elif domain_end == "hk":
            d[domain_end] = ["Hong Kong",1]
        elif domain_end == "ie":
            d[domain_end] = ["Ireland",1]
        elif domain_end == "il":
            d[domain_end] = ["Israel",1]
        elif domain_end == "in":
            d[domain_end] = ["India",1]
        elif domain_end == "jp":
            d[domain_end] = ["Japan",1]
        elif domain_end == "lu":
            d[domain_end] = ["Luxembourg",1]
        elif domain_end == "nl":
            d[domain_end] = ["Netherlands",1]
        elif domain_end == "ro":
            d[domain_end] = ["Romania",1]
        elif domain_end == "sv":
            d[domain_end] = ["El Salvador",1]
        elif domain_end == "uk":
            d[domain_end] = ["United Kingdom",1]
        elif domain_end == "us":
            d[domain_end] = ["United States",1]
        elif domain_end == "za":
            d[domain_end] = ["South Africa",1]

f.close()

# create a new csv file
f = open("countries.csv", "w", encoding='UTF8', newline='')
writer = csv.writer(f)

# write the first row of the file
writer.writerow(["email domain ending", "country", "number of instances"])

# add each item from the dictionary to you CSV file
for item in d:
    writer.writerow([item, str(d[item][0]), str(d[item][1])])

f.close()
