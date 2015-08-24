import requests
import json
import time
import webbrowser
import urllib2
 
uw_key = "214e8ed9e80e2d6ab66c00d10a7c1495"
uw_call = "https://api.uwaterloo.ca/v2/"
cur_year = time.strftime("%Y")
cur_month = int((time.strftime("%m")))
leave = ""

print("Welcome to the UW Course Finder!")
time.sleep(1)

while (leave != "x"):
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
            statement = item["section"] + " has " + str(spots) + " slots available. It is taught by "
            for prof in y["instructors"]:
                print(statement + prof + ".")
            total_spots += spots
        
    if total_spots < 1:
        print("There are no available slots.")

    if total_spots >= 1:
        if cur_year[-2:] == term[1:3]: #same year
            if abs(int(term[3:4]) - cur_month) <= 2:
                ans = raw_input("Would you like to enrol in this course? Answer \"yes\" or \"no\"\n")
                helper = raw_input("Would you like instructions on how to enrol? Answer \"yes\" or \"no\"\n")
                if ans == "yes":
                    webbrowser.open("https://uwaterloo.ca/quest/")
                if helper == "yes":
                    webbrowser.open("https://uwaterloo.ca/quest/help/students/how-do-i/add-classes")
        elif term[1:3] - cur_year[-2:] == 1: #year before (e.g., 2015 schedule in 2014)
            if cur_year == 11 or cur_year == 12:
                ans = raw_input("Would you like to enrol in this course? Answer \"yes\" or \"no\"\n")
                helper = raw_input("Would you like instructions on how to enrol? Answer \"yes\" or \"no\"\n")
                if ans == "yes":
                    webbrowser.open("https://uwaterloo.ca/quest/")
                if helper == "yes":
                    webbrowser.open("https://uwaterloo.ca/quest/help/students/how-do-i/add-classes")
                    
        

    leave = raw_input("Enter x to quit, or any other key to search again.\n")

print("Thanks for using the UW Course Finder. See you later!")



