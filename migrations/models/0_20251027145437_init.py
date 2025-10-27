from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "author" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "age" INT NOT NULL,
    "password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlW9P2zAQxr9KlVdMYhOEMtDelUrThrYisT+ahFDkxm5i1bGDfRkglO8+n5PgNE06kJ"
    "hWBK+aPPc4vvvprncXZIoyYd5NCkiVDj6M7gJJMmYfOpHdUUDy3OsoAJkLZyXeMzegSQxW"
    "XRBhmJUoM7HmOXAlrSoLIVBUsTVymXipkPyqYBGohEHKMJeLSytzSdkNM81rvowWnAm6ki"
    "qneLfTI7jNnfZZwkdnxNvmUaxEkUlvzm9tyvLezSWgmjDJNAGGnwddYPqYXV1nU1GVqbdU"
    "KbbOULYghYBWuQ9kECuJ/Gw2xhWY4C1vw/3x0fj44P342FpcJvfKUVmV52uvDjoCs+9B6e"
    "IESOVwGD0397tGbpoS3Y+u8Xfg2ZS78BpUm+g1gsfnW+aJ+GXkJhJMJpDa1/29vQ20fk7O"
    "p58m5zvW9QarUbaNq+6e1aGwiiFSj5AkPQQHe692/735toTfk/Sfh5UTY66V7pnW4Z5rn3"
    "mefRceHj6g76xrsO9crCzx/2+xbE0yCnMSL6+JptFaRIVqyLseysKsqxBp25XWRWIFzUZg"
    "msdp766oIpt3hfe87oqtm9XhXfGbaYMpPWJ0W0de+OSubAw7Go+AWNufJ8B/snLtjcCqGV"
    "yFePrtbNYPsXWkA/KHtAVeUB7D7khwA5fbiXUDRawak86MuRJteDtfJ7+6XKdfzk4cBWUg"
    "0e4r7gMn/3u9lH8Ak3j7yw=="
)
