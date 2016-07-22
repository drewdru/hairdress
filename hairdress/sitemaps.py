# from django.contrib.sitemaps import Sitemap
# from main.models import Publisher

# class PublisherSitemap(Sitemap):
#     changefreq = "never"
#     priority = 0.5

#     def items(self):
#         return Publisher.objects.filter(is_draft=False)

#     def lastmod(self, obj):
#         return obj.pub_date