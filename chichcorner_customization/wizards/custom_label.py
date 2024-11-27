from odoo import models, fields, _

class ProductLabelLayoutInherit(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(selection_add=[
        ('etiquette_solde', 'Etiquette Solde')
    ], ondelete={'etiquette_solde': 'set default'})


    def _prepare_report_data(self):
        # Call the super method to retain original behavior
        xml_id, data = super()._prepare_report_data()
        if self.print_format == 'etiquette_solde':
            xml_id = 'chichcorner_customization.report_product_template_label_solde'

        return xml_id, data
