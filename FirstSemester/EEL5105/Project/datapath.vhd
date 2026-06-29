library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_arith.all;
  use ieee.std_logic_unsigned.all;

entity datapath is
  port (
    S                                              : in    std_logic_vector(15 downto 0); -- dos switches
    CLK, R1, R2, E1, E2, E3, E4, E5                : in    std_logic;
    END_GAME, END_TIME, END_ROUND                  : out   std_logic;
    HEX7, HEX6, HEX5, HEX4, HEX3, HEX2, HEX1, HEX0 : out   std_logic_vector(6 downto 0);
    LED                                            : out   std_logic_vector(15 downto 0)
  );
end datapath;

architecture arqdtp of datapath is

  signal sel_mux     : std_logic_vector(1 downto 0);
  signal y           : std_logic_vector(3 downto 0);
  signal counttime   : std_logic_vector(3 downto 0);
  signal temp        : std_logic_vector(3 downto 0);
  signal x           : std_logic_vector(3 downto 0);
  signal xb          : std_logic_vector(3 downto 0);
  signal q           : std_logic_vector(3 downto 0);
  signal q1          : std_logic_vector(3 downto 0);
  signal preg        : std_logic_vector(3 downto 0);
  signal ereg        : std_logic_vector(3 downto 0);
  signal selecc      : std_logic_vector(3 downto 0);
  signal f           : std_logic_vector(3 downto 0);
  signal result      : std_logic_vector(7 downto 0);
  signal p           : std_logic_vector(2 downto 0);
  signal p_reg       : std_logic_vector(2 downto 0);
  signal e           : std_logic_vector(2 downto 0);
  signal e_reg       : std_logic_vector(2 downto 0);
  signal p0          : std_logic_vector(2 downto 0);
  signal p1          : std_logic_vector(2 downto 0);
  signal p2          : std_logic_vector(2 downto 0);
  signal p3          : std_logic_vector(2 downto 0);
  signal sel         : std_logic_vector(5 downto 0);
  signal user        : std_logic_vector(15 downto 0);
  signal code        : std_logic_vector(15 downto 0);
  signal ledr150     : std_logic_vector(15 downto 0);
  signal z           : std_logic_vector(15 downto 0);
  signal m0          : std_logic_vector(15 downto 0);
  signal m1          : std_logic_vector(15 downto 0);
  signal m2          : std_logic_vector(15 downto 0);
  signal m3          : std_logic_vector(15 downto 0);
  signal h71         : std_logic_vector(6 downto 0);
  signal h61         : std_logic_vector(6 downto 0);
  signal h41         : std_logic_vector(6 downto 0);
  signal h31         : std_logic_vector(6 downto 0);
  signal h33         : std_logic_vector(6 downto 0);
  signal h20         : std_logic_vector(6 downto 0);
  signal h21         : std_logic_vector(6 downto 0);
  signal h22         : std_logic_vector(6 downto 0);
  signal h23         : std_logic_vector(6 downto 0);
  signal h11         : std_logic_vector(6 downto 0);
  signal h13         : std_logic_vector(6 downto 0);
  signal h00         : std_logic_vector(6 downto 0);
  signal h01         : std_logic_vector(6 downto 0);
  signal h02         : std_logic_vector(6 downto 0);
  signal h03         : std_logic_vector(6 downto 0);
  signal clk1        : std_logic;
  signal rst_divfreq : std_logic;
  signal e4r1        : std_logic;
  signal endgame     : std_logic;
  signal endtime     : std_logic;
  signal endround    : std_logic;

  -- para funcionar no emulador
  signal decsignal0 : std_logic_vector(3 downto 0);
  signal decsignal1 : std_logic_vector(3 downto 0);
  signal decsignal2 : std_logic_vector(3 downto 0);

  signal pe_reg, pe : std_logic_vector(5 downto 0);

  component somador is
    port (
      A : in    std_logic_vector(2 downto 0);
      B : in    std_logic_vector(2 downto 0);
      C : in    std_logic_vector(2 downto 0);
      D : in    std_logic_vector(2 downto 0);
      F : out   std_logic_vector(2 downto 0)
    );
  end component somador;

  component selector is
    port (
      IN0, IN1, IN2, IN3 : in    std_logic;
      SAIDA              : out   std_logic_vector(1 downto 0)
    );
  end component selector;

  component rom3 is
    port (
      ADDRESS : in    std_logic_vector(3 downto 0);
      DATA    : out   std_logic_vector(15 downto 0)
    );
  end component rom3;

  component rom2 is
    port (
      ADDRESS : in    std_logic_vector(3 downto 0);
      DATA    : out   std_logic_vector(15 downto 0)
    );
  end component rom2;

  component rom1 is
    port (
      ADDRESS : in    std_logic_vector(3 downto 0);
      DATA    : out   std_logic_vector(15 downto 0)
    );
  end component rom1;

  component rom0 is
    port (
      ADDRESS : in    std_logic_vector(3 downto 0);
      DATA    : out   std_logic_vector(15 downto 0)
    );
  end component rom0;

  component registrador16 is
    port (
      CLK, RST, EN : in    std_logic;
      D            : in    std_logic_vector(15 downto 0);
      Q            : out   std_logic_vector(15 downto 0)
    );
  end component registrador16;

  component registrador6 is
    port (
      CLK, RST, EN : in    std_logic;
      D            : in    std_logic_vector(5 downto 0);
      Q            : out   std_logic_vector(5 downto 0)
    );
  end component registrador6;

  component registrador is
    port (
      CLK, RST, EN : in    std_logic;
      D            : in    std_logic_vector(3 downto 0);
      Q            : out   std_logic_vector(3 downto 0)
    );
  end component registrador;

  component multiplexador74 is
    port (
      F1, F2, F3, F4 : in    std_logic_vector(6 downto 0);
      SEL            : in    std_logic_vector(1 downto 0);
      SAIDA          : out   std_logic_vector(6 downto 0)
    );
  end component multiplexador74;

  component multiplexador72 is
    port (
      F1, F2 : in    std_logic_vector(6 downto 0);
      SEL    : in    std_logic;
      SAIDA  : out   std_logic_vector(6 downto 0)
    );
  end component multiplexador72;

  component multiplexador16 is
    port (
      F1, F2, F3, F4 : in    std_logic_vector(15 downto 0);
      SEL            : in    std_logic_vector(1 downto 0);
      SAIDA          : out   std_logic_vector(15 downto 0)
    );
  end component multiplexador16;

  component decodtermo is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(15 downto 0)
    );
  end component decodtermo;

  component decod7seg is
    port (
      G     : in    std_logic_vector(3 downto 0);
      SAIDA : out   std_logic_vector(6 downto 0)
    );
  end component decod7seg;

  component counter_time is
    port (
      CLOCK    : in    std_logic;
      RESET    : in    std_logic;
      E        : in    std_logic;
      CONTAGEM : out   std_logic_vector(3 downto 0);
      END_TIME : out   std_logic
    );
  end component counter_time;

  component counter_round is
    port (
      CLOCK     : in    std_logic;
      RESET     : in    std_logic;
      E         : in    std_logic;
      CONTAGEM  : out   std_logic_vector(3 downto 0);
      END_ROUND : out   std_logic
    );
  end component counter_round;

  component comp_4 is
    port (
      P    : in    std_logic_vector(2 downto 0);
      PEQ4 : out   std_logic
    );
  end component comp_4;

  component comp_n is
    port (
      C, U : in    std_logic_vector(3 downto 0);
      P0   : out   std_logic_vector(2 downto 0)
    );
  end component comp_n;

  component comp_e is
    port (
      INC, INU : in    std_logic_vector(15 downto 0);
      E        : out   std_logic_vector(2 downto 0)
    );
  end component comp_e;

  component buttonsync is
    port (
      KEY0, KEY1, CLK : in    std_logic;
      ENTER, RESET    : out   std_logic
    );
  end component buttonsync;

  component div_freq_de2 is
    port (
      CLK     : in    std_logic;
      RESET   : in    std_logic;
      CLK_1HZ : out   std_logic
    );
  end component div_freq_de2;

  component div_freq is
    port (
      CLK              : in    std_logic;
      RESET            : in    std_logic;
      CLK_1HZ, SIM_2HZ : out   std_logic
    );
  end component div_freq;

