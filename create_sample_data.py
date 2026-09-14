import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ============================================================
# SETTINGS
# ============================================================

N = 8688
SEED = 42

np.random.seed(SEED)
random.seed(SEED)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def random_dates(start, end, n):
    start = pd.Timestamp(start)
    end = pd.Timestamp(end)
    days = (end - start).days
    return [
        start + pd.Timedelta(days=random.randint(0, days),
                             hours=random.randint(0, 23),
                             minutes=random.randint(0, 59))
        for _ in range(n)
    ]


def fake_turkish_name(i):
    first_names = [
        "Ahmet", "Mehmet", "Ayşe", "Fatma", "Zeynep",
        "Emre", "Burak", "Elif", "Mert", "Ece",
        "Can", "Deniz", "Selin", "Berk", "Derya"
    ]

    last_names = [
        "Yılmaz", "Kaya", "Demir", "Şahin", "Çelik",
        "Arslan", "Aydın", "Öztürk", "Koç", "Kurt",
        "Polat", "Aksoy", "Güneş", "Tekin", "Doğan"
    ]

    return f"{first_names[i % len(first_names)]} {last_names[i % len(last_names)]}"


# ============================================================
# LOCATION DATA
# ============================================================

cities = {
    1: "Adana",
    6: "Ankara",
    7: "Antalya",
    10: "Balıkesir",
    16: "Bursa",
    20: "Denizli",
    21: "Diyarbakır",
    26: "Eskişehir",
    27: "Gaziantep",
    31: "Hatay",
    34: "İstanbul",
    35: "İzmir",
    38: "Kayseri",
    41: "Kocaeli",
    42: "Konya",
    45: "Manisa",
    46: "Kahramanmaraş",
    54: "Sakarya",
    55: "Samsun",
    61: "Trabzon",
    63: "Şanlıurfa",
    67: "Zonguldak",
    71: "Kırıkkale",
    78: "Karabük",
    80: "Osmaniye",
    81: "Düzce",
    90: "Yalova"
}

city_ids = np.random.choice(
    list(cities.keys()),
    size=N,
    p=None
)

city_names = [cities[x] for x in city_ids]


# ============================================================
# PROPERTY CHARACTERISTICS
# ============================================================

sub_categories = [
    "Dükkan & Mağaza",
    "Ofis",
    "Büro",
    "Depo & Antrepo",
    "Fabrika",
    "Plaza Katı",
    "Plaza",
    "Atölye",
    "İmalathane",
    "Restaurant & Lokanta",
    "Cafe & Bar",
    "Otel",
    "Apartman",
    "İş Hanı"
]

sub_category = np.random.choice(
    sub_categories,
    size=N,
    p=[
        0.48, 0.12, 0.08, 0.07,
        0.04, 0.04, 0.03, 0.03,
        0.02, 0.02, 0.02, 0.01,
        0.02, 0.02
    ]
)

room_types = [
    "Stüdyo",
    "1+0",
    "1+1",
    "2+0",
    "2+1",
    "3+1",
    "4+1",
    "5+1",
    "6+1"
]

room_and_living = np.random.choice(
    room_types,
    size=N,
    p=[
        0.30, 0.10, 0.14, 0.08,
        0.14, 0.10, 0.06,
        0.04, 0.04
    ]
)

room = np.array([
    int(x.split("+")[0]) if "+" in x else 0
    for x in room_and_living
])

living_room = np.random.choice(
    [0, 1],
    size=N,
    p=[0.98, 0.02]
)

# ============================================================
# SQM
# ============================================================

sqm = np.random.lognormal(
    mean=np.log(120),
    sigma=0.75,
    size=N
)

sqm = np.clip(sqm, 20, 5000)
sqm = np.round(sqm, 0)

# ============================================================
# PRICE
# ============================================================

# Approximate city-based price per sqm.
price_per_sqm = {
    "İstanbul": 95000,
    "İzmir": 65000,
    "Ankara": 50000,
    "Antalya": 60000,
    "Bursa": 42000,
    "Kocaeli": 40000,
    "Muğla": 70000
}

base_ppsqm = np.array([
    price_per_sqm.get(city, 30000)
    for city in city_names
])

# Random variation
noise = np.random.lognormal(
    mean=0,
    sigma=0.45,
    size=N
)

realty_price_tl = sqm * base_ppsqm * noise

# Keep values within a reasonable synthetic range
realty_price_tl = np.clip(
    realty_price_tl,
    500000,
    300000000
)

realty_price_tl = np.round(
    realty_price_tl / 10000
) * 10000

realty_price_tl = realty_price_tl.astype(int)


# ============================================================
# LOCATION IDS
# ============================================================

county_ids = np.random.randint(
    1100,
    2131,
    size=N
)

district_ids = np.random.randint(
    10000,
    162000,
    size=N
)

county_names = [
    f"İlçe_{x}"
    for x in county_ids
]

district_names = [
    f"Mahalle_{x}"
    for x in district_ids
]

area_ids = [
    f"{random.randint(100,999)},{random.randint(100,999)},{random.randint(100,999)}"
    for _ in range(N)
]

