library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;

-- para uso com o clock de 50MHz da placa DE2 (CLOCK_50)

entity div_freq_de2 is
  port (
    CLK     : in    std_logic;
    RESET   : in    std_logic;
    CLK_1HZ : out   std_logic
  );
end div_freq_de2;

architecture divisor of div_freq_de2 is

  signal cont : std_logic_vector(27 downto 0); -- Registra valor da contagem

begin

  p1 : process (CLK, RESET, cont) is
  begin

    if (RESET = '1') then
      cont    <= x"0000000";
      CLK_1HZ <= '0';
    elsif (CLK'event and CLK = '1') then
      -- 1Hz = 1s = 50.000.000Hz = 50.000.000
      if (cont < x"2FAF07F") then  -- se contador < 49.999.999 (2FAF07F em hexadecimal)
        CLK_1HZ <= '0';
        cont    <= cont + 1;
      else
        cont    <= x"0000000";
        CLK_1HZ <= '1';
      end if;
    end if;

  end process;

end divisor;

