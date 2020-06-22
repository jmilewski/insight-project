create table iex_events_test
(
    symbol text,
    primaryExchange text,
    eventType text,
    timestamp bigint,
    reason text,
    price numeric(10,2),
    size numeric(20,4),
    side text
);
