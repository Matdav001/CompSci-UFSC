library ieee;
  use ieee.std_logic_1164.all;

entity controle is
  port (
    CLOCK, K1, K0, ENDTIME, ENDGAME, ENDROUND : in    std_logic;
    R1, R2, E1, E2, E3, E4, E5                : out   std_logic
  );
end controle;

architecture bhv of controle is

  type states is (s_init, s_setup, s_play, s_count_round, s_check, s_wait, s_result);

  signal ea, pe : states;

begin

  p1 : process (CLOCK, K0) is
  begin

    if (K0 = '1') then
      ea <= s_init;
    elsif (CLOCK'event and CLOCK = '1') then
      ea <= pe;
    end if;

  end process;

  p2 : process (ea, K1, ENDTIME, ENDGAME, ENDROUND) is
  begin

    R1 <= '1';
    R2 <= '1';
    E1 <= '0';
    E2 <= '0';
    E3 <= '0';
    E4 <= '0';
    E5 <= '0';

    case ea is
      when s_init =>
        R1 <= '0';
        R2 <= '0';
        pe <= s_setup;
      when s_setup =>
        E1 <= '1';
        R1 <= '0';
        if (K1 = '1') then
          pe <= s_play;
        else
          pe <= s_setup;
        end if;
      when s_play =>
        E2 <= '1';
        if (ENDTIME = '1') then
          pe <= s_result;
        elsif (K1 = '1') then
          pe <= s_count_round;
        else
          pe <= s_play;
        end if;
      when s_count_round =>
        E3 <= '1';
        E4 <= '1';
        pe <= s_check;
      when s_check =>
        R1 <= '0';
        if (ENDGAME = '1' or ENDROUND = '1') then
          pe <= s_result;
        else
          pe <= s_wait;
        end if;
      when s_wait =>
        R1 <= '1';
        if (K1 = '1') then
          pe <= s_play;
        else
          pe <= s_wait;
        end if;
      when s_result =>
        E5 <= '1';
        R1 <= '0';
        if (K1 = '1') then
          pe <= s_init;
        else
          pe <= s_result;
        end if;
    end case;

  end process;

end bhv;

