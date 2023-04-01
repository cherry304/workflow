def add(c,d):
  sum =c+d
  return sum
sum=add(8,8)
print(sum)


def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
