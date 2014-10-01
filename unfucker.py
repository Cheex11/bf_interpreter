import sys

def stage(filename):
    clean_bf_string = cleanup(list(open(filename, "r").read()))
    primas = dict(code=clean_bf_string)
    primas['current_bucket'],primas['code_pointer'],primas['bucket_at_start_of_loop'] = 0,0,[]
    primas['buckets'],primas['beginning_of_loop'] = [0],[]
    unfuck(clean_bf_string, primas)

def unfuck(code, dictionary):
    while dictionary['code_pointer'] < len(dictionary['code']):
        current_character = code[dictionary['code_pointer']]

        if current_character == ">":
            dictionary["current_bucket"] += 1
            if dictionary['current_bucket'] == len(dictionary['buckets']):
                dictionary['buckets'].append(0)
        if current_character == "<":
            dictionary['current_bucket'] -= 1
            if dictionary['current_bucket'] < 0:
                dictionary['current_bucket'] = len(dictionary['buckets'])-1
        if current_character == "+":
            dictionary['buckets'][dictionary['current_bucket']] += 1
        if current_character == "-":
            dictionary['buckets'][dictionary['current_bucket']] -= 1
        if current_character == ".":
            print chr(dictionary['buckets'][dictionary['current_bucket']])
        if current_character == '[':
            dictionary['bucket_at_start_of_loop'].append(dictionary['current_bucket'])
            dictionary['beginning_of_loop'].append(dictionary['code_pointer'])
        if current_character == ']':
            if dictionary['buckets'][dictionary['bucket_at_start_of_loop'][-1]] != 0:
                dictionary['code_pointer'] = dictionary['beginning_of_loop'][-1]
            else:
                dictionary['bucket_at_start_of_loop'].pop(-1)
                dictionary['beginning_of_loop'].pop(-1)
        dictionary["code_pointer"] += 1

def cleanup(code):
  return filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code)

def main():
  if len(sys.argv) == 2:
    stage(sys.argv[1])
  else:
    print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__":
    main()
