import pandas as pd
import random
import uuid
from faker import Faker
from datetime import date  # datetime.date をインポート

# Fakerを使ってランダムなデータを生成
fake = Faker()

# 元データを読み込む
input_file = "data/Personal_Finance_Dataset_2024.csv"
df = pd.read_csv(input_file)

# カテゴリと説明をリスト化
categories = df["Category"].unique().tolist()
descriptions = df["Transaction Description"].unique().tolist()

# 金額の範囲を設定（単位はドル
# カテゴリごとの金額範囲を辞書で定義
category_amount_ranges = {
    "Utilities": (10, 5000),
    "Other": (5, 1000),
    "Rent": (1000, 3000),
    "Health & Fitness": (20, 2000),
    "Salary": (3000, 10000),
    "Travel": (100, 5000),
    "Investment": (50, 10000),
    "Entertainment": (10, 500),
    "Food & Drink": (5, 500),
    "Shopping": (1, 2000),
}

# ユーザ数と年間の取引数の範囲
num_users = 100
transactions_per_user = (300, 500)

# 新しいデータを格納するリスト
expanded_data = []

# データを生成
for _ in range(num_users):
    user_id = str(uuid.uuid4())  # 一意のUUIDを生成
    num_transactions = random.randint(*transactions_per_user)  # 取引数をランダムに決定

    for _ in range(num_transactions):
        category = random.choice(categories)  # カテゴリをランダムに選択
        amount_min, amount_max = category_amount_ranges.get(category, (1, 1000))  # 金額範囲を取得（デフォルトは (1, 1000)）

        transaction = {
            "USERID": user_id,
            "Date": fake.date_between(
                start_date=date(2024, 1, 1),  # datetime.date オブジェクトを使用
                end_date=date(2024, 12, 31)
            ),
            "Transaction Description": random.choice(descriptions),
            "Category": random.choice(categories),
            "Amount": round(random.uniform(amount_min, amount_max), 2),
            "Type": random.choice(["Expense", "Income"]),
        }
        expanded_data.append(transaction)

# データフレームに変換
expanded_df = pd.DataFrame(expanded_data)

# CSVに保存
output_file = "data/Expanded_Personal_Finance_Dataset.csv"
expanded_df.to_csv(output_file, index=False)

print(f"データ生成が完了しました。ファイルは {output_file} に保存されました。")

