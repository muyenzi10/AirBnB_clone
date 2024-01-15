#!/usr/bin/python3
from datetime import datetime
import uuid
class BaseModel:
    def __init__(self, *args, **kwargs):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, t_format))
                else:
                    setattr(self, k, v)
    def save(self):
        self.updated_at = datetime.utcnow()
    def to_dict(self):
        """
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = __class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    def __str__(self):
        my_obj = __class__.__name__
        return "[{}] [{}] [{}]".format(my_obj, self.id, self.__dict__)
