library ieee;
  use ieee.std_logic_1164.all;

entity selector is
  port (
    IN0, IN1, IN2, IN3 : in    std_logic;
    SAIDA              : out   std_logic_vector(1 downto 0)
  );
end selector;

architecture arc_selector of selector is begin

  SAIDA <= "00" when IN0 = '1' else
           "01" when IN1 = '1' else
           "10" when IN2 = '1' else
           "11" when IN3 = '1' else
           "01";

end arc_selector;

