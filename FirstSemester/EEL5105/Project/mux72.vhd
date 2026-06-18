library ieee;
  use ieee.std_logic_1164.all;

entity multiplexador72 is
  port (
    F1, F2 : in    std_logic_vector(6 downto 0);
    SEL    : in    std_logic;
    SAIDA  : out   std_logic_vector(6 downto 0)
  );
end multiplexador72;

architecture circuito of multiplexador72 is

begin

  SAIDA <= F1 when SEL = '0' else
           F2;

end circuito;
