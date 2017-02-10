# caddy
The next big thing


# Bootstrap
```
# Set up your environment
$ cd lander
$ virtualenv env
$ source env/bin/activate

$ pip install fabric  # If this is not already installed globally.
# Bootstrap dependencies
$ fab bootstrap
```

# Testing
```
# After bootstrapping
$ fab test
```

# Running locally
```
# Run a local server
fab serve
```

# Usage
* Add a new page route to lander/__init__.py
* Set a template for the route, defaults to home.html
* Edit development.yaml and production.yaml with appropriate variables to include your new page

You may include mailchimp and google analytics options by manually updating the template.
You can also show/hide sections of a template by using the 'show' booleans.

Place all images in the `static/img/` folder.

# Migrations on production (Heroku)
```
# Migrate to head.
heroku db upgrade head

# Upgrade +X revisions.
heroku db upgrade +1

# Downgrade -X revisions.
heroku db downgrade -1
```

# Deploying to Heroku
```
# Deploys on push.
$ git heroku push master
```

# Future Work
More templates to come, and more dynamic pages will be added in the future.


