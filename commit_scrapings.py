import MySQLdb

def commit(data):
    conn = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd=''
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS game_scrapings")
    cursor.execute("USE game_scrapings")
    table = """CREATE TABLE IF NOT EXISTS `gamefaqs` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(450) NULL,
        `platform` VARCHAR(45) NULL,
        `rating` FLOAT NULL,
        `difficulty` FLOAT NULL,
        `length` FLOAT NULL,
        PRIMARY KEY (`id`),
        CONSTRAINT game_id UNIQUE (`name`, `platform`)
     )"""
    cursor.execute(table)

    for row in data:
        cursor.execute (
            """
               INSERT INTO gamefaqs (`name`, `platform`, `rating`, `difficulty`, `length`)
               VALUES (%s, %s, %s, %s, %s)
               ON DUPLICATE KEY UPDATE
                   `name` = VALUES(`name`),
                   `platform` = VALUES(`platform`),
                   `rating` = VALUES(`rating`),
                   `difficulty` = VALUES(`difficulty`),
                   `length` = VALUES(`length`)
            """,
            (
                row['name'],
                row['platform'],
                row['rating'],
                row['difficulty'],
                row['length'],
            )
        )
        conn.commit()

    conn.close()
