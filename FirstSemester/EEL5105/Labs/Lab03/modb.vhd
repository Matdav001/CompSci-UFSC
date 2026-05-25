library ieee;
  use ieee.std_logic_1164.all;

entity modb is
  port (
    I2, I1, I0 : in    std_logic;
    R          : out   std_logic
  );
end modb;

architecture mdb of modb is

begin

  R <= (I2 and not I0) or (not I1 and I0);

end mdb;

