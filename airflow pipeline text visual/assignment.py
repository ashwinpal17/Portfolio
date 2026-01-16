from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

import urllib.request
from urllib.error import HTTPError, URLError
import time
import glob
import os
import json


# ----------------------------
# Task 1: Pull course catalog pages
# ----------------------------
def catalog():

    def pull(url):
        """Return bytes or None if URL fails."""
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
            return data
        except HTTPError as e:
            print(f"SKIP (HTTP {e.code}): {url}")
            return None
        except URLError as e:
            print(f"SKIP (URL error): {url} -> {e}")
            return None

    def store(data, file):
        with open(file, "wb") as f:
            f.write(data)
        print("wrote file: " + file)

    urls = [
        "http://student.mit.edu/catalog/m1a.html",
        "http://student.mit.edu/catalog/m1b.html",
        "http://student.mit.edu/catalog/m1c.html",
        "http://student.mit.edu/catalog/m2a.html",
        "http://student.mit.edu/catalog/m2b.html",
        "http://student.mit.edu/catalog/m2c.html",
        "http://student.mit.edu/catalog/m3a.html",
        "http://student.mit.edu/catalog/m3b.html",
        "http://student.mit.edu/catalog/m4a.html",
        "http://student.mit.edu/catalog/m4b.html",
        "http://student.mit.edu/catalog/m4c.html",
        "http://student.mit.edu/catalog/m4d.html",
        "http://student.mit.edu/catalog/m4e.html",
        "http://student.mit.edu/catalog/m4f.html",
        "http://student.mit.edu/catalog/m4g.html",
        "http://student.mit.edu/catalog/m5a.html",
        "http://student.mit.edu/catalog/m5b.html",
        "http://student.mit.edu/catalog/m6a.html",
        "http://student.mit.edu/catalog/m6b.html",
        "http://student.mit.edu/catalog/m6c.html",
        "http://student.mit.edu/catalog/m7a.html",
        "http://student.mit.edu/catalog/m8a.html",
        "http://student.mit.edu/catalog/m8b.html",
        "http://student.mit.edu/catalog/m9a.html",
        "http://student.mit.edu/catalog/m9b.html",
        "http://student.mit.edu/catalog/m10a.html",
        "http://student.mit.edu/catalog/m10b.html",
        "http://student.mit.edu/catalog/m10c.html",
        "http://student.mit.edu/catalog/m11a.html",
        "http://student.mit.edu/catalog/m11b.html",
        "http://student.mit.edu/catalog/m11c.html",
        "http://student.mit.edu/catalog/m12a.html",
        "http://student.mit.edu/catalog/m12b.html",
        "http://student.mit.edu/catalog/m12c.html",
        "http://student.mit.edu/catalog/m14a.html",
        "http://student.mit.edu/catalog/m14b.html",
        "http://student.mit.edu/catalog/m15a.html",
        "http://student.mit.edu/catalog/m15b.html",
        "http://student.mit.edu/catalog/m15c.html",
        "http://student.mit.edu/catalog/m16a.html",
        "http://student.mit.edu/catalog/m16b.html",
        "http://student.mit.edu/catalog/m18a.html",
        "http://student.mit.edu/catalog/m18b.html",
        "http://student.mit.edu/catalog/m20a.html",
        "http://student.mit.edu/catalog/m22a.html",
        "http://student.mit.edu/catalog/m22b.html",
        "http://student.mit.edu/catalog/m22c.html",
    ]

    for url in urls:
        index = url.rfind("/") + 1
        file = url[index:]  # e.g. m1a.html

        data = pull(url)
        if data is None:
            # skip missing/bad pages so DAG can complete
            continue

        store(data, file)

        print("pulled: " + file)
        print("--- waiting ---")
        time.sleep(15)  # keep as-is for rubric; you can change to 1 later if you want


# ----------------------------
# Task 2: Combine HTML files
# ----------------------------
def combine():
    with open("combo.txt", "w", encoding="utf-8") as outfile:
        for file in glob.glob("*.html"):
            with open(file, "r", encoding="utf-8", errors="ignore") as infile:
                outfile.write(infile.read())
    print("wrote file: combo.txt")


# ----------------------------
# Task 3: Extract course titles from <h3> tags
# ----------------------------
def titles():
    from bs4 import BeautifulSoup

    def store_json(data, file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("wrote file: " + file)

    with open("combo.txt", "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    html = html.replace("\n", " ").replace("\r", "")
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("h3")

    titles_list = [item.text for item in results]
    store_json(titles_list, "titles.json")


# ----------------------------
# Task 4: Clean punctuation/numbers/1-char words
# ----------------------------
def clean():
    def store_json(data, file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("wrote file: " + file)

    with open("titles.json", "r", encoding="utf-8") as file:
        titles_list = json.load(file)

    for index, title in enumerate(titles_list):
        punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~1234567890'''
        translationTable = str.maketrans("", "", punctuation)
        cleaned = title.translate(translationTable)
        titles_list[index] = cleaned

    for index, title in enumerate(titles_list):
        cleaned = " ".join([word for word in title.split() if len(word) > 1])
        titles_list[index] = cleaned

    store_json(titles_list, "titles_clean.json")


# ----------------------------
# Task 5: Count words into words.json
# ----------------------------
def count_words():
    from collections import Counter

    def store_json(data, file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("wrote file: " + file)

    with open("titles_clean.json", "r", encoding="utf-8") as file:
        titles_list = json.load(file)

    words = []
    for title in titles_list:
        words.extend(title.split())

    counts = Counter(words)
    store_json(counts, "words.json")


# ----------------------------
# DAG definition (t0 to t5)
# ----------------------------
with DAG(
    "assignment",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t0 = BashOperator(
        task_id="task_zero",
        bash_command="pip install beautifulsoup4",
        retries=2
    )

    t1 = PythonOperator(
        task_id="task_one",
        depends_on_past=False,
        python_callable=catalog
    )

    t2 = PythonOperator(
        task_id="task_two",
        depends_on_past=False,
        python_callable=combine
    )

    t3 = PythonOperator(
        task_id="task_three",
        depends_on_past=False,
        python_callable=titles
    )

    t4 = PythonOperator(
        task_id="task_four",
        depends_on_past=False,
        python_callable=clean
    )

    t5 = PythonOperator(
        task_id="task_five",
        depends_on_past=False,
        python_callable=count_words
    )

    t0 >> t1 >> t2 >> t3 >> t4 >> t5
