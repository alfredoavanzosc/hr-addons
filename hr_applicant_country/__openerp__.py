# -*- coding: utf-8 -*-
# (Copyright) 2018 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Hr Applicant Country",
    'version': '8.0.1.1.0',
    'license': "AGPL-3",
    'author': "AvanzOSC",
    'website': "http://www.avanzosc.es",
    'contributors': [
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        "Alfredo de la Fuente <alfredodelafuente@avanzosc.es",
    ],
    "category": "Human Resources",
    "depends": [
        'hr_recruitment',
        'partner_contact_birthdate'
    ],
    "data": [
        'views/hr_job_view.xml',
        'views/hr_applicant_view.xml',
        'views/res_partner_view.xml',
    ],
    "installable": True,
}
