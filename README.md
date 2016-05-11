# accounts

This is a program intended to aid in the functions of personal accounting.

It operates over abstractions of values, transactions, parties, balances, 
invoices, and receipts.

## `Value`

Any good, service, or idea possessing value insofar as it can be represented by 
a quantifiable form of currency.

Examples:
- `Cash`
- `Check`
- `Consultation`
- `Bread`

## `Party`

Unfortunately not the cake kind of party, but feel free to eat cake anyway. 
A `Party` is an entity that can own value. Denoted in this document by capital 
letters.

## `Transaction`

T<sub>AB</sub>

A change in ownership of `Value` occuring in time between two `Parties`, from A 
to B.

## `Balance`

B<sub>AB</sub> = Σ T<sub>AB</sub> - Σ T<sub>BA</sub>

`Balance` is defined directionally between two `Parties`, A and B, as the total 
value of `Transactions` from A to B ***minus*** the total value of 
`Transactions` from B to A. It follows that a positive `Balance` indicates that 
`Party` A has given more `Value` to `Party` B.

## `Invoice`

A request from `Party` A to `Party` B to perform payment for the `Balance`, 
B<sub>AB</sub>. An `Invoice` is only meaningful when the `Balance` is positive.

This is a document which indicates the most recent `Transactions`, 
T<sub>AB</sub> such that Σ(T<sub>AB</sub>.value()) is less than or equal to 
B<sub>AB</sub>.

In other words, an itemized invoice pointing to specific goods or services 
rendered that accumulate to the remaining `Balance`.

Since B<sub>AB</sub> may not align with the full value of the recent 
`Transactions`, the `Invoice` should indicate when partial payment has already 
been made, perhaps as a pseudo-transaction called partial credit.


                         partial credit
                            v
                           / \
    [ Tba                     ][ Bab             ]
    [ Tab     |   |    |  |        |         |   ]
                              ^         ^      ^
                           partial    unpaid  unpaid


   Resulting in an invoice of `unpaid + unpaid + partial - credit`.

## `Receipt`

A document rendered by `Party` A acknowledging the validity of a `Transaction`, 
T<sub>BA</sub>.

