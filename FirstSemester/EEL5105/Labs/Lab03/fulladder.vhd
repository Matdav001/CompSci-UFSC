library ieee;
  use ieee.std_logic_1164.all;

entity fulladder is
  port (
    A, B, CIN : in    std_logic;
    SUM, COUT : out   std_logic
  );
end fulladder;

architecture fadder of fulladder is

begin

  SUM  <= (A xor B) xor CIN;
  COUT <= ((A xor B) and CIN) or (A and B);

end fadder;

