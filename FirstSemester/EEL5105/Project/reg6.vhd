library ieee;
  use ieee.std_logic_1164.all;

entity registrador6 is
  port (
    RST, CLK, EN : in    std_logic;
    D            : in    std_logic_vector(5 downto 0);
    Q            : out   std_logic_vector(5 downto 0)
  );
end registrador6;

architecture arc_reg4 of registrador6 is

begin

  process (CLK, D, RST) is
  begin

    if (RST = '0') then
      Q <= "000000";
    elsif (CLK'event and CLK = '1') then
      if (EN = '0') then
        Q <= D;
      end if;
    end if;

  end process;

end arc_reg4;
