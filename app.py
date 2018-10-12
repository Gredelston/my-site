import os
import tornado.ioloop
import tornado.web

import config

### Page handlers ###

class PageHandler(tornado.web.RequestHandler):
    template = "base.html"
    navbar_display_text = None
    navbar_items = [
        {
            "display-text": page["navbar-display-text"],
            "route": page["route"]
        } for page in config.pages if page["navbar-display"]
    ]

    def get(self):
        self.render(
            self.template,
            navbar_items=self.navbar_items,
            navbar_current=self.navbar_display_text)


### Application logic

def make_app():
    handlers = create_route_handlers(config.pages)
    settings = {
        "static_path": config.static_path,
        "template_path": config.template_path,
        "debug": True
    }
    return tornado.web.Application(handlers, **settings)


def create_route_handlers(pages):
    handlers = []
    for page in pages:
        route = page["route"]
        handler_name = page["name"] + "Handler"
        handler_attributes = {
            "template": page["template"],
            "navbar_display_text": page.get("navbar-display-text", None)
        }
        page_handler = type(handler_name, (PageHandler, ), handler_attributes)
        handlers.append((route, page_handler))
    return handlers


def shutdown_app():
    print("Shutting down app.")
    tornado.ioloop.IOLoop.current().stop()


### Run the app

if __name__ == "__main__":
    app = make_app()
    app.listen(config.port)
    tornado.ioloop.IOLoop.current().start()
