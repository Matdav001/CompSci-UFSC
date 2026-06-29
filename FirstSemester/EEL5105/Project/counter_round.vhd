library ieee;
  use ieee.std_logic_1164.all;

entity counter_round is
  port (
    CLOCK     : in    std_logic;
    RESET     : in    std_logic;
    E         : in    std_logic;
    CONTAGEM  : out   std_logic_vector(3 downto 0);
    END_ROUND : out   std_logic
  );
end counter_round;

architecture simple of counter_round is

  signal atual, proximo : std_logic_vector(3 downto 0);

begin

  p0 : process (CLOCK, RESET, atual) is
  begin

    if (RESET = '0') then
      atual <= "1111";
    elsif (CLOCK'event and CLOCK = '0') then
      if (E = '1') then
        if (atual = "0000") then
          END_ROUND <= '1';
        else
          END_ROUND <= '0';
        end if;
        atual <= proximo;
      end if;
    end if;

  end process;

  p1 : process (atual) is
  begin

    case atual is
      when "0000" =>
        proximo <= "1111"; -- 0 -> 15
      when "0001" =>
        proximo <= "0000"; -- 1 -> 0
      when "0010" =>
        proximo <= "0001"; -- 2 -> 1
      when "0011" =>
        proximo <= "0010"; -- 3 -> 2
      when "0100" =>
        proximo <= "0011"; -- 4 -> 3
      when "0101" =>
        proximo <= "0100"; -- 5 -> 4
      when "0110" =>
        proximo <= "0101"; -- 6 -> 5
      when "0111" =>
        proximo <= "0110"; -- 7 -> 6
      when "1000" =>
        proximo <= "0111"; -- 8 -> 7
      when "1001" =>
        proximo <= "1000"; -- 9 -> 8
      when "1010" =>
        proximo <= "1001"; -- 10 -> 9
      when "1011" =>
        proximo <= "1010"; -- 11 -> 10
      when "1100" =>
        proximo <= "1011"; -- 12 -> 11
      when "1101" =>
        proximo <= "1100"; -- 13 -> 12
      when "1110" =>
        proximo <= "1101"; -- 14 -> 13
      when "1111" =>
        proximo <= "1110"; -- 15 -> 14
      when others =>
        proximo <= "0000";

    end case;

  end process;

  CONTAGEM <= atual;

end simple;
