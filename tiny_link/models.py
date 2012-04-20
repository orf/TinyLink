from django.db import models
import string

_char_map = [x for x in string.ascii_letters+string.digits]

def index_to_char(sequence):
    return "".join([_char_map[x] for x in sequence])


class Link(models.Model):
    link = models.URLField()
    # Store the total redirects here so we don't need to do a possibly expensive SUM query on HitsDatePoint
    hits = models.IntegerField(default=0)

    def __repr__(self):
        return "<Link (Hits %s): %s>"%(self.hits, self.link)

    def get_short_id(self):
        _id = self.id
        digits = []
        while _id > 0:
            rem = _id % 62
            digits.append(rem)
            _id /= 62
        digits.reverse()
        return index_to_char(digits)

    @staticmethod
    def decode_id(string):
        i = 0
        for c in string:
            i = i * 64 + _char_map.index(c)
        return i



class HitsDatePoint(models.Model):
    day = models.DateField(auto_now=True, db_index=True)
    hits = models.IntegerField(default=0)
    link = models.ForeignKey(Link)

    class Meta:
        unique_together = (("day", "link"),)