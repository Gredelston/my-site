import os
import tornado.ioloop
import tornado.web

import config

### Page handlers ###

class PageHandler(tornado.web.RequestHandler):
    template = "base.html"
    navbar_item = None

    def get(self):
        navbar_items = [
            {
                "name": "Home",
                "route": "/"
            },
            {
                "name": "About",
                "route": "/about"
            },
            {
                "name": "Shutdown",
                "route": "/shutdown"
            }
        ]
        self.render(
            self.template,
            navbar_items=navbar_items,
            navbar_selected=self.navbar_item
        )


class HomepageHandler(PageHandler):
    template = "home.html"
    navbar_item = "Home"


class AboutPageHandler(PageHandler):
    template = "about.html"
    navbar_item = "About"


class ShutdownHandler(PageHandler):
    template = "shutdown.html"
    navbar_item = "Shutdown"

    def get(self):
        PageHandler.get(self)
        shutdown_app()


### Application logic

def make_app():
    handlers = [
        (r"/", HomepageHandler),
        (r"/home", HomepageHandler),
        (r"/index", HomepageHandler),
        (r"/about", AboutPageHandler),
        (r"/shutdown", ShutdownHandler)
    ]
    settings = {
        "static_path": config.static_path,
        "template_path": config.template_path

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