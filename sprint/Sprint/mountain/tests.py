from django.test import TestCase
from models import Users, PerevalAdded, Coords, PerevalAreas, PerevalImages, SprActivitiesTypes


class UsersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Users.objects.create(email="test@example.com", phone="+1234567890", password="password", fam="Фамилия",
                             name="Имя", otc="Отчество")

    def test_str_method(self):
        user = Users.objects.get(id=1)
        self.assertEqual(str(user), "Фамилия Имя")

class PerevalAddedModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = Users.objects.create(email="test@example.com", phone="+1234567890", password="password", fam="Фамилия",
                                    name="Имя", otc="Отчество")
        coords = Coords.objects.create(latitude=55.751244, longitude=37.618423, height=0)
        PerevalAdded.objects.create(raw_data={"data": "test"}, beauty_title="Красивый заголовок", title="Заголовок",
                                    other_titles="Другие заголовки", connect="Связи", add_time="2021-06-28 12:00:00",
                                    user=user, winter_level="20", summer_level="30", autumn_level="25",
                                    spring_level="15", coord_id=coords, status="new")

    def test_str_method(self):
        obj = PerevalAdded.objects.get(id=1)
        self.assertEqual(str(obj), "Красивый заголовок")


class CoordsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coords.objects.create(latitude=55.751244, longitude=37.618423, height=0)

    def test_str_method(self):
        coord = Coords.objects.get(id=1)
        self.assertEqual(str(coord), "55.751244 37.618423 0")


class PerevalAreasModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PerevalAreas.objects.create(id_parent=1, title="Аренда")

    def test_str_method(self):
        area = PerevalAreas.objects.get(id=1)
        self.assertEqual(str(area), "Аренда")


class PerevalImagesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PerevalImages.objects.create(img="test_img")

    def test_str_method(self):
        img = PerevalImages.objects.get(id=1)
        self.assertEqual(str(img), "test_img")


class SprActivitiesTypesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SprActivitiesTypes.objects.create(title="Подъём")

    def test_str_method(self):
        activity = SprActivitiesTypes.objects.get(id=1)
        self.assertEqual(str(activity), "Подъём")



