import requests

from models import Post, Session


def main():
    session = Session()
    items = get_items()

    if items:
        delete_items(session)
        save_items(items, session)
    session.git commit()
    session.close()


def get_items():
    """Get posts from API."""
    endpoint = 'https://jsonplaceholder.typicode.com/posts'

    r = requests.get(endpoint)
    return r.json()


def save_items(items, session):
    """Save posts to DB."""
    for item in items:
        post = Post()
        post.id = item['id']
        post.userId = item['userId']
        post.title = item['title']
        post.body = item['body']
        session.add(post)

def delete_items(session):
    """Delete all posts."""
    session.query(Post).delete(synchronize_session=False)


if __name__ == "__main__":
    main()
