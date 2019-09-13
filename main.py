import requests
import requests_cache


def main():
    print("Verifique a sua maestria em League of Legends!")

    requests_cache.install_cache("cache")

    champions_response = requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/pt_BR/champion.json")

    if champions_response.status_code != 200:
        print("Request error. Status code:", champions_response.status_code)


if __name__ == "__main__":
    main()
