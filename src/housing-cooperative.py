from pyteal import *

def coop():
    # Define schema: one Global (entire network sees the same value) and one Local (each user sees a different value)
    global_schema = GlobalSchema(num_uints=1, num_byte_slices=0)
    local_schema = LocalSchema(num_uints=1, num_byte_slices=1)

    # On initialization, store the creator's address in global state
    initializing = Seq([
        App.globalPut(Bytes("creator"), Txn.sender()),
        Return(Int(1))
    ])

    # Ensure that only the creator can change the app
    running = Assert(Txn.sender() == App.globalGet(Bytes("creator")))

    # If transaction is a NoOp, expect two arguments: 
    # - a byte string "add" or "setOwner"
    # - an address (house identifier)
    on_initialization = Seq([
        Assert(Txn.application_id() == Int(0)),
        Cond(
            [Txn.application_args[0] == Bytes("add"), initializing],
            [Txn.application_args[0] == Bytes("setOwner"), running]
        )
    ])

    # Set house owner
    set_owner = Seq([
        App.localPut(Int(0), Bytes("owner"), Txn.application_args[1]),
        Return(Int(1))
    ])

    # Add house
    add_house = Seq([
        App.localPut(Int(0), Bytes("houseId"), Txn.application_args[1]),
        Return(Int(1))
    ])

    # On a call (not initialization), expect two arguments and make changes
    on_call = Seq([
        Cond(
            [Txn.application_args[0] == Bytes("add"), add_house],
            [Txn.application_args[0] == Bytes("setOwner"), set_owner]
        )
    ])

    # Main contract
    return Cond(
        [Txn.application_id() == Int(0), on_initialization],
        [Txn.application_id() != Int(0), on_call]
    )

# Compile PyTeal to TEAL
compiled = compileTeal(coop(), mode=Mode.Application, version=3)
print(compiled)
