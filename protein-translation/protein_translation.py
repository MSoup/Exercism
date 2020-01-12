def proteins(strand):
  my_Data = {
  'AUG': 'Methionine',
  'UUU': 'Phenylalanine', 
  'UUC': 'Phenylalanine',
  'UUA': 'Leucine', 
  'UUG': 'Leucine',
  'UCU': 'Serine', 
  'UCC': 'Serine',
  'UCA': 'Serine',
  'UCG': 'Serine',
  'UAU': 'Tyrosine', 
  'UAC': 'Tyrosine',
  'UGU': 'Cysteine',
  'UGC': 'Cysteine',
  'UGG': 'Tryptophan',
  }
  
  strand_blocks = [strand[i:i+3] for i in range(0,len(strand),3)]
  translated = []

  for i in strand_blocks:
    if i == 'UAA' or i == 'UAG' or i == 'UGA':
      break
    else:
      translated.append(my_Data[i])

  return translated

