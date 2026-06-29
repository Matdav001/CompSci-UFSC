library ieee;
  use ieee.std_logic_1164.all;

entity decodtermo is
  port (
    G     : in    std_logic_vector(3 downto 0);
    SAIDA : out   std_logic_vector(15 downto 0)
  );
end decodtermo;

architecture circuito of decodtermo is

begin

  SAIDA <= "0000000000000001" when G = "0000" else -- 0
           "0000000000000011" when G = "0001" else -- 1
           "0000000000000111" when G = "0010" else -- 2
           "0000000000001111" when G = "0011" else -- 3
           "0000000000011111" when G = "0100" else -- 4
           "0000000000111111" when G = "0101" else -- 5
           "0000000001111111" when G = "0110" else -- 6
           "0000000011111111" when G = "0111" else -- 7
           "0000000111111111" when G = "1000" else -- 8
           "0000001111111111" when G = "1001" else -- 9
           "0000011111111111" when G = "1010" else -- 10
           "0000111111111111" when G = "1011" else -- 11
           "0001111111111111" when G = "1100" else -- 12
           "0011111111111111" when G = "1101" else -- 13
           "0111111111111111" when G = "1110" else -- 14
           "1111111111111111";                     -- 15

end circuito;
