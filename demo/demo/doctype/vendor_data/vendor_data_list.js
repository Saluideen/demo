frappe.listview_settings['Vendor Data'] = {
    onload: function (listview) {
        // Add a custom button to the list view toolbar
        listview.page.add_button(__("Sync"), function () {
            frappe.call({
                method: "demo.demo.doctype.vendor_data.vendor_data.get_vendor_data",
                freeze: true,
                callback: function (r) {
                    console.log(r.message);
                   
                    
                },
                error: function (r) {
                    frappe.msgprint(r.message);
                },
            });
        });
    }
};
