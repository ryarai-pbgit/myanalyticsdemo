import csv
import pandas as pd
import random
import uuid
from faker import Faker
from datetime import date 

# Fakerを使ってランダムなデータを生成
fake = Faker()

### Customer Dataを作成する
def generate_customer_data(user_ids, output_file):
    """
    指定されたユーザーIDのリストを基に、顧客データを生成してCSVに書き出す関数。

    Args:
        user_ids (list): UUID形式のユーザーIDのリスト。
        output_file (str): 書き出すCSVファイルのパス。
    """
    # 年齢、性別、居住地域、職業などの選択肢
    age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    genders = ["男性", "女性", "その他"]
    regions = [
        "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
        "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
        "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
        "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県",
        "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県",
        "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
        "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"
    ]
    occupations = [
        "会社員", "学生", "フリーランス", "主婦", "無職", "公務員", "医師", "弁護士",
        "エンジニア", "デザイナー", "研究者", "教師", "販売員", "経営者", "アーティスト"
    ]
    income_levels = ["300万円未満", "300-500万円", "500-700万円", "700-1000万円", "1000万円以上"]
    education_levels = ["高卒", "大卒", "大学院卒", "専門学校卒"]
    family_structures = ["独身", "既婚", "子供あり"]
    interests = [
        "旅行", "テクノロジー", "ファッション", "スポーツ", "音楽", "映画鑑賞", "読書",
        "料理", "アウトドア", "ゲーム", "写真撮影", "ガーデニング", "プログラミング",
        "投資", "ペット"
    ]
    device_usage = ["スマホ中心", "PC中心", "マルチデバイス"]

    # CSVのヘッダー
    headers = ["ユーザID", "年齢", "性別", "居住地域", "職業", "所得水準", "教育レベル", "家族構成", "興味・関心", "デバイス利用状況"]

    # データを格納するリスト
    data = []

    for user_id in user_ids:
        record = {
            "ユーザID": user_id,
            "年齢": random.choice(age_groups),
            "性別": random.choice(genders),
            "居住地域": random.choice(regions),
            "職業": random.choice(occupations),
            "所得水準": random.choice(income_levels),
            "教育レベル": random.choice(education_levels),
            "家族構成": random.choice(family_structures),
            "興味・関心": random.choice(interests),
            "デバイス利用状況": random.choice(device_usage),
        }
        data.append(record)

    # CSVに書き出し
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"顧客データが {output_file} に保存されました。")



def generate_transaction_data(user_ids, transactions_per_user_range, output_file):
    """
    個人の収入、支出のトランザクションデータを生成してCSVに書き出す関数。

    Args:
        user_ids (list): UUID形式のユーザーIDのリスト。
        transactions_per_user_range (tuple): 各ユーザーのトランザクション数の範囲 (min, max)。
        output_file (str): 書き出すCSVファイルのパス。
    """
    # カテゴリと金額範囲
    categories = ["Utilities", "Rent", "Health & Fitness", "Travel", "Investment", "Entertainment", "Food & Drink", "Shopping"]
    category_amount_ranges = {
        "Utilities": (10, 5000),
        "Rent": (1000, 3000),
        "Health & Fitness": (20, 2000),
        "Travel": (100, 5000),
        "Investment": (50, 10000),
        "Entertainment": (10, 500),
        "Food & Drink": (5, 500),
        "Shopping": (1, 2000),
    }
    payment_methods = ["Cash", "Credit Card", "Mobile Payment", "Other"]
    locations = [
        "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
        "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
        "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
        "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県",
        "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県",
        "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
        "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県", "オンライン", "その他"
    ]
    income_expense_types = ["Expense", "Income"]

    # CSVのヘッダー
    headers = ["ユーザID", "日付", "カテゴリ", "単価", "数量", "金額", "支払区分", "店舗場所", "収支"]

    # データを格納するリスト
    data = []

    for user_id in user_ids:
        num_transactions = random.randint(*transactions_per_user_range)  # トランザクション数をランダムに決定

        for _ in range(num_transactions):
            category = random.choice(categories)  # カテゴリをランダムに選択
            amount_min, amount_max = category_amount_ranges[category]  # 金額範囲を取得
            unit_price = round(random.uniform(amount_min, amount_max), 2)  # 単価を生成
            quantity = random.randint(1, 10)  # 数量をランダムに生成
            total_amount = round(unit_price * quantity, 2)  # 金額を計算

            transaction = {
                "ユーザID": user_id,
                "日付": fake.date_between(
                    start_date=date(2024, 1, 1),
                    end_date=date(2024, 12, 31)
                ),
                "カテゴリ": category,
                "単価": unit_price,
                "数量": quantity,
                "金額": total_amount,
                "支払区分": random.choice(payment_methods),
                "店舗場所": random.choice(locations),
                "収支": random.choice(income_expense_types),
            }
            data.append(transaction)

    # CSVに書き出し
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"トランザクションデータが {output_file} に保存されました。")

### 
def generate_overdue_table(user_ids, output_file):
    """
    ユーザIDを基にテーブルデータを生成してCSVに書き出す関数。

    Args:
        user_ids (list): UUID形式のユーザーIDのリスト。
        output_file (str): 書き出すCSVファイルのパス。
    """
    # CSVのヘッダー
    headers = ["ユーザID"]

    # データを格納するリスト
    data = []

    for user_id in user_ids:
        record = {
            "ユーザID": user_id
        }
        data.append(record)

    # CSVに書き出し
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"ユーザテーブルデータが {output_file} に保存されました。")

# 使用例
if __name__ == "__main__":
    user_ids = [str(uuid.uuid4()) for _ in range(100)]  # 100個のUUIDを生成



# 使用例
if __name__ == "__main__":

    user_ids = [str(uuid.uuid4()) for _ in range(10)]

    generate_customer_data(user_ids, "data/Customer_Data.csv")

    generate_transaction_data(
        user_ids=user_ids,
        transactions_per_user_range=(300, 500),
        output_file="data/Transaction_Data.csv"
    )

    generate_overdue_table(user_ids, "data/Overdue_Table.csv")