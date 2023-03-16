import multiprocessing
import gunicorn.app.base

HOST = "0.0.0.0"
PORT = "8080"

class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == "__main__":
    from medsonic.app import create_app
    server_application = create_app()
    options = {
        "bind": "%s:%s" % (HOST, PORT),
        "workers": (multiprocessing.cpu_count() * 2) + 1,
        "worker_class": "tornado",
    }
    StandaloneApplication(server_application, options).run()
