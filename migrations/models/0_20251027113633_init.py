from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "author" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "age" INT NOT NULL
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
    "eJztlW9r2zAQxr9K8KsOutF66Vr2Lg2MbWwpdH8YlGIUW7FFZMmVzltLyXffnWRXrpN4LX"
    "Qshb1K/Nxj67kf5/NtVOqMS/tqUkOhTfR2dBspVnL806vsjyJWVUEnAdhcOisLnrkFw1JA"
    "dcGk5Shl3KZGVCC0QlXVUpKoUzQKlQepVuKq5gnonEPBKcvFJcpCZfya2/ayWiYLwWV2L6"
    "rI6GynJ3BTOe2DgnfOSKfNk1TLulTBXN1gZHXnFgpIzbnihgGnx4OpKT6la/psO/JJg8VH"
    "7NyT8QWrJXTafSCDVCvih2msazCnU17Gh+Pj8cnrN+MTtLgkd8rxyrcXevc3OgKzr9HK1R"
    "kw73AYAzf3u0ZuWjCzGV3r78HDyH14Laoheq0Q8IWReSJ+JbtOJFc5FHh5eHAwQOv75Hz6"
    "fnK+h64X1I3GMfbTPWtKsa8R0oCQ5RsIbp29xv3n4dsRfk8wf/TSLpad8SNhztLlL2ayZK"
    "2iY73Nu14q47KvMIWMs6YjCteuMW5EWmxccL4yvOCC5/+C27EBG1pwP7mxFOkRO65zy/Nc"
    "c/HR0QPWHLq2rjlX6605fDUeAbGxP0+Af+U7gScC9+/gfYgfv5zNNkPs3NID+U1hgxeZSG"
    "F/JIWFy93EOkCRuqbQpbVXsgtv7/PkR5/r9NPZqaOgLeTGPcU94PRff15WvwHUPZIn"
)
