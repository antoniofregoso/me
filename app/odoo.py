import xmlrpc.client


class server:
      
    def create_object(self,odoo, odoo_object, values):
        url = odoo['host']
        db = odoo['dbname']
        uid  = odoo['uid']
        password = odoo['pwd']
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        object_id = models.execute_kw(db, uid, password, odoo_object, 'create', [values])
        return object_id

    def check_contact(self,odoo, res):
        url = odoo['host']
        db = odoo['dbname']
        uid  = odoo['uid']
        password = odoo['pwd']
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        try:
            res = models.execute_kw(db, uid, password,
                                                 'res.partner', 'search_read',
                                                 [['|', ('email','=', res['email']), ('email','=', res['name'])]], 
                                                 {'fields': ['name', 'email', 'phone']})[0]['id']
        except:
            res = 0
        return res
        
    