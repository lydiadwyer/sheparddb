from shepard import create_flask

application = create_flask()
if __name__ == "__main__":
    print 'wsgi::__main__'
    application.run()
