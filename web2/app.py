import mlab
from movie import Movie
from resource import Resource

from faker import Faker

faker = Faker("en_US")

# for _ in range(500):
#   print(faker.state())

mlab.connect()

# m = Movie.objects().with_id("5bf80115fb6fc0561fff7d80")
# print(m.title)
# m.delete()

# movie_list = Movie.objects()

# for m in movie_list:
#   print(m.title, m.image, m.year, sep="\n")

# m = Movie(title="Batman", year=2005, image="https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Bale_as_Batman.jpg/170px-Bale_as_Batman.jpg")
# m.save()


# r = Resource(name="Hoang Duc", city="Hai Phong", yob=1996, height=165, weight=60)
# r.save()

# resourse_list = Resource.objects()

# print(len(resourse_list))

# for r in resourse_list:
  # print(r.name, r.city, r.height, sep="\t|\t")


# r = Resource.objects().with_id("5bf800051d4f0c39b7d26ca7")
# if r is None:
#   print("Not found")
# else:
#   print("Found")
#   r.delete()

# r = Resource.objects().first()
# r.delete()

from random import randint

# for _ in range(100):
#   name = faker.name()
#   city = faker.state()
#   yob = randint(1953, 2000)
#   height = randint(150, 200)
#   weight = randint(40, 150)
#   r = Resource(name=name, city=city, yob=yob, height=height, weight=weight)
#   r.save()

# records = Resource.objects(name="Paul West")
# for r in records:
#   print(r.city)
#   print(r.weight)
#   print(r.height)

# records = Resource.objects(height=172)
# for r in records:
#   print(r.name)
#   print(r.city)
#   print("-------")

# records = Resource.objects(height__gt=170, name__icontains="John")
# print(len(records))

# records = Resource.objects()

# for r in records:
#   r.update(set__available=False)

r = Resource.objects().with_id("5bf80cd61d4f0c4484c8e5bc")
r.update(set__available=True)