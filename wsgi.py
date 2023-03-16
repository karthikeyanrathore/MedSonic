
if __name__ == "__main__":
    from medsonic.app import create_app

    server_application = create_app()
    server_application.run()