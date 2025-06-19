import requests

def main():
    game_names = ['Red Dead Redemption 2', 'The Witcher 3', 'Cyberpunk 2077', 'Doom Eternal', 'Astroneer', 'Subnautica', 'Elite Dangerous']  # Example game names
    for game in game_names:
        # Build the API URL with the game name
        request_url = f"https://www.allkeyshop.com/api/latest/vaks.php?action=CatalogV2&currency=eur&per_page=1&locale=en_US&name={game}"
        response = requests.get(request_url)
        data = response.json()

        # Check if the API call was successful (this only checks if the request was made successfully, not if the game was found)
        if data.get('status') != 'success':
            print(f"Error fetching data for {game}: {data.get('errors', 'Unknown error')}")
            continue

        # Check if the game was found in the response
        if not data.get('products'):
            print(f"Game not found: {game}")
            continue

        # Print the fetched data
        print(f"Game: {game}")
        product = data['products'][0]

        # Best official offer
        best_official_offer = product.get('best_official_offer', {})
        official_price = best_official_offer.get('price')
        official_link = best_official_offer.get('buy_url')
        official_voucher = best_official_offer.get('voucher')

        # Best current offer (best_offer)
        best_offer = product.get('best_offer', {})
        offer_price = best_offer.get('price')
        offer_link = best_offer.get('buy_url')
        offer_voucher = best_offer.get('voucher')

        print(f"  - Best Official Offer: {official_price} EUR, Link: {official_link}, Voucher: {official_voucher}")
        print(f"  - Best Current Offer: {offer_price} EUR, Link: {offer_link}, Voucher: {offer_voucher}")

if __name__ == '__main__':
    main()