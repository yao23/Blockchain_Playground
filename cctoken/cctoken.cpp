//
// Created by Yao Li on 3/7/18.
//

#include <eosiolib/eosio.hpp>
#include <eosiolib/token.hpp>
#include <eosiolib/generic_currency.hpp>

typedef eosio::generic_currency<eosio::token<N(cctoken), S(10,CCH)> > cctoken;

extern  "C" {
    void apply(uint64_t code, uint64_t action) {
        cctoken::apply(code, action);
    }
}