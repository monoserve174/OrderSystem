from app import db, datetime


class Role(db.Model):
    __tabelname__ = 'role'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True, comment='角色編號')
    name = db.Column(db.String(20), nullable=False, unique=True, comment='角色名稱')
    info = db.Column(db.Text(500), comment='角色其他資訊')
    create_at = db.Column(db.DateTime, nullable=True, comment='角色建立時間')
    update_at = db.Column(db.DateTime, nullable=True, comment='角色修改時間')
    # 外鍵
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __repr__(self):
        return f'<Role {self.id}: {self.name}>'

    @staticmethod
    def create(name, info=''):
        data = Role(name, info)
        db.session.add(data)
        db.session.commit()
        return Role.query.filter_by(name=name).all()[-1]

    @staticmethod
    def read(id=None):
        if id:
            return Role.query.get(id)
        else:
            return Role.query.all()

    @staticmethod
    def update(id, name='', info=''):
        data = Role.read(id)
        if name == '' and info == '':
            return data
        if not name == '':
            data.name = name
        if not info == '':
            data.info = info
        data.update_at = datetime.now()
        db.session.add(data)
        db.session.commit()
        return f"{Role.read(id)} update at {data.update_at}"

    @staticmethod
    def delete(id):
        data = Role.read(id)
        db.session.delete(data)
        db.session.commit()
        return f"{data} be delete"
