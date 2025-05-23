# -*- coding: utf-8 -*-
{
    'name': "malkion",

    'summary': """
        Módulo para la gestión de toma de datos para la aplicación Asclepio""",

    'description': """
        Módulo que simplifica el trabajo de gestores de data.

        Características principales:
        - Gestión de contratos con sus datos requeridos.
        - Gestión de empleados, almacenes, equipo, puntos de interés y demas elementos implicados.
        - Gestión de plantillas de misión para la obtención de los datos requeridos.
        - Gestión de misiones hasta la entrega de datos a los gestores de Asclepios.
    """,

    'author': "David Albi Garcia",
    'website': "github.com/DavidAlbiGarcia/malkion",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Malkion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'hr'],

    # always loaded
    'data': [
        'security/groups.xml',
        'data/init_admin_group.xml',
        'security/ir.model.access.csv',
        'security/rules/mission_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/dashboard_views.xml', # primero, copón!
        'views/contract_views.xml',
        'views/point_of_interest_views.xml',
        'views/almacenes_views.xml',
        'views/employee_views.xml',
        'views/transport_views.xml',
        'views/equipo_views.xml',
        'views/plantilla_views.xml',
        'views/orden_trabajo_views.xml',
        'views/mission_views.xml',
        'views/wizard_mission_report.xml',
        'views/wizard_recursos_report.xml',
        'views/wizard_equipo_antiguo.xml',

        # 1. Definiciones base
        'data/hr_job.xml',

        # 2. Usuarios y empleados
        'data/users.xml',
        'data/employees.xml',

        # 3. Almacenes
        'data/almacenes.xml',

        # 4. Recursos
        'data/equipos.xml',
        'data/transportes.xml',

        # 5. Puntos de interés
        'data/puntos_interes.xml',

        # 6. Clientes y contratos
        'data/clientes.xml',
        'data/contratos.xml',

        # 7. Plantillas de misión
        'data/plantillas/plantillas.xml', # imagino primero para ser referenciada
        'data/plantillas/plantilla_roles.xml',
        'data/plantillas/plantilla_equipo.xml',
        'data/plantillas/plantilla_transporte.xml',

        # 8. Misión precargada de ejemplo, mission imposible
        # 'data/misiones.xml',
        # uso método alternativo, quiero que pase por la lógica de create order para poblar ternarias, cambiar equipo etc
        # si lo ajusto manual sería problemático y, a la vez, quiero una misión ya hecha de ejemplo
        # como la plantilla se puebla en onchangecontract, opto por mandar los datos poblados ya:

        'data/orden_trabajo.xml',


        #reports
        'reports/report_mission.xml',
        'reports/report_mission_template.xml',
        'reports/report_recursos_asignados.xml',
        'reports/report_recursos_asignados_template.xml',
        'reports/report_equipos_antiguos.xml',
        'reports/report_equipos_antiguos_template.xml',

        
        
    ],

    'post_init_hook': 'post_init_hook_regenerar_xml',
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
