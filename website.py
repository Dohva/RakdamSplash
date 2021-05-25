# website.py

from splashgen import launch
from splashgen.components import SplashSite, CTAButton

site = SplashSite(title="Integrating CI via Github Actions",
                  theme="dark")
site.enable_splashgen_analytics = False
site.headline = "Never run another console command again."
site.subtext = """
Just build it in the cloud. It's easy. Automate everything and anything.
This is python, but it'll work for nearly all languages you'll use.
It's just good practice :-)
"""
site.call_to_action = CTAButton(
    "https://github.com/Dohva/RakdamSplash", "View on GitHub")

launch(site)