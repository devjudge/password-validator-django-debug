from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'restapi'

    def ready(self):
        Users_Details = self.get_model('Users_Details')
        Users_Details.objects.all().delete()

        user1 = Users_Details(name="abc", email="abc@gmail.com", password="abcd123456", auth_token="abcd-12345-shbbchsj-12bbbch", is_logged_in=0)
        user1.save()

        user2 = Users_Details(name="abc", email="abcd@gmail.com", password="abc@123", auth_token="abcd-123-shbbchsj-12bbbch", is_logged_in=0)
        user2.save()
