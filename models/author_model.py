from tortoise import fields, models

class Author(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    age = fields.IntField()

    def __str__(self):
        return self.name
