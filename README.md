# Purdue University's Programming Languages Group

Welcome!

## Adding/Updating Members

Open an issue! We have a template for adding new members to the website. If you want to update your information or add a picture, just open a normal issue or submit a pr.

## Testing the Website

Either:

- Install Ruby and subsequent dependencies. Then use `./serve`
- Install Docker and run `docker run --rm --volume="${PWD}:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:3.8 jekyll serve --incremental --drafts --config _config.yml` from the root of this project