area_names = [
    f"Bölge_{random.randint(1,1200)}"
    for _ in range(N)
]


# ============================================================
# FLOOR
# ============================================================

floor_names = [
    "Zemin",
    "Yüksek giriş",
    "1. Kat",
    "2. Kat",
    "3. Kat",
    "4. Kat",
    "5. Kat",
    "6. Kat",
    "7. Kat",
    "8. Kat",
    "9. Kat",
    "10. Kat"
]

floor_name = np.random.choice(
    floor_names,
    size=N
)

floor_id_map = {
    "Zemin": 101200,
    "Yüksek giriş": 101201,
    "1. Kat": 101202,
    "2. Kat": 101203,
    "3. Kat": 101204,
    "4. Kat": 101205,
    "5. Kat": 101206,
    "6. Kat": 101207,
    "7. Kat": 101208,
    "8. Kat": 101209,
    "9. Kat": 101210,
    "10. Kat": 101211
}

floor_id = [
    floor_id_map[x]
    for x in floor_name
]

floor_count = np.random.choice(
    [2, 3, 4, 5, 6, 7, 8, 10],
    size=N
)

# ============================================================
# DATES
# ============================================================

created_dates = random_dates(
    "2024-01-01",
    "2025-12-31",
    N
)

updated_dates = [
    date + pd.Timedelta(days=random.randint(1, 60))
    for date in created_dates
]

start_dates = [
    date + pd.Timedelta(days=random.randint(1, 10))
    for date in created_dates
]

end_dates = [
    date + pd.Timedelta(days=random.randint(60, 180))
    for date in start_dates
]


def iso_date(x):
    return x.strftime("%Y-%m-%dT%H:%M:%S.000Z")


# ============================================================
# IDS
# ============================================================

listing_ids = [
    f"SAMPLE-{i:06d}"
    for i in range(1, N + 1)
]

realty_nos = np.random.randint(
    100,
    150000,
    size=N
)

realty_ids = np.arange(
    10000000,
    10000000 + N
)


# ============================================================
# OTHER FEATURES
# ============================================================

advertise_owner = np.random.choice(
    ["Emlakçıdan", "Sahibinden", "Bankadan", "Müteahhitten", "Firma"],
    size=N,
    p=[0.88, 0.07, 0.01, 0.02, 0.02]
)

age = np.random.choice(
    [0, 1, 5, 10, 15, 20, 25],
    size=N
).astype(float)

floor_count = floor_count.astype(float)

bath_room = np.zeros(N, dtype=int)

image_count = np.random.randint(
    1,
    30,
    size=N
)

description_templates = [
    "Detaylı bilgi için iletişime geçebilirsiniz.",
    "Merkezi konumda satılık ticari gayrimenkul.",
    "Yatırıma uygun işyeri.",
    "Ulaşımı kolay ve merkezi konumda.",
    "Detaylar için ilan sahibi ile iletişime geçiniz."
]

description = [
    random.choice(description_templates)
    for _ in range(N)
]

build_state_names = np.random.choice(
    ["İkinci El", "Sıfır", "Proje", "Yapım Aşamasında"],
    size=N,
    p=[0.75, 0.15, 0.05, 0.05]
)

build_state_ids = np.random.randint(
    101600,
    101609,
    size=N
).astype(float)

furnished = np.random.choice(
    [False, True],
    size=N,
    p=[0.96, 0.04]
)

fuel_names = np.random.choice(
    ["Doğalgaz", "Elektrik", "Merkezi", "Yok", "Diğer"],
    size=N
)

heating_names = np.random.choice(
    ["Kombi", "Merkezi", "Klima", "Yok", "Soba", "Yerden Isıtma"],
    size=N
)

heating_ids = np.random.randint(
    101300,
    101316,
    size=N
).astype(float)

credit_names = np.random.choice(
    ["Uygun", "Uygun Değil", "Bilinmiyor", "Değerlendiriliyor"],
    size=N,
    p=[0.81, 0.08, 0.08, 0.03]
)

# ============================================================
# FIRM DATA
# ============================================================

firm_ids = np.random.randint(
    2000,
    7000,
    size=N
).astype(str)

firm_user_ids = np.random.randint(
    2000,
    8000,
    size=N
).astype(str)

firm_names = [
    f"Örnek Emlak {i % 250 + 1}"
    for i in range(N)
]

firm_last_names = [
    "Gayrimenkul",
    "Danışmanlığı",
    "Emlak",
    "Yatırım",
    "Property"
]

firm_user_last_names = [
    random.choice(firm_last_names)
    for _ in range(N)
]

firm_user_full_names = [
    f"{fake_turkish_name(i)}"
    for i in range(N)
]

# ============================================================
# URL / COORDINATE-LIKE FIELDS
# ============================================================

# IMPORTANT:
# These are deliberately fake and do NOT point to real listings.

detail_urls = [
    f"https://example.com/sample-listing/{i:06d}"
    for i in range(1, N + 1)
]

image_urls = [
    f"https://example.com/sample-image/{i:06d}.jpg"
    for i in range(1, N + 1)
]

