SCHEMA = """\
CREATE TABLE gene (
    id              INTEGER PRIMARY KEY,
    name            TEXT,
    start_pos       INTEGER,
    end_pos         INTEGER,
    strand          INTEGER,
    translation     TEXT,
    scaffold        TEXT,
    organism        TEXT
);\
"""

ID_QUERY = """\
SELECT
    id,
    name,
    start_pos,
    end_pos,
    strand,
    scaffold,
    organism
FROM
    gene
WHERE
    id IN ({})\
"""

NAME_QUERY = """\
SELECT
    name,
    translation,
    scaffold
FROM
    gene
WHERE
    name IN ({})\
"""

FASTA = 'SELECT ">"||gene.id||"\n"||gene.translation||"\n" FROM gene'

INSERT = """\
INSERT INTO gene (
    name,
    start_pos,
    end_pos,
    strand,
    translation,
    scaffold,
    organism
)
VALUES
    (?, ?, ?, ?, ?, ?, ?)\
"""
