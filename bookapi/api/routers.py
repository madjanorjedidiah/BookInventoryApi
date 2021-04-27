from rest_framework import routers
from api.viewset import *


router = routers.DefaultRouter()
router.register(r'book', InventoryView, 'book')
router.register(r'users', UserProfileViewSet)
router.register(r'login', LoginViewSet, 'login')
