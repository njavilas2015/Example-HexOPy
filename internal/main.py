from hexopy.server import create_app, HexoServer
from pkg.crm.main import Module as CRM

server: HexoServer = create_app(port=8000)

crm = CRM(server.config).init()