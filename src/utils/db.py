
# class SqlHelper:
#     engine: Engine = None
#     session: Session = None
 
#     def __init__(self):
#         Session = sessionManager.get_session(db_type=Constant.DB_TYPE)
#         self.session = Session()
#         self.engine = sessionManager.get_engine(db_type=Constant.DB_TYPE)
 
#     def add(self, obj):
#         self.session.add(obj)
#         self.session.commit()
 
#     def delete(self, obj):
#         self.session.delete(obj)
#         self.session.commit()
 
#     def update(self, obj):
#         self.session.merge(obj)
#         self.session.commit()
 
#     def upsert(self, model):
#         self._upsert(model)
#         self.session.commit()
 
#     def query(self, model):
#         return self.session.query(model)