from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CustomUserViewset

router = SimpleRouter()
router.register("users", CustomUserViewset, basename="users")
urlpatterns = router.urls

