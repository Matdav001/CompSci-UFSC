library ieee;
  use ieee.std_logic_1164.all;

entity rom3 is
  port (
    ADDRESS : in    std_logic_vector(3 downto 0);
    DATA    : out   std_logic_vector(15 downto 0)
  );
end rom3;

architecture rom_arch of rom3 is

  type memory is array (00 to 15) of std_logic_vector(15 downto 0);

  constant my_rom : memory :=
  (

    00 => "0111100101010100", -- 7954
    01 => "0100100100100001", -- 4921
    02 => "0001100001001001", -- 1849
    03 => "1000100101110010", -- 8972
    04 => "0001100010010010", -- 1892
    05 => "0110100000100101", -- 6825
    06 => "0110100100100001", -- 6921
    07 => "0001001001101001", -- 1269
    08 => "1001100001110110", -- 9876
    09 => "0110011110001001", -- 6789
    10 => "0101011010000010", -- 5682
    11 => "0111010100111001", -- 7539
    12 => "0111100000010010", -- 7812
    13 => "1000000110010011", -- 8193
    14 => "0101011010010011", -- 5693
	15 => "0110100101111000"
  );                          -- 6978

begin

  process (ADDRESS) is
  begin

    case ADDRESS is

      when "0000" =>

        DATA <= my_rom(00);

      when "0001" =>

        DATA <= my_rom(01);

      when "0010" =>

        DATA <= my_rom(02);

      when "0011" =>

        DATA <= my_rom(03);

      when "0100" =>

        DATA <= my_rom(04);

      when "0101" =>

        DATA <= my_rom(05);

      when "0110" =>

        DATA <= my_rom(06);

      when "0111" =>

        DATA <= my_rom(07);

      when "1000" =>

        DATA <= my_rom(08);

      when "1001" =>

        DATA <= my_rom(09);

      when "1010" =>

        DATA <= my_rom(10);

      when "1011" =>

        DATA <= my_rom(11);

      when "1100" =>

        DATA <= my_rom(12);

      when "1101" =>

        DATA <= my_rom(13);

      when "1110" =>

        DATA <= my_rom(14);

      when others =>

        DATA <= my_rom(15);

    end case;

  end process;

end rom_arch;

