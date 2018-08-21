from app.utils.feedly_client import FeedlyClient

feedly = FeedlyClient(
    client_id="sandbox",  # https://groups.google.com/forum/#!topic/feedly-cloud/9hUAAjulF30
    client_secret="LbQeeuE3YjcKwDBU",  # (expires on October 1st 2018)
    sandbox=True
)

res = feedly.search("react", 100)
res = res.json()
pass
