library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_arith.all;
  use ieee.std_logic_unsigned.all;

entity datapath is
  port (
    M             : in    std_logic_vector(6 downto 0);
    R             : out   std_logic_vector(6 downto 0);
    CLOCK, TW, TC : in    std_logic;
    TM            : out   std_logic
  );
end datapath;

architecture arqdtp of datapath is

  signal tot : std_logic_vector(6 downto 0);

begin

  process (CLOCK, TC, TW) is
  begin

    if (TC = '1') then
      tot <= "0000000";
    elsif (CLOCK'event and CLOCK = '1') then
      if (TW = '1') then
        tot <= tot + 1;
      end if;
    end if;

  end process;

  R <= tot;

  TM <= '1' when (tot < M) else
        '0';

end arqdtp;