breadcrumb_urls = [
    f"https://example.com/sample-location/{i:05d}"
    for i in range(N)
]

map_lat_lon = [
    f"{round(np.random.uniform(36.0, 42.0), 4)},"
    f"{round(np.random.uniform(26.0, 45.0), 4)}"
    for _ in range(N)
]

# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame({

    "listingId": listing_ids,
    "realtyNo": realty_nos,
    "realtyId": realty_ids,

    "advertiseOwnerName": advertise_owner,

    "mainCategoryName": ["İşyeri"] * N,
    "categories": ["İşyeri Satılık"] * N,
    "subCategoryName": sub_category,

    "mainCategoryId": [1000020000] * N,
    "categoryId": [1000010000] * N,

    "cityId": city_ids,
    "cityName": city_names,

    "countyId": county_ids,
    "countyName": county_names,

    "areaName": area_names,
    "areaId": area_ids,

    "districtId": district_ids,
    "districtName": district_names,

    "title": [
        f"SATILIK {sub_category[i].upper()}"
        for i in range(N)
    ],

    "age": age,
    "roomAndLivingRoom": room_and_living,

    "sqm": sqm,

    "floorName": floor_name,
    "floorId": floor_id,

    "bathRoom": bath_room,
    "livingRoom": living_room,
    "room": room,

    "floorCount": floor_count,

    "mapLatLon": map_lat_lon,

    "detailUrl": detail_urls,

    "breadcrumbs4Url": breadcrumb_urls,
    "breadcrumbs3Url": breadcrumb_urls,

    "imageUrl": image_urls,
    "images": image_urls,

    "imageCount": image_count.astype(str),

    "description": description,

    "createdDate": [iso_date(x) for x in created_dates],
    "updatedDate": [iso_date(x) for x in updated_dates],
    "startDate": [iso_date(x) for x in start_dates],
    "endDate": [iso_date(x) for x in end_dates],

    "realtyPrice": realty_price_tl.astype(str),

    "realtyPriceCurrencyCode": ["TL"] * N,

    "realtyPriceTl": realty_price_tl,

    "realtyPriceCurrencyId": ["1"] * N,

    "showPrice": np.random.choice(
        ["false", "true"],
        size=N,
        p=[0.65, 0.35]
    ),

    "firmUserId": firm_user_ids,
    "firmUserFirstName": firm_names,
    "firmUserLastName": firm_user_last_names,

    "firmUserPhoto": [
        f"sample/profile_{i:05d}.jpg"
        for i in range(N)
    ],

    "firmId": firm_ids,

    "firmLogo": [
        f"https://example.com/sample-logo/{i:05d}.png"
        for i in range(N)
    ],

    "firmUserFullName": firm_user_full_names,

    "productCount": np.random.choice(
        [0, 1, 2],
        size=N,
        p=[0.98, 0.015, 0.005]
    ).astype(float),

    "featuringProduct": [False] * N,

    "superRealty": np.random.choice(
        ["false", "true"],
        size=N,
        p=[0.95, 0.05]
    ),

    "firmSummaryPackageCategoryTypeId": np.random.randint(
        0,
        181316,
        size=N
    ).astype(float),

    "buildStateId": build_state_ids.astype(str),
    "buildStateName": build_state_names,

    "furnished": furnished,

    "sideName": np.random.choice(
        [
            "Doğu",
            "Batı",
            "Kuzey",
            "Güney",
            "Doğu,Kuzey",
            "Doğu,Güney",
            "Kuzey,Batı",
            "Doğu,Kuzey,Güney,Batı"
        ],
        size=N
    ),

    "fuelName": fuel_names,

    "heatingName": heating_names,
    "heatingId": heating_ids,

    "amount": np.zeros(N),

    "currencycode": ["TL"] * N,

    "creditName": credit_names,

    "productIds": [
        ""
        for _ in range(N)
    ]
})


# ============================================================
# INTRODUCE SOME MISSING VALUES
# ============================================================

missing_rates = {
    "age": 0.15,
    "floorName": 0.18,
    "floorId": 0.18,
    "floorCount": 0.42,
    "firmUserPhoto": 0.32,
    "firmId": 0.08,
    "firmLogo": 0.13,
    "buildStateId": 0.35,
    "buildStateName": 0.37,
    "fuelName": 0.48,
    "heatingName": 0.17,
    "heatingId": 0.17,
    "sideName": 0.99,
    "productIds": 0.99,
    "currencycode": 0.80
}

for column, rate in missing_rates.items():

    mask = np.random.random(N) < rate

    df.loc[mask, column] = np.nan


# ============================================================
# SAVE
# ============================================================

import os

# data klasörünü oluştur
os.makedirs("data", exist_ok=True)

# Synthetic dataset'i data klasörüne kaydet
df.to_csv(
    "data/sample_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("========================================")
print("Synthetic dataset created successfully!")
print("========================================")
print(f"Rows   : {len(df)}")
print(f"Columns: {len(df.columns)}")
print("File   : data/sample_data.csv")
print("========================================")
print("\nColumn names:")
print(df.columns.tolist())