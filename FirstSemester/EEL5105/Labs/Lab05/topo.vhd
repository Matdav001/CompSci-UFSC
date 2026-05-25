library ieee;
  use ieee.std_logic_1164.all;

entity topo is
  port (
    SW                                 : in    std_logic_vector(9 downto 0);
    LEDR                               : out   std_logic_vector(9 downto 0);
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5 : out   std_logic_vector(6 downto 0);
    KEY                                : in    std_logic_vector(3 downto 0);
    CLOCK_50                           : in    std_logic
  );
end topo;

architecture arc_topo of topo is

  signal f1 : std_logic_vector(3 downto 0);
  signal f2 : std_logic_vector(3 downto 0);
  signal f3 : std_logic_vector(3 downto 0);
  signal f4 : std_logic_vector(3 downto 0);
  signal f  : std_logic_vector(3 downto 0);
  signal g  : std_logic_vector(3 downto 0);
  signal h  : std_logic_vector(3 downto 0);
  signal s  : std_logic_vector(6 downto 0);
  signal ha : std_logic_vector(6 downto 0);
  signal hb : std_logic_vector(6 downto 0);

  component mux is
    port (
      W     : in    std_logic_vector(3 downto 0);
      X     : in    std_logic_vector(3 downto 0);
      Y     : in    std_logic_vector(3 downto 0);
      Z     : in    std_logic_vector(3 downto 0);
      SEL   : in    std_logic_vector(1 downto 0);
      SAIDA : out   std_logic_vector(3 downto 0)
    );
  end component mux;

  component sum is
    port (
      A : in    std_logic_vector(3 downto 0);
      B : in    std_logic_vector(3 downto 0);
      F : out   std_logic_vector(3 downto 0)
    );
  end component sum;

  component reg4 is
    port (
      CLK, RST, EN : in    std_logic;
      D            : in    std_logic_vector(3 downto 0);
      Q            : out   std_logic_vector(3 downto 0)
    );
  end component reg4;

  component decod7seg is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(6 downto 0)
    );
  end component decod7seg;

begin

  f1(3 downto 0) <= '0' & SW(2 downto 0); -- A
  f2(3 downto 0) <= SW(2 downto 0) & '0'; -- 2A
  f3(3 downto 0) <= '0' & SW(6 downto 4); -- B
  f4(3 downto 0) <= SW(6 downto 4) & '0'; -- 2B

  fa1 : component mux port map (f1, f2, f3, f4, SW(9 downto 8), f);

  fa2 : component sum port map (f1, f, g);

  fa3 : component reg4 port map (CLOCK_50, KEY(0), KEY(1), g, h);

  fa4 : component decod7seg port map (h, s);

  fa5 : component decod7seg port map (f1, ha);

  fa6 : component decod7seg port map (f3, hb);

  LEDR(9 downto 0) <= "000000" & h;
  HEX0(6 downto 0) <= s;
  HEX1(6 downto 0) <= "0110111";
  HEX2(6 downto 0) <= hb;
  HEX3(6 downto 0) <= "0000011";
  HEX4(6 downto 0) <= ha;
  HEX5(6 downto 0) <= "0001000";

end arc_topo;

