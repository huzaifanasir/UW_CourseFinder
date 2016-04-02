import json
import time
import webbrowser
import urllib2
import sys


uw_key = "214e8ed9e80e2d6ab66c00d10a7c1495"
uw_call = "https://api.uwaterloo.ca/v2/"
cur_year = time.strftime("%Y")
cur_month = int((time.strftime("%m")))
leave = ""      

terms = {1: '1', 2:'1', 3:'5', 4:'5', 5:'5', 6:'5', 7:'9', 8:'9', 9:'9', 10:'9', 11:'1', 12:'1'}

default_term = "".join(["1", cur_year[-2:],terms[cur_month]])
print default_term
print(type(cur_month))
print(type(cur_year))

def get_info(term, subj, catalog_num):
  uw_url = uw_call + "terms/" + term + "/" + subj + "/" + catalog_num + "/schedule.json?key=" + uw_key
  json_obj = urllib2.urlopen(uw_url)
  course_data = json.load(json_obj)
  classes = course_data["data"] 
  number_sections = len(classes)

  for oneclass in classes:
    if oneclass["enrollment_total"] < oneclass["enrollment_capacity"] and oneclass["section"].startswith("LEC"):
      spots = oneclass["enrollment_capacity"] - oneclass["enrollment_total"] 
      section = oneclass["section"]
      profs = oneclass["classes"][0]["instructors"]

if __name__ == "__main__":
  if len(sys.argv) == 3:
    term = "".join(["1", cur_year[-2:],terms[cur_month]])
    subj = sys.argv[1]
    catalog_num = sys.argv[2]

  elif len(sys.argv) == 4:
    term = sys.argv[1]
    subj = sys.argv[2]
    catalog_num = sys.argv[3]

  get_info(term, subj, catalog_num)


