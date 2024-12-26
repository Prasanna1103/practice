import click
import requests

@click.command()
@click.argument('bitcoins', required=False, default='1')
def main(bitcoins):
    try:
        bitcoins = float(bitcoins)
    except ValueError:
        raise click.BadParameter("The number of Bitcoins must be a numeric value.")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()

        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]

        total_cost = bitcoins * price_per_bitcoin
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        click.echo("Error", err=True)

if __name__ == "__main__":
    main()
