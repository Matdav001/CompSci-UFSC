library ieee;
  use ieee.std_logic_1164.all;

entity counter_time is
  port (
    UPDOWN   : in    std_logic;
    CLOCK    : in    std_logic;
    RESET    : in    std_logic;
    CONTAGEM : out   std_logic_vector(3 downto 0)
  );
end counter_time;

architecture bhv of counter_time is

  type states is (e0, e1, e2, e3, e4);

  signal ea, pe : states;

begin

  p1 : process (CLOCK, RESET) is
  begin

    if (RESET = '0') then
      ea <= e0;
    elsif (CLOCK'event and CLOCK = '0') then
      ea <= pe;
    end if;

  end process;

  p2 : process (ea, UPDOWN) is
  begin

    case ea is

      when e0 =>

        CONTAGEM <= "0001";

        if (UPDOWN = '1') then
          pe <= e4;
        else
          pe <= e1;
        end if;

      when e1 =>

        CONTAGEM <= "0010";

        if (UPDOWN = '1') then
          pe <= e0;
        else
          pe <= e2;
        end if;

      when e2 =>

        CONTAGEM <= "0011";

        if (UPDOWN = '1') then
          pe <= e1;
        else
          pe <= e3;
        end if;

      when e3 =>

        CONTAGEM <= "0100";

        if (UPDOWN = '1') then
          pe <= e2;
        else
          pe <= e4;
        end if;

      when e4 =>

        CONTAGEM <= "0101";

        if (UPDOWN = '1') then
          pe <= e3;
        else
          pe <= e0;
        end if;

    end case;

  end process;

end bhv;

