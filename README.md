# mastodon-ebooks

A tool to create and administer [Markov](https://en.wikipedia.org/wiki/Markov_chain) bots for [Mastodon](https://joinmastodon.org/). Use it to create and administer your very own ebooks.

Based on the [Lynnesbian](https://github.com/Lynnesbian/mastodon-ebooks) fork of [Jess3Jane](https://github.com/Jess3Jane/mastodon-ebooks)'s ebooks helper.

## Install

This tool is not currently on [PyPI](https://pypi.org/) and so requires you to install it from source using [git](https://git-scm.com/) and [pip](https://pip.pypa.io/en/stable/installing/):

```bash
$ git clone garbados/mastodon-ebooks
$ cd mastodon-ebooks
$ pip install -r requirements.txt
$ python cli.py setup
No clientcred.secret, registering application
No usercred.secret, registering application
Email: you@whatever.online
Password: ...
Downloading toots for user @you
```

Though the tool asks for your login information, it does not retain it in any way. It only saves the access credentials granted by your instance, which you can revoke at any time from your instance's web interface.

By default, setup assumes your bot lives on [botsin.space](https://botsin.space), but you can specify otherwise with the `--api-url` option, like this:

```bash
$ python cli.py setup --api-url https://toot.cat
```

## Usage

To generate a toot, use the `gen` command. It will ask you to confirm if you want to post this toot, as [a bot's administrator is responsible for its actions](http://mewo2.com/notes/bot-ethics/).

```bash
$ python cli.py gen
Generating a toot...
[extremely surreal content]
Do you want to post this toot? [yN]
```

For additional usage information, use the `--help` flag to print help text:

```bash
$ python cli.py --help
$ python cli.py setup --help
$ python cli.py gen --help
```

## Testing

This project has no test suite currently. Not even a linter! It's pretty barebones. If you'd like to fix this, please submit a [pull request](https://github.com/garbados/mastodon-ebooks/pulls).

## Contributing

All contributions are welcome, but are subject to moderation at the sole discretion of project maintainers.

To request a feature or report a bug, please file an [issue](https://github.com/garbados/mastodon-ebooks/issues).

To submit a patch, please file a [pull request](https://github.com/garbados/mastodon-ebooks/pulls).

## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
