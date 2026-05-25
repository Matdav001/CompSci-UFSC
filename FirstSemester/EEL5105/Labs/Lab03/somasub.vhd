library ieee;
  use ieee.std_logic_1164.all;

entity somasub is
  port (
    SW   : in    std_logic_vector(9 downto 0);
    LEDR : out   std_logic_vector(9 downto 0)
  );
end somasub;

architecture soma4 of somasub is

  signal sb   : std_logic_vector(3 downto 0);
  signal cout : std_logic_vector(3 downto 0);

  component modb is
    port (
      I2 : in    std_logic;
      I1 : in    std_logic;
      I0 : in    std_logic;
      R  : out   std_logic
    );
  end component modb;

  component fulladder is
    port (
      A    : in    std_logic;
      B    : in    std_logic;
      CIN  : in    std_logic;
      SUM  : out   std_logic;
      COUT : out   std_logic
    );
  end component fulladder;

begin

  modb1 : component modb port map (SW(9), SW(8), SW(4), sb(0));

  modb2 : component modb port map (SW(9), SW(8), SW(5), sb(1));

  modb3 : component modb port map (SW(9), SW(8), SW(6), sb(2));

  modb4 : component modb port map (SW(9), SW(8), SW(7), sb(3));

  fa0 : component fulladder port map (SW(0), sb(0), SW(8), LEDR(0), cout(0));

  fa1 : component fulladder port map (SW(1), sb(1), cout(0), LEDR(1), cout(1));

  fa2 : component fulladder port map (SW(2), sb(2), cout(1), LEDR(2), cout(2));

  fa3 : component fulladder port map (SW(3), sb(3), cout(2), LEDR(3), cout(3));

  LEDR(9) <= cout(3) xor cout(2);

end soma4;
