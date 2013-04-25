'''
Test script
*WARNING* Don't run this on a production litecoin server! *WARNING*
Only on the test network.
'''
import sys
sys.path.append('../src')

import litecoinrpc
# from litecoinrpc.exceptions import LitecoinException, InsufficientFunds 

from decimal import Decimal

if __name__ == "__main__":
    conn = litecoinrpc.connect_to_local()
    assert(conn.getinfo().testnet) # don't test on prodnet

    assert(type(conn.getblockcount()) is int)
    assert(type(conn.getconnectioncount()) is int)
    assert(type(conn.getdifficulty()) is Decimal)
    assert(type(conn.getgenerate()) is bool)
    conn.setgenerate(True)
    conn.setgenerate(True, 2)
    conn.setgenerate(False)
    assert(type(conn.gethashespersec()) is int)
    account = "testaccount"
    account2 = "testaccount2"
    litecoinaddress = conn.getnewaddress(account)
    conn.setaccount(litecoinaddress, account)
    address = conn.getaccountaddress(account)
    address2 = conn.getaccountaddress(account2)
    assert(conn.getaccount(address) == account) 
    addresses = conn.getaddressesbyaccount(account)
    assert(address in addresses)
    #conn.sendtoaddress(litecoinaddress, amount, comment=None, comment_to=None)
    conn.getreceivedbyaddress(litecoinaddress)
    conn.getreceivedbyaccount(account)
    conn.listreceivedbyaddress()
    conn.listreceivedbyaccount()
    #conn.backupwallet(destination)
    x = conn.validateaddress(address)
    assert(x.isvalid == True)
    x = conn.validateaddress("invalid")
    assert(x.isvalid == False)

    for accid in conn.listaccounts(as_dict=True).iterkeys():
      tx = conn.listtransactions(accid)
      if len(tx) > 0:
        txid = tx[0].txid
        txdata = conn.gettransaction(txid)
        assert(txdata.txid == tx[0].txid)

    assert(type(conn.listunspent()) is list)  # needs better testing

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
    
    m_info = conn.getmininginfo()
    print ("Pooled Transactions: {pooledtx}\n"
           "Testnet: {testnet}\n"
           "Hash Rate: {hashes} H/s".format(pooledtx=m_info.pooledtx,
                                            testnet=m_info.testnet,
                                            hashes=m_info.hashespersec))
