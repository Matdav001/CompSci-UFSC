library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_signed.all;

entity usertop is
  port (
    SW                                             : in    std_logic_vector(17 downto 0);
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, HEX6, HEX7 : out   std_logic_vector(6 downto 0)
  );
end usertop;

architecture circuito_exe2 of usertop is

  signal f2 : std_logic_vector(3 downto 0);
  signal f3 : std_logic_vector(3 downto 0);
  signal h  : std_logic;

  component mux21_4 is
    port (
      F1, F2 : in    std_logic_vector(3 downto 0);
      SEL    : in    std_logic;
      SAIDA  : out   std_logic_vector(3 downto 0)
    );
  end component mux21_4;

  component mux21_7 is
    port (
      F1, F2 : in    std_logic_vector(6 downto 0);
      SEL    : in    std_logic;
      SAIDA  : out   std_logic_vector(6 downto 0)
    );
  end component mux21_7;

  component decod7seg is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(6 downto 0)
    );
  end component decod7seg;

begin

  mux0 : component mux21_7 port map ("1000110", "0001001", SW(17), HEX0);

  mux1 : component mux21_7 port map ("0011100", "0001100", SW(17), HEX1);

  mux2 : component mux21_4 port map (SW(11 downto 8), SW(3 downto 0), SW(17), f2);

  mux3 : component mux21_4 port map (SW(15 downto 12), SW(7 downto 4), SW(17), f3);

  decod7seg2 : component decod7seg port map (f2, HEX2);

  decod7seg3 : component decod7seg port map (f3, HEX3);

  h <= (not SW(17)) and (SW(15) or SW(14));

  mux4 : component mux21_7 port map ("1111111", "1111011", h, HEX4);

  mux5 : component mux21_7 port map ("1111111", "0001001", h, HEX5);

  HEX6 <= "1111111";
  HEX7 <= "1111111";

end circuito_exe2;

