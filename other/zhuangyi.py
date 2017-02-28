from django.utils.safestring import mark_safe

def get_username(self):
      return mark_safe("<a href='/accounts/%s/'>%s</a>" %('12', 'blx'))


if __name__ == "__main__":

    pass