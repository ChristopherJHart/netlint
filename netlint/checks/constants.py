bogus_as_numbers = [0, 23456, 4294967295]  # RFC6483, RFC7607  # RFC6793  # RFC7300
bogus_as_numbers += list(range(64496, 64511 + 1))  # RFC5398
bogus_as_numbers += list(range(65536, 65551 + 1))  # RFC4893, RFC5398