def sets_to_dict(*args):
    ans = {}
    for i in range(len(args)-1):
        for j in range(i+1, len(args)):
            ans[f'{args[i]} | {args[j]}'] = args[i] | args[j]
            ans[f'{args[i]} & {args[j]}'] = args[i] & args[j]
            ans[f'{args[i]} - {args[j]}'] = args[i] - args[j]
            ans[f'{args[j]} - {args[i]}'] = args[j] - args[i]
    return ans

print(sets_to_dict({1,2}, {2,3}))
