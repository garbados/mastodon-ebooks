from ebooks import MastodonEbooks
import click

@click.group()
def cli():
	pass

@cli.command()
@click.option("--api-url", default="https://botsin.space", help="The instance hosting your bot account.")
def setup(api_url):
	"""
	Perform first-time setup.
	Registers the application and retrieves toots.
	"""
	click.echo("Performing first-time setup...")
	ebooks = MastodonEbooks({
		"api_base_url": api_url
		})
	ebooks.setup()

@cli.command()
@click.option("--api-url", default="https://botsin.space", help="The instance hosting your bot account.")
@click.option("--post", default=False, is_flag=True, help="Automatically post the generated toot.")
def gen(api_url, post):
	"""
	Generate a toot.
	Optionally require approval before posting.
	"""
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
