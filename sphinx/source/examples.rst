****************************
  Examples
****************************

A basic program that uses ``python-litecoin`` looks like this:

First, import the library and exceptions.

::

    import litecoinrpc
    from litecoinrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``litecoin`` instance of the current user on the local machine
with one call to
:func:`~litecoinrpc.connect_to_local`. This returns a :class:`~litecoinrpc.connection.LitecoinConnection` objects:

::

    conn = litecoinrpc.connect_to_local()

Try to move one litecoin from account ``testaccount`` to account ``testaccount2`` using 
:func:`~litecoinrpc.connection.LitecoinConnection.move`. Catch the :class:`~litecoinrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~litecoinrpc.connection.LitecoinConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

