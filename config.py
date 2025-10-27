# config.py
from tortoise.contrib.fastapi import register_tortoise

TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["models.author_model", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app):
    """
    Connects Tortoise ORM with FastAPI app
    and sets up Aerich migrations.
    """
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,       # False because Aerich will handle migrations
        add_exception_handlers=True,  # Helps show DB errors in Swagger UI
    )