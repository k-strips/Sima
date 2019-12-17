#import flask-assets
from flask_assets import Environment, Bundle
from .. import create_app

app = create_app()

bundles = {
    'web_css': Bundle(
        'scss/web.scss',
        filters='libsass, cssmin',
        output='gen/css/web.css'),
    'admin_css': Bundle(
        'scss/admin.scss',
        filters='libsass, cssmin',
        output='gen/css/admin.css'),
}

assets = Environment(app)

assets.register(bundles)
