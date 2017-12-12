# from app import app
# from app import db

# db = SQLAlchemy(app)


# ######################## MAIN TABLES ########################


# #Defines General Journal Structure
# class Journal(db.Model):
#     id =        db.Column(db.Integer, primary_key=True)
#     datecash =  db.Column(db.Date)
#     dateacc =   db.Column(db.Date)
#     ref =       db.Column(db.Integer)
#     credit =    db.Column(db.String(64), index=True, foreign_key='Accounts.account')
#     debit =     db.Column(db.String(64), index=True, foreign_key='Accounts.account')
#     description=db.Column(db.String(200))
#     value =     db.Column(db.Float(2))


# #Defines Chart of Accounts structure
# class Accounts(db.Model):
#     id =        db.Column(db.Integer, primary_key=True)
#     code =      db.Column(db.Integer(11))
#     report =    db.Column(db.String(64))
#     account =   db.Column(db.String(64), index=True)
#     level =     db.Column(db.String(64))
#     parent =    db.Column(db.String(64), index=True)
#     nature =    db.Column(db.String(11))
#     isactive =  db.Column(db.Boolean, default=1)
#     iscash =    db.Column(db.Boolean, default=0)

#     journal =   db.relationship('Journal', backref='', lazy='dynamic')
 

# ######################## BILLS TABLES ########################

# class Bills(db.Model):
#     id =                    db.Column(db.Integer, primary_key=True)
#     dateAcc =               db.Column()
#     supplier =              db.Column()
#     account =               db.Column()
#     value =                 db.Column()
#     frequency =             db.Column()
#     repetition_start =      db.Column()
#     repetition_end =        db.Column()





# ######################## BUDGETS & FORECAST TABLES ########################

# class Budgets(db.Model):
#     id =                    db.Column(db.Integer, primary_key=True)
#     dateAcc =               db.Column()
#     account =               db.Column()
#     budgeted =              db.Column()
#     frequency =             db.Column()
#     repetition_start =      db.Column()
#     repetition_end =        db.Column()



# ######################## RULES TABLES ########################


# class Rules(db.Model):
#     id =            db.Column(db.Integer, primary_key=True)
#     extrato =       db.Column()
#     account =       db.Column()



# class RulesActions(db.Model):
#     user_id =       db.Column()
#     role_id =       db.Column()


# class RulesTriggers(db.Model):
#     user_id =       db.Column()
#     role_id =       db.Column()



# ######################## SUPORTING TABLES ########################

# class Attachments(db.Model):
#     id =                db.Column(db.Integer, primary_key=True)
#     journal_ref =       db.Column()
#     filename =          db.Column()
#     type =              db.Column()
#     title =             db.Column()
#     description =       db.Column()
#     notes =             db.Column()
#     size =              db.Column()
#     uploaded =          db.Column()


# class AttachmentType(db.Model):
#     id =                db.Column(db.Integer, primary_key=True)
#     journal_ref =       db.Column()
#     filename =          db.Column()
#     type =              db.Column()
#     title =             db.Column()
#     description =       db.Column()
#     notes =             db.Column()
#     size =              db.Column()
#     uploaded =          db.Column()


# class Tags(db.Model):
#     user_id =       db.Column(db.Integer, primary_key=True)
#     role_id =       db.Column()




# # ######################## CONFIG TABLES ########################

# # class Preferences(db.Model):
# #     id =            db.Column(db.Integer, primary_key=True)
# #     timestamps =    db.Column()
# #     user_id =       db.Column()
# #     name =          db.Column()
# #     data =          db.Column()



# # class Users(db.Model):
# #     id =            db.Column(db.Integer, primary_key=True)
# #     email =         db.Column()
# #     username =      db.Column()
# #     password =      db.Column()


