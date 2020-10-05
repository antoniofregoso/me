import xmlrpc.client
from config import Config 


class server:

    def __init__(self):
        odoo = Config.ODOO
        self.host = odoo['host']
        self.db = odoo['dbname']
        self.username = odoo['user']
        self.password = odoo['pwd']

    def cnn(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.host))
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.host))


    def get(self, model, domain = [], fields=[]):
        res = self.models.execute_kw(self.db, self.uid, self.password, model, 'search_read', domain, fields)
        return res

    def create(self, model, values):
        id = self.models.execute_kw(self.db, self.uid, self.password, model, 'create', [values])
        return id





    