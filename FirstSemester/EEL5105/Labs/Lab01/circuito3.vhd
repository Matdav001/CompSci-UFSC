library ieee;
  use ieee.std_logic_1164.all;

entity circuito3 is
  port (
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5 : out   std_logic_vector(6 downto 0)
  );
end circuito3;

architecture arc_circuito3 of circuito3 is

begin

  HEX5(6 downto 0) <= "0101011"; -- M
  HEX4(6 downto 0) <= "0001000"; -- A
  HEX3(6 downto 0) <= "0000111"; -- T
  HEX2(6 downto 0) <= "0000110"; -- E
  HEX1(6 downto 0) <= "1000001"; -- U
  HEX0(6 downto 0) <= "0010010"; -- S

end arc_circuito3;

