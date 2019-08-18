# MRP parallel manufacturing extension for Odoo Community

Adds extra features needed by a custom/bespoke manufacturing business that makes unique products and needs to produce them in large quantity on parallel machines (work centers). It adds a timeline (GANTT) view using the web_timeline OCA module to allow planning work orders easily.
It also depends on the mrp_production_request OCA module which gives ability to split manufacturing orders easily.
Overall fills the gaps in Odoo manufacturing my company required and hopefully of use to others.

## Features:

-Engineering Spec Sheet: A model to store custom engineered products that require their own spec sheets for manufacture.
Each have a unique id, name, revision, attachment and approval status field for engineers to approve with manufacturing department.
Appears in main menu under engineering, under products where you select the associated spec sheet, and overrides the work order worksheet PDF if chosen.

-Parallel manufacturing work centers: Normally Odoo is designed for a single assembly line per product, however in large capacity manufacturing companies you have many identical machines performing the same action and no easy way to split jobs across all of them.
Combined with the mrp_production_request model, this module gives the ability to assign also a "TBC" flag to a workcenter which allows you to set a routing that defines a TBC workcenter as it's default. When trying to start the WO it will force it to be manually reassigned to a "real" workcenter (using Kanban, Form or Timeline view)
You can also choose to fold it in the kanban by default.

-Timeline view for Work Orders: Normally no GANTT view is present in community and the enterprise GANTT is limited. Using web_timeline allows for a very interactive planner that can work well for manufacturing work order planning. This module adds origin field, colour and notes to the workorder that are shown in the timeline view.
Access via the Operations > Work Orders menu.

-Also adds custom search and grouping capabilities to the timeline view for work orders.

## Automated actions:

-Warning automated action when starting a work order that has a TBC flag set

-Assign duration expected to work orders to set a default planned start / end date
If an engineering spec sheet is assigned to this product, override the work order "worksheet" field with the custom PDF spec sheet

## Engineering screenshots
![Alt text](/static/img/icon.jpg?raw=true "Engineering")
![Alt text](/static/img/engspecsheets-1.PNG?raw=true "Engineering Spec Sheet list")
![Alt text](/static/img/engspecsheets-2.PNG?raw=true "Engineering Spec Sheet form")
![Alt text](/static/img/engspecsheets-3.PNG?raw=true "Engineering Spec Sheet assigned to product")
## Work Center and Work Order screenshots
![Alt text](/static/img/workcenter-1.PNG?raw=true "Work Center extra fields")
![Alt text](/static/img/workorders-1.PNG?raw=true "Work Order kanban all stages")
![Alt text](/static/img/workorders-2.PNG?raw=true "Work Order TBC warning")
![Alt text](/static/img/workorders-3.PNG?raw=true "Work Order planner")
![Alt text](/static/img/workorders-4.PNG?raw=true "Work Order planner custom fields")
