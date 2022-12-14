from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user import User

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("photos.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    body = db.Column(db.String(255))

    def to_dict(self):
        user = User.query.get(self.user_id)

        return {
            "id": self.id,
            "photo_id": self.photo_id,
            "user_id": self.user_id,
            "body": self.body,
            "username": user.username
        }

    def edit_comment(self, body):
        self.body = body
        return body

    user = db.relationship("User", back_populates="comments")
    photos = db.relationship("Photo", back_populates="comments")
