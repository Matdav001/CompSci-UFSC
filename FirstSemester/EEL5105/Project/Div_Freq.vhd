library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;

-- para uso com o clock de 500Hz do FPGAEmu (CLK_500Hz)

entity div_freq is
  port (
    CLK              : in    std_logic;
    RESET            : in    std_logic;
    CLK_1HZ, SIM_2HZ : out   std_logic
  );
end div_freq;

architecture divisor of div_freq is

  signal cont : std_logic_vector(11 downto 0); -- Registra valor da contagem

begin

  p1 : process (CLK, RESET, cont) is -- clock 500Hz
  begin

    if (RESET = '1') then
      cont    <= x"000";
      CLK_1HZ <= '0';
      SIM_2HZ <= '0';
    elsif (CLK'event and CLK = '1') then
      -- 1Hz = 1s = 500Hzx1 = 500
      if (cont < x"0F9") then            -- se contador < 249 (0F9 em hexadecimal)
        SIM_2HZ <= '0';
        CLK_1HZ <= '0';
        cont    <= cont + 1;
      elsif (cont < x"1F3") then         -- se contador < 499 (1F3 em hexadecimal)
        CLK_1HZ <= '0';
        SIM_2HZ <= '1';
        cont    <= cont + 1;
      else
        cont    <= x"000";
        CLK_1HZ <= '1';
        SIM_2HZ <= '1';
      end if;
    end if;

  end process;

end divisor;
