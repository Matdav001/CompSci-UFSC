library ieee;
  use ieee.std_logic_1164.all;

entity majority3 is
  port (
    SW   : in    std_logic_vector(9 downto 0);
    LEDR : out   std_logic_vector(9 downto 0)
  );
end majority3;

architecture circuito_logico of majority3 is

begin

  LEDR(0) <= SW(2) and (not SW(1)) and (not SW(0));

end circuito_logico;

