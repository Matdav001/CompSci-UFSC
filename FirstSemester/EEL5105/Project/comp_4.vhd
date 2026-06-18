
library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;

entity comp_4 is
  port (
    P    : in    std_logic_vector(2 downto 0);
    PEQ4 : out   std_logic
  );
end comp_4;

architecture circuito of comp_4 is

begin

  PEQ4 <= '1' when (P = "100") else
          '0';

end circuito;
