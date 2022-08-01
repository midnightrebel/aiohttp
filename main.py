from aiohttp import web
from models import Users

from tortoise.contrib.aiohttp import register_tortoise


routes = web.RouteTableDef()

@routes.get('/index')
async def hello(request):
    return web.Response(text="Hello, world!")

@routes.get('/users')
async def list_all(request):
    users = await Users.all()
    return web.json_response({"users": [str(user) for user in users]})

@routes.get('/user')
async def add_user(request):
    user = await Users.create(name="New User")
    return web.json_response({"user": str(user)})


app = web.Application()
register_tortoise(
    app, db_url="sqlite://:memory:", modules={"models": ["models"]}, generate_schemas=True
)
app.add_routes(routes)
web.run_app(app)
