finished = False
while(not(finished)):
  j = input("Provide a MIPS instruction machine code in hex (type 'q' to quit): ")
  if(j[0] == 'q'):
    finished = True
  else:
    h = int(j, 16)
    h = bin(h)
    h = h[2:]
    h = h.zfill(32)
    print(f'Binary: {h}')

    op = h[:6]
    rs = h[6:11]
    rt = h[11:16]
    rd = h[16:21]
    func = h[26:]
    imm = h[16:]

    if op == '000000' and func == '100000':
      instruction_name = 'add'
      instruction_type = 'R-Type'
    elif op == '000000' and func == '100010':
      instruction_name = 'sub'
      instruction_type = 'R-Type'
    elif op == '000000' and func == '101010':
      instruction_name = 'slt'
      instruction_type = 'R-Type'
    elif op == '001000':
      instruction_name = 'addi'
      instruction_type = 'I-Type'
    else:
      instruction_name = 'Unknown'
      instruction_type = 'Unknown'

    print(f'op: {op}, rs: {rs}, rt: {rt}, rd: {rd}, func: {func}, imm: {imm}')

    imm_decimal = int(imm, 2)
    if imm_decimal >= 2**15:
      imm_decimal -= 2**16

    if instruction_type == 'I-Type':
      print(f'Registers: rs = ${int(rs, 2)}, rt = ${int(rt, 2)}')
    elif instruction_type == 'R-Type':
      print(f'Registers: rd = ${int(rd, 2)}, rs = ${int(rs, 2)}, rt = ${int(rt, 2)}')

    
    if instruction_name == 'add':
      print(f"Assembly: add ${int(rd, 2)}, ${int(rs, 2)}, ${int(rt, 2)}\n")
    elif instruction_name == 'sub':
      print(f"Assembly: sub ${int(rd, 2)}, ${int(rs, 2)}, ${int(rt, 2)}\n")
    elif instruction_name == 'slt':
      print(f"Assembly: slt ${int(rd, 2)}, ${int(rs, 2)}, ${int(rt, 2)}\n")
    elif instruction_name == 'addi':
      print(f"Assembly: addi ${int(rt, 2)}, ${int(rs, 2)}, {imm_decimal}\n")