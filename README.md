# Sistema de Gestión de Inventario

## Descripción
Es un sistema de gestión de inventario para administrar productos, categorías de productos y movimientos con operaciones de crear, listar, editar y eliminar cada una de ellas.

La entidad "movimientos" se refiere a la entrada y salida de stock.

Está compuesto por un menú principal que permite administrar categorías de productos, productos y movimientos. Cada entidad tiene un submenú con las siguientes opciones:
1. Crear
2. Listar
3. Editar
4. Eliminar
5. Salir al menú principal

## Tecnologías
- Python 3.13.1
- Git/GitHub

## Estructura del proyecto
```sistema_gestion_inventario/
├── main.py
├── data/                    # archivos de datos (la base, cuando exista)
└── inventory/
    ├── entities/           # modelos: Category, Product, Movement
    ├── repositories/        # acceso a los datos (en desarrollo)
    ├── services/            # lógica de negocio (en desarrollo)
    └── submenus/            # menús e interacción con el usuario
```

**Flujo:** `submenus` → `services` → `repositories` → `data`
- Cada capa se comunica sólo con la siguiente.

## Instalación y uso
```bash
git clone https://github.com/VirPalo/sistema_gestion_inventario.git
cd sistema_gestion_inventario
python main.py
```

## Ejemplo / Captura
Próximamente.

## Estado del proyecto
En desarrollo.

- [x] Menú principal y submenús
- [ ] CRUD de categorías
- [ ] CRUD de productos
- [ ] CRUD de movimientos
- [ ] Persistencia de datos

## Autora
Virginia L. Paloma - Desarrolladora Python Jr




