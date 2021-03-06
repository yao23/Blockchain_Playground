/**
 *  @file
 *  @copyright defined in eos/LICENSE.txt
 */
#include <cloudcoin.hpp>
#include <eoslib/eos.hpp>
#include <eoslib/token.hpp>
#include <eoslib/generic_currency.hpp>

typedef eosio::generic_currency<eosio::token<N(cloudcoin), S(10, CCH)> >cloud_coin;

/**
 *  The init() and apply() methods must have C calling convention so that the blockchain can lookup and
 *  call these methods.
 */
extern "C" {

    /**
     *  This method is called once when the contract is published or updated.
     */
    void init()  {
        eosio::print( "Init Cloud Coin!\n" ); // Replace with actual code
    }

    /// The apply method implements the dispatch of events to this contract
    void apply( uint64_t code, uint64_t action ) {
       eosio::print( "Hello World: ", eosio::name(code), "->", eosio::name(action), "\n" );
/*
        if (code == N(${contract_name})) {
            //your handler to response to particular message
            eosio::print( "Smart Contract: ", eosio::name(contrac_name), "\n" );
        }

        if (action == N(${action_name})) {
            //your handler to respond to a particular action
            eosio::print( "Action: ", eosio::name(action_name), "\n" );
        }
*/
        cloud_coin::apply(code, action);
    }

} // extern "C"
