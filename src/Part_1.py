import requests
import json

API_KEY = 'API 키를 입력해주세요'


def get_city_data(city_name):
    """
    get_city_data 함수는 OpenWeather 에서부터 가져온 데이터를 json 형태로
    리턴해야 합니다.

    파라미터:
        - city_name: 조회할 도시 이름을 담은 문자열(str) 입니다.

    리턴:
        - 파이썬 딕셔너리: 조회한 API JSON 데이터를 파이썬 딕셔너리 형태로
        리턴합니다.
    """

    current_weather = None
    
    return current_weather



def get_weather_description(json_data):
    """
    get_weather_description 함수는 weather description, 날씨가 어떤지 알려주는 문자열을 리턴합니다.

    파라미터:
        - json_data: OpenWeather API 로부터 받아온 JSON 데이터입니다.

    리턴:
        - 날씨 정보: 주어진 데이터에서 날씨에 대해서 담고 있는 문자열(str) 을
        리턴합니다.
    """

    weather_description = None

    return weather_description


def get_minimum_temp(json_data):
    """
    get_minimum_temp 함수는 최저 온도를 섭씨(℃) 단위로 리턴해야 합니다.

    파라미터:
        - json_data: OpenWeather API 로부터 받아온 JSON 데이터입니다.

    리턴:
        - 온도 정보: 주어진 JSON 데이터에서 온도 정보를 리턴합니다.
    """

    temp_min = None

    return temp_min
