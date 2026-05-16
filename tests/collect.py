from bs4 import BeautifulSoup
import os
import pandas as pd

records = []

for index, file_name in enumerate(sorted(os.listdir("data")), start=1):
    file_path = os.path.join("data", file_name)
    with open(file_path, encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    title_tag = soup.find("h2")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    link_tag = None
    if title_tag:
        link_tag = title_tag.find_parent("a") or title_tag.find("a")
    if not link_tag:
        link_tag = soup.find("a", href=True)

    link = "N/A"
    if link_tag and link_tag.get("href"):
        href = link_tag["href"]
        link = href if href.startswith("http") else f"https://amazon.in{href}"

    price_tag = soup.find("span", class_="a-offscreen")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"

    records.append({
        "no": index,
        "title": title,
        "price": price,
        "link": link,
    })

if records:
    df = pd.DataFrame(records, columns=["no", "title", "price", "link"])
    output_path = "collected_data.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Saved {len(records)} records to {output_path}")
else:
    print("No data files found in the data folder.")