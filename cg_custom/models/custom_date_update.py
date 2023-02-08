# -*- coding: utf-8 -*-




if records:
    for record in records:
        if record.x_custom_date_studio:
            if record.move_raw_ids:
                for move in record.move_raw_ids:
                    move.write({'date': record.x_custom_date_studio})
                    if move.move_line_ids:
                        for ln in move.move_line_ids:
                            ln.write({'date': record.x_custom_date_studio})
            if record.move_finished_ids:
                for mv in record.move_finished_ids:
                    mv.write({'date': record.x_custom_date_studio})
                    if mv.move_line_ids:
                        for ln in mv.move_line_ids:
                            ln.write({'date': record.x_custom_date_studio})
            if record.finished_move_line_ids:
                for line in record.finished_move_line_ids:
                    line.write({'date': record.x_custom_date_studio})
            if record.scrap_ids:
                record.scrap_ids.write({'date_done': record.x_custom_date_studio})
                record.scrap_ids.move_id.write({'date': record.x_custom_date_studio})
                record.scrap_ids.move_id.move_line_ids.write({'date': record.x_custom_date_studio})
            domain = [('id', 'in', (record.move_raw_ids + record.move_finished_ids + record.scrap_ids.move_id).stock_valuation_layer_ids.ids)]
            stock_valuation_records = env['stock.valuation.layer'].search(domain)
            stock_valuation_records._write({'create_date': record.x_custom_date_studio})