begin

  END_TIME  <= endtime;
  END_GAME  <= endgame;
  END_ROUND <= endround;

  -- divfreq_emu : component div_freq port map (CLK, R2, clk1);  -- usar esse componente para o emulador

  divfreq : component div_freq_de2 port map (CLK, R2, clk1); -- usar esse componente para a placa

  e4r1 <= E4 or R1;

  selector0 : component selector port map (E1, E2, e4r1, E5, sel_mux);

  f      <= x when endtime = '0' else
            (others => '0');
  result <= "000" & endgame & f;

  reg0 : component registrador6 port map (CLK, R2, E1, S(5 downto 0), sel);

  pe <= p & e;

  reg1 : component registrador6 port map (CLK, R2, E4, pe, pe_reg);

  p_reg <= pe_reg(5 downto 3);
  e_reg <= pe_reg(2 downto 0);

  reg2 : component registrador16 port map (CLK, R2, E2, S(15 downto 0), user);

  rom0_inst : component rom0 port map (sel(5 downto 2), m0);

  rom1_inst : component rom1 port map (sel(5 downto 2), m1);

  rom2_inst : component rom2 port map (sel(5 downto 2), m2);

  rom3_inst : component rom3 port map (sel(5 downto 2), m3);

  mux0 : component multiplexador16 port map (m0, m1, m2, m3, sel(1 downto 0), code);

  comp0 : component comp_e port map (code, user, e);

  comp1 : component comp_n port map (code(3 downto 0), user(3 downto 0), p0);

  comp2 : component comp_n port map (code(7 downto 4), user(7 downto 4), p1);

  comp3 : component comp_n port map (code(11 downto 8), user(11 downto 8), p2);

  comp4 : component comp_n port map (code(15 downto 12), user(15 downto 12), p3);

  soma0 : component somador port map (p0, p1, p2, p3, p);

  comp5 : component comp_4 port map (p, endgame);

  cont_round : component counter_round port map (CLK, R2, E3, x, endround);

  cont_time : component counter_time port map (clk1, R1, E2, counttime, endtime);

  decod7seg71 : component decod7seg port map (result(7 downto 4), h71);

  mux1 : component multiplexador72 port map ("1111111", h71, E5, HEX7);

  decod7seg61 : component decod7seg port map (result(3 downto 0), h61);

  mux2 : component multiplexador72 port map ("1111111", h61, E5, HEX6);

  mux3 : component multiplexador72 port map ("1111111", "0000111", E2, HEX5);

  decod7seg41 : component decod7seg port map (counttime, h41);

  mux4 : component multiplexador72 port map ("1111111", h41, E2, HEX4);

  decod7seg31 : component decod7seg port map (user(15 downto 12), h31);

  decod7seg33 : component decod7seg port map (code(15 downto 12), h33);

  mux5 : component multiplexador74 port map ("1000110", h31, "0001100", h33, sel_mux, HEX3);

  decod7seg20 : component decod7seg port map (sel(5 downto 2), h20);

  decod7seg21 : component decod7seg port map (user(11 downto 8), h21);

  decsignal2 <= '0' & p_reg;

  decod7seg22 : component decod7seg port map (decsignal2, h22);

  decod7seg23 : component decod7seg port map (code(11 downto 8), h23);

  mux6 : component multiplexador74 port map (h20, h21, h22, h23, sel_mux, HEX2);

  decod7seg11 : component decod7seg port map (user(7 downto 4), h11);

  decod7seg13 : component decod7seg port map (code(7 downto 4), h13);

  mux7 : component multiplexador74 port map ("1000111", h11, "0000110", h13, sel_mux, HEX1);

  decsignal0 <= "00" & sel(1 downto 0);

  decod7seg00 : component decod7seg port map (decsignal0, h00);

  decod7seg01 : component decod7seg port map (user(3 downto 0), h01);

  decsignal1 <= '0' & e_reg;

  decod7seg02 : component decod7seg port map (decsignal1, h02);

  decod7seg03 : component decod7seg port map (code(3 downto 0), h03);

  mux8 : component multiplexador74 port map (h00, h01, h02, h03, sel_mux, HEX0);

  decodtermo_inst : component decodtermo port map (x, ledr150);

  LED <= ledr150 when E1 = '0' else
         (others => '0');

end arqdtp;
