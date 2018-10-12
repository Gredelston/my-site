import os
import tornado.ioloop
import tornado.web

import config

### Page handlers ###

class PageHandler(tornado.web.RequestHandler):
    template = "base.html"
    navbar_current = None

    def get(self):
        navbar_items = [
            {
                "name": "Home",
                "route": "/"
            },
            {
                "name": "About",
                "route": "/about"
            }
        ]
        self.render(
            self.template,
            navbar_items=navbar_items,
            navbar_current=self.navbar_current)


class HomepageHandler(PageHandler):
    template = "home.html"
    navbar_current = "Home"


class AboutPageHandler(PageHandler):
    template = "about.html"
    navbar_current = "About"


### Application logic

def make_app():
    handlers = [
        (r"/", HomepageHandler),
        (r"/home", HomepageHandler),
        (r"/index", HomepageHandler),
        (r"/about", AboutPageHandler)
    ]
    settings = {
        "static_path": config.static_path,
        "template_path": config.template_path,
        "debug": True

    }
    return tornado.web.Application(handlers, **settings)

def shutdown_app():
    print("Shutting down app.")
    tornado.ioloop.IOLoop.current().stop()


### Run the app

if __name__ == "__main__":
    app = make_app()
    app.listen(config.port)
    tornado.ioloop.IOLoop.current().start()
