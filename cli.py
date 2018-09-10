from ebooks import MastodonEbooks
import click

@click.group()
def cli():
	pass

@cli.command()
@click.option("--api-url", default="https://botsin.space")
def setup(api_url):
	click.echo("Performing first-time setup...")
	ebooks = MastodonEbooks({
		"api_base_url": api_url
		})
	ebooks.setup()

@cli.command()
@click.option("--api-url", default="https://botsin.space")
@click.option("--post", default=False, help="Automatically post the generated toot.")
def gen(api_url, post):
	click.echo("Generating a toot...")
	ebooks = MastodonEbooks({
		"api_base_url": api_url
		})
	toot = ebooks.gen_toot()
	click.echo(toot)
	post = post if post else input("Do you want to post this toot? [yN] ")
	if post:
		click.echo("Posting toot...")
		ebooks.post_toot(toot)
		click.echo("Tooted!")

if __name__ == '__main__':
	cli()
