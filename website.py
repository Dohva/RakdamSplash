# website.py

from splashgen import launch
from splashgen.components import SplashSite, CTAButton

site = SplashSite(title="Splashgen - Splash Pages Built In Python",
                  theme="dark")
site.enable_splashgen_analytics = False
site.headline = "Build your splash page in python effortlessly"
site.subtext = """
In less than 20 lines of python, create clean and beautiful splash pages with
Splashgen. Don't waste time with no-code tools when you already know how to
code.
"""
site.call_to_action = CTAButton(
    "https://github.com/true3dco/splashgen", "View on GitHub")

launch(site)