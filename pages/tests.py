# from django.test import SimpleTestCase
#
# class HomepageTests(SimpleTestCase):
#    def test_url_exists_at_correct_location(self):
#        response = self.client.get("/")
#        self.assertEqual(response.status_code, 200)
#
# class AboutpageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(self):
#         response = self.client.get("/about/")
#         self.assertEqual(response.status_code, 200)

#******** for testing correctly URL***** our URL locations and URL names
# from django.test import SimpleTestCase
# from django.urls import reverse # new
#
# class HomepageTests(SimpleTestCase):
#     def test_url_exists_at_correct_location(self):
#        response = self.client.get("/")
#        self.assertEqual(response.status_code, 200)
#     def test_url_available_by_name(self): # new
#        response = self.client.get(reverse("home"))
#        self.assertEqual(response.status_code, 200)
#
#
# class AboutpageTests(SimpleTestCase):
#       def test_url_exists_at_correct_location(self):
#          response = self.client.get("/about/")
#          self.assertEqual(response.status_code, 200)
#       def test_url_available_by_name(self): # new
#           response = self.client.get(reverse("about"))
#           self.assertEqual(response.status_code, 200)

'''
We have tested our URL locations and URL names so far but not our templates. Let’s make sure
that the correct templates–home.html and about.html–are used on each page and that they
display the expected content of “<h1>Homepage</h1>” and “<h1>About page</h1>” respectively
'''
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
      def test_url_exists_at_correct_location(self):
           response = self.client.get("/")
           self.assertEqual(response.status_code, 200)
      def test_url_available_by_name(self):
           response = self.client.get(reverse("home"))
           self.assertEqual(response.status_code, 200)
      def test_template_name_correct(self): # new
           response = self.client.get(reverse("home"))
           self.assertTemplateUsed(response, "home.html")
      def test_template_content(self): # new
          response = self.client.get(reverse("home"))
          self.assertContains(response, "<h1>Homepage</h1>")

class AboutpageTests(SimpleTestCase):
      def test_url_exists_at_correct_location(self):
           response = self.client.get("/about/")
           self.assertEqual(response.status_code, 200)
      def test_url_available_by_name(self):
           response = self.client.get(reverse("about"))
           self.assertEqual(response.status_code, 200)
      def test_template_name_correct(self): # new
          response = self.client.get(reverse("about"))
          self.assertTemplateUsed(response, "about.html")
      def test_template_content(self): # new
          response = self.client.get(reverse("about"))
          self.assertContains(response, "<h1>About page</h1>")
