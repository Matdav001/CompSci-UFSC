library ieee;
  use ieee.std_logic_1164.all;

entity somador is
  port (
    X3, X2, X1, X0     : in    std_logic;
    Y3, Y2, Y1, Y0     : in    std_logic;
    S4, S3, S2, S1, S0 : out   std_logic
  );
end somador;

architecture soma4 of somador is

  signal c0 : std_logic;
  signal c1 : std_logic;
  signal c2 : std_logic;

  component halfadder is
    port (
      A    : in    std_logic;
      B    : in    std_logic;
      SUM  : out   std_logic;
      COUT : out   std_logic
    );
  end component halfadder;

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

  ha : component halfadder port map (X0, Y0, S0, c0);

  fa1 : component fulladder port map (X1, Y1, c0, S1, c1);

  fa2 : component fulladder port map (X2, Y2, c1, S2, c2);

  fa3 : component fulladder port map (X3, Y3, c2, S3, S4);

end soma4;

