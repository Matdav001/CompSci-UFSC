library ieee;
  use ieee.std_logic_1164.all;

entity circuito_multi_d is
  port (
    SW   : in    std_logic_vector(3 downto 0);
    LEDR : out   std_logic_vector(3 downto 0)
  );
end circuito_multi_d;

architecture circuito_d of circuito_multi_d is

begin

  LEDR(3) <= ((not SW(3)) and (not SW(2)) and  SW(1) and SW(0)) or (SW(2) and SW(1) and (not SW(0))) or (SW(3) and (not SW(1)) and SW(0)) or (SW(3) and SW(2));
  LEDR(2) <= not SW(0);
  LEDR(1) <= (SW(0) and (SW(1) or SW(2))) or (SW(1) and (SW(3) nor SW(2)));
  LEDR(0) <= (not SW(1)) and (SW(2) or not SW(0));

end circuito_d;
