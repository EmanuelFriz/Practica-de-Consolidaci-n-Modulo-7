from django.core.management.base import BaseCommand
from laboratorio.models import Laboratorio, DirectorGeneral, Producto
from datetime import date

class Command(BaseCommand):
    help = "Poblar la base de datos con datos iniciales"

    def handle(self, *args, **kwargs):
        # Crear laboratorios
        laboratorio_a = Laboratorio.objects.create(nombre="Laboratorio A", ciudad="Santiago", pais="Chile")
        laboratorio_b = Laboratorio.objects.create(nombre="Laboratorio B", ciudad="Bogotá", pais="Colombia")
        laboratorio_c = Laboratorio.objects.create(nombre="Laboratorio C", ciudad="Lima", pais="Perú")

        # Crear directores generales
        DirectorGeneral.objects.create(nombre="Juan Pérez", laboratorio=laboratorio_a, especialidad="Biotecnología")
        DirectorGeneral.objects.create(nombre="Ana Gómez", laboratorio=laboratorio_b, especialidad="Farmacología")
        DirectorGeneral.objects.create(nombre="Luis Martínez", laboratorio=laboratorio_c, especialidad="Química")

        # Crear productos
        Producto.objects.create(
            nombre="Producto 1",
            laboratorio=laboratorio_a,
            f_fabricacion=date(2023, 1, 1),
            p_costo=1000.00,
            p_venta=1500.00,
        )
        Producto.objects.create(
            nombre="Producto 2",
            laboratorio=laboratorio_b,
            f_fabricacion=date(2023, 2, 15),
            p_costo=2000.00,
            p_venta=3000.00,
        )
        Producto.objects.create(
            nombre="Producto 3",
            laboratorio=laboratorio_c,
            f_fabricacion=date(2023, 3, 10),
            p_costo=2500.00,
            p_venta=3500.00,
        )

        self.stdout.write(self.style.SUCCESS("Datos iniciales creados exitosamente."))