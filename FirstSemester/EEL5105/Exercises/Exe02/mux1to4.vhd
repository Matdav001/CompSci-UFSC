library ieee;
  use ieee.std_logic_1164.all;

entity mux1to4 is
  port (
    SEL    : in    std_logic;
    F1, F2 : in    std_logic_vector(3 downto 0);
    SAIDA  : out   std_logic_vector(3 downto 0)
  );
end mux1to4;

architecture circuito of mux1to4 is

begin

  SAIDA <= F1 when SEL = '0' else
           F2;

end circuito;
