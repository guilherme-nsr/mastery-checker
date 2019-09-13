import requests
import requests_cache


API_KEY = ""  # Private API key omitted


def get_encrypted_summoner_id(summoner):
    response = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=%s" %
                            (summoner, API_KEY))

    if response.status_code == 200:
        return response.json()["id"]

    elif response.status_code == 404:
        raise Exception("Invocador inexistente")

    else:
        raise Exception("Request error. Status code:", response.status_code)


def get_champion_name(champions, champion_id):
    for champion in champions["data"]:
        if champions["data"][champion]["key"] == champion_id:
            return champion


def main():
    print("Verifique a sua maestria em League of Legends!")
    print()

    requests_cache.install_cache("cache")

    champions_response = requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/pt_BR/champion.json")
    champions = champions_response.json()

    summoner = input("Forneça o seu nome de invocador (servidor Brasileiro): ")
    encrypted_summoner_id = get_encrypted_summoner_id(summoner)

    mastery_response = requests.get("https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-"
                                    "summoner/%s?api_key=%s" % (encrypted_summoner_id, API_KEY))

    mastery = mastery_response.json()

    top_three_mastery = mastery[:3]

    for mastered in top_three_mastery:
        print("%s: %d pontos" % (get_champion_name(champions, str(mastered["championId"])), mastered["championPoints"]))


if __name__ == "__main__":
    main()
