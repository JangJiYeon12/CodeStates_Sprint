import tweepy

def connect_api():
    """
    connect_api 함수는 tweepy 로 API 를 연결한 'api' 객체를 리턴합니다.

    Hint: api 객체는 tweepy.API 로 만들 수 있습니다.
    """

    api_key = 'API 키를 입력해주세요'
    api_key_secret = 'API 비밀 키를 입력해주세요'
    access_token = 'Access 토큰을 입력해주세요'
    access_token_secret = '비밀 access 토큰을 입력해주세요'

    api = None

    return api


def get_tweets(api, username):
    """
    'username' 이 주어지면 해당 유저의 트윗들을 가지고 올 수 있어야 합니다.
    각 트윗은 140 자 이상이어도 모든 내용을 가지고 올 수 있어야 합니다.

    Hint: 'tweet_mode' 에 대해서 알아보세요!
    """

    tweets = None

    return tweets
