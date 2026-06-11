library ieee;
  use ieee.std_logic_1164.all;

entity machinemanager is
  port (
    KEY        : in    std_logic_vector(3 downto 0);
    SW         : in    std_logic_vector(9 downto 0);
    CLOCK_50   : in    std_logic;
    LEDR       : out   std_logic_vector(9 downto 0);
    HEX0, HEX1 : out   std_logic_vector(6 downto 0)
  );
end machinemanager;

architecture arqmachine of machinemanager is

  signal m, r    : std_logic_vector(6 downto 0);
  signal c, c1hz : std_logic;

  signal tw      : std_logic;
  signal tc      : std_logic;
  signal tm      : std_logic;
  signal hex1_in : std_logic_vector(3 downto 0);

  component datapath is
    port (
      M             : in    std_logic_vector(6 downto 0);
      R             : out   std_logic_vector(6 downto 0);
      CLOCK, TW, TC : in    std_logic;
      TM            : out   std_logic
    );
  end component datapath;

  component controle is
    port (
      C, TM, CLOCK, RESET : in    std_logic;
      TC, TW              : out   std_logic
    );
  end component controle;

  component div_freq is
    port (
      RESET : in    std_logic;
      CLOCK : in    std_logic;
      C1HZ  : out   std_logic
    );
  end component div_freq;

  component decod7seg is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(6 downto 0)
    );
  end component decod7seg;

begin

  m                <= SW(6 downto 0);
  c                <= KEY(1);
  LEDR(6 downto 0) <= r;

  clk1hz : component div_freq port map (KEY(0), CLOCK_50, c1hz);

  cont : component controle port map (c, tm, c1hz, KEY(0), tc, tw);

  datapath1 : component datapath port map (m, r, c1hz, tw, tc, tm);

  LEDR(9) <= c;

  decod7seg1 : component decod7seg port map (r(3 downto 0), HEX0);

  hex1_in <= '0' & r(6 downto 4);

  decod7seg2 : component decod7seg port map (hex1_in, HEX1);

end arqmachine;
