create table token_transfers_test
(
    type varchar(42),
    token_address varchar(42),
    from_address varchar(42),
    to_address varchar(42),
    value numeric(78),
    transaction_hash varchar(255),
    log_index bigint,
    block_number bigint,
    block_timestamp bigint,
    block_hash varchar(255),
    item_id varchar(255),
    item_timestamp text
);
