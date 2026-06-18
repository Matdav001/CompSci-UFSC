library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;

entity somador is
   port (
      A : in    std_logic_vector(2 downto 0);
      B : in    std_logic_vector(2 downto 0);
      C : in    std_logic_vector(2 downto 0);
      D : in    std_logic_vector(2 downto 0);
      F : out   std_logic_vector(2 downto 0)
    );
end somador;

architecture circuito of somador is

begin

  F <= A + B + C + D;

end circuito;
