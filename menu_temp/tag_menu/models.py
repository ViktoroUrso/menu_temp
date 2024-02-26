'''Tag Menu Model module'''
from django.db import models


class TagMenu(models.Model):
    '''TagMenu class.'''
    name = models.CharField(
        max_length=255,
        help_text='Menu item',
        null=False,
        unique=True
        )
    url = models.CharField(
        default='menu/',
        max_length=255
        )
    left = models.IntegerField(
        blank=True,
        null=True
        )
    right = models.IntegerField(
        blank=True,
        null=True
        )
    parent = models.ForeignKey(
        to='self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
        )
    level = models.IntegerField(
        blank=True,
        null=True
        )
    root = models.ForeignKey(
        to='self',
        blank=True,
        null=True,
        related_name='head',
        on_delete=models.CASCADE
        )

    def save(self, *args, **kwargs):
        super(TagMenu, self).save(*args, **kwargs)
        self.set_menu_tree()

    def set_menu_tree(self, left=1, parent=None, level=1, root=None):
        '''Make menu tree from database data.'''
        for i in type(self).objects.filter(parent=parent):
            if i.parent is None:
                root = i
            obj, children_count = i, 0
            while obj.children.exists():
                for child in obj.children.all():
                    children_count += 1
                    obj = child
            data = {
                'level': level,
                'left': left,
                'right': left + (children_count * 2) + 1,
                'root': root
            }
            type(self).objects.filter(id=i.id).update(**data)
            left = data['right'] + 1
            self.set_menu_tree(
                left=data['left'] + 1,
                parent=i.id,
                level=data['level'] + 1,
                root=root)

    def __str__(self):
        '''String representation of TagMenu class.'''
        return str(self.name)

    def display_children(self):
        '''Sring representation of menu's child items.'''
        return '\n'.join(child.name for child in self.children.all())

    def display_parent(self):
        '''Sring representation of menu item's perent.'''
        return '\n'.join(item.name for item in TagMenu.objects.all())

    def display_root(self):
        '''Sring representation of menu's root item.'''
        return str(self.root)
