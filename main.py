import requests
import requests_cache


API_KEY = ""  # Private API key omitted


def get_encrypted_summoner_id(summoner):
    response = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s" %
                            (summoner, API_KEY))

    if response.status_code == 200:
        return response.json()["id"]

    else:
        print("Request error. Status code:", response.status_code)


def main():
    print("Verifique a sua maestria em League of Legends!")

    requests_cache.install_cache("cache")

    champions_response = requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/pt_BR/champion.json")

    if champions_response.status_code != 200:
        print("Request error. Status code:", champions_response.status_code)


if __name__ == "__main__":
    main()
