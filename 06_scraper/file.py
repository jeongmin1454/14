import csv

def save_to_file(jobs):
    with open("jobs.csv", "w", encoding="cp949") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["No", "제목", "회사", "지역", "링크"])

        for i, job in enumerate(jobs):
            csv_writer.writerow([i, job["title"], job["company"], job["location"], job["href"]])

    