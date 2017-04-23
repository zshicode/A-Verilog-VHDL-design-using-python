


`timescale 1ns/10ps

module dff (
    q,
    d,
    clk
);


output q;
reg q;
input d;
input clk;






always @(posedge clk) begin: DFF_LOGIC
    q <= d;
end

endmodule
