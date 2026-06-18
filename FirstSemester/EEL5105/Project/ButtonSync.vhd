library ieee;
  use ieee.std_logic_1164.all;

entity buttonsync is
  port (
    KEY0, KEY1, CLK : in    std_logic;
    ENTER, RESET    : out   std_logic
  );
end buttonsync;

architecture buttonsyncimpl of buttonsync is

  type states is (esperaapertar, saidaativa, esperasoltar);

  signal enter_state, reset_state : states := esperaapertar;
  signal enter_next,  reset_next  : states := esperaapertar;

begin

  process (CLK) is
  begin

    if (CLK'event and CLK = '1') then
      enter_state <= enter_next;
      reset_state <= reset_next;
    end if;

  end process;

  process (KEY0, reset_state) is
  begin

    case reset_state is

      when esperaapertar =>

        if (KEY0 = '0') then
          reset_next <= saidaativa;
        else
          reset_next <= esperaapertar;
        end if;

        RESET <= '0';

      when saidaativa =>

        if (KEY0 = '0') then
          reset_next <= esperasoltar;
        else
          reset_next <= esperaapertar;
        end if;

        RESET <= '1';

      when esperasoltar =>

        if (KEY0 = '0') then
          reset_next <= esperasoltar;
        else
          reset_next <= esperaapertar;
        end if;

        RESET <= '0';

    end case;

  end process;

  process (KEY1, enter_state) is
  begin

    case enter_state is

      when esperaapertar =>

        if (KEY1 = '0') then
          enter_next <= saidaativa;
        else
          enter_next <= esperaapertar;
        end if;

        ENTER <= '0';

      when saidaativa =>

        if (KEY1 = '0') then
          enter_next <= esperasoltar;
        else
          enter_next <= esperaapertar;
        end if;

        ENTER <= '1';

      when esperasoltar =>

        if (KEY1 = '0') then
          enter_next <= esperasoltar;
        else
          enter_next <= esperaapertar;
        end if;

        ENTER <= '0';

    end case;

  end process;

end buttonsyncimpl;

