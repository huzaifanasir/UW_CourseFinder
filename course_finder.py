import requests
import json
import urllib2
 
uw_key = "214e8ed9e80e2d6ab66c00d10a7c1495"
uw_call = "https://api.uwaterloo.ca/v2/"

term = ""
while len(term) != 4:
    term = "1"
    school_term = raw_input("Which school term would you like course information for? (e.g., Winter 2014, Fall 2015)\n")
    term += school_term[-2:]
    month = school_term[0:1]
    if month == "f" or month == "F":
        term += "9"
    elif month == "w" or month == "W":
        term += "1"
    elif month == "s" or month == "S":
        term += "5"
    else:
        print("Error: please enter a valid school term")

course = raw_input("Please enter the course code for the class you're looking for (e.g., ECON 101)\n")
#no space in between
if course.find(" ") == -1:
    catalog_num = course[::-1]
    catalog_num = catalog_num[0:3]
    catalog_num = catalog_num[::-1]
    subj = course.replace(catalog_num, "")
#space
else:
    subj,catalog_num = course.split(" ")


uw_url = uw_call + "terms/" + term + "/" + subj + "/" + catalog_num + "/schedule.json?key=" + uw_key
json_obj = urllib2.urlopen(uw_url)
course_data = json.load(json_obj)


print("For " + subj.upper() + " " + catalog_num + ":")


total_spots = 0
for item in course_data["data"]:
    x = item["classes"]
    y = x[0]
    
    if (item["section"])[0:3] == "LEC" and item["enrollment_capacity"] > item["enrollment_total"]:
        spots = item["enrollment_capacity"] - item["enrollment_total"]
        sec = item["classes"]
        print(item["section"] + " has " + str(spots) + " slots available.")
        total_spots += spots
    
if total_spots < 1:
    print("There are no available slots.")

    
  


