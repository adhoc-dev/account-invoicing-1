import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-account-invoicing",
    description="Meta package for oca-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_billing',
        'odoo13-addon-account_global_discount',
        'odoo13-addon-account_invoice_check_total',
        'odoo13-addon-account_invoice_date_due',
        'odoo13-addon-account_invoice_fiscal_position_update',
        'odoo13-addon-account_invoice_fixed_discount',
        'odoo13-addon-account_invoice_force_number',
        'odoo13-addon-account_invoice_pricelist',
        'odoo13-addon-account_invoice_pricelist_sale',
        'odoo13-addon-account_invoice_refund_link',
        'odoo13-addon-account_invoice_search_by_reference',
        'odoo13-addon-account_invoice_section_sale_order',
        'odoo13-addon-account_invoice_supplier_ref_reuse',
        'odoo13-addon-account_invoice_supplier_ref_unique',
        'odoo13-addon-account_invoice_transmit_method',
        'odoo13-addon-account_invoice_validation_queued',
        'odoo13-addon-account_invoice_warn_message',
        'odoo13-addon-account_menu_invoice_refund',
        'odoo13-addon-account_move_tier_validation',
        'odoo13-addon-purchase_batch_invoicing',
        'odoo13-addon-purchase_stock_picking_return_invoicing',
        'odoo13-addon-sale_order_invoicing_grouping_criteria',
        'odoo13-addon-sale_order_invoicing_queued',
        'odoo13-addon-sale_timesheet_invoice_description',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
