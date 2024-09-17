# Odoo Custom Event Ticket Template Modification
This custom module extends the Odoo Event module by modifying the event ticket template to include dynamic QR codes with custom URLs. Specifically, the default barcode displayed on event tickets is replaced by a QR code that incorporates the event's URL (event_url field) and the attendee's barcode, allowing for more personalized and event-specific ticketing.

### Key Features:
- Inherits and extends the default foldable event badge template (event_report_template_foldable_badge).
- Replaces the default QR code source with a custom URL (event_url from event_event model).
- Dynamically includes the attendee's barcode within the custom URL.
- Customizable and easily adaptable for other event-related modifications.
### Technical Details:
- Model Inheritance: The event.event model is extended to include an event_url field, which is used within the QR code URL.
- Template Inheritance: The QWeb template event_report_template_foldable_badge is modified using an XPath expression to replace the default QR code image with a custom one.
- Dynamic QR Code: The QR code source now reflects a custom URL structure combining the event’s URL and the attendee’s barcode.
### Usage:
- Install the module in an Odoo instance that has the Event module installed.
- Ensure that the event_url field is filled out for each event.
- Generate event tickets as usual, and the custom QR code will be included with each ticket.

### Code Example:
Here’s an example of the XPath modification used in the QWeb template:

```xml
<odoo>
    <template id="report_event_ticket_custom" inherit_id="event_report_template_foldable_badge">
        <xpath expr="//div[@class='o_event_foldable_badge_barcode_container_top']/img" position="replace">
            <img t-attf-src="/report/barcode/QR/{{event_url}}/{{attendee.barcode if attendee else '12345678901234567890'}}?&amp;width=174&amp;height=174&amp;quiet=0"
                 alt="QR Code"/>
        </xpath>
    </template>
</odoo>
```

### Installation:
- Clone or download the module into your Odoo addons directory.
- Update your Odoo apps list, then install the module via the Odoo interface.
### Requirements:
- Odoo 14.0 or higher.
- Odoo Events module installed and configured.
