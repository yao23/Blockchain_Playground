//
// Created by Yao Li on 3/8/18.
//

#include <eosiolib/eosio.hpp>
#include <eosiolib/token.hpp>
#include <eosiolib/generic_currency.hpp>

typedef eosio::generic_currency<eosio::token<N(multi.token), S(8,TKA)> > token_a;
typedef eosio::generic_currency<eosio::token<N(multi.token), S(8,TKB)> > token_b;

extern  "C" {
    void apply(uint64_t code, uint64_t action) {
        token_a::apply(code, action);
        token_b::apply(code, action);
    }
}
