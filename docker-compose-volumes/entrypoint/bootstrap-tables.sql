USE chartdata;

CREATE TABLE pairs
(
    id    BIGINT      NOT NULL AUTO_INCREMENT,
    sym   VARCHAR(10) NOT NULL,
    tf    VARCHAR(3)  NOT NULL,
    d     DATETIME    NOT NULL,
    o     DOUBLE      NOT NULL,
    h     DOUBLE      NOT NULL,
    l     DOUBLE      NOT NULL,
    c     DOUBLE      NOT NULL,
    vol   DOUBLE      NOT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX idx_sym ON pairs(sym);
CREATE INDEX idx_tf ON pairs(tf);
CREATE INDEX idx_d ON pairs(d);
ALTER TABLE pairs ENGINE = INNODB;