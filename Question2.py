def make_joint(withdraw,old_password,new_password):
    def joint_count(balance,new_password):
        if new_password in save_password:
            return withdraw(balance,old_password)
        else:
            return withdraw(balance,new_password)
    save_password = []
    back = withdraw(0,old_password)
    if type(back) == str:
        return back
    else:
        save_password.append(new_password)
        return joint_count