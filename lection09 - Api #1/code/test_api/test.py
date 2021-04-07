

class TestApi:

    def test_valid_login(self, api_client, credentials):
        res = api_client.post_login(*credentials)
        assert res.status_code == 200

    def test_invalid_login(self, api_client):
        res = api_client.post_login('123', '456')
        assert res.status_code == 200
        assert res.json()['bStateError'] is True
