import webapp2

from google.cloud import pubsub


class WatchPage(webapp2.RequestHandler):
    def get(self):
        pubsub_client = pubsub.Client()
        topic = pubsub_client.topic('api-scheduler')

        message_id = topic.publish('ping'.encode('utf-8'))
        self.response.write(message_id)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('This is a landing page for the FreeCon cloud scheduler for GCP!')

app = webapp2.WSGIApplication([
    ('/', MainPage), ('/watch', WatchPage),
], debug=True)
