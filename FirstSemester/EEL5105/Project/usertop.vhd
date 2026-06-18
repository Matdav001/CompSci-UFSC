library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all; -- necessário para o +

entity usertop is
  port (
    -- CLOCK_50:in std_logic;
    CLK_500HZ : in    std_logic;
    -- RKEY:in std_logic_vector(3 downto 0);
    KEY : in    std_logic_vector(3 downto 0);
    -- RSW:in std_logic_vector(17 downto 0);
    SW                                             : in    std_logic_vector(17 downto 0);
    LEDR                                           : out   std_logic_vector(17 downto 0);
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, HEX6, HEX7 : out   std_logic_vector(6
downto 0)
  );
end usertop;

architecture circuito of usertop is

  signal r1        : std_logic;
  signal r2        : std_logic;
  signal e1        : std_logic;
  signal e2        : std_logic;
  signal e3        : std_logic;
  signal e4        : std_logic;
  signal e5        : std_logic;
  signal end_game  : std_logic;
  signal end_time  : std_logic;
  signal end_round : std_logic;
  signal enter     : std_logic;
  signal reset     : std_logic;

  component datapath is
    port (
      S                                              : in    std_logic_vector(15 downto 0);
      CLK, R1, R2, E1, E2, E3, E4, E5                : in    std_logic;
      END_GAME, END_TIME, END_ROUND                  : out   std_logic;
      HEX7, HEX6, HEX5, HEX4, HEX3, HEX2, HEX1, HEX0 : out   std_logic_vector(6 downto 0);
      LED                                            : out   std_logic_vector(15 downto 0)
    );
  end component datapath;

  component controle is
    port (
      CLOCK, K1, K0, ENDTIME, ENDGAME, ENDROUND : in    std_logic;
      R1, R2, E1, E2, E3, E4, E5                : out   std_logic
    );
  end component controle;

  component buttonsync is
    port (
      KEY0, KEY1, CLK : in    std_logic;
      ENTER, RESET    : out   std_logic
    );
  end component buttonsync;

begin

  bot : component buttonsync port map (KEY(0), KEY(1), CLK_500HZ, enter, reset); -- CLK??

  data : component datapath port map (SW(15 downto 0), CLK_500HZ, r1, r2, e1, e2, e3, e4, e5, end_game, end_time, end_round, HEX7, HEX6, HEX5, HEX4, HEX3, HEX2, HEX1, HEX0, LEDR(15 downto 0));

  ctrl : component controle port map (CLK_500HZ, enter, reset, end_time, end_game, end_round, r1, r2, e1, e2, e3, e4, e5);

end circuito;

