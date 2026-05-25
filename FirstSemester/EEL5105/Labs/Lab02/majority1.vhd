library ieee;
  use ieee.std_logic_1164.all;

entity majority1 is
  port (
    A : in    std_logic;
    B : in    std_logic;
    C : in    std_logic;
    Y : out   std_logic
  );
end majority1;

architecture circuito_logico of majority1 is

begin

  Y <= (A and B) or (A and C) or (B and C);

end circuito_logico;

