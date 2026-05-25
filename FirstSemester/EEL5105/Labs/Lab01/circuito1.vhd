library ieee;
  use ieee.std_logic_1164.all;

entity circuito1 is
  port (
    LEDR : out   std_logic_vector(9 downto 0)
  );
end circuito1;

architecture arc_circuito1 of circuito1 is

begin

  LEDR(9 downto 0) <= "1011010111";

end arc_circuito1;

