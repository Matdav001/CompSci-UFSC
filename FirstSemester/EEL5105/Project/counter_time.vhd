library ieee;
  use ieee.std_logic_1164.all;

entity counter_time is
  port (
    CLOCK    : in    std_logic;
    RESET    : in    std_logic;
    CONTAGEM : out   std_logic_vector(3 downto 0)
  );
end counter_time;

architecture simple of counter_time is

  signal atual, proximo : std_logic_vector(3 downto 0);

begin

  p_registrador : process (CLOCK, RESET) is
  begin

    if (RESET = '0') then
      atual <= "0000";
    elsif (CLOCK'event and CLOCK = '0') then
      atual <= proximo;
    end if;

  end process;

  p_proximo : process (atual) is
  begin

    case atual is

      when "0000" =>

        proximo <= "0001"; -- 0 -> 1

      when "0001" =>

        proximo <= "0010"; -- 1 -> 2

      when "0010" =>

        proximo <= "0011"; -- 2 -> 3

      when "0011" =>

        proximo <= "0100"; -- 3 -> 4

      when "0100" =>

        proximo <= "0101"; -- 4 -> 5

      when "0101" =>

        proximo <= "0110"; -- 5 -> 6

      when "0110" =>

        proximo <= "0111"; -- 6 -> 7

      when "0111" =>

        proximo <= "1000"; -- 7 -> 8

      when "1000" =>

        proximo <= "1001"; -- 8 -> 9

      when "1001" =>

        proximo <= "1010"; -- 9 -> 10

      when "1010" =>

        proximo <= "1011"; -- 10 -> 11

      when "1011" =>

        proximo <= "1100"; -- 11 -> 12

      when "1100" =>

        proximo <= "1101"; -- 12 -> 13

      when "1101" =>

        proximo <= "1110"; -- 13 -> 14

      when "1110" =>

        proximo <= "1111"; -- 14 -> 15

      when "1111" =>

        proximo <= "0000"; -- 15 -> 0

      when others =>

        proximo <= "0000";

    end case;

  end process;

  CONTAGEM <= atual;

end simple;
