# Script for populating the database. You can run it as:
#
#     mix run priv/repo/seeds.exs
#
# Inside the script, you can read and write to any of your
# repositories directly:
#
#     Todolist.Repo.insert!(%Todolist.SomeSchema{})
#
# We recommend using the bang functions (`insert!`, `update!`
# and so on) as they will fail if something goes wrong.

#usernames = ~w(daniel admin goran marex User2)
#mails = ~w(123456@gmail.com 000000@gmail.com 123456@gmail.com 123456@gmail.com 123456@gmail.com)

#for {{username}, mail} <-  Enum.zip(usernames) |> Enum.zip(mails) do
 # Todolist.Repo.insert!(%Todolist.Tmanage.User{
  #  username: username,
   # email: mail
#  })
#end

## User table alimentation


#Todolist.Repo.insert!(%Todolist.Tmanage.Role{
  #username: "Jojo",
 # email: "jojo@gmail.com",
 # role: "directeur"
#})

## Clock table alimentation

Todolist.Repo.insert!(%Todolist.Tmanage.Clock{
  status: true,
  time: ~N[2021-11-03 08:00:02],
  user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Clock{
  status: false,
  time: ~N[2021-11-03 12:30:02],
  user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Clock{
  status: true,
  time: ~N[2021-11-03 14:39:02],
  user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Clock{
  status: false,
  time: ~N[2021-11-03 16:39:02],
  user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Clock{
  status: true,
  time: ~N[2021-11-04 08:39:02],
  user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Clock{
  status: false,
  time: ~N[2021-11-04 16:39:02],
  user_id: 1
})

## Workingtime table alimentation

Todolist.Repo.insert!(%Todolist.Tmanage.Workingtime{
end: ~N[2021-11-03 12:30:02] ,
start:  ~N[2021-11-03 08:00:02],
user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Workingtime{
end: ~N[2021-11-03 16:39:02],
start: ~N[2021-11-03 14:39:02],
user_id: 1
})

Todolist.Repo.insert!(%Todolist.Tmanage.Workingtime{
end: ~N[2021-11-04 16:39:02],
start: ~N[2021-11-04 08:39:02],
user_id: 1
})
