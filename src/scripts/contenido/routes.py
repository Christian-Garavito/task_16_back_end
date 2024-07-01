""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers

#------------cracion del blueprint----------------------
servicio_1_blueprint = Blueprint(
    "servicio_1_blueprint",
    __name__,
    url_prefix='/servicio-1',
)

#------------Rutas de contenido----------------------
servicio_1_blueprint.add_url_rule(
    "/vuelos",
    view_func=controllers.crud_vuelos,
    methods=["GET"]
)
















