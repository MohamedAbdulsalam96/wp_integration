frappe.listview_settings['WhatsApp Templates'] = {

	onload: function(listview) {
		listview.page.add_menu_item(__("Fetch templates from meta"), function() {
			frappe.call({
				method:'wp_integration.whatsapp_notifications.doctype.whatsapp_templates.whatsapp_templates.fetch',
				callback: function(res) {
					frappe.msgprint(res.message)
					listview.refresh();
				}
			});
		});
	}
};