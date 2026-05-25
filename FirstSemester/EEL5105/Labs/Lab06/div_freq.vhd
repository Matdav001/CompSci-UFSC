library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;

entity div_freq is
  port (
    RESET : in    std_logic;
    CLOCK : in    std_logic;
    C1HZ  : out   std_logic
  );
end div_freq;

architecture topo_beh of div_freq is

  signal contador : std_logic_vector(27 downto 0);

begin

  p1 : process (CLOCK, RESET, contador) is
  begin

    if (RESET = '0') then
      contador <= x"0000000";
    elsif (CLOCK'event and CLOCK = '1') then
      contador <= contador + 1;
      if (contador = x"2FAF07F") then
        contador <= x"0000000";
        C1HZ     <= '1';
      else
        C1HZ <= '0';
      end if;
    end if;

  end process;

end topo_beh;

