"""
ASGI config for mysite project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from fastapi import FastAPI
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_asgi_application()


from CustomerSupportAPI.routers import calling, matter


fastapp = FastAPI()  # initialize


# for Bigger Applications - Multiple Files - FastAPI --------------------------
# cf. https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi

# include from `router.calling`
fastapp.include_router(
    calling.router,
    prefix="/callings",
    tags=["callings"]
)

# include from `router.matter`
fastapp.include_router(
    matter.router,
    prefix="/matters",
    tags=["matters"]
)
# -----------------------------------------------------------------------------
