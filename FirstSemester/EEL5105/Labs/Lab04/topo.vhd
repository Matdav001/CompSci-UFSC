library ieee;
  use ieee.std_logic_1164.all;

entity topo is
  port (
    SW   : in    std_logic_vector(9 downto 0);
    LEDR : out   std_logic_vector(3 downto 0);
    HEX0 : out   std_logic_vector(6 downto 0)
  );
end topo;

architecture summux of topo is

  signal f  : std_logic_vector(3 downto 0);
  signal f1 : std_logic_vector(3 downto 0);
  signal f2 : std_logic_vector(3 downto 0);
  signal f3 : std_logic_vector(3 downto 0);
  signal f4 : std_logic_vector(3 downto 0);
  signal g  : std_logic_vector(3 downto 0);

  component sum is
    port (
      A : in    std_logic_vector(3 downto 0);
      B : in    std_logic_vector(3 downto 0);
      F : out   std_logic_vector(3 downto 0)
    );
  end component sum;

  component mux is
    port (
      SEL            : in    std_logic_vector(1 downto 0);
      F1, F2, F3, F4 : in    std_logic_vector(3 downto 0);
      SAIDA          : out   std_logic_vector(3 downto 0)
    );
  end component mux;

  component decod7seg is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(6 downto 0)
    );
  end component decod7seg;

begin

  f1 <= "0" & SW(2 downto 0);
  f2 <= SW(2 downto 0) & "0";
  f3 <= "0" & SW(6 downto 4);
  f4 <= SW(6 downto 4) & "0";

  mux1 : component mux port map (SW(9 downto 8), f1, f2, f3, f4, f);

  sum1 : component sum port map (f1, f, g);

  decod7seg1 : component decod7seg port map (g, HEX0);

  LEDR(3 downto 0) <= g;

end summux;
