from django.db import models
from core.base_model import BaseModel

from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


class CategoryManager(TreeManager):
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset