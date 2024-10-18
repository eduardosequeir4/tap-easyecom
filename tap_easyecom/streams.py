"""Stream type classes for tap-easyecom."""

from singer_sdk import typing as th
from tap_easyecom.client import EasyEcomStream


class ProductsStream(EasyEcomStream):
    name = "products"
    path = "/Products/GetProductMaster?custom_fields=1"
    primary_keys = ["product_id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("cp_id", th.IntegerType),
        th.Property("product_id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("product_name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("inventory", th.IntegerType),
        th.Property("product_type", th.StringType),
        th.Property("brand", th.StringType),
        th.Property("colour", th.StringType),
        th.Property("category_id", th.IntegerType),
        th.Property("brand_id", th.IntegerType),
        th.Property("accounting_sku", th.StringType),
        th.Property("accounting_unit", th.StringType),
        th.Property("category_name", th.StringType),
        th.Property("expiry_type", th.IntegerType),
        th.Property("company_name", th.StringType),
        th.Property("c_id", th.IntegerType),
        th.Property("height", th.IntegerType),
        th.Property("length", th.IntegerType),
        th.Property("width", th.IntegerType),
        th.Property("weight", th.IntegerType),
        th.Property("cost", th.IntegerType),
        th.Property("mrp", th.IntegerType),
        th.Property("size", th.StringType),
        th.Property("cp_sub_products_count", th.IntegerType),
        th.Property("model_no", th.StringType),
        th.Property("hsn_code", th.StringType),
        th.Property("tax_rate", th.NumberType),
        th.Property("product shelf life", th.StringType),
        th.Property("product_image_url", th.StringType),
        th.Property("cp_inventory", th.IntegerType),
        th.Property("custom_fields", th.ArrayType(th.ObjectType(
            th.Property("cp_id", th.IntegerType),
            th.Property("field_name", th.StringType),
            th.Property("value", th.StringType),
            th.Property("enabled", th.BooleanType),
        ))),
    ).to_dict()


class SuppliersStream(EasyEcomStream):
    name = "suppliers"
    path = "/wms/V2/getVendors"
    primary_keys = ["vendor_c_id"]

    schema = th.PropertiesList(
        th.Property("vendor_name", th.StringType),
        th.Property("vendor_c_id", th.IntegerType),
        th.Property("address", th.ObjectType(
            th.Property("dispatch", th.ObjectType(
                th.Property("address", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state_id", th.IntegerType),
                th.Property("state_name", th.StringType),
                th.Property("zip", th.StringType),
                th.Property("country", th.StringType),
            )),
            th.Property("billing", th.ObjectType(
                th.Property("address", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state_id", th.IntegerType),
                th.Property("state_name", th.StringType),
                th.Property("zip", th.StringType),
                th.Property("country", th.StringType),
            ))
        )),
    ).to_dict()


class SellOrdersStream(EasyEcomStream):
    name = "sell_orders"
    path = "/orders/V2/getAllOrders"
    primary_keys = ["order_id"]
    records_jsonpath = "$.data.orders[*]"

    schema = th.PropertiesList(
        th.Property("invoice_id", th.IntegerType),
        th.Property("order_id", th.IntegerType),
        th.Property("queue_message", th.StringType),
        th.Property("queue_status", th.IntegerType),
        th.Property("order_priority", th.IntegerType),
        th.Property("blockSplit", th.IntegerType),
        th.Property("reference_code", th.StringType),
        th.Property("company_name", th.StringType),
        th.Property("location_key", th.StringType),
        th.Property("warehouseId", th.IntegerType),
        th.Property("seller_gst", th.StringType),
        th.Property("import_warehouse_id", th.IntegerType),
        th.Property("import_warehouse_name", th.StringType),
        th.Property("pickup_address", th.StringType),
        th.Property("pickup_city", th.StringType),
        th.Property("pickup_state", th.StringType),
        th.Property("pickup_state_code", th.StringType),
        th.Property("pickup_pin_code", th.StringType),
        th.Property("pickup_country", th.StringType),
        th.Property("invoice_currency_code", th.StringType),
        th.Property("order_type", th.StringType),
        th.Property("order_type_key", th.StringType),
        th.Property("replacement_order", th.IntegerType),
        th.Property("marketplace", th.StringType),
        th.Property("marketplace_id", th.IntegerType),
        th.Property("qcPassed", th.IntegerType),
        th.Property("salesmanUserId", th.IntegerType),
        th.Property("order_date", th.DateTimeType),
        th.Property("tat", th.DateTimeType),
        th.Property("available_after", th.DateTimeType),
        th.Property("invoice_date", th.DateTimeType),
        th.Property("import_date", th.DateTimeType),
        th.Property("last_update_date", th.DateTimeType),
        th.Property("manifest_date", th.DateTimeType),
        th.Property("manifest_no", th.StringType),
        th.Property("invoice_number", th.StringType),
        th.Property("marketplace_invoice_num", th.StringType),
        th.Property("shipping_last_update_date", th.DateTimeType),
        th.Property("batch_id", th.StringType),
        th.Property("batch_created_at", th.DateTimeType),
        th.Property("message", th.StringType),
        th.Property("courier_aggregator_name", th.StringType),
        th.Property("courier", th.StringType),
        th.Property("carrier_id", th.StringType),
        th.Property("awb_number", th.StringType),
        th.Property("Package Weight", th.StringType),
        th.Property("Package Height", th.StringType),
        th.Property("Package Length", th.StringType),
        th.Property("Package Width", th.StringType),
        th.Property("order_status", th.StringType),
        th.Property("order_status_id", th.IntegerType),
        th.Property("suborder_count", th.IntegerType),
        th.Property("shipping_status", th.StringType),
        th.Property("shipping_status_id", th.IntegerType),
        th.Property("shipping_history", th.ObjectType(
            th.Property("qc_pass_datetime", th.DateTimeType),
            th.Property("confirm_datetime", th.DateTimeType),
            th.Property("print_datetime", th.DateTimeType),
            th.Property("manifest_datetime", th.DateTimeType),
        )),
        th.Property("delivery_date", th.DateTimeType),
        th.Property("payment_mode", th.StringType),
        th.Property("payment_mode_id", th.IntegerType),
        th.Property("payment_gateway_transaction_number", th.StringType),
        th.Property("payment_gateway_name", th.StringType),
        th.Property("buyer_gst", th.StringType),
        th.Property("customer_name", th.StringType),
        th.Property("contact_num", th.StringType),
        th.Property("address_line_1", th.StringType),
        th.Property("address_line_2", th.StringType),
        th.Property("city", th.StringType),
        th.Property("pin_code", th.StringType),
        th.Property("state", th.StringType),
        th.Property("state_code", th.StringType),
        th.Property("country", th.StringType),
        th.Property("email", th.StringType),
        th.Property("latitude", th.StringType),
        th.Property("longitude", th.StringType),
        th.Property("billing_name", th.StringType),
        th.Property("billing_address_1", th.StringType),
        th.Property("billing_address_2", th.StringType),
        th.Property("billing_city", th.StringType),
        th.Property("billing_state", th.StringType),
        th.Property("billing_state_code", th.StringType),
        th.Property("billing_pin_code", th.StringType),
        th.Property("billing_country", th.StringType),
        th.Property("billing_mobile", th.StringType),
        th.Property("order_quantity", th.StringType),
        th.Property("meta", th.StringType),
        th.Property("documents", th.StringType),
        th.Property("total_amount", th.NumberType),
        th.Property("total_tax", th.NumberType),
        th.Property("total_shipping_charge", th.NumberType),
        th.Property("total_discount", th.NumberType),
        th.Property("collectable_amount", th.NumberType),
        th.Property("tcs_rate", th.NumberType),
        th.Property("tcs_amount", th.NumberType),
        th.Property("customer_code", th.StringType),
        th.Property("fulfillable_status", th.IntegerType),
    ).to_dict()

    def get_child_context(self, record: dict, context) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "order_id": record["order_id"],
        }

class SellOrderLinesStream(EasyEcomStream):
    name = "sell_order_lines"
    path = "/orders/V2/getAllOrders?order_id={order_id}"
    primary_keys = ["suborder_id"]
    records_jsonpath = "$.data.orders[*].suborder"
    parent_stream_type = SellOrdersStream

    schema = th.PropertiesList(
        th.Property("suborder_id", th.StringType),
        th.Property("suborder_num", th.StringType),
        th.Property("item_status", th.StringType),
        th.Property("shipment_type", th.StringType),
        th.Property("suborder_quantity", th.IntegerType),
        th.Property("item_quantity", th.IntegerType),
        th.Property("returned_quantity", th.IntegerType),
        th.Property("cancelled_quantity", th.IntegerType),
        th.Property("shipped_quantity", th.IntegerType),
        th.Property("batch_codes", th.StringType),
        th.Property("serial_nums", th.StringType),
        th.Property("batchcode_serial", th.StringType),
        th.Property("batchcode_expiry", th.StringType),
        th.Property("tax_type", th.StringType),
        th.Property("suborder_history", th.ObjectType(
            th.Property("qc_pass_datetime", th.DateTimeType),
            th.Property("confirm_datetime", th.DateTimeType),
            th.Property("print_datetime", th.DateTimeType),
            th.Property("manifest_datetime", th.DateTimeType),
        )),
        th.Property("meta", th.StringType),
        th.Property("selling_price", th.NumberType),
        th.Property("total_shipping_charge", th.NumberType),
        th.Property("total_miscellaneous", th.NumberType),
        th.Property("tax_rate", th.IntegerType),
        th.Property("tax", th.NumberType),
        th.Property("product_id", th.IntegerType),
        th.Property("company_product_id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("sku_type", th.StringType),
        th.Property("sub_product_count", th.StringType),
        th.Property("marketplace_sku", th.StringType),
        th.Property("productName", th.StringType),
        th.Property("Identifier", th.StringType),
        th.Property("description", th.StringType),
        th.Property("category", th.StringType),
        th.Property("brand", th.StringType),
        th.Property("model_no", th.StringType),
        th.Property("product_tax_code", th.StringType),
        th.Property("AccountingSku", th.StringType),
        th.Property("ean", th.StringType),
        th.Property("size", th.StringType),
        th.Property("cost", th.IntegerType),
        th.Property("mrp", th.IntegerType),
        th.Property("weight", th.IntegerType),
        th.Property("length", th.IntegerType),
        th.Property("width", th.IntegerType),
        th.Property("height", th.IntegerType),
        th.Property("scheme_applied", th.IntegerType),
    ).to_dict()


class BuyOrdersStream(EasyEcomStream):
    name = "buy_orders"
    path = "/wms/V2/getPurchaseOrderDetails"
    primary_keys = ["po_id"]

    schema = th.PropertiesList(
        th.Property("po_id", th.IntegerType),
        th.Property("total_po_value", th.NumberType),
        th.Property("po_number", th.IntegerType),
        th.Property("po_ref_num", th.StringType),
        th.Property("po_status_id", th.IntegerType),
        th.Property("po_created_date", th.DateTimeType),
        th.Property("po_updated_date", th.DateTimeType),
        th.Property("po_created_warehouse", th.StringType),
        th.Property("po_created_warehouse_c_id", th.IntegerType),
        th.Property("vendor_name", th.StringType),
        th.Property("vendor_c_id", th.IntegerType),
    ).to_dict()

    def get_child_context(self, record: dict, context) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "po_id": record["po_id"],
        }


class BuyOrderLinesStream(EasyEcomStream):
    name = "buy_order_lines"
    path = "/wms/V2/getPurchaseOrderDetails"
    primary_keys = ["purchase_order_detail_id"]
    records_jsonpath = "$.data[*].po_items[*]"
    parent_stream_type = BuyOrdersStream

    schema = th.PropertiesList(
        th.Property("purchase_order_detail_id", th.IntegerType),
        th.Property("cp_id", th.IntegerType),
        th.Property("product_id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("hsn", th.StringType),
        th.Property("model_no", th.StringType),
        th.Property("ean", th.StringType),
        th.Property("product_description", th.StringType),
        th.Property("original_quantity", th.IntegerType),
        th.Property("pending_quantity", th.IntegerType),
        th.Property("item_price", th.NumberType),
    ).to_dict()


class ReceiptsStream(EasyEcomStream):
    name = "receipts"
    path = "/Grn/V2/getGrnDetails"
    primary_keys = ["grn_id"]

    schema = th.PropertiesList(
        th.Property("grn_id", th.IntegerType),
        th.Property("grn_invoice_number", th.StringType),
        th.Property("total_grn_value", th.IntegerType),
        th.Property("grn_status_id", th.IntegerType),
        th.Property("grn_status", th.StringType),
        th.Property("grn_created_at", th.DateTimeType),
        th.Property("grn_invoice_date", th.DateType),
        th.Property("po_id", th.IntegerType),
        th.Property("po_number", th.IntegerType),
        th.Property("po_ref_num", th.StringType),
        th.Property("po_status_id", th.IntegerType),
        th.Property("po_created_date", th.DateTimeType),
        th.Property("po_updated_date", th.DateTimeType),
        th.Property("inwarded_warehouse", th.StringType),
        th.Property("inwarded_warehouse_c_id", th.IntegerType),
        th.Property("vendor_name", th.StringType),
        th.Property("vendor_c_id", th.IntegerType),
    ).to_dict()

    def get_child_context(self, record: dict, context) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "grn_id": record["grn_id"],
        }


class ReceiptLineStream(EasyEcomStream):
    name = "receipt_lines"
    path = "/Grn/V2/getGrnDetails"
    primary_keys = ["grn_detail_id"]
    records_jsonpath = "$.data[*].grn_items[*]"
    parent_stream_type = ReceiptsStream

    schema = th.PropertiesList(
        th.Property("grn_detail_id", th.IntegerType),
        th.Property("purchase_order_detail_id", th.IntegerType),
        th.Property("cp_id", th.IntegerType),
        th.Property("product_id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("hsn", th.StringType),
        th.Property("model_no", th.StringType),
        th.Property("ean", th.StringType),
        th.Property("product_description", th.StringType),
        th.Property("original_quantity", th.IntegerType),
        th.Property("pending_quantity", th.IntegerType),
        th.Property("received_quantity", th.IntegerType),
        th.Property("grn_detail_price", th.NumberType),
        th.Property("item_price", th.NumberType),
        th.Property("expire_date", th.DateTimeType),
        th.Property("batch_code", th.StringType),
        th.Property("available", th.IntegerType),
        th.Property("reserved", th.IntegerType),
        th.Property("sold", th.IntegerType),
        th.Property("repair", th.IntegerType),
        th.Property("lost", th.IntegerType),
        th.Property("damaged", th.IntegerType),
        th.Property("gifted", th.IntegerType),
        th.Property("return_to_source", th.IntegerType),
        th.Property("return_available", th.IntegerType),
        th.Property("qc_pending", th.IntegerType),
        th.Property("qc_pass", th.IntegerType),
        th.Property("qc_fail", th.IntegerType),
        th.Property("transfer", th.IntegerType),
        th.Property("discard", th.IntegerType),
        th.Property("used_in_manufacturing", th.IntegerType),
        th.Property("adjusted", th.IntegerType),
        th.Property("near_expiry", th.IntegerType),
        th.Property("expiry", th.IntegerType),
    ).to_dict()


class ReturnsStream(EasyEcomStream):
    name = "returns"
    path = "/Grn/V2/getAllReturns"
    primary_keys = ["credit_note_id"]
    records_jsonpath = "$.data.credit_notes[*]"

    schema = th.PropertiesList(
        th.Property("credit_note_id", th.IntegerType),
        th.Property("invoice_id", th.IntegerType),
        th.Property("order_id", th.IntegerType),
        th.Property("reference_code", th.StringType),
        th.Property("company_name", th.StringType),
        th.Property("warehouseId", th.IntegerType),
        th.Property("seller_gst", th.StringType),
        th.Property("forward_shipment_pickup_address", th.StringType),
        th.Property("forward_shipment_pickup_city", th.StringType),
        th.Property("forward_shipment_pickup_state", th.StringType),
        th.Property("forward_shipment_pickup_pin_code", th.StringType),
        th.Property("forward_shipment_pickup_country", th.StringType),
        th.Property("order_type", th.StringType),
        th.Property("order_type_key", th.StringType),
        th.Property("replacement_order", th.IntegerType),
        th.Property("marketplace", th.StringType),
        th.Property("marketplace_id", th.IntegerType),
        th.Property("salesmanUserId", th.IntegerType),
        th.Property("order_date", th.DateTimeType),
        th.Property("invoice_date", th.DateTimeType),
        th.Property("import_date", th.DateTimeType),
        th.Property("last_update_date", th.DateTimeType),
        th.Property("manifest_date", th.DateTimeType),
        th.Property("credit_note_date", th.DateTimeType),
        th.Property("return_date", th.DateTimeType),
        th.Property("manifest_no", th.StringType),
        th.Property("invoice_number", th.StringType),
        th.Property("credit_note_number", th.StringType),
        th.Property("marketplace_credit_note_num", th.StringType),
        th.Property("marketplace_invoice_num", th.StringType),
        th.Property("batch_id", th.StringType),
        th.Property("batch_created_at", th.DateTimeType),
        th.Property("payment_mode", th.StringType),
        th.Property("payment_mode_id", th.IntegerType),
        th.Property("buyer_gst", th.StringType),
        th.Property("forward_shipment_customer_name", th.StringType),
        th.Property("forward_shipment_customer_contact_num", th.StringType),
        th.Property("forward_shipment_customer_address_line_1", th.StringType),
        th.Property("forward_shipment_customer_address_line_2", th.StringType),
        th.Property("forward_shipment_customer_city", th.StringType),
        th.Property("forward_shipment_customer_pin_code", th.StringType),
        th.Property("forward_shipment_customer_state", th.StringType),
        th.Property("forward_shipment_customer_country", th.StringType),
        th.Property("forward_shipment_customer_email", th.StringType),
        th.Property("forward_shipment_billing_name", th.StringType),
        th.Property("forward_shipment_billing_address_1", th.StringType),
        th.Property("forward_shipment_billing_address_2", th.StringType),
        th.Property("forward_shipment_billing_city", th.StringType),
        th.Property("forward_shipment_billing_state", th.StringType),
        th.Property("forward_shipment_billing_pin_code", th.StringType),
        th.Property("forward_shipment_billing_country", th.StringType),
        th.Property("forward_shipment_billing_mobile", th.StringType),
        th.Property("order_quantity", th.IntegerType),
        th.Property("total_invoice_amount", th.IntegerType),
        th.Property("total_invoice_tax", th.IntegerType),
        th.Property("invoice_collectable_amount", th.IntegerType),
    ).to_dict()

    def get_child_context(self, record: dict, context) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "credit_note_id": record["credit_note_id"],
        }


class ReturnLinesStream(EasyEcomStream):
    name = "return_lines"
    path = "/Grn/V2/getAllReturns"
    primary_keys = ["company_product_id"]
    records_jsonpath = "$.data.credit_notes[*]"
    parent_stream_type = ReturnsStream
    
    schema = th.PropertiesList(
        th.Property("company_product_id", th.IntegerType),
        th.Property("product_id", th.IntegerType),
        th.Property("suborder_id", th.IntegerType),
        th.Property("suborder_num", th.StringType),
        th.Property("return_reason", th.StringType),
        th.Property("inventory_status", th.StringType),
        th.Property("shipment_type", th.StringType),
        th.Property("suborder_quantity", th.IntegerType),
        th.Property("returned_item_quantity", th.IntegerType),
        th.Property("tax_type", th.StringType),
        th.Property("total_item_selling_price", th.StringType),
        th.Property("credit_note_total_item_shipping_charge", th.StringType),
        th.Property("credit_note_total_item_miscellaneous", th.StringType),
        th.Property("item_tax_rate", th.IntegerType),
        th.Property("credit_note_total_item_tax", th.IntegerType),
        th.Property("credit_note_total_item_excluding_tax", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("productName", th.StringType),
        th.Property("description", th.StringType),
        th.Property("category", th.StringType),
        th.Property("brand", th.StringType),
        th.Property("model_no", th.StringType),
        th.Property("product_tax_code", th.StringType),
        th.Property("ean", th.StringType),
        th.Property("size", th.StringType),
        th.Property("cost", th.IntegerType),
        th.Property("mrp", th.IntegerType),
        th.Property("weight", th.IntegerType),
        th.Property("length", th.IntegerType),
        th.Property("width", th.IntegerType),
        th.Property("height", th.IntegerType),
    ).to_dict()