library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_signed.all;

entity usertop is
  port (
    CLOCK_50                                       : in    std_logic;
    KEY                                            : in    std_logic_vector(3 downto 0);
    SW                                             : in    std_logic_vector(17 downto 0);
    LEDR                                           : out   std_logic_vector(17 downto 0);
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, HEX6, HEX7 : out   std_logic_vector(6 downto 0)
  );
end usertop;

architecture circuito_exe2 of usertop is

  signal estado : std_logic_vector(1 downto 0);
  signal f1     : std_logic_vector(15 downto 0);
  signal f2     : std_logic_vector(15 downto 0);
  signal f3     : std_logic_vector(15 downto 0);
  signal f4     : std_logic_vector(15 downto 0);
  signal f      : std_logic_vector(15 downto 0);
  signal q      : std_logic_vector(15 downto 0);

  component mux41_16 is
    port (
      F1    : in    std_logic_vector(15 downto 0);
      F2    : in    std_logic_vector(15 downto 0);
      F3    : in    std_logic_vector(15 downto 0);
      F4    : in    std_logic_vector(15 downto 0);
      SEL   : in    std_logic_vector(1 downto 0);
      SAIDA : out   std_logic_vector(15 downto 0)
    );
  end component mux41_16;

  component reg16 is
    port (
      RST : in    std_logic;
      CLK : in    std_logic;
      EN  : in    std_logic;
      D   : in    std_logic_vector(15 downto 0);
      Q   : out   std_logic_vector(15 downto 0)
    );
  end component reg16;

begin

  f1(15 downto 0) <= q + SW(15 downto 0);  -- soma
  f2(15 downto 0) <= SW(15 downto 0);      -- in
  f3(15 downto 0) <= '0' & q(15 downto 1); -- >>
  f4(15 downto 0) <= q(14 downto 0) & '0'; -- <<

  fa1 : component mux41_16 port map (f1, f2, f3, f4, SW(17 downto 16), f);

  fa3 : component reg16 port map (KEY(0), KEY(1), '0', f, q);

  LEDR(15 downto 0) <= q;

end circuito_exe2;

