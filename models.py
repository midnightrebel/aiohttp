from tortoise import Model, fields

TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:bayonet@localhost:5432/test"},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
class Users(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50)

    def __str__(self):
        return f"User {self.id}: {self.name}"

