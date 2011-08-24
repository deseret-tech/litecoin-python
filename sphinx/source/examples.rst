****************************
  Examples
****************************

A basic program that uses ``python-bitcoin`` looks like this:

First, import the library and exceptions.

::

    import bitcoinrpc
    from bitcoinrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``bitcoin`` instance of the current user on the local machine
with one call to
:func:`~bitcoinrpc.connect_to_local`. This returns a :class:`~bitcoinrpc.connection.BitcoinConnection` objects:

::

    conn = bitcoinrpc.connect_to_local()

Try to move one bitcoin from account ``testaccount`` to account ``testaccount2`` using 
:func:`~bitcoinrpc.connection.BitcoinConnection.move`. Catch the :class:`~bitcoinrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~bitcoinrpc.connection.BitcoinConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

