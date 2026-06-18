library ieee;
  use ieee.std_logic_1164.all;

entity mux41_16 is
  port (
    F1, F2, F3, F4 : in    std_logic_vector(15 downto 0);
    SEL            : in    std_logic_vector(1 downto 0);
    SAIDA          : out   std_logic_vector(15 downto 0)
  );
end mux41_16;

architecture circuito of mux41_16 is

begin

  SAIDA <= F1 when SEL = "00" else
           F2 when SEL = "01" else
           F3 when SEL = "10" else
           F4;

end circuito;

