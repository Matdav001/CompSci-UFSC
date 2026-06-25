library ieee;
use ieee.std_logic_1164.all;

entity controle is port(
              clock, K1, K0, endtime, endgame, endround: in std_logic;             
              R1, R2, E1, E2, E3, E4, E5: out std_logic);
end controle;

architecture bhv of controle is

  type states is (s_Init, s_Setup, s_Play, s_Count_Round, s_Check, s_Wait, s_Result);
  signal ea, pe : states;

begin

  p1 : process (clock, K0) is
  begin
    if (K0 = '1') then 
      ea <= s_Init;
    elsif (clock'event and clock = '1') then
      ea <= pe;
    end if;
  end process;

  p2 : process (ea, K1, endtime, endgame, endround) is
  begin
    
    R1 <= '1'; R2 <= '1'; -- Active LOW Resets (1 = not reset)
    E1 <= '0'; E2 <= '0'; E3 <= '0'; E4 <= '0'; E5 <= '0'; -- Active HIGH Enables

    case ea is
      
      when s_Init =>
        R1 <= '0'; R2 <= '0'; -- Reset everything
        pe <= s_Setup;

      when s_Setup =>
        E1 <= '1'; -- Show 'C' in HEX3 and Enable reg0 (SW to sel)
        R1 <= '0'; -- Keep timer reset
        if (K1 = '1') then
          pe <= s_Play;
        else
          pe <= s_Setup;
        end if;

      when s_Play =>
        E2 <= '1'; -- Show user guess and Enable reg2 (SW to user)
        if (endtime = '1') then
          pe <= s_Result;
        elsif (K1 = '1') then
          pe <= s_Count_Round;
        else
          pe <= s_Play;
        end if;

      when s_Count_Round =>
        E3 <= '1'; -- Enable counter_round (to decrement/increment round)
        E4 <= '1'; -- Enable reg1 (to save P and E)
        pe <= s_Check;

      when s_Check =>
        if (endgame = '1' or endround = '1') then
          pe <= s_Result;
        else
          pe <= s_Wait;
        end if;

      when s_Wait =>
        -- R1 is '1', which makes selector output "10" -> Shows 'P' and 'E'
        if (K1 = '1') then
          pe <= s_Play;
        else
          pe <= s_Wait;
        end if;

      when s_Result =>
        E5 <= '1'; -- Shows secret code and score
        R1 <= '0'; -- Ensure Wait graphics (IN2) don't override Result graphics (IN3)
        if (K1 = '1') then
          pe <= s_Init;
        else
          pe <= s_Result;
        end if;

    end case;
  end process;

end bhv;