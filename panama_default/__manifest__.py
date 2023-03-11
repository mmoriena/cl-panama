##############################################################################
#
#    Copyright (C) 2021  ADEN
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'panama11',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'summary': "Proyect module for panama",
    'author': "ADEN",
    'website': 'aden.com',
    'license': 'AGPL-3',
    'depends': [
            # Modulos odoo
            'account_balance_line',
            'account_credit_control',
            'account_credit_control_dunning_fees',
            'account_due_list',
            'account_financial_report',
            'account_financial_report_aden',
            'account_financial_report_date_range',
            'account_fiscal_year',
            'account_group_menu',
            'account_invoice_aden',
            'account_invoice_constraint_chronology',
            'account_invoice_currency',
            'account_invoice_import_panama',
            'account_invoice_panama',
            'account_loan',
            'account_move_aden',
            'account_move_fiscal_year',
            'account_move_line_tax_editable',
            'account_partner_required',
            'account_payment_aden',
            'account_reports',
            'account_reports_cash_flow',
            'account_reports_followup',
            'account_reversal',
            'account_statement_move_import',
            'account_tag_menu',
            'account_type_menu',
            'auditlog',
            'auto_backup',
            'backend_theme_v11',
            'crm_aden',
            'customer_activity_statement',
            'date_range',
            'dynamic_tree_view',
            'generic_excel_reports',
            'gestion_avisos_vencimientos_aden',
            'l10n_ar_account_check_duo',
            'l10n_ar_account_period',
            'l10n_ar_account_period_aden',
            'l10n_ar_account_report',
            'l10n_ar_account_tax',
            'l10n_ar_account_tax_ganancias',
            'l10n_ar_account_tax_iibb',
            'l10n_ar_account_tax_pursale_invoice',
            'l10n_ar_bank',
            'l10n_ar_base',
            'l10n_ar_base_vat',
            'l10n_ar_chart_generic',
            'l10n_ar_invoice',
            'l10n_ar_libro_iva_xlsx',
            'l10n_ar_purchase',
            'l10n_ar_sale',
            'l10n_ar_states',
            'l10n_ar_wsafip',
            'l10n_ar_wsafip_fe',
            'l10n_ar_wsafip_fex',
            'multipay',
            'odoo_account_invoice',
            'odoo_bank_aden',
            'odoo_cheques_aden',
            'odoo_cotizacion_pagos',
            'odoo_crm_erp',
            'odoo_custom_payment_term',
            'odoo_educat_erp',
            'odoo_estado_cuenta',
            'odoo_exposicion_contable',
            'odoo_fp_server',
            'odoo_multicompany_aden',
            'odoo_orden_pago_sis',
            'odoo_report_libro_diario',
            'odoo_report_libro_mayor',
            'odoo_report_per_gan',
            'odoo_report_situa_patri',
            'payment_two_checkout',
            'purchase_order_type',
            'report_excel_partner_ledger',
            'report_wkhtmltopdf_param',
            'report_xlsx',
            'web_aden',
            'web_advanced_search',
            'web_decimal_numpad_dot',
            'web_responsive',

        ],
    'installable': True,

    'env-ver': '2',
    'odoo-license': 'CE',
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
                'workers = 0',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
    ],

    'port': '8069',

    'git-repos': [
        'git@github.com:quilsoft-org/cl-qmequipments.git',

        # Quilsoft
        'git@github.com:quilsoft-org/qmequipments.git -b 16.0',

    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres jobiols/postgres:11'
    ]
}
