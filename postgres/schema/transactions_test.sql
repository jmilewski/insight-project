create table transactions_test
(
    type varchar(66),
    hash varchar(66),
    nonce bigint,
    transaction_index bigint,
    from_address varchar(42),
    to_address varchar(42),
    value numeric(38),
    gas bigint,
    gas_price bigint,
    input text,
    block_timestamp bigint,
    block_number bigint,
    block_hash varchar(66),
    receipt_cumulative_gas_used bigint,
    receipt_gas_used bigint,
    receipt_contract_address varchar(42),
    receipt_root varchar(66),
    receipt_status bigint,
    item_id varchar(100),
    item_timestamp text
);
