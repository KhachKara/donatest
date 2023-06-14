import requests

s = f'https://core.telegram.org/bot' \
    f'{TOKEN}/sendMessage?chat_id=42791670&text={datetime.now()} ::: ' \
    f'{err.__class__} ::: {err}'


class TelegramBotInit:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def prepare_url(self, method: str):
        result_url = f'{self.base_url}/bot{self.token}/'
        if method is not  None:
            result_url += method
        return result_url

    def post(self, method: str = None, params: dict = None, body: dict = None ):
        url = self.prepare_url(method)
        resp = requests.post(url, params=params, data=body)
        return resp.json