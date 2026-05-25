library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_signed.all;

entity usertop is
  port (
    CLOCK_50 : in    std_logic;
    KEY                                            : in    std_logic_vector(3 downto 0);
    SW                                             : in    std_logic_vector(17 downto 0);
    LEDR                                           : out   std_logic_vector(17 downto 0);
    HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, HEX6, HEX7 : out   std_logic_vector(6 downto 0)
  );
end usertop;

architecture circuito_exe3 of usertop is

  signal s : std_logic_vector(3 downto 0);
  signal t : std_logic_vector(3 downto 0);
  signal n : std_logic_vector(3 downto 0);

  component decod7seg is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(6 downto 0)
    );
  end component decod7seg;

  component reg4 is
    port (
      CLK, RST, EN : in    std_logic;
      D            : in    std_logic_vector(3 downto 0);
      Q            : out   std_logic_vector(3 downto 0)
    );
  end component reg4;

begin

  n(0) <= s(3) and ((not s(1)) or (not s(2)));
  n(1) <= (s(3) xor s(1)) or (s(1) and (not s(0)));
  n(2) <= ((not s(1)) and s(2)) or (s(0) and s(3) and (not s(2)));
  n(3) <= (not s(3)) or ((not s(1)) and s(2)) or (s(1) and (not s(0)));

  reg0 : component reg4 port map (KEY(1), KEY(0), '0', n, s);

  decoder0 : component decod7seg port map (s, HEX0);

  LEDR(3 downto 0) <= s;

  t <= s(1) & s(2) & s(0) & s(3);

  decoder1 : component decod7seg port map (t, HEX1);

end circuito_exe3;
