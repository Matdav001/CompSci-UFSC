library ieee;
  use ieee.std_logic_1164.all;

entity mux is
  port (
    F1, F2, F3, F4 : in    std_logic_vector(6 downto 0);
    SEL            : in    std_logic_vector(1 downto 0);
    SAIDA          : out   std_logic_vector(6 downto 0)
  );
end mux;

architecture circuito of mux is

begin

  SAIDA <= F1 when SEL = "00" else
           F2 when SEL = "01" else
           F3 when SEL = "10" else
           F4;

end circuito;
