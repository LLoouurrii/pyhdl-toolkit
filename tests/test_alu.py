import cocotb
from cocotb.triggers import Timer


def alu_reference(a, b, operation):
    if operation == 0:
        return (a + b) & 0xF
    elif operation == 1:
        return (a - b) & 0xF
    elif operation == 2:
        return a & b
    elif operation == 3:
        return a | b


@cocotb.test()
async def test_alu(dut):

    for operation in range(4):
        for a in range(16):
            for b in range(16):

                dut.a.value = a
                dut.b.value = b
                dut.operation.value = operation

                await Timer(1, unit="ns")

                expected = alu_reference(a, b, operation)
                expected_zero = '1' if expected == 0 else '0'

                assert dut.result.value.to_unsigned() == expected
                assert dut.zero.value == expected_zero