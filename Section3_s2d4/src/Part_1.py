"""
Part_1

NoSQL 데이터 입력하기 (Openweather API)

Openweather JSON 데이터가 작성되어 있습니다. 이 데이터를 MongoDB에 입력하세요
하단의 pass 라는 코드를 지우고 문제를 풀어주세요
pytest 로만 통과할 수 없습니다. `python src/Part_1.py`로 MongoDB 에 데이터를 입력하세요
- 코드에 적혀있는 대로 콜렉션 이름은 변경하지 말아주세요!

# 클라우드 데이터베이스는 테스트에 시간이 걸릴 수 있습니다. 기다려주세요.
"""
from pymongo import MongoClient

openweather = {
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }

"""
MONGODB SETUP
"""
#dont_touch 변수는 변경하지마세요
dont_touch = openweather.copy()


url = 'mongodb+srv://cluster0.jpu3q.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority'

HOST = 'cluster0.jpu3q.mongodb.net'
USER = 'Jang-Ji-Yeon'
PASSWORD = 'wldus1021'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'openweather'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

database_1 = client[DATABASE_NAME]
collection_1 = database_1[COLLECTION_NAME]
collection_1.insert_one(
  {
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }
  )