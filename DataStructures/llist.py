class Node:
  def __init__(self, cargo=None, next=None):
    self.car = cargo
    self.cdr = next
  def __str__(self):
    return str(self.car)


def display(lst):
  if lst:
    w("%s " % lst)
    display(lst.cdr)
  else:
    w("nil\n")