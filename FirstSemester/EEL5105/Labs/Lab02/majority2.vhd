library ieee;
  use ieee.std_logic_1164.all;

entity majority2 is
  port (
    SW   : in    std_logic_vector(9 downto 0);
    LEDR : out   std_logic_vector(9 downto 0)
  );
end majority2;

architecture circuito_logico of majority2 is

begin

  LEDR(0) <= (SW(0) and SW(1)) or (SW(0) and SW(2)) or (SW(1) and SW(2));

end circuito_logico;

