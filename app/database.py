import sqlite3
    from typing import Dict, List
    from datetime import datetime
    import json

    class Database:
        def __init__(self, db_name='arvea_elite.db'):
            self.db_name = db_name
            self.init_db()
            self.initialize_settings()

        def init_db(self):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            
            for table_name, table_sql in TABLES.items():
                c.execute(table_sql)
            
            conn.commit()
            conn.close()

        def initialize_settings(self):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            
            for name, value in DEFAULT_BOT_SETTINGS.items():
                c.execute("""
                    INSERT INTO bot_settings (setting_name, setting_value)
                    VALUES (?, ?)
                    ON CONFLICT (setting_name) DO NOTHING
                """, (name, value))
            
            conn.commit()
            conn.close()

        # Distributor operations
        def add_distributor(self, data: Dict):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("""
                INSERT INTO distributors (
                    telegram_id, arvea_id, first_name, last_name,
                    email, phone, country, opportunity_link, shop_link,
                    upline_id, level
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                RETURNING id
            """, (data['telegram_id'], data['arvea_id'], data['first_name'],
                  data['last_name'], data['email'], data['phone'], data['country'],
                  data['opportunity_link'], data['shop_link'], data['upline_id'],
                  data['level']))
            distributor_id = c.fetchone()[0]
            conn.commit()
            conn.close()
            return distributor_id

        def get_downline(self, distributor_id: int) -> List:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("""
                WITH RECURSIVE downline AS (
                    SELECT id, upline_id, level, 1 as depth
                    FROM distributors
                    WHERE id = ?
                    UNION ALL
                    SELECT d.id, d.upline_id, d.level, dl.depth + 1
                    FROM distributors d
                    INNER JOIN downline dl ON d.upline_id = dl.id
                )
                SELECT * FROM downline WHERE id != ?
            """, (distributor_id, distributor_id))
            downline = c.fetchall()
            conn.close()
            return downline

        # Lead operations
        def add_lead(self, data: Dict):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("""
                INSERT INTO leads (
                    telegram_id, first_name, last_name, email,
                    phone, country, distributor_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                RETURNING id
            """, (data['telegram_id'], data['first_name'], data['last_name'],
                  data['email'], data['phone'], data['country'],
                  data['distributor_id']))
            lead_id = c.fetchone()[0]
            conn.commit()
            conn.close()
            return lead_id

        # Template operations
        def get_sequence_templates(self) -> List:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("""
                SELECT m.*, a.delay_days, a.sequence_order
                FROM message_templates m
                JOIN autoresponder_sequence a ON m.id = a.template_id
                WHERE m.active = 1
                ORDER BY a.sequence_order
            """)
            templates = c.fetchall()
            conn.close()
            return templates

        # Distributor retrieval
        def get_distributor(self, distributor_id: int):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM distributors WHERE id = ?", (distributor_id,))
            distributor = c.fetchone()
            conn.close()
            return distributor

        # Lead retrieval
        def get_lead(self, lead_id: int):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM leads WHERE id = ?", (lead_id,))
            lead = c.fetchone()
            conn.close()
            return lead
