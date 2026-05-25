library ieee;
  use ieee.std_logic_1164.all;

entity circuito2 is
  port (
    SW   : in    std_logic_vector(9 downto 0);
    LEDR : out   std_logic_vector(9 downto 0)
  );
end circuito2;

architecture arc_circuito2 of circuito2 is

begin

  LEDR(9 downto 0) <= SW(9 downto 0);

end arc_circuito2;
