import requests
import requests_cache
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")  # Private API key omitted


def get_encrypted_summoner_id(summoner):
    summoner_response = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s" %
                                     (summoner, API_KEY))

    response = summoner_response.json()

    if summoner_response.status_code == 200:
        return response["id"], response["summonerLevel"]

    elif response.status_code == 404:
        raise Exception("Invocador inexistente")

    else:
        raise Exception("Request error. Status code:", summoner_response.status_code)


def get_champion_name(champions, champion_id):
    for champion in champions["data"]:
        if champions["data"][champion]["key"] == champion_id:
            return champions["data"][champion]["name"]


def main():
    print("Verifique a sua maestria em League of Legends!")
    print()

    requests_cache.install_cache("cache")

    versions_response = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
    newest_version = versions_response.json()[0]

    champions_response = requests.get("http://ddragon.leagueoflegends.com/cdn/%s/data/pt_BR/champion.json" %
                                      newest_version)
    champions = champions_response.json()

    summoner = input("Forneça o seu nome de invocador (servidor Brasileiro): ")
    encrypted_summoner_id, summoner_level = get_encrypted_summoner_id(summoner)

    mastery_response = requests.get("https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-"
                                    "summoner/%s?api_key=%s" % (encrypted_summoner_id, API_KEY))
    mastery = mastery_response.json()

    top_three_mastery = mastery[:3]

    print("%s - Nível de invocador %d\nSeus top 3 campeões:" % (summoner, summoner_level))
    print()

    for i, mastered in enumerate(top_three_mastery):
        print("%d - %s: %d pontos" % (i+1, get_champion_name(champions, str(mastered["championId"])),
                                      mastered["championPoints"]))


if __name__ == "__main__":
    main()
