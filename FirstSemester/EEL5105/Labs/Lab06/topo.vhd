library ieee;
  use ieee.std_logic_1164.all;

entity topo is
  port (
    LEDR     : out   std_logic_vector(3 downto 0);
    CLOCK_50 : in    std_logic;
    KEY      : in    std_logic_vector(1 downto 0);
    HEX0     : out   std_logic_vector(6 downto 0);
    SW       : in    std_logic_vector(9 downto 0)
  );
end topo;

architecture topo_beh of topo is

  signal c1hz : std_logic;
  signal f    : std_logic_vector(3 downto 0);

  component fsm_conta is
    port (
      UPDOWN   : in    std_logic;
      CONTAGEM : out   std_logic_vector(3 downto 0);
      CLOCK    : in    std_logic;
      RESET    : in    std_logic
    );
  end component fsm_conta;

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

  clk1hz : component div_freq port map (KEY(0), CLOCK_50, c1hz);

  cont : component fsm_conta port map (SW(0), f, c1hz, KEY(0));

  decod7seg1 : component decod7seg port map (f, HEX0);

  LEDR <= f;

end topo_beh;

