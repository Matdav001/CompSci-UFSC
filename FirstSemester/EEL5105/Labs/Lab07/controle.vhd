library ieee;
  use ieee.std_logic_1164.all;

entity controle is
  port (
    C, TM, CLOCK, RESET : in    std_logic;
    TC, TW              : out   std_logic
  );
end controle;

architecture ctrl of controle is

  type states is (e0, e1, e2);

  signal ea, pe : states;

begin

  p1 : process (CLOCK, RESET) is
  begin

    if (RESET = '0') then
      ea <= e0;
    elsif (CLOCK'event and CLOCK = '1') then
      ea <= pe;
    end if;

  end process;

  p2 : process (ea, C, TM) is
  begin

    case ea is

      when e0 =>

        TC <= '1';
        TW <= '0';

        pe <= e1;

      when e1 =>

        TC <= '0';
        TW <= '0';

        if (TM = '0') then
          pe <= e0;
        else
          if (C = '1') then
            pe <= e2;
          else
            pe <= e1;
          end if;
        end if;

      when e2 =>

        TC <= '0';
        TW <= '1';
        pe <= e1;

    end case;

  end process;

end ctrl;

