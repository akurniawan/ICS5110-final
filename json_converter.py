import csv
import json

f = csv.writer(open("test.csv", "w", newline=""), delimiter="\t")
f.writerow(["review_id", "stars", "useful", "date", "text"])

with open("yelp_academic_dataset_review.json", "r") as jsonf:
    for line in jsonf:
        x = json.loads(line)
        f.writerow([x["review_id"], x["stars"], x["useful"], x["date"], x["text"]])
