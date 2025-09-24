def isHappy(n):
  if (n < 1) or (n > 2**31-1):
    return False

  s = []
  while n != 1:
    if n in s:
      return False
    s.append(n)
    n = sum(int(i) ** 2 for i in str(n))
  return True

if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)
  
  with open("/app/bind_mount/output.txt","w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
    
  print("Result saved to /app/bind_mount/output.txt")