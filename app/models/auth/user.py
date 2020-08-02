from app import db, datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tabelname__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True, comment='用戶編號')
    username = db.Column(db.String(30), nullable=False, unique=True, comment='用戶登入名稱')
    email = db.Column(db.String(200), nullable=False, unique=True, comment='用戶信箱')
    _hash_pwd = db.Column(db.String(300), nullable=False, comment='用戶密碼')
    # 與角色連結
    rid = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, comment='用戶角色類型:1.管理者 2.主要用戶 3.被動用戶')
    name = db.Column(db.String(30), nullable=True, comment='用戶姓名')
    info = db.Column(db.Text(500), comment='用戶其他資訊')
    create_at = db.Column(db.DateTime, nullable=True, comment='用戶建立時間')
    update_at = db.Column(db.DateTime, nullable=True, comment='用戶修改時間')
    # 外鍵

    # 將密碼設定為不可讀取
    @property
    def pwd(self):
        raise Exception('密碼不可讀取')

    # 將密碼加密
    @pwd.setter
    def pwd(self, pwd):
        self._hash_pwd = generate_password_hash(pwd)

    def __init__(self, username, email, pwd, rid, name, info):
        self.username = username
        self.email = email
        self.pwd = pwd
        self.rid = rid
        self.name = name
        self.info = info
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

    def check_hash_pwd(self, pwd):
        return check_password_hash(self._hash_pwd, pwd)

    @staticmethod
    def create(username, email, pwd, rid=3, name='', info=''):
        data = User(username, email, pwd, rid, name, info)
        db.session.add(data)
        db.session.commit()
        return User.query.filter_by(username=username).all()[-1]

    @staticmethod
    def read(id=None):
        if id:
            return User.query.get(id)
        else:
            return User.query.all()

    @staticmethod
    def update(id, org_pwd='', username='', email='', pwd='', rid=0, name='', info=''):
        data = User.read(id)
        if org_pwd == '' and username == '' and email == '' and pwd == '' and rid == 0 and name == '' and info == '':
            return data
        # 修改資料則先驗證密碼正確
        if data.check_hash_pwd(org_pwd):
            if not username == '':
                data.username = username
            if not email == '':
                data.email = email
            if not pwd == '':
                data.pwd = pwd
            if not rid == 0:
                data.rid = rid
            if not name == '':
                data.name = name
            if not info == '':
                data.info = info
        else:
            return f"Org Pass Error."
        data.update_at = datetime.now()
        db.session.add(data)
        db.session.commit()
        return f"{User.read(id)} update at {data.update_at}"

    @staticmethod
    def delete(id):
        data = User.read(id)
        db.session.delete(data)
        db.session.commit()
        return f"{data} be delete"
