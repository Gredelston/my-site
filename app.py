import os
import tornado.ioloop
import tornado.web

import config

### Page handlers ###

class PageHandler(tornado.web.RequestHandler):
    def write_headers(self):
        self.write('<link rel="stylesheet" href="{}">'.format(
            os.path.join(config.static_files_dir, 'navbar.css')
        ))
        self.write_navbar()

    def write_newline(self):
        self.write("<br>")
    
    def write_navbar(self):
        self.write("<ul id='navbar'>")
        self.write_navbar_item("Home", "/home")
        self.write_navbar_item("About", "/about")
        self.write_navbar_item("Shutdown", "/shutdown")
        self.write("</ul>")
    
    def write_navbar_item(self, name, route):
        self.write("<li class='navbar-item'><a href='{}'>{}</a></li>".format(
            route,
            name
        ))

class HomepageHandler(PageHandler):
    def get(self):
        self.write_headers()
        self.write("Hello, world!")

class AboutPageHandler(PageHandler):
    def get(self):
        self.write_headers()
        self.write("About")

class ShutdownHandler(PageHandler):
    def get(self):
        self.write_headers()
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
        "static_path": os.path.join(os.path.dirname(__file__), "static")
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