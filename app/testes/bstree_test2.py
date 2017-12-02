import json

def export_balance_sheet():

    cnx = mariadb.connect(user='root', password='', database='test')
    cursor = cnx.cursor()

    pdc = "pdc_teste"

    query = """
            SELECT
                t1.account AS Level1,
                t2.account AS Level2,
                t3.account AS Level3,
                t4.account AS Level4

            FROM %s AS t1

            LEFT JOIN pdc_teste AS t2 ON t2.parent = t1.code
            LEFT JOIN pdc_teste AS t3 ON t3.parent = t2.code
            LEFT JOIN pdc_teste AS t4 ON t4.parent = t3.code

            WHERE
                t1.account = 'Ativo' OR
                t1.account = 'Passivo';
            """ % (pdc)
    
    cursor.execute(query)
    rows = cursor.fetchall()
    desc = cursor.description
    cnx.close()        
        
    lista = [dict(itertools.izip([col[0] for col in desc], row)) 
        for row in rows]

    cnx.close()

    bs_tree = json.dumps(lista)

results = export_balance_sheet()


class Node(object):
    def __init__(self, component=None, status=None, level=0):
        self.component = component
        self.status    = status
        self.level     = level
        self.children  = []

    def __repr__(self):        
        return '\n{indent}Node({component},{status},{children})'.format(
                                         indent = self.level*'\t', 
                                         component = self.component,
                                         status = self.status,
                                         children = repr(self.children))
    def add_child(self, child):
        self.children.append(child)    

def tree_builder(obj, level=0):
    node = Node(component=obj['component'], status=obj['status'], level=level)
    for child in obj.get('children',[]):
        node.add_child(tree_builder(child, level=level+1))
    return node

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

obj = load_json('test.json')
tree = tree_builder(obj)
print tree