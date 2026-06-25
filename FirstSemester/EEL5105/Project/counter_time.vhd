library ieee;
  use ieee.std_logic_1164.all;

entity counter_time is
  port (
    CLOCK    : in    std_logic;
    RESET    : in    std_logic;
    E        : in    std_logic;
    CONTAGEM : out   std_logic_vector(3 downto 0)
  );
end counter_time;

architecture simple of counter_time is

  signal atual, proximo : std_logic_vector(3 downto 0);

begin

  p_registrador : process (CLOCK, RESET) is
  begin

    if (RESET = '0') then
      atual <= "1001";
    elsif (CLOCK'event and CLOCK = '0') then
      if (E = '1') then
        atual <= proximo;
      end if;
    end if;

  end process;

  p_proximo : process (atual) is
  begin

    case atual is
      when "1001" => proximo <= "1000"; -- 9 -> 8
      when "1000" => proximo <= "0111"; -- 8 -> 7
      when "0111" => proximo <= "0110"; -- 7 -> 6
      when "0110" => proximo <= "0101"; -- 6 -> 5
      when "0101" => proximo <= "0100"; -- 5 -> 4
      when "0100" => proximo <= "0011"; -- 4 -> 3
      when "0011" => proximo <= "0010"; -- 3 -> 2
      when "0010" => proximo <= "0001"; -- 2 -> 1
      when "0001" => proximo <= "0000"; -- 1 -> 0
      when "0000" => proximo <= "0000"; -- Halts at 0
      when others => proximo <= "1001";
    end case;

  end process;

  CONTAGEM <= atual;

end simple;
