//
// Created by Yao Li on 3/7/18.
//

#include <eosiolib/eosio.hpp>
#include <eosiolib/token.hpp>
#include <eosiolib/generic_currency.hpp>

typedef eosio::generic_currency<eosio::token<N(my.token), S(8,MYT)> > my_token;

extern  "C" {
    void apply(uint64_t code, uint64_t action) {
        my_token::apply(code, action);
    }
}
