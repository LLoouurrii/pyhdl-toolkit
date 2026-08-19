library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu is 
    port (
        a           : in    std_logic_vector(3 downto 0);
        b           : in    std_logic_vector(3 downto 0);
        operation   : in    std_logic_vector(1 downto 0);
        result      : out   std_logic_vector(3 downto 0);
        zero        : out   std_logic
    );
end entity alu;

architecture rtl of alu is
    signal result_internal : unsigned(3 downto 0);
begin

    process(a, b, operation)
    begin
        case operation is
            when "00" =>
                result_internal <= unsigned(a) + unsigned(b);
            when "01" =>
                result_internal <= unsigned(a) - unsigned(b);
            when "10" =>
                result_internal <= unsigned(a) and unsigned(b);
            when "11" =>
                result_internal <= unsigned(a) or unsigned(b);
            when others =>
                result_internal <= (others => '0');
        end case;
    end process;

    result <= std_logic_vector(result_internal);
    zero <= '1' when result_internal = 0 else '0';

end architecture rtl;
