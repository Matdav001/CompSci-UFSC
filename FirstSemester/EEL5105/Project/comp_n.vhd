
library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;

entity comp_n is
  port (
    C  : in    std_logic_vector(3 downto 0);
    U  : in    std_logic_vector(3 downto 0);
    P0 : out   std_logic_vector(2 downto 0)
  );
end comp_n;

architecture circuito of comp_n is

begin

  P0 <= "001" when (C = U) else
        "000";

end circuito;